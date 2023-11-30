def moyenne(note1, note2, note3):
    moyenne = (note1 + note2 + note3) / 3
    return moyenne

def evaluer_moyenne(moyenne):
    if 15 <= moyenne <= 20:
        return "Très bon élève"
    elif 11 <= moyenne <= 14:
        return "Bon élève"
    elif 8 <= moyenne <= 10:
        return "Élève moyen"
    elif 0 <= moyenne <= 7:
        return "Élève devant faire des efforts"

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_calcul = moyenne(note1, note2, note3)
resultat = evaluer_moyenne(moyenne_calcul)

print(f"La moyenne de l'étudiant est : {moyenne_calcul}")
print(f"Appréciation : {resultat}")