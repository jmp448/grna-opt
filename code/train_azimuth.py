import copy
import os
import numpy as np
import pandas as pd
import shutil
import pickle
import pandas
try:
    import azimuth.model_comparison
except:
    import sys
    sys.path.insert(1, "../Azimuth/")
    import azimuth.model_comparison
import azimuth.util
import azimuth.local_multiprocessing
import azimuth.load_data
import azimuth.features.featurization as feat
import sklearn.ensemble as en
import azimuth.predict as pred


def load_data(data_filename, label_filename):
    X = pd.read_csv(data_filename, names=["30mer"], header=0)
    y = pd.read_csv(label_filename)
    return X, y


def get_features(data):
    learn_options = {
        "nuc_features": True,
        "order": 1,
        "gc_features": True,
        "include_gene_position": False,
        "include_gene_effect": False,
        "include_know_pairs": False,
        "include_NGGX_interaction": True,
	"include_pi_nuc_feat": True,
        "include_Tm": False,
        "include_sgRNAscore": False,
        "include_drug": False,
        "include_strand": False,
        "include_gene_feature": False,
        "include_gene_guide_feature": 0,
	"include_known_pairs": False,
        "random_seed": 7,
	"num_proc": 1,
	"include_microhomology": False,
	"normalize_features": False
    }
    feature_sets = feat.featurize_data(data, learn_options, Y=None, gene_position=None, pam_audit=True, length_audit=True, quiet=True)
    return feature_sets, learn_options


def build_train_model(X, y, learn_options, train=None, test=None):
    X, featdims, totdims, feature_names = azimuth.util.concatenate_feature_sets(X)
    clf = en.GradientBoostingRegressor(loss='ls', learning_rate=0.1,
				       n_estimators=100,
                                       alpha=0.5,
                                       subsample=1.0, min_samples_split=2, min_samples_leaf=1,
                                       max_depth=3,
                                       init=None,  max_features=None,
                                       verbose=0, max_leaf_nodes=None, warm_start=False, random_state=learn_options["random_seed"])
    if train is not None:
	print "boutta train!"
        clf.fit(X[train], y[train].flatten())
    else:
	print "boutta train!"
        clf.fit(X, y)
    if test is not None:
        y_pred = clf.predict(X[test])
    else:
        y_pred = clf.predict(X)
    return clf, y_pred


def save_model(model, learn_options, filename):
    model_save = model.values()[0][3][0]
    with open(filename, 'wb') as f:
        pickle.dump((model_save, learn_options), f, -1)


def main():
    X, y = load_data("../data/hct116.seqs.30mers.sorted.txt", "../data/efficacy.sorted.txt")
    X, learn_options = get_features(X)
    model, preds = build_train_model(X, y, learn_options)
    save_model(model, learn_options, filename="../data/dctrained.seqonly.pickle")


if __name__ == '__main__':
    main()
