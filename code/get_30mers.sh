#!/bin/bash

while read p; do
  grep "$p" ../data/deephf/Brunello.txt | cut -f 9 >> ../data/deephf/30mers.txt
done <../data/deephf/23mers.txt
