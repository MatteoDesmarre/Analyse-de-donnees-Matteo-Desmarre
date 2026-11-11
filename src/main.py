#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")
print("Résultat sur le calcul d'un intervalle de fluctuation")


print("\nQUESTION 1 — Intervalles de fluctuation")
echantillons = ouvrirUnFichier("C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-04\src\data\Echantillonnage-100-Echantillons.csv")

# Moyenne par opinion, arrondie à l'entier avec round()
moyennes = echantillons.mean().round()
print("Moyennes arrondies :")
print(moyennes)

# Fréquences calculées à partir des moyennes arrondies
frequences_moyennes = moyennes / moyennes.sum()

# Population réelle : les effectifs sont dans le CSV fourni
population = ouvrirUnFichier(
    r"C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-04\src\data\Echantillonnage-Population-reelle.csv"
) if False else pd.read_csv(
    r"C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-04\src\data\Echantillonnage-Population-reelle.csv",
    header=None
)

frequences = population.iloc[:, 0] / population.iloc[:, 0].sum()


print("\nFréquences issues des moyennes :")
print(frequences_moyennes.round(2))
print("Fréquences de la population réelle :")
print(frequences.round(2))

# Les 100 échantillons ont chacun une taille de 1000.
zC = 1.96

for i in range(3):
    p = frequences.iloc[i]
    marge = zC * math.sqrt(p * (1 - p) / 1000)

    print(round(p - marge, 2), "-", round(p + marge, 2))

# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")
print("Résultat sur le calcul d'un intervalle de confiance")

echantillon = list(echantillons.iloc[0])

for i in range(3):
    p = echantillon[i] / 1000
    marge = 1.96 * math.sqrt(p * (1 - p) / 1000)

    print(echantillons.columns[i])
    print("Fréquence :", round(p, 2))
    print("Intervalle de confiance :", round(p - marge, 2), "-", round(p + marge, 2))

# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")
test1 = ouvrirUnFichier(r"C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-04\src\data\Loi-normale-Test-1.csv")
test2 = ouvrirUnFichier(r"C:\Desmarre-Matteo-2026-2027-Analyse-de-donnees\Seance-04\src\data\Loi-normale-Test-2.csv")

resultat1 = scipy.stats.shapiro(test1.iloc[:, 0])
resultat2 = scipy.stats.shapiro(test2.iloc[:, 0])

print("Test 1 :", resultat1)
print("Test 2 :", resultat2)

# Question bonus
print("Question bonus")
