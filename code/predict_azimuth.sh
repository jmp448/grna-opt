#!/bin/bash

#indels, based on retrained model
python predict_azimuth.py ../models/azimuth.indel.all.pickle ../data/indel/dataset.txt indel ../results/indel_data/azimuth.indel.preds
