#
# projet Chloe : code Vigenere
#

# alphabet est la liste qui contient notre alphabet
alphabet=["A", "B","C", "D", "E", "F"]

# Table est la table de Vigenere
table=[]


def chloplus(premiernombre, deuxiemenombre) :
    resultat = premiernombre + deuxiemenombre +1
    return resultat


# decale une liste d'éléments d'alphabet d'un élément vers la droite
def decale(alpha):
    alphaGauche = alpha[:-1]
    alphaDroit = ["".join(alpha[-1])]
    newAlpha = alphaDroit + alphaGauche
    return newAlpha


def creeTableVigenere():
    longueur=len(alphabet)
    print("longeur de l'alphabet : {}".format(longueur))

    for ligne in range(longueur):
        print("nous sommes dans le tour de boucle n°{}".format(ligne))
        table.append(alphabet)
        print(table)
        print(" ")

    print("Resultat : ")
    print("Voici la table de Vigenere : ")
    print(table)
    decale(alphabet)
    
    age=10
    if age <10
    print("vient jouer avec nous!")
    else:
    print("Tu es trop vieux!"
