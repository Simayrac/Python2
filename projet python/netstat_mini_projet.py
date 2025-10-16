# =====================================================================
# Mini-projet Python : netstat -a
# Auteur : (à compléter)
# Fichier : netstat_mini_projet.py
# =====================================================================

from pathlib import Path
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------
# 2.1 - Lecture du fichier CSV et création de la liste globale
# ---------------------------------------------------------------------

def lire_fichier_csv(chemin: str) -> List[List[str]]:
    """
    Lit un fichier CSV ligne par ligne, affiche un '*' pour chaque ligne,
    et retourne une liste de listes (listeGlobale).
    """
    listeGlobale = []
    compteur = 0
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            compteur += 1
            print("*", end="")
            listeGlobale.append(ligne.strip().split(","))
    print("\nNombre total de lignes :", compteur)
    return listeGlobale


# ---------------------------------------------------------------------
# 2.2.1 - Parcours de la listeGlobale
# ---------------------------------------------------------------------

def parcours(liste: List[List[str]]) -> None:
    """Affiche chaque sous-liste contenue dans listeGlobale."""
    for sousListe in liste:
        print(sousListe)


# ---------------------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------------------

def extract_port(chaine: str) -> Optional[int]:
    """Tente d'extraire le numéro de port d'une adresse du type IP:PORT."""
    if ":" not in chaine:
        return None
    try:
        return int(chaine.split(":")[-1])
    except ValueError:
        return None


# ---------------------------------------------------------------------
# 2.2.2 - FonctionEgale
# ---------------------------------------------------------------------

def fonctionEgale(liste: List[List[str]], numCol: int, filtre: str) -> List[List[str]]:
    """
    Retourne les lignes dont la valeur de la colonne numCol est égale à filtre.
    """
    resultat = [liste[0]]  # garder l'en-tête
    for ligne in liste[1:]:
        if numCol < len(ligne) and ligne[numCol] == filtre:
            resultat.append(ligne)
    return resultat


# ---------------------------------------------------------------------
# 2.2.3 - PrefixeSuffixe
# ---------------------------------------------------------------------

def prefixeSuffixe(chaine: str, choix: str) -> str:
    """Retourne le préfixe ou le suffixe d'une chaîne séparée par ':'."""
    if ":" not in chaine:
        return chaine
    prefixe, suffixe = chaine.rsplit(":", 1)
    choix = choix.lower()
    if choix == "prefixe":
        return prefixe
    elif choix == "suffixe":
        return suffixe
    else:
        raise ValueError("Le choix doit être 'prefixe' ou 'suffixe'.")


# ---------------------------------------------------------------------
# 2.2.4 - FonctionSup
# ---------------------------------------------------------------------

def fonctionSup(liste: List[List[str]], numCol: int, seuil: int) -> List[List[str]]:
    """
    Retourne les lignes dont le numéro de port (dans la colonne numCol)
    est supérieur au seuil.
    """
    resultat = [liste[0]]
    for ligne in liste[1:]:
        if numCol >= len(ligne):
            continue
        port = extract_port(ligne[numCol])
        if port is not None and port > seuil:
            resultat.append(ligne)
    return resultat


# ---------------------------------------------------------------------
# 2.2.5 - FonctionPlage
# ---------------------------------------------------------------------

def fonctionPlage(liste: List[List[str]],
                  numCol: int,
                  borne1: Optional[int] = None,
                  borne2: Optional[int] = None) -> List[List[str]]:
    """
    Retourne les lignes selon une plage de valeurs :
    - si une seule borne est donnée -> < ou > selon la borne
    - si deux bornes -> valeurs entre borne1 et borne2
    """
    resultat = [liste[0]]
    for ligne in liste[1:]:
        if numCol >= len(ligne):
            continue
        port = extract_port(ligne[numCol])
        if port is None:
            continue

        if borne1 is not None and borne2 is not None:
            if min(borne1, borne2) <= port <= max(borne1, borne2):
                resultat.append(ligne)
        elif borne1 is not None and port > borne1:
            resultat.append(ligne)
        elif borne2 is not None and port < borne2:
            resultat.append(ligne)
    return resultat


# ---------------------------------------------------------------------
# 2.2.6 - Création d'un fichier CSV à partir d'un filtrage
# ---------------------------------------------------------------------

def creer_fichier(liste: List[List[str]], fichier: str, mode: str, *args) -> Tuple[str, int]:
    """
    Crée un fichier CSV en appliquant une fonction (egale, sup, plage).
    Retourne le nom du fichier et le nombre de lignes écrites.
    """
    mode = mode.lower()
    if mode == "egale":
        lignes = fonctionEgale(liste, *args)
    elif mode == "sup":
        lignes = fonctionSup(liste, *args)
    elif mode == "plage":
        lignes = fonctionPlage(liste, *args)
    else:
        raise ValueError("Mode inconnu : 'egale', 'sup' ou 'plage' attendus.")

    with open(fichier, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(",".join(ligne) + "\n")

    print(f"Fichier '{fichier}' créé avec {len(lignes) - 1} lignes de données.")
    return fichier, len(lignes)


# ---------------------------------------------------------------------
# Programme principal (démo)
# ---------------------------------------------------------------------

if __name__ == "__main__":
    chemin_csv = "netstat_a.csv"  # à placer dans le même dossier que ce script
    listeGlobale = lire_fichier_csv(chemin_csv)
    print("\nEn-tête :", listeGlobale[0])
    print("Aperçu des 5 premières lignes :")
    for ligne in listeGlobale[1:6]:
        print(ligne)

    # Exemples d'utilisation :
    tcp = fonctionEgale(listeGlobale, 0, "TCP")
    creer_fichier(tcp, "proto_TCP.csv", "egale", 0, "TCP")

    ports_sup = fonctionSup(listeGlobale, 1, 49700)
    creer_fichier(ports_sup, "local_port_gt_49700.csv", "sup", 1, 49700)

    ports_faibles = fonctionPlage(listeGlobale, 1, None, 512)
    creer_fichier(ports_faibles, "local_port_lt_512.csv", "plage", 1, None, 512)

    print("\nExemples de prefixe/suffixe :")
    print(prefixeSuffixe("172.17.1.125:52224", "prefixe"))
    print(prefixeSuffixe("172.17.1.125:52224", "suffixe"))
