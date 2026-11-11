#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Question 4
print("Question 4")
# Source des données : https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef?tab=1&elems=391f8b4f-bda5-46f9-91e6-abf2fe4c2935 (ou https://doi.org/10.21338/ess11e04_2)
with open("./data/happy-cntry.csv", "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
print("Question 5")
print(pd.DataFrame(contenu))

# Question 6
print("Question 6")
print("Nombre de lignes :", len(contenu))
print("Nombre de colonnes :", len(contenu.columns))

# Question 7
print("Question 7")
print(contenu.columns)

# Question 8
print("Question 8")

# Contenu des colonnes
# "code_ISO" : code ISO à deux caractères du territoire
# "country" : nom du territoire
# "Extremely unhappy" : taux de réponses pour une note de 0 au niveau du bonheur
# "1" : taux de réponses pour une note de 1 au niveau du bonheur
# "2" : taux de réponses pour une note de 2 au niveau du bonheur
# "3" : taux de réponses pour une note de 3 au niveau du bonheur
# "4" : taux de réponses pour une note de 4 au niveau du bonheur
# "5" : taux de réponses pour une note de 5 au niveau du bonheur
# "6" : taux de réponses pour une note de 6 au niveau du bonheur
# "7" : taux de réponses pour une note de 7 au niveau du bonheur
# "8" : taux de réponses pour une note de 8 au niveau du bonheur
# "9" : taux de réponses pour une note de 9 au niveau du bonheur
# "Extremely happy" : taux de réponses pour une note de 10 au niveau du bonheur
types_colonnes = [str, str,float, float, float, float, float, float,float, float, float, float, float]
print(types_colonnes)

# Question 9
print("Question 9")
notes_bonheur = contenu[["Extremely unhappy", "1", "2", "3", "4", "5","6", "7", "8", "9", "Extremely happy"]]
print(notes_bonheur)

# Question 10
print("Question 10")
effectifs = []

for i in range(len(notes_bonheur)):
    total = float(notes_bonheur.iloc[i].sum())
    effectifs.append(total)

print(effectifs)

# Question 11
print("Question 11")
# 11.b - Un diagramme circulaire pour chaque territoire
colonnes_bonheur = ["Extremely unhappy", "1", "2", "3", "4", "5","6", "7", "8", "9", "Extremely happy"]

for i in range(len(contenu)):
    pays = contenu.iloc[i]["country"]

    valeurs = contenu.loc[i, colonnes_bonheur].astype(float)

    plt.figure()
    plt.pie(valeurs, labels=colonnes_bonheur, autopct="%1.1f%%")
    plt.title("Niveau de bonheur - " + pays)
    plt.savefig("./img/" + str(pays) + ".png", bbox_inches="tight")
    plt.close()

# 11.c - Transposition du tableau de données
tableau_transpose = contenu.set_index("country")[colonnes_bonheur].transpose()

print(tableau_transpose)

# Un diagramme en bâtons pour chaque niveau de bonheur
for niveau in tableau_transpose.index:
    tableau = tableau_transpose.loc[[niveau]].transpose()
    ax = tableau.plot.bar(legend=False,figsize=(10, 6))
    ax.set_title("Niveau de bonheur : " + niveau)
    ax.set_xlabel("Territoire")
    ax.set_ylabel("Pourcentage de réponses")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("./img/bonheur_" + str(niveau) + ".png", bbox_inches="tight")
    plt.close()

# Question 12
print("Questions 12 et 14")
# Tableau de données initial
moyennes = []
medianes = []
modes = []
ecarts_types = []
ecarts_absolus_moyenne = []
etendues = []

for colonne in contenu.columns:
    if colonne != "code_ISO" and colonne != "country":
        donnees = contenu[colonne]
        moyennes.append(float(round(donnees.mean(), 2)))
        medianes.append(float(round(donnees.median(), 2)))
        modes.append(float(round(donnees.mode().iloc[0], 2)))
        ecarts_types.append(float(round(donnees.std(), 2)))
        ecarts_absolus_moyenne.append(float(round(np.abs(donnees - donnees.mean()).mean(), 2)))
        etendues.append(float(round(donnees.max() - donnees.min(), 2)))



# Tableau de données transposé
moyennes_transpose = []
medianes_transpose = []
modes_transpose = []
ecarts_types_transpose = []
ecarts_absolus_moyenne_transpose = []
etendues_transpose = []

for colonne in tableau_transpose.columns:
    if colonne != "code_ISO" and colonne != "country":
        donnees = tableau_transpose[colonne]
        moyennes_transpose.append(float(round(donnees.mean(), 2)))
        medianes_transpose.append(float(round(donnees.median(), 2)))
        modes_transpose.append(float(round(donnees.mode().iloc[0], 2)))
        ecarts_types_transpose.append(float(round(donnees.std(), 2)))
        ecarts_absolus_moyenne_transpose.append(float(round(np.abs(donnees - donnees.mean()).mean(), 2)))
        etendues_transpose.append(float(round(donnees.max() - donnees.min(), 2)))

# Question 13
print("Question 13")
print("Moyennes :", moyennes)
print("Médianes :", medianes)
print("Modes :", modes)
print("Écarts types :", ecarts_types)
print("Écarts absolus à la moyenne :", ecarts_absolus_moyenne)
print("Étendues :", etendues)

print("Moyennes :", moyennes_transpose)
print("Médianes :", medianes_transpose)
print("Modes :", modes_transpose)
print("Écarts types :", ecarts_types_transpose)
print("Écarts absolus à la moyenne :", ecarts_absolus_moyenne_transpose)
print("Étendues :", etendues_transpose)

# Question 14
print("Question 14")
# Tableau initial
distances_interquartiles = []
distances_interdeciles = []

for colonne in contenu.columns:
    if colonne != "code_ISO" and colonne != "country":
        donnees = contenu[colonne]

        q1 = donnees.quantile(0.25)
        q3 = donnees.quantile(0.75)
        d1 = donnees.quantile(0.10)
        d9 = donnees.quantile(0.90)

        distances_interquartiles.append(
            round(float(q3 - q1), 2)
        )
        distances_interdeciles.append(
            round(float(d9 - d1), 2)
        )

print("Tableau initial")
print("Distances interquartiles :", distances_interquartiles)
print("Distances interdeciles :", distances_interdeciles)


# Tableau transposé
distances_interquartiles_transpose = []
distances_interdeciles_transpose = []

for colonne in tableau_transpose.columns:
    donnees = tableau_transpose[colonne]

    q1 = donnees.quantile(0.25)
    q3 = donnees.quantile(0.75)
    d1 = donnees.quantile(0.10)
    d9 = donnees.quantile(0.90)

    distances_interquartiles_transpose.append(
        round(float(q3 - q1), 2)
    )
    distances_interdeciles_transpose.append(
        round(float(d9 - d1), 2)
    )

print("Tableau transposé")
print("Distances interquartiles :", distances_interquartiles_transpose)
print("Distances interdeciles :", distances_interdeciles_transpose)

# Question 15
print("Question 15")
for pays in tableau_transpose.columns:
    valeurs = tableau_transpose[pays].astype(float)
    plt.figure()
    plt.boxplot(valeurs)
    plt.title("Boîte à moustaches - " + str(pays))
    plt.ylabel("Pourcentage de réponses")
    plt.xticks([1], [pays])
    plt.tight_layout()
    plt.savefig("./img/boite_moustaches_" + str(pays) + ".png",bbox_inches="tight")
    plt.close()

# Question 16
print("Question 16")
# Intervalles de valeurs en pourcentage
intervalles = [(0, 5),(5, 10),(10, 15),(15, 20),(20, 25),(25, 30),(30, 35),(35, 40),(40, 45)]

# Dictionnaire contenant les résultats pour chaque colonne
resultats = {}

# Parcours des colonnes du tableau initial
for colonne in contenu.columns:

    # Exclusion des colonnes non quantitatives
    if colonne != "code_ISO" and colonne != "country":
        valeurs = contenu[colonne]
        effectifs_intervalles = []

        # Parcours de chaque intervalle
        for borne_inf, borne_sup in intervalles:
            effectif = ((valeurs > borne_inf) & (valeurs <= borne_sup)).sum()
            effectifs_intervalles.append(int(effectif))
        resultats[colonne] = effectifs_intervalles

# Affichage des résultats
for colonne, effectifs in resultats.items():
    print("\nColonne :", colonne)
    for i in range(len(intervalles)):
        borne_inf, borne_sup = intervalles[i]
        print("]" + str(borne_inf) + ", " + str(borne_sup) + "] :",effectifs[i],"valeur(s)")

# Question bonus
print("Question bonus")
