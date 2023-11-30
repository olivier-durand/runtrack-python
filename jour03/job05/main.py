def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Opérateur non valide"

resultat = calcule(8, '+', 25)
print(resultat)

resultat = calcule(143, '/', 2)
print(resultat)

resultat = calcule(130, '*', 4)
print(resultat)
