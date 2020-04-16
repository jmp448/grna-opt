import tensorflow as tf
import numpy as np
import os
from scipy.stats import linregress, spearmanr, pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


try:
    from prediction_util import *
except:
    import sys
    sys.path.insert(1, "../DeepHF/")
    from prediction_util import *


def load_data():
    scorefile = "../data/hct116.allcols.txt"
    scores = np.loadtxt(scorefile, usecols=5)

    seqfile = "../data/hct116.allcols.txt"
    sequences = np.loadtxt(seqfile, usecols=4, dtype='str')

    return(scores, sequences)


def deephf_pred(seqs):
    for s in seqs:
        print()


def compare_preds(scores, preds):
    plt.scatter(scores, preds)
    plt.xlabel("True Efficacy")
    plt.ylabel("Rule Set 2 Predictions")
    plt.savefig("../figs/dcscatter.png")


def test_correlation():
    scorefile = "../data/hct116.allcols.txt"
    scores = np.loadtxt(scorefile, usecols=5)
    predfile = "../data/hct116.dcpreds.txt"
    preds = np.loadtxt(predfile)
    pears, p = pearsonr(scores, preds)
    print("Pearson correlation: %.3f, p value %.2f" % (pears, p))
    spear, p = spearmanr(scores, preds)
    print("Spearman rank correlation: %.3f, p value %.2f" % (spear, p))


def main():
    scores, seqs = load_data()
    preds = deephf_pred(seqs)
    # compare_preds(scores, preds)
    test_correlation()

if __name__=="__main__":
    main()
