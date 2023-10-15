#!/bin/bash

# Crée le répertoire de la bibliothèque
mkdir Py_PSIDP-EL
cd Py_PSIDP-EL

# Crée les sous-répertoires
mkdir charges calculs utils exemples

# Crée des fichiers __init__.py dans tous les sous-répertoires
touch charges/__init__.py
touch calculs/__init__.py
touch utils/__init__.py
touch exemples/__init__.py

# Crée les fichiers spécifiques pour chaque sous-répertoire
# Vous pouvez ajouter d'autres fichiers selon vos besoins
touch charges/charges_A.py
touch charges/charges_B.py
touch charges/charges_CE.py
touch charges/charges_trottoirs.py
touch calculs/calcul_portee_maximale.py
touch calculs/calcul_precontrainte_longitudinale.py
touch calculs/verification_precontrainte.py
touch calculs/calcul_ferraillage_longitudinal.py
touch calculs/calcul_ferraillage_transversal.py
touch calculs/verification_etats_limites.py
touch calculs/modification_et_amelioration.py
touch utils/rapport_calcul.py
touch utils/interface_utilisateur.py
touch utils/fonctions_auxiliaires.py
touch exemples/exemple_calcul.py

echo "Structure de la bibliothèque Py_PSIDP-EL créée avec succès!"
