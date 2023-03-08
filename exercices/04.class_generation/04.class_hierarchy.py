# Import des modules nécessaires
import json
from unidecode import unidecode
import re
import os

# Charger des données JSON à partir du fichier dans un dictionnaire python
local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# Reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
json_str = json.dumps(json_data)
json_str = json_str.replace("-", "_")

# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
json_data = (unidecode(json_str))

# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
# Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
json_dict = json.loads(json_data)


#generate class def
def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []) -> str:
    # Cette fonction génère une définition de classe Python à partir des paramètres passés et retourne une chaîne de caractères représentant la définition de classe générée.
    """
    `nom_classe`: une chaîne de caractères représentant le nom de la classe à générer.
    `attributs`: un dictionnaire représentant les attributs de la classe, où les clés sont les noms des attributs et les valeurs sont les types des attributs.
    `nom_superclasse`: une chaîne de caractères représentant le nom de la superclasse éventuelle. Si la classe n'a pas de superclasse, on peut passer une chaîne vide en argument.
    `args_superclasse`: une liste de chaînes de caractères représentant les arguments à passer au constructeur de la superclasse éventuelle. Si la classe n'a pas de superclasse, on peut passer une liste vide en argument.

    La fonction retourne une chaîne de caractères représentant le code source de la classe.
    """

    # Initialisation des variables
    """
    On commence par initialiser plusieurs variables utiles pour la suite de la fonction :

    `args_constructeur`: une liste des noms des arguments à passer au constructeur de la classe.
    `definition_constructeur`: une chaîne de caractères représentant la définition du constructeur de la classe, à remplir au fur et à mesure qu'on parcourt les attributs.
    `has_attributs`: un booléen qui permet de savoir si la classe a des attributs ou non.

    """
    args_constructeur = [] # une liste qui stocke les noms des attributs qui seront utilisés pour créer le constructeur
    definition_constructeur = "" # une chaîne de caractères qui stocke le code qui sera utilisé pour initialiser les attributs de la classe
    has_attributs = False # un booléen qui vérifie si la classe a des attributs ou non
    modele_classe = f"class {nom_classe}" # une chaîne de caractères qui stocke la définition de base de la classe

    """
    Si la classe a une superclasse, celle-ci est spécifiée dans la définition. 
    La chaîne de caractères est stockée dans la variable modele_classe.
    """
    # Gestion de la superclasse
    if nom_superclasse: # si la classe a une superclasse
        modele_classe += f"({nom_superclasse})" # ajouter la superclasse à la définition de la classe

    modele_classe += ":\n" # ajouter une nouvelle ligne à la définition de la classe
    """
    Ensuite, la fonction parcourt les attributs de la classe. 
    Pour chaque attribut, elle ajoute le nom de l'attribut à la liste args_constructeur et construit 
    une ligne de code de la forme `self.nom_attribut = nom_attribut` pour la définition du constructeur.     
    """
    # Gestion des attributs
    for nom_attribut in attributs.keys(): # pour chaque attribut dans le dictionnaire d'attributs
        if nom_attribut != "subclasses": # si l'attribut n'est pas une sous-classe
            has_attributs = True # la classe a des attributs
            args_constructeur.append(nom_attribut) # ajouter le nom de l'attribut à la liste des arguments du constructeur
            definition_constructeur += f"\n\t\tself.{nom_attribut} = {nom_attribut}" # ajouter une ligne au code de définition du constructeur pour initialiser l'attribut

    """
    Si l'attribut est `name` et que la classe est une classe `Product`, 
    la fonction ajoute également une ligne de code pour initialiser `self.name` avec le nom de la classe. 
    """
    # Gestion du nom de la classe si c'est une classe Product
    if nom_classe == "Product": # si la classe est de type Product
        definition_constructeur += "\n\t\tself.name=type(self).__name__" # ajouter une ligne au code de définition du constructeur pour initialiser le nom de la classe

    """
    Si la classe a des attributs:
    la fonction construit une chaîne de caractères représentant le constructeur de la classe en utilisant les arguments fournis. 
    La chaîne de caractères est stockée dans la variable `modele_constructeur`.
    """
    # Gestion du constructeur
    if has_attributs: # la classe a des attributs
        modele_constructeur = f"\tdef __init__(self, {', '.join(args_constructeur + args_superclasse)}):" # créer la signature du constructeur en incluant les arguments des attributs et les arguments de la superclasse

        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})" # ajouter une ligne pour initialiser la superclasse

        modele_constructeur += definition_constructeur # ajouter le code d'initialisation des attributs à la définition du constructeur
   
        """
        Si la classe n'a pas d'attributs:
        la fonction construit une chaîne de caractères représentant le constructeur de la classe 
        en utilisant uniquement les arguments de la superclasse (s'il y en a). 
        La chaîne de caractères est stockée dans la variable modele_constructeur.
        """
    else: # la classe n'a pas d'attributs
        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur = f"\tdef __init__(self, {', '.join(args_superclasse)}):" # créer la signature du constructeur en incluant les arguments de la superclasse
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"
      
        else:    
            modele_constructeur = "\tpass"
    
    """
    On retourne une chaîne de caractères qui représente le code source complet de la classe, 
    en utilisant les chaînes de caractères stockées précédemment dans modele_classe et `modele_constructeur`.
    """
    return modele_classe + modele_constructeur + "\n\n"
     


