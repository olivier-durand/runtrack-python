def decaler_message(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''

    for lettre in message:
        if lettre.isalpha():
            est_majuscule = lettre.isupper()
            lettre = lettre.lower()

            index = alphabet.find(lettre)
            if index != -1:  # Si la lettre est trouvée dans l'alphabet
                index = (index + decalage) % 26
                lettre_decalee = alphabet[index]

                if est_majuscule:
                    lettre_decalee = lettre_decalee.upper()

                resultat += lettre_decalee
            else:
                resultat += lettre  # Ajouter la lettre telle quelle (non alphabétique)
        else:
            resultat += lettre

    return resultat

message_original = "Jules César, général et stratège romain !"
decalage = 3
message_decale = decaler_message(message_original, decalage)

print("Message original:", message_original)
print("Message décalé de {} rangs dans l'alphabet:".format(decalage), message_decale)
