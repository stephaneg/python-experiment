#
# projet Chloe : code Vigenere
#

# alphabet est la liste qui contient notre alphabet
alphabet=["A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

# Table est la table de Vigenere
table=[]




# decale une liste d'éléments d'alphabet d'un élément vers la droite
def decale(alpha):
    alphaGauche = alpha[:-1]
    alphaDroit = ["".join(alpha[-1])]
    newAlpha = alphaDroit + alphaGauche
    return newAlpha


def creeTableVigenere():
    longueur=len(alphabet)
    print("longeur de l'alphabet : {}".format(longueur))
    nouvelAlphabet = alphabet

    for ligne in range(longueur):
        table.append(nouvelAlphabet)
        nouvelAlphabet=decale(nouvelAlphabet)

    print("Resultat : ")
    print("Voici la table de Vigenere : ")
    print(table)
    
# renvoie la colonne numero col de la table de Vigenere
def donneColonne(col):
    colonne=[]
    for l in table:
        colonne.append(l[0])
    return colonne


def code(texte,cle):

    secret=""

    for lettre in texte:
        print("codage de la lettre: {}".format(lettre))
        ligne=0
        colonne=0
        secret=secret+table[ligne][colone]

    return secret
