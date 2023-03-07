class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__

class Biens Consommation(subclasses):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Articles Menagers(subclasses):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(subclasses):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiau = materiau
		self.couleur = couleur
		self.dimensions = dimensions

class Canape(subclasses):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Chaise(subclasses):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Table(subclasses):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(materiau, couleur, dimensions, cost, price, marque)

class Appareils Electromenagers(subclasses):
	def __init__(self, capacite, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacite = capacite

class Refrigerateur(subclasses):
	def __init__(self, efficacite, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.efficacite = efficacite

class Lave-vaisselle(subclasses):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Lave-linge(subclasses):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Ustensiles Cuisine(subclasses):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux

class Casserole(subclasses):
	def __init__(self, diametre, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.diametre = diametre

class Batterie Cuisine(subclasses):
	def __init__(self, nombre_pieces, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.nombre_pieces = nombre_pieces

class Habillement(subclasses):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vetements(subclasses):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(cost, price, marque)
		self.taille = taille
		self.couleur = couleur
		self.matiere = matiere

class Haut(subclasses):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(subclasses):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(subclasses):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Casquette(subclasses):
	def __init__(self, couleur, cost, price, marque):
		super().__init__(cost, price, marque)
		self.couleur = couleur

class Chaussures(subclasses):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure

