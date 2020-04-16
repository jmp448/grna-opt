import numpy as np
from scipy.stats import linregress, spearmanr, pearsonr

def test_correlation(scores, preds):
    pears, p = pearsonr(scores, preds)
    print("Pearson correlation: %.3f, p value %.2f" % (pears, p))
    spear, p = spearmanr(scores, preds)
    print("Spearman rank correlation: %.3f, p value %.2f" % (spear, p))


def main():
    # scorefile = "../data/hct116.allcols.txt"
    # scores = np.loadtxt(scorefile, usecols=5)
    dcpredfile = "../data/hct116.dcpreds.txt"
    dcpreds = np.loadtxt(dcpredfile)
    rs2predfile = "../data/hct116.rs2preds.txt"
    rs2preds = np.loadtxt(rs2predfile)
    test_correlation(dcpreds, rs2preds)


if __name__=="__main__":
    main()
