def L():
    liste_L = [1, 2, 3, 4, 5]
    liste_L[3] = liste_L[2] + liste_L[4]
    return liste_L

liste_L = L()
la_deuxieme_valeur = liste_L[1]

print("La deuxième valeur est :", la_deuxieme_valeur)
print(liste_L)


