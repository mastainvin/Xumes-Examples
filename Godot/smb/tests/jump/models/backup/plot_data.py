import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Liste des dossiers contenant les fichiers CSV
dossiers = ['IL_RL', 'RL']

# Créer un dictionnaire pour stocker les données
donnees = {}

# Charger et lisser les données pour chaque fichier dans les dossiers
for dossier in dossiers:
    chemin_fichier = os.path.join(dossier, 'success.csv')
    df = pd.read_csv(chemin_fichier)
    smoothed_values = gaussian_filter1d(df['Value'], sigma=2)
    donnees[dossier] = {
        'step': df['Step'],
        'smoothed_values': smoothed_values
    }

# Créer un graphique comparatif
plt.figure(figsize=(7, 5))  # Ajustez la taille du graphique pour un meilleur ratio

# Ajouter chaque série de données au graphique
for dossier, data in donnees.items():
    plt.plot(data['step'], data['smoothed_values'], label=dossier, linewidth=2)

# Ajouter des étiquettes et un titre
plt.xlabel('Step')
plt.ylabel('Number of Tests passed')
plt.title('Comparison of Test Success During Training: Pre-trained RL vs. Standard RL')

# Ajouter une grille pour améliorer la lisibilité
plt.grid(True, linestyle='--', alpha=0.6)

# Afficher la légende
plt.legend(loc='upper right', fontsize='small')

# Réduire les marges
plt.tight_layout(pad=1.0)

# Sauvegarder le graphique avec des marges réduites
plt.savefig('success_comparison.png', dpi=300, bbox_inches='tight')

# Afficher le graphique
plt.show()