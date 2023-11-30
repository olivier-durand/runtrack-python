n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
   print("{0} est Paire".format(n))
else:
   print("{0} est Impaire".format(n))
print(verifier_pair_impair(7))
print(verifier_pair_impair(2))
print(verifier_pair_impair(1))
print(verifier_pair_impair(-5))
print(verifier_pair_impair(10.3))