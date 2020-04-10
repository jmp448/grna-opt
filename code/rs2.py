try:
    import azimuth.model_comparison
except:
    import sys
    sys.path.insert(1, "../Azimuth/")
    import azimuth.model_comparison

sequences = np.array(['ACAGCTGATCTCCAGATATGACCATGGGTT', 'CAGCTGATCTCCAGATATGACCATGGGTTT', 'CCAGAAGTTTGAGCCACAAACCCATGGTCA'])
amino_acid_cut_positions = np.array([2, 2, 4])
percent_peptides = np.array([0.18, 0.18, 0.35])
predictions = azimuth.model_comparison.predict(sequences, amino_acid_cut_positions, percent_peptides)

for i, prediction in enumerate(predictions):
    print sequences[i], prediction
