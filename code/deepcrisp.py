import tensorflow as tf
import numpy as np

try:
    from deepcrispr_src import DCModelOntar
except:
    import sys
    sys.path.insert(1, "../DeepCRISPR/deepcrispr/")
    from deepcrispr_src import DCModelOntar


def load_data():
    scorefile = "../data/hct116.allcols.txt"
    scores = np.loadtxt(scorefile, usecols=5)

    seq_feature_only = True
    channels = 4 if seq_feature_only else 8

    seqfile = "../data/hct116.allcols.txt"
    sequences = np.loadtxt(seqfile, usecols=4, dtype='str')
    sequences = np.reshape([len(sequences), 4, 1, 23])

    sess = tf.InteractiveSession()
    on_target_model_dir = '../DeepCRISPR/trained_models/ontar_cnn_reg_seq.tar.gz'
    # using regression model, otherwise classification model
    is_reg = True
    # using sequences feature only, otherwise sequences feature + selected epigenetic features
    seq_feature_only = True
    dcmodel = DCModelOntar(sess, on_target_model_dir, is_reg, seq_feature_only)
    return(scores, sequences, dcmodel)


def dc_pred(dcmodel, seqs):
    preds = dcmodel.ontar_predict(seqs)
    np.savetxt("../data/hct116.dcpreds.txt", preds, fmt='%1.10f', newline=os.linesep)
    return(preds)


def compare_preds(scores, preds):
    plt.scatter(scores, preds)
    plt.xlabel("True Efficacy")
    plt.ylabel("Rule Set 2 Predictions")
    plt.savefig("../figs/dcscatter.png")


def test_correlation():
    scorefile = "../data/hct116.allcols.txt"
    scores = np.loadtxt(scorefile, usecols=5)
    predfile = "../data/hct116.rs2preds.txt"
    preds = np.loadtxt(predfile)
    pears, p = pearsonr(scores, preds)
    print("Pearson correlation: %.3f, p value %.2f" % (pears, p))
    spear, p = spearmanr(scores, preds)
    print("Spearman rank correlation: %.3f, p value %.2f" % (spear, p))


def main():
    scores, seqs, dcmodel = load_data()
    preds = dc_pred(dcmodel, seqs)
    compare_preds(scores, preds)

if __name__=="__main__":
    main()
