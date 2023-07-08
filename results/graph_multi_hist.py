import matplotlib.pyplot as plt
import numpy as np

#valeurs négatives = barre rouge négative
def plot_negative_values(ax, data):
    for i, value in enumerate(data):
        if value < 0:
            ax.text(i, value - 0.5, str(value), ha='center', va='top', color='red')

#roary
souches_A = ['SRR8182677', 'SRR5329951', 'SRR6482979', 'SRR16993378', 'SRR16993379', 'hybride']
bactopia_genes_A = [10, 13, -10, 584, 8, 6]
asap_genes_A = [36, 123, 1406, 392, 44, 10]
nullarbor_genes_A = [-10, 10, 17, -10, 5, -10]

#quast
souches_B = ['SRR8182677', 'SRR5329951', 'SRR6482979', 'SRR16993378', 'SRR16993379', 'hybride']
bactopia_genes_B = [23, -10, -10, 2, 5, 0]
asap_genes_B = [50, -10, 792, 0, 31, 0]
nullarbor_genes_B = [-10, -10, 5, -10, 3, -10]

figure, (ax1, ax2) =  plt.subplots(1, 2, figsize=(20, 8))
bar_width = 0.3
colors = ['#A9A9A9', '#808080', '#D3D3D3']

#roary
ax1.bar(np.arange(len(souches_A)), bactopia_genes_A, width=bar_width, label='Bactopia', color=np.where(np.array(bactopia_genes_A) < 0, 'red', colors[0]))
ax1.bar(np.arange(len(souches_A)) + bar_width, asap_genes_A, width=bar_width, label='ASAP', color=np.where(np.array(asap_genes_A) < 0, 'red', colors[1]))
ax1.bar(np.arange(len(souches_A)) + (2 * bar_width), nullarbor_genes_A, width=bar_width, label='Nullarbor', color=np.where(np.array(nullarbor_genes_A) < 0, 'red', colors[2]))
ax1.set_ylabel('Nombre de gènes annotés spécifiques à chaque pipeline')
ax1.set_title('A.\n', loc='left', fontweight='bold')
ax1.set_xticks(np.arange(len(souches_A)) + 1.5 * bar_width)
ax1.set_xticklabels(souches_A)
legend_labels = ['Bactopia', 'ASAP', 'Nullarbor']
ax1.legend(handles=[plt.Rectangle((0, 0), 1, 1, color='red'), plt.Rectangle((0, 0), 1, 1, color=colors[2])] + [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(colors)-1)], labels=['Non traitée', 'Nullarbor'] + legend_labels, loc='upper left')
plot_negative_values(ax1, bactopia_genes_A)
plot_negative_values(ax1, asap_genes_A)
plot_negative_values(ax1, nullarbor_genes_A)

#quast
ax2.bar(np.arange(len(souches_B)), bactopia_genes_B, width=bar_width, label='Bactopia', color=np.where(np.array(bactopia_genes_B) < 0, 'red', colors[0]))  # Barres pour Bactopia
ax2.bar(np.arange(len(souches_B)) + bar_width, asap_genes_B, width=bar_width, label='ASAP', color=np.where(np.array(asap_genes_B) < 0, 'red', colors[1]))  # Barres pour ASAP
ax2.bar(np.arange(len(souches_B)) + (2 * bar_width), nullarbor_genes_B, width=bar_width, label='Nullarbor', color=np.where(np.array(nullarbor_genes_B) < 0, 'red', colors[2]))  # Barres pour Nullarbor
ax2.set_ylabel('Nombre de gènes annotés spécifiques à chaque pipeline')
ax2.set_title('B.\n', loc='left', fontweight='bold')
ax2.set_xticks(np.arange(len(souches_B)) + 1.5 * bar_width)
ax2.set_xticklabels(souches_B)
ax2.legend(handles=[plt.Rectangle((0, 0), 1, 1, color='red'), plt.Rectangle((0, 0), 1, 1, color=colors[2])] + [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(colors)-1)], labels=['Non traitée', 'Nullarbor'] + legend_labels, loc='upper left')
plot_negative_values(ax2, bactopia_genes_B)
plot_negative_values(ax2, asap_genes_B)
plot_negative_values(ax2, nullarbor_genes_B)

plt.show()