"""
La méthode generate_class_hierarchy permet de générer une hiérarchie des classes en utilisant un dictionnaire comme entrée.
Elle prend les arguments suivant: 
    - json_dict : un dictionnaire Python représentant une hiérarchie des classes.
    - superclass_name : une chaîne de caractères représentant le nom de la classe parente. Par défaut, sa valeur est None pour la racine de la hiérarchie.
    - superclass_args : une liste des arguments des arguments de la classe mère à passer à la classe fille.
"""
# Generate class hierarchy
def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    # Initialisation de la chaîne de caractères contenant les définitions de classes
    class_defs = ""

    #Itération sur les éléments du dictionnaire
    #pour chaque nom de classe (class_name) et attribut de cette dernière (class_attrs) dans les éléments de  json_dict, faire:
    for class_name, class_attrs in json_dict.items() :
       # - Générer la définition de la classe avec la méthode generate_class_def() en passant les arguments superclass_name et superclass_args comme entrées
        if(class_attrs != ''):
             class_def = generate_class_def(class_name, class_attrs, superclass_name, superclass_args)
             # - le résultat de la méthode generate_class_def() est stocker dans une variable 'class_def'
             # - Concaténer la définition de la classe à la chaîne de caractères class_defs
             class_defs = class_defs + class_def
  
        # - Ensuite, vérifier la présence des sous-classes dans la classe courante
        # - Si "subclasses" existe parmi les attributs de la classe courante, faire:
        if "subclasses" in class_attrs :
        #   -Construire une liste "super_attr" contenant les attributs de la classe courante concaténées aux arguments de la superclasse
        #   -Puis, supprimer l'attribut 'subclasses' à partir de la liste créée
            super_attr = list(class_attrs.keys()) + superclass_args
            super_attr.remove("subclasses")
        #   - Ensuite, faire une récursion pour générer la définition de la sous-classe en utilisant la méthode generate_class_hierarchy
        #   - En passant le nom de la classe courante en tant que superclass_name et la liste super_attr en tant que superclass_args
        #   - Concaténer la définition de la sous-classe à la chaîne de caractères class_defs
            for key, value in class_attrs.items() :
                if(value != ''):
                    class_def = generate_class_hierarchy(value, class_name, super_attr)
                    class_defs = class_defs + class_def

    
    #Retourne la chaîne de caractères contenant les définitions de classes
    return class_defs
    
    
   
 
# la méthode write_content va nous permet d'écrire le code généré automatiquement des classes dans un fichier Python séparé
"""
La méthode write_content prend deux arguments:
        -content: une chaîne de caractères qui représente le contenu que l'on veut écrire dans le fichier.
        -filename: une chaîne de caractères qui représente le nom du fichier dans lequel on veut écrire le contenu.
        
La méthode utilise une clause with pour ouvrir le fichier en mode écriture ("w") en utilisant l'encodage "utf-8".
Ensuite, elle écrit le contenu passé en argument dans le fichier à l'aide de la méthode write. 
Après avoir terminé d'écrire dans le fichier, la méthode se termine et le fichier est automatiquement fermé grâce à l'utilisation de la clause with.
"""    
def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)


def main() :
    # Appeler la méthode generate_class_hierarchy pour générer le code des classes automatiquement en se basant sur le dictionnaire json_dict
    # Stocker le résultat de la classe dans une variable
    classContent = generate_class_hierarchy(json_dict)
    # Appeler la fonction write_content pour stocker le code des classes dans un fichier Python 'product_classes.py'
    write_content(classContent, 'product_classes.py')

if __name__ == '__main__':
    # Appeler la fonction principale
    main()