import copy
import os
import numpy as np
import pandas as pd
import shutil
import pickle
import pandas
import sys
sys.path.insert(1, "../Azimuth")
import azimuth.model_comparison
import azimuth.util
import azimuth.local_multiprocessing
import azimuth.load_data
import sklearn.ensemble as en
import azimuth.predict as pred
import imp
imp.load_source("featko", "../Azimuth_ko/azimuth/features/featurization.py")
import featko
imp.load_source("featindel", "../Azimuth_indel/azimuth/features/featurization.py")
import featindel


def get_data(dtype):
    if dtype == "indel":
	fname = "../data/indel/dataset.txt"
	X = pd.read_csv(fname, sep="\t", usecols=[4], names=["23mer"], header=0)
	y = pd.read_csv(fname, sep="\t", usecols=[6], names=["score"], header=0)
	model_name = "../models/azimuth.indel.all.pickle"
	return X, y, model_name
    elif dtype == "knockout":
	fname = "../data/knockout/dataset.txt"
	X = pd.read_csv(fname, sep="\t", usecols=[3,5], names=["Percent Peptide", "24mer"], header=0)
	y = pd.read_csv(fname, sep="\t", usecols=[4], names=["score"], header=0)
	model_name = "../models/azimuth.ko.all.pickle"
	return X, y, model_name


def get_features(trainmode, data):
    if trainmode == "indel":
    	learn_options = {
        	"nuc_features": True,
        	"order": 3,
        	"gc_features": True,
        	"include_gene_position": False,
        	"include_gene_effect": False,
        	"include_know_pairs": False,
        	"include_NGGX_interaction": False,
		"include_pi_nuc_feat": True,
        	"include_Tm": True,
        	"include_sgRNAscore": False,
        	"include_drug": False,
        	"include_strand": False,
        	"include_gene_feature": False,
        	"include_gene_guide_feature": 0,
		"include_known_pairs": False,
        	"random_seed": 7,
		"num_proc": 1,
		"include_microhomology": False,
		"include_structural_feats": True,
		"normalize_features": False
        }
	feature_sets = featindel.featurize_data(data, learn_options, Y=None, pam_audit=False, length_audit=False, quiet=True)
    elif trainmode == "knockout":
	learn_options = {
                "nuc_features": True,
                "order": 3,
                "gc_features": True,
                "include_gene_position": True,
                "include_gene_effect": False,
                "include_know_pairs": False,
                "include_NGGX_interaction": True,
                "include_pi_nuc_feat": True,
                "include_Tm": True,
                "include_sgRNAscore": False,
                "include_drug": False,
                "include_strand": False,
                "include_gene_feature": False,
                "include_gene_guide_feature": 0,
                "include_known_pairs": False,
                "random_seed": 7,
                "num_proc": 1,
                "include_microhomology": False,
		"include_structural_feats": True,
                "normalize_features": False
        }	
    	feature_sets = featko.featurize_data(data, learn_options, Y=None, pam_audit=False, length_audit=False, quiet=True)
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
        clf.fit(X[train], y[train].flatten())
    else:
        clf.fit(X, y)
    if test is not None:
        y_pred = clf.predict(X[test])
    else:
        y_pred = clf.predict(X)
    return clf, y_pred, feature_names


def save_model(model, learn_options, featnames, filename):
    with open(filename, 'wb') as f:
        pickle.dump((model, learn_options, featnames), f, -1)


def main():
    trainmode = sys.argv[1]
    X, y, modname = get_data(trainmode)
    X, learn_options = get_features(trainmode, X)
    model, preds, feat_names = build_train_model(X, y, learn_options)
    save_model(model, learn_options, feat_names, filename=modname)


if __name__ == '__main__':
    main()
