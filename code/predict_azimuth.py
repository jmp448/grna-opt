import copy
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


def get_data(dtype, fname):
    if dtype == "indel":
	X = pd.read_csv(fname, sep="\t", usecols=[4], names=["23mer"], header=0)
	return X
    elif dtype == "knockout":
	X = pd.read_csv(fname, sep="\t", usecols=[0,1], names=["24mer", "Percent Peptide"], header=0)
	return X


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


def load_model(modfile):
    with open(modfile, 'rb') as f:
        model, learn_options, featnames = pickle.load(f)
    return model, learn_options, featnames


def main():
    modname = sys.argv[1]
    datafile = sys.argv[2]
    dtype = sys.argv[3]
    outfile = sys.argv[4]
    X = get_data(dtype, datafile)
    mod, _, _ = load_model(modname)
    X, learn_options = get_features(dtype, X)
    X, featdims, totdims, feature_names = azimuth.util.concatenate_feature_sets(X)
    preds = mod.predict(X)
    np.savetxt(outfile, preds)


if __name__ == '__main__':
    main()
