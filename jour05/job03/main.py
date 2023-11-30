def draw_triangle(width, height):
    for i in range(height):
        if i == height - 1:
            print('_' * (2 * width - 1))
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i - 1) + '\\')

hauteur = int(input("Entrez la hauteur du triangle : "))
base = int(input("Entrez la base du triangle : "))

draw_triangle(base, hauteur)




           