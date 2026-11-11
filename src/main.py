#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1
print("Question 1")

# "Annee"
# "Pouvoir_d_achat_par_unite_de_consommation"
# "Pouvoir_d_achat_du_revenu_disponible_brut"
data = ouvrirUnFichier("C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-06\src\data\Revenu-vs-pouvoir.csv")

colonnes = data[["Pouvoir_d_achat_par_unite_de_consommation","Pouvoir_d_achat_du_revenu_disponible_brut"]]

print(colonnes)

# Question 2
print("Question 2")
# Calcul de la régression linéaire pour la méthode des moindres carrées 1

# Calcul de la droite de régression 1

# Calcul de la régression linéaire pour la méthode des moindres carrées 2

# Calcul de la droite de régression 2

# Charger les données
data = ouvrirUnFichier("C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-06\src\data\Revenu-vs-pouvoir.csv")

# Première régression linéaire
x = data["Pouvoir_d_achat_par_unite_de_consommation"]
y = data["Pouvoir_d_achat_du_revenu_disponible_brut"]

regression1 = scipy.stats.linregress(x, y)
print(regression1)

# Deuxième régression en inversant les variables
regression2 = scipy.stats.linregress(y, x)
print(regression2)

# Question 3
print("Question 3")
# Calcul du coefficient de corrélation 1
print(data["Pouvoir_d_achat_par_unite_de_consommation"].corr(data["Pouvoir_d_achat_du_revenu_disponible_brut"]))

# Calcul du coefficient de corrélation 2
print(data["Pouvoir_d_achat_du_revenu_disponible_brut"].corr(data["Pouvoir_d_achat_par_unite_de_consommation"]))


# Question 4
print("Question 4")
# Calcul du graphique 1
plt.scatter(x, y)
plt.plot(x, regression1.intercept + regression1.slope * x)
plt.savefig("img/graphique1.png")
plt.show()
plt.close()
# Calcul du graphique 2
plt.scatter(y, x)
plt.plot(y, regression2.intercept + regression2.slope * y)
plt.savefig("img/graphique2.png")
plt.show()
plt.close()
# Question bonus
print("Question Bonus")
