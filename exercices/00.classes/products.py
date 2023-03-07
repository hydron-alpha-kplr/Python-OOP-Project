"""1. Créez un nouveau fichier Python et nommez-le "products.py".
2. Définissez la classe Product avec ses attributs cost, price, et marque dans la méthode init.
3. Définissez la classe Meubles en tant que sous-classe de la classe Product, en utilisant le mot-clé "class Meubles(Product):".
4. Définissez la méthode init de la classe Meubles en appelant la méthode init de la classe parent avec le super().init(cost, price, marque).
5. Ajoutez les attributs spécifiques à la classe Meubles, tels que les matériaux, la couleur et les dimensions.
6. Répétez les étapes 3 à 5 pour les classes Canape, Chaise et Table.
7. Vous pouvez maintenant utiliser ces classes pour créer des instances de meubles spécifiques dans votre programme principal."""

class Product:
    def __init__(self, cost, price, marque):
        self.marque = marque
        self.cost = cost
        self.price = price

class Meubles(Product):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
       super().__init__(cost, price, marque)
       self.materiaux = materiaux
       self.couleur = couleur
       self.dimensions = dimensions

class Chaise(Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
       super().__init__(cost, price, marque, materiaux, couleur, dimensions)
       


class Canape(Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
       super().__init__(cost, price, marque, materiaux, couleur, dimensions)
       


class Table(Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
       super().__init__(cost, price, marque, materiaux, couleur, dimensions)
      


# Exemple d'instances :
chaise1 = Chaise(50, 100, "PEPOUSE", "Plastique", "Rouge", "50x50x70")
chaise2 = Chaise(75, 150, "PEPOUSE", "Métal", "Gris", "60x60x80")
canape1 = Canape(1000, 2000, "OKLM", "Cuir", "Blanc", "200x100x80")
canape2 = Canape(800, 1600, "SIESTA", "Tissu", "Bleu", "150x90x70")
table1 = Table(250, 500, "TEX", "Bois", "Chêne", "150x80x75")
table2 = Table(350, 700, "TEX", "Verre", "Transparent", "120x60x75")
