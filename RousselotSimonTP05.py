# def generer_table(table_num):
#     termes = []
#     for i in range(1, 11):
#         termes.append(f"{i}*{table_num} = {i*table_num}")
#     return " | ".join(termes) + " |"

# nom_fichier = input("Entrez le nom du fichier pour enregistrer les tables de multiplication : ")

# with open(nom_fichier, "w", encoding="utf-8") as f:
#     for n in range(2, 31):
#         f.write(generer_table(n) + "\n")

# with open("lorem_ipsum.txt", "r", encoding="utf-8") as f:
#     lignes = f.readlines()

# max_len = 0
# max_index = 0
# max_phrase = ""

# for idx, ligne in enumerate(lignes, start=1):
#     longueur = len(ligne.rstrip('\n'))
#     if longueur > max_len:
#         max_len = longueur
#         max_index = idx
#         max_phrase = ligne.rstrip('\n')

# print(f"La ligne la plus longue est la {max_index}eme,")
# print(f"Elle contient {max_len} caractères, la voici :")
# print(max_phrase)



# def nbMots(chaine):
#     count = 0
#     in_word = False
#     for c in chaine:
#         if c.isspace():
#             in_word = False
#         elif not in_word:
#             count += 1
#             in_word = True
#     return count

# with open("lorem_ipsum.txt", "r", encoding="utf-8") as f:
#     lignes = f.readlines()

# max_len = 0
# max_index = 0
# max_phrase = ""
# max_mots = 0
# max_mots_index = 0
# max_mots_phrase = ""

# for idx, ligne in enumerate(lignes, start=1):
#     phrase = ligne.rstrip('\n')
#     longueur = len(phrase)
#     nb_mots = nbMots(phrase)
#     print(f"Ligne n°:{idx}, longueur = {longueur}, {nb_mots} mots.")
#     if longueur > max_len:
#         max_len = longueur
#         max_index = idx
#         max_phrase = phrase
#     if nb_mots > max_mots:
#         max_mots = nb_mots
#         max_mots_index = idx
#         max_mots_phrase = phrase

# print(f"La ligne la plus longue est la {max_index}eme,")
# print(f"Elle contient {max_len} caractères, la voici :")
# print(max_phrase)
# print(f"La ligne ayant le plus de mots est la {max_mots_index}eme,")
# print(f"Elle contient {max_mots} mots, la voici :")
# print(max_mots_phrase)


# def nbMots(chaine):
#     return len(list(filter(lambda mot: mot, [mot.strip() for mot in chaine.split()])))

# # Test de la nouvelle fonction
# with open("lorem_ipsum.txt", "r", encoding="utf-8") as f:
#     lignes = f.readlines()

# max_len = 0
# max_index = 0
# max_phrase = ""
# max_mots = 0
# max_mots_index = 0
# max_mots_phrase = ""

# for idx, ligne in enumerate(lignes, start=1):
#     phrase = ligne.rstrip('\n')
#     longueur = len(phrase)
#     nb_mots = nbMots(phrase)
#     print(f"Ligne n°:{idx}, longueur = {longueur}, {nb_mots} mots.")
#     if longueur > max_len:
#         max_len = longueur
#         max_index = idx
#         max_phrase = phrase
#     if nb_mots > max_mots:
#         max_mots = nb_mots
#         max_mots_index = idx
#         max_mots_phrase = phrase

# print(f"La ligne la plus longue est la {max_index}eme,")
# print(f"Elle contient {max_len} caractères, la voici :")
# print(max_phrase)
# print(f"La ligne ayant le plus de mots est la {max_mots_index}eme,")
# print(f"Elle contient {max_mots} mots, la voici :")
# print(max_mots_phrase)

# def arrondir_chaine(chaine):
#     try:
#         return str(round(float(chaine.strip())))
#     except ValueError:
#         return chaine.strip()

# with open("listeNombres.txt", "r", encoding="utf-8") as fin, open("listeNombresArrondis.txt", "w", encoding="utf-8") as fout:
#     for ligne in fin:
#         fout.write(arrondir_chaine(ligne) + "\n")


with open("lorem_ipsum.txt", "r", encoding="utf-8") as f1, open("lorem_ipsumModifie.txt", "r", encoding="utf-8") as f2:
    contenu1 = f1.read()
    contenu2 = f2.read()

min_len = min(len(contenu1), len(contenu2))
diff_found = False

for i in range(min_len):
    if contenu1[i] != contenu2[i]:
        print(f"Ces 2 fichiers diffèrent à partir du caractère n°{i+1}")
        diff_found = True
        break

if not diff_found:
    if len(contenu1) != len(contenu2):
        print(f"Ces 2 fichiers diffèrent à partir du caractère n°{min_len+1}")
    else:
        print("Ces 2 fichiers sont identiques.")