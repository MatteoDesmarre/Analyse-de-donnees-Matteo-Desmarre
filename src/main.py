#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def tableauDeContingence(nom, donnees):
    indexValeurs = {}
    for element in range(0,len(nom)):
        indexValeurs.update({element: nom[element]})
    return pd.DataFrame(donnees).rename(index = indexValeurs)

def sommeDesColonnes(tableau):
    colonne = list(tableau.head(0))
    sommeColonne = []
    for element in colonne:
        sommeColonne.append(tableau[element].sum())
    return sommeColonne

def sommeDesLignes(tableau):
    colonne = list(tableau.head(0))
    sommeLigne = []
    for element1 in range(0,len(tableau)):
        ligne = []
        for element2 in range(0,len(colonne)):
            ligne.append(tableau.iloc[element1, element2])
        sommeLigne.append(np.sum(list(ligne)))
    return sommeLigne

data = pd.DataFrame(ouvrirUnFichier("./data/Socioprofessionnelle-vs-sexe.csv"))
# print(data)

# Création du tableau de contingence
# Contrairement à l'usage, vous ne devez pas créer de tableau croisé dynamique, puisque le fichier est déjà un tableau de contingence
tableauDeContingence = tableauDeContingence(data["Catégorie"], {"Femmes": data["Femmes"], "Hommes": data["Hommes"]})
print(tableauDeContingence)

# Question 1
print("Question 1")
# Calculer les marges
print("Somme des colonnes :", sommeDesColonnes(tableauDeContingence))
print("Somme des lignes :", sommeDesLignes(tableauDeContingence))

# Question 2
print("Question 2")
# Vérification du calcul des marges
if sum(sommeDesLignes(tableauDeContingence)) == sum(sommeDesColonnes(tableauDeContingence)):
    print("Les totaux des marges sont identiques.")
else:
    print("Les totaux des marges sont différents.")

# Question 3
print("Question 3")
# Faire le test du chi2 avec les outils Scipy.stats
resultat = scipy.stats.chi2_contingency(tableauDeContingence)

print("Chi2 :", resultat.statistic)
print("p-value :", resultat.pvalue)

if resultat.pvalue < 0.05:
    print("Il existe une liaison entre le sexe et la catégorie socioprofessionnelle.")
else:
    print("Il n'y a pas de liaison significative entre le sexe et la catégorie socioprofessionnelle.")

# Question 4
print("Question 4")
# Calculer l'intensité de liaison phi2 de Pearson
phi2 = resultat.statistic / sum(sommeDesLignes(tableauDeContingence))

print("Intensité de liaison phi² de Pearson :", phi2)
