nom_produit = "Ballon Adidas" 
detail_produit = "Al Rihla Coupe du Monde Qatar 2022"
prix_unitaire = 150
stock = 3000
print("Ballon Adidas", nom_produit)
print("detail du produit", detail_produit)
print("prix unitaire", prix_unitaire)
print("stock", stock)
print("nombre de produits vendus", nombre_produits_vendus)
quantite_vendue = int(input("Entrez la quantité de produits : "))
stock -= quantite_vendue
prix_unitaire *= 1.10
print("stock en temps reel:", stock, "unité")
print("nouveau_prix", prix_unitaire, "Euros")