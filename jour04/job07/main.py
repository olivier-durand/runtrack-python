def nombre_multiple_3():
    liste_L = [8, 24, 48, 2, 16]
    compte = 0
    for i in liste_L:
        if i %3 == 0:
          compte += 1
    return compte

resultat = nombre_multiple_3()
print(resultat)        
