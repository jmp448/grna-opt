# Data - Table of Contents

- deepcrispr_ontarget.xlsx
  - Data from DeepCRISPR paper
    - "Chromosome"
    - "Start"
      - One-indexed (I assume) start point
    - "End"
      - Inclusive end point (interval is [start, end])
    - "Strand"
      - +/-
    - "sgRNA"
      - sgRNA sequence, 23bp, NGG PAM at the end
    - "Normalized efficacy"
      - Float
  - Four tabs, one for each cell line examined
    - hct116, hek293t, hela, hl60 (in that order)
  - Efficacy scores integrated results from several experiments (see _Methods_ section of paper)

- efficacy.sorted.txt
  - sorted efficacy scores as assigned by DeepCRISPR
