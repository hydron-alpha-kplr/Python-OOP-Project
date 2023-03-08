# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.

class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity
        # Initialisation des variables
        self.sales = 0
        self.expenses = 0

    #Méthode Sell
    def sell(self, quantity):
        #Avant de mettre à jour l'état du stocke du produit, on doit vérifier si on a déjà une quantité suffisante à vendre     
        if quantity > self.quantity :
            print("Le stock du produit" + self.product.name + "est insuffisant.")
            return False
        else :
            self.quantity -= quantity
            self.sales += quantity * self.product.price
            return True
    
    #Méthode Restock
    
    def restock(self, quantity):
        self.quantity += quantity
        self.expenses += quantity * self.product.cost

    #Méthode repr
  
    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        response = "Produit :" + self.product.name + "\n"
        response += "Marque :" + self.product.marque + "\n"
        response += "Stock :" + self.product.quantity + "\n"
        response += "Prix :" + self.product.price + "\n"

        return response