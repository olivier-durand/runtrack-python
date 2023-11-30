def valeur_paire():
    liste_L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    addition = 0
    for i in liste_L:
        if i % 2 == 0:
            addition += i
    return addition

resultat = valeur_paire()
print(resultat)
