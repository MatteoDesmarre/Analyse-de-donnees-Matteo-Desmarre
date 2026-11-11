#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding='utf-8') as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

# Question 2
print("Question 2")

# "Country Name" : nom du territoire
# "Country Code" : code ISO du territoire
# "Continent" : nom du continent
# "1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024" : une colonne par année

data = ouvrirUnFichier("C:/Desmarre-Matteo-2026-2027-Analyse-de-donnees/Seance-05/src/data/Nombre-moyen-d-enfants-par-femme-par-territoire.csv")

# Question 3
print("Question 3")
population = data["2024"]

# Question 4
print("Question 4")
population = ordreDecroissant(list(population))

# Question 5
print("Question 5")
plt.plot(range(1, len(population) + 1), population, 'o')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Rang")
plt.ylabel("Nombre moyen d'enfants par femme")
plt.title("Loi rang-taille")
plt.savefig("loi_rang_taille.png")
plt.show()

# Question 6
print("Question 6")
population = conversionLog(population)

# Question 7
print("Question 7")
# Mettre ici votre réponse argumentée
# Non, il n'est pas possible de faire un test sur les rangs, car ils sont déjà ordonnés.

# Question 9
print("Question 9")
data = ouvrirUnFichier("C:/Desmarre-Matteo-2026-2027-Analyse-de-donnees/Seance-05/src/data/Le-Monde-HS-Etats-du-monde-2007-2026.csv")

# Question 10
print("Question 10")
data = data[["État", "Pop 2007", "Pop 2026", "Densité 2007", "Densité 2026"]]

# Question 11
print("Question 11")
etat = list(data["État"])

pop2007 = ordrePopulation(list(data["Pop 2007"]), etat)
pop2026 = ordrePopulation(list(data["Pop 2026"]), etat)
densite2007 = ordrePopulation(list(data["Densité 2007"]), etat)
densite2026 = ordrePopulation(list(data["Densité 2026"]), etat)

# Question 12
print("Question 12")
classementPop = classementPays(pop2007, pop2026)
classementDensite = classementPays(densite2007, densite2026)

classementPop.sort()
classementDensite.sort()

# Question 13
print("Question 13")
differentPop = []
differentDensite = []

for element in classementPop:
    differentPop.append([element[0], element[1]])

for element in classementDensite:
    differentDensite.append([element[0], element[1]])

# Question 14
print("Question 14")
print("Population :")
print(scipy.stats.spearmanr(differentPop[0], differentPop[1]))
print(scipy.stats.kendalltau(differentPop[0], differentPop[1]))

print("Densité :")
print(scipy.stats.spearmanr(differentDensite[0], differentDensite[1]))
print(scipy.stats.kendalltau(differentDensite[0], differentDensite[1]))

# Question Bonus
print("Question Bonus")
