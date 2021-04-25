"""
Exemple de codage / decodage avec la methode de Vigenere
"""


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
tableVigenere = []

# decale une liste d'éléments d'alphabet d'un élément vers la droite
def decale(alpha):
    alphaGauche = alpha[:-1]
    alphaDroit = ["".join(alpha[-1])]
    newAlpha =  alphaDroit + alphaGauche
    return newAlpha


def indexAlphabet(lettre):
    return alphabet.index(lettre)


# genere la matrice de Vigenere à partir d'un alphabet
def creeTableVigenere():
    currentAlpha = alphabet
    for i in range(len(alphabet)):
        tableVigenere.append(currentAlpha)
        currentAlpha = decale(currentAlpha)
    print("table de Vigenere initialisee")    
    return tableVigenere


def code(texte, cle):
    """
    encode un texte avec la clé donnée
    """
    longueur_cle = len(cle)
    lettre_cle = ""
    position_cle=0

    # on itere sur toutes les lettres du texte
    for lettre in texte:
        print(lettre)

        # on determine la lettre de la clé
        lettre_cle = cle[position_cle]
        print("lette de la cle : {}".format(lettre_cle))

        # on fait avancer la position de la clé
        position_cle = position_cle+1
        if position_cle>=longueur_cle :
            position_cle = 0

        # on determine la ligne a utiliser dans la table de Vigenere
        ligne = indexAlphabet(lettre_cle)
        print(ligne)


# initialise la table de Vigenere
creeTableVigenere()

