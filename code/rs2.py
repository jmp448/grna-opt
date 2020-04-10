import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

try:
    import azimuth.model_comparison
except:
    import sys
    sys.path.insert(1, "../Azimuth/")
    import azimuth.model_comparison


def test():
    sequences = np.array(['ACAGCTGATCTCCAGATATGACCATGGGTT', 'CAGCTGATCTCCAGATATGACCATGGGTTT', 'CCAGAAGTTTGAGCCACAAACCCATGGTCA'])
    predictions = azimuth.model_comparison.predict(sequences)

    for i, pred in enumerate(predictions):
        print sequences[i], pred


def load_data():
    seqfile = "../data/hct116.seqs.30mers.txt"
    sequences = np.loadtxt(seqfile, dtype='str')
    scorefile = "../data/hct116.allcols.txt"
    scores = np.loadtxt(scorefile, usecols=5)
    return sequences, scores


def predict_efficacy(s):
    """
    Input: np array of strings, gRNA candidates
    Output: np array of Rule Set 2 scores
    """
    predictions = azimuth.model_comparison.predict(s)
    np.savetxt("../data/hct116.rs2preds.txt", predictions, fmt='%1.10f', newline=os.linesep)
    return predictions


def compare_preds(scores, preds):
    plt.scatter(scores, preds)
    plt.xlabel("True Efficacy")
    plt.ylabel("Rule Set 2 Predictions")
    plt.savefig("../figs/rs2scatter.png")


def main():
    seqs, scores = load_data()
    preds = predict_efficacy(seqs)
    compare_preds(scores, preds)


if __name__=="__main__":
    main()
