import numpy as np

try:
    import azimuth.model_comparison
except:
    import sys
    sys.path.insert(1, "../Azimuth/")
    import azimuth.model_comparison

sequences = np.array(['ACAGCTGATCTCCAGATATGACCATGGGTT', 'CAGCTGATCTCCAGATATGACCATGGGTTT', 'CCAGAAGTTTGAGCCACAAACCCATGGTCA'])
predictions = azimuth.model_comparison.predict(sequences)

for i, pred in enumerate(predictions):
    print sequences[i], pred
