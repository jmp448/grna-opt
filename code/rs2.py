import numpy as np

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
    fname = "../data/dc_ontarget_hct116.txt"
    sequences = np.loadtxt(fname, dtype='str', skiprows=1, usecols=4)
    scores = np.loadtxt(fname, skiprows=1, usecols=5)
    return sequences, scores


def predict_efficacy(s):
    """
    Input: np array of strings, gRNA candidates
    Output: np array of Rule Set 2 scores
    """
    predictions = azimuth.model_comparison.predict(s, pam_audit=False)
    return predictions


def compare_preds(scores, preds):


def main():
    seqs, scores = load_data()
    preds = predict_efficacy(seqs)


if __name__=="__main__":
    main()
