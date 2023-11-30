def tapisserie(n): 
	# Le bord 
	print("+" + "-" * (n+1) + "+") 
  
	# La boucle d'affichage 
	for i in range(n+1): 
		print(" "+"#" * (n-i) + " " + "#" * i + " ") 
  
	# Le bord 
	print("+" + "-" * (n+1) + "+") 
# tapisserie() 
  
tapisserie(10)