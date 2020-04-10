#!/bin/bash

# Get BED files, get sequence data, etc

# Convert one-indexed 23-mer guide locations to BED format
# one-indexing -> zero-indexing, closed end interval -> open end interval
if false;
then
  cat ../data/hct116.allcols.txt | cut -f 1,2,3 | awk '{($2 = $2-1); print}' > ../data/hct116.23mer.bed
fi

# Get sequence data from location info
if false;
then
  while read p; do
    chr=$(echo "$p" | cut -f 1)
    start=$(echo "$p" | cut -f 2 | awk '{($1=$1-1); print}')
    end=$(echo "$p" | cut -f 3)
    wget -O- 'api.genome.ucsc.edu/getData/sequence?genome=hg19;chrom='"$chr"';start='"$start"';end='"$end" > ../data/tmp.txt
    seq=$(cat ../data/tmp.txt | awk -F\" '{print $22}')
    rm ../data/tmp.txt
    # if it's on the reverse strand, get the reverse complement
    strand=$(echo "$p" | cut -f 4)
    if [ "$strand" == "-" ];
    then
      seq2=$(echo "$seq" | tr ACGTacgt TGCATGCA | rev)
      seq="$seq2"
    fi
    echo "$seq" >> ../data/hct116.seqs.test.txt
  done < ../data/hct116.allcols.test.txt
fi

# Get surrounding 30mer from 23mer location info
if true;
then
  while read p; do
    chr=$(echo "$p" | cut -f 1)
    strand=$(echo "$p" | cut -f 4)
    if [ "$strand" == "+" ]
    then
      start=$(echo "$p" | cut -f 2 | awk '{($1=$1-5); print}')
      end=$(echo "$p" | cut -f 3 | awk '{($1=$1+3); print}')
    elif [ "$strand" == "-" ]
    then
      start=$(echo "$p" | cut -f 2 | awk '{($1=$1-4); print}')
      end=$(echo "$p" | cut -f 3 | awk '{($1=$1+4); print}')
    fi
    wget -O- 'api.genome.ucsc.edu/getData/sequence?genome=hg19;chrom='"$chr"';start='"$start"';end='"$end" > ../data/tmp.txt
    seq=$(cat ../data/tmp.txt | awk -F\" '{print $22}')
    # if it's on the reverse strand, get the reverse complement
    if [ "$strand" == "-" ];
    then
      seq2=$(echo "$seq" | tr ACGTacgt TGCAtgca | rev)
      seq="$seq2"
    fi
    echo "$seq" >> ../data/hct116.seqs.30mers.txt
  done < ../data/hct116.allcols.txt
  grep -i "\S" ../data/hct116.seqs.30mers.txt > tmp.txt
  mv tmp.txt ../data/hct116.seqs.30mers.txt
fi
