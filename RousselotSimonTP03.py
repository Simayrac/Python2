annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12] 
annee.pop()
annee.pop()
annee.pop()
annee.extend(['Octobre', 'Novembre', 'Décembre'])
print(annee)


annee2= ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12] 
annee2[-3:] = ['Octobre', 'Novembre', 'Décembre']
print(annee2)


moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre') 
print(moisDeLannee[3])
print('mars' in moisDeLannee)
print('Mars' in moisDeLannee)


age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23, "david" : 22 , "veronique" : 21 , "sylvie" : 30 , "damien" : 37} 
print(age["sylvie"])
print('jean' in age)



club = {}
club['pierre durand'] = (1986, 1.72, 70)
club['victor dupont'] = (1987, 1.89, 57)
club['paul dupuis'] = (1989, 1.60, 92)
club['jean rieux'] = (1985, 1.88, 77)

varTuple = club['paul dupuis']
dateNaissSportif, tailleSportif, poidsSportif = varTuple
formatDonnees = f"Le sportif nommé Paul Dupuis est né en {dateNaissSportif}, sa taille est de {tailleSportif}m et son poids est de {poidsSportif}Kg"
print(formatDonnees)



nomSportif = input("Entrez le nom du sportif : ")
if nomSportif in club:
    dateNaissSportif, tailleSportif, poidsSportif = club[nomSportif]
    formatDonnees = f"Le sportif nommé {nomSportif.title()} est né en {dateNaissSportif}, sa taille est de {tailleSportif}m et son poids est de {poidsSportif}Kg"
    print(formatDonnees)
else:
    print("Ce sportif n'existe pas dans la base de données.")