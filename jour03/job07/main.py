def langage(valeur_langage):
    if valeur_langage == "JavaScript":
        return "tu es un développeur web"
    elif valeur_langage == "python":
        return "tu es un développeur IA"
    elif valeur_langage == "java":
        return "tu es un développeur logiciel"
    elif valeur_langage == "reactjs":
        return "tu es un développeur mobile"
    else:
        return "un jour, je serai le meilleur développeur..."

resultat = langage("python")
print(resultat)