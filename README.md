# Mini-projet Python : netstat -a

## Description
Ce projet Python analyse des fichiers CSV issus de la commande réseau `netstat -a`. Il permet de filtrer, manipuler et exporter des données réseau (protocole, adresses IP, ports, etc.) à partir de fichiers CSV, en automatisant des tâches courantes d'analyse réseau.

## Fonctionnalités principales
- **Lecture de fichiers CSV** : Importation des données réseau dans une structure de listes.
- **Affichage et parcours** : Visualisation des données ligne par ligne ou sous forme de sous-listes.
- **Extraction de ports** : Récupération du numéro de port à partir d'une adresse IP:PORT.
- **Filtrage avancé** :
  - Filtrer par protocole (ex : TCP)
  - Filtrer par numéro de port supérieur à une valeur
  - Filtrer par plage de ports
- **Export CSV** : Génération de nouveaux fichiers CSV à partir des résultats filtrés.
- **Manipulation de chaînes** : Extraction du préfixe (IP) ou du suffixe (port) d'une adresse.

## Utilisation
1. Placez le fichier CSV à analyser (ex : `netstat_a.csv`) dans le même dossier que le script principal.
2. Exécutez le script `netstat_mini_projet.py`.
3. Les fichiers filtrés seront générés automatiquement :
   - `proto_TCP.csv` : lignes TCP
   - `local_port_gt_49700.csv` : ports locaux > 49700
   - `local_port_lt_512.csv` : ports locaux < 512

## Structure du projet
```
projet python/
├── netstat_mini_projet.py
├── netstat_a.csv
├── proto_TCP.csv
├── local_port_gt_49700.csv
├── local_port_lt_512.csv
```

## Exemples de commandes et fonctions
- `lire_fichier_csv(chemin)` : lit le fichier CSV et retourne la liste globale.
- `fonctionEgale(liste, numCol, filtre)` : filtre les lignes selon une valeur exacte.
- `fonctionSup(liste, numCol, seuil)` : filtre les lignes dont le port est supérieur au seuil.
- `fonctionPlage(liste, numCol, borne1, borne2)` : filtre les lignes selon une plage de ports.
- `creer_fichier(liste, fichier, mode, ...)` : exporte le résultat filtré dans un nouveau CSV.

## Auteur
Simon Rousselot

## Prérequis
- Python 3.x
- Fichier CSV au format attendu (colonnes séparées par des virgules, adresses IP:PORT)

## Licence
Projet pédagogique, libre d'utilisation pour l'apprentissage.
