Montant_initial_investissement = 120000
Taux_rendement_annuel = 3
Gain_annuel = (Taux_rendement_annuel / 100) * Montant_initial_investissement
print("Gain annuel initial :", Gain_annuel, "euros")

Augmentation_capital = 25000
Montant_initial_investissement += Augmentation_capital

Taux_rendement_annuel = 3

Résultat_nouveau_gain = (Taux_rendement_annuel / 100) * Montant_initial_investissement
print("Nouveau gain annuel :", Résultat_nouveau_gain, "euros")

Somme_retirée = 0.10 * Montant_initial_investissement

Evolution_rendement = 1

Evolution_rendement -= 1

Montant_final = Montant_initial_investissement - Somme_retirée + Résultat_nouveau_gain
print("Montant final de l'investissement après retrait :", Montant_final, "euros")

Gain_final = Montant_final - Montant_initial_investissement
print("Gain final :", Gain_final, "euros")
