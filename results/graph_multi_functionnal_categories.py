import importlib.util
import numpy as np
from matplotlib import pyplot as plt

#import fonctions
relative_path = "../scripts/process_roary_file.py"
spec = importlib.util.spec_from_file_location("process_roary_file", relative_path)
process_roary_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process_roary_file)

titles = ['SRR5329951', 'SRR8182677', 'SRR6482979', 'SRR16993378', 'SRR16993379', 'hybride']
X = ['Transposases/hypothetical proteins', 'Autres']

# graph 1
data1 = process_roary_file.all_mixed_annotation_specific_bactopia[0]
data2 = process_roary_file.all_mixed_annotation_specific_asa3p[0]
data3 = process_roary_file.all_mixed_annotation_specific_nullarbor[0]
data1_counts = process_roary_file.count_occurrences(data1)
data2_counts = process_roary_file.count_occurrences(data2)
data3_counts = process_roary_file.count_occurrences(data3)
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
X_axis = np.arange(len(X))
axs[0, 0].bar(X_axis - 0.2, data1_counts, 0.2, color='lightgray', label='Bactopia')
axs[0, 0].bar(X_axis + 0, data2_counts, 0.2, color='grey', label='ASA3P')
axs[0, 0].bar(X_axis + 0.2, data3_counts, 0.2, color='darkgray', label='Nullarbor')
axs[0, 0].set_xticks(X_axis)
axs[0, 0].set_xticklabels(X)
axs[0, 0].set_ylabel("Nombre de gènes")
axs[0, 0].set_title("A. SRR5329951")
axs[0, 0].legend()

# graph 2
data4 = process_roary_file.all_mixed_annotation_specific_bactopia[2]
data5 = process_roary_file.all_mixed_annotation_specific_asa3p[3]
data4_counts = process_roary_file.count_occurrences(data4)
data5_counts = process_roary_file.count_occurrences(data5)
data6_counts = (0, 0)
X_axis2 = np.arange(len(X))
axs[0, 1].bar(X_axis2 - 0.2, data4_counts, 0.2, color='lightgray', label='Bactopia')
axs[0, 1].bar(X_axis2 + 0, data5_counts, 0.2, color='grey', label='ASA3P')
axs[0, 1].bar(X_axis2 + 0.2, data6_counts, 0.2, color='darkgray', label='Nullarbor')
axs[0, 1].set_xticks(X_axis2)
axs[0, 1].set_xticklabels(X)
axs[0, 1].set_ylabel("Nombre de gènes")
axs[0, 1].set_title("B. SRR8182677")
axs[0, 1].legend()

# graph 3
data = process_roary_file.all_mixed_annotation_specific_asa3p[2]
data2 = process_roary_file.all_mixed_annotation_specific_nullarbor[1]
data4_counts = (0, 0)
data5_counts = process_roary_file.count_occurrences(data)
data6_counts = process_roary_file.count_occurrences(data2)
X_axis2 = np.arange(len(X))
axs[0, 2].bar(X_axis2 - 0.2, data4_counts, 0.2, color='lightgray', label='Bactopia')
axs[0, 2].bar(X_axis2 + 0, data5_counts, 0.2, color='grey', label='ASA3P')
axs[0, 2].bar(X_axis2 + 0.2, data6_counts, 0.2, color='darkgray', label='Nullarbor')
axs[0, 2].set_xticks(X_axis2)
axs[0, 2].set_xticklabels(X)
axs[0, 2].set_ylabel("Nombre de gènes")
axs[0, 2].set_title("C. SRR6482979")
axs[0, 2].legend()

# graph 4
data4 = process_roary_file.all_mixed_annotation_specific_bactopia[4]
data5 = process_roary_file.all_mixed_annotation_specific_asa3p[5]
data6 = process_roary_file.all_mixed_annotation_specific_nullarbor[2]
data4_counts = process_roary_file.count_occurrences(data4)
data5_counts = process_roary_file.count_occurrences(data5)
data6_counts = process_roary_file.count_occurrences(data6)
X_axis2 = np.arange(len(X))
axs[1, 0].bar(X_axis2 - 0.2, data4_counts, 0.2, color='lightgray', label='Bactopia')
axs[1, 0].bar(X_axis2 + 0, data5_counts, 0.2, color='grey', label='ASA3P')
axs[1, 0].bar(X_axis2 + 0.2, data6_counts, 0.2, color='darkgray', label='Nullarbor')
axs[1, 0].set_xticks(X_axis2)
axs[1, 0].set_xticklabels(X)
axs[1, 0].set_ylabel("Nombre de gènes")
axs[1, 0].set_title("D. SRR16993379 - Illumina")
axs[1, 0].legend()

# graph 5
data4 = process_roary_file.all_mixed_annotation_specific_bactopia[3]
data5 = process_roary_file.all_mixed_annotation_specific_asa3p[4]
data4_counts = process_roary_file.count_occurrences(data4)
data5_counts = process_roary_file.count_occurrences(data5)
data6_counts = (0, 0)
X_axis2 = np.arange(len(X))
axs[1, 1].bar(X_axis2 - 0.2, data4_counts, 0.2, color='lightgray', label='Bactopia')
axs[1, 1].bar(X_axis2 + 0, data5_counts, 0.2, color='grey', label='ASA3P')
axs[1, 1].bar(X_axis2 + 0.2, data6_counts, 0.2, color='darkgray', label='Nullarbor')
axs[1, 1].set_xticks(X_axis2)
axs[1, 1].set_xticklabels(X)
axs[1, 1].set_ylabel("Nombre de gènes")
axs[1, 1].set_title("E. SRR16993378 - ONT")
axs[1, 1].legend()

# graph 6
data4 = process_roary_file.all_mixed_annotation_specific_bactopia[1]
data5 = process_roary_file.all_mixed_annotation_specific_asa3p[1]
data4_counts = process_roary_file.count_occurrences(data4)
data5_counts = process_roary_file.count_occurrences(data5)
data6_counts = (0, 0)
X_axis2 = np.arange(len(X))
axs[1, 2].bar(X_axis2 - 0.2, data4_counts, 0.2, color='lightgray', label='Bactopia')
axs[1, 2].bar(X_axis2 + 0, data5_counts, 0.2, color='grey', label='ASA3P')
axs[1, 2].bar(X_axis2 + 0.2, data6_counts, 0.2, color='darkgray', label='Nullarbor')
axs[1, 2].set_xticks(X_axis2)
axs[1, 2].set_xticklabels(X)
axs[1, 2].set_ylabel("Nombre de gènes")
axs[1, 2].set_title("B. hybride")
axs[1, 2].legend()

#plot
plt.tight_layout()
plt.show()
