def valeur_max_min():
    liste_L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    max_val = liste_L[0]
    min_val = liste_L[0]

    for i in liste_L:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val, min_val

resultat_max, resultat_min = valeur_max_min()
print("Valeur maximale :", resultat_max)
print("Valeur minimale :", resultat_min)
