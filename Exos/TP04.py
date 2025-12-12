# import math

# for _ in range(50):
#     print("facile !")
    
    
    
#     for _ in range(25):
#         print("*", end='')
#    print()

    
    
#    for i in range(21, 146):
#        print(i)

        
#         for i in range(1, 41):
#             print(f"le carre de {i} = {i**2}")

            
# somme = sum(range(21, 146))
# print(f"La somme de tous les entiers de 21 à 145 est {somme}")
# fact_35 = math.factorial(35)
# print(f"35! = {fact_35}")



# for i in range(1, 16):
#     print('*' * i)


#  dicoAF = {}
#  while True:
#      anglais = input("Entrez un mot anglais : ")
#      francais = input("Entrez sa traduction en français : ")
#      dicoAF[anglais] = francais
#      continuer = input("Voulez-vous continuer à saisir des mots ? (o pour oui) : ")
#      if continuer.lower() != 'o':
#          break

#  print(f"Nombre d'éléments dans le dictionnaire : {len(dicoAF)}")
#  for k, v in dicoAF.items():
#      print(k, v)



# dicoAF = {}
# while True:
#     anglais = input("Entrez un mot anglais (ou '$' pour terminer) : ")
#     if anglais == '$':
#         break
#     francais = input("Entrez sa traduction en français : ")
#     dicoAF[anglais] = francais

# print(f"Nombre d'éléments dans le dictionnaire : {len(dicoAF)}")
# for k, v in dicoAF.items():
#     print(k, v)

dicoAF = {}
while True:
        anglais = input("Entrez un mot anglais (ou '$' pour terminer) : ")
        if anglais == '$':
            break
        francais = input("Entrez sa traduction en français : ")
        dicoAF[anglais] = francais
    
n = len(dicoAF)
if n == 1:
        print(f"Le dictionnaire contient {n} entrée")
else:
        print(f"Le dictionnaire contient {n} entrées")
for k, v in dicoAF.items():
        print(k, v)