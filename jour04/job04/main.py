def liste_fruits():
    liste_fruits = ["pommes", "cerises", "orange"]
    return liste_fruits 

fruits = liste_fruits()
fruits.append("melon")
fruits.insert(2, "mangue")
print(fruits)
