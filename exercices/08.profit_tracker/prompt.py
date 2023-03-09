# L'ojectif de ce fichier est de créer un prompt qui nous permettra d'intéragir avec les différentes fonctionnalités codées

#sell, add, buy, restock, getlist

demandeUtilisateur = input("Que souhaitez vous faire ? \n 1.Ajouter un produit \n 2.Supprimer un produit \n 3.Consulter votre solde \n 4.acheter un produit \n 5.Vendre un produit \n 6.Voir la liste des produits en stock \n 7.Rajouter du stock à un produit")

if demandeUtilisateur == "1":
    #add_product

elif demandeUtilisateur == "2":
    #remove_product

elif demandeUtilisateur == "3":
    #getSolde

elif demandeUtilisateur == "4":
    #BuyProduct

elif demandeUtilisateur == "5":
    #Sell product

elif demandeUtilisateur == "6":
    #getListProducts

elif demandeUtilisateur == "7":
    #Restock product

else :
    print("Nous n'avons pas compris votre demande, veuillez réessayer")
