import numpy as np
from scipy.stats import linregress, spearmanr, pearsonr

def test_correlation(scores, preds):
    pears, p = pearsonr(scores, preds)
    print("Pearson correlation: %.3f, p value %.2f" % (pears, p))
    spear, p = spearmanr(scores, preds)
    print("Spearman rank correlation: %.3f, p value %.2f" % (spear, p))


def main():
    scorefile = "../data/hct116.allcols.sorted.txt"
    scores = np.loadtxt(scorefile, usecols=5)
    dcpredfile = "../data/hct116.dcpreds.sorted.txt"
    dcpreds = np.loadtxt(dcpredfile)
    rs2predfile = "../data/hct116.rs2preds.sorted.txt"
    rs2preds = np.loadtxt(rs2predfile)
    hfpredfile = "../data/hct116.hfpreds.sorted.txt"
    hfpreds = np.loadtxt(hfpredfile)

    print("Exp vs HF")
    test_correlation(scores, hfpreds)

    print("Exp vs DC")
    test_correlation(scores, dcpreds)

    print("Exp vs RS2")
    test_correlation(scores, rs2preds)

    print("HF vs DC")
    test_correlation(hfpreds, dcpreds)

    print("DC vs RS2")
    test_correlation(dcpreds, rs2preds)

    print("HF vs RS2")
    test_correlation(hfpreds, rs2preds)


if __name__=="__main__":
    main()
