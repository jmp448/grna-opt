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
    sequences = np.loadtxt()

def predict_efficacy():

def compare_preds():

def main():

if __name__=="__main__":
    main()
