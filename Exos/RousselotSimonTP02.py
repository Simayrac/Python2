print("4.A accès aux éléments d'une chaine")
ch = "Esope reste ici et se repose"
print(len(ch))
print(ch[6:11])
print(ch[21:])
print(ch[13])


meteo = "aujourd'hui, il fait {} , la vitesse du vent est {} ,l'humidité est {}"
tempDeg = "24°" 
vent = "12kmh"
humidite = "45%"
temp = "beau"
vent2 = "faible"
humi = "correcte"
print(meteo.format(tempDeg, vent, humidite))
print(meteo.format(temp, vent2, humi))



chaineA = "cette chaine " 
chaineB = "contient {} caractères" 
chaineC = "par contre" 
chaineD = "celle-ci " 

print(chaineA + chaineB.format(len(chaineA + chaineB)) + "\net\n" + chaineD + chaineB.format(len(chaineD + chaineB)) + chaineC)

chaineE = 'un deux trois quatre'
chaineE = chaineE.replace('trois', '3')
chaineEnew = chaineE.replace('quatre', '4')
print(chaineEnew) 

