"""
Exemple de codage / decodage avec la methode de Vigenere
"""


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
table = []


# decale une liste d'éléments d'alphabet d'un élément vers la droite
def decale(alpha):
    alphaGauche = alpha[:-1]
    alphaDroit = ["".join(alpha[-1])]
    newAlpha =  alphaDroit + alphaGauche
    return newAlpha

# renvoie l'indice d'une lettre dans l'alphabet
def indexAlphabet(lettre):
    return alphabet.index(lettre)

# renvoie la lettre située en ligne, colonne dans la table de Vigenere
def findInTable(ligne, colonne):
    return table[ligne][colonne]

# genere la matrice de Vigenere à partir d'un alphabet
def creeTableVigenere():
    currentAlpha = alphabet
    for i in range(len(alphabet)):
        table.append(currentAlpha)
        currentAlpha = decale(currentAlpha)
    print("table de Vigenere initialisee")    



# code le texte selon la clé
def code(texte, cle):
    longueur_cle = len(cle)
    lettre_cle = ""
    position_cle=0
    code=""

    # on itere sur toutes les lettres du texte
    for lettre in texte:
        # on determine la lettre de la clé
        lettre_cle = cle[position_cle]

        # on fait avancer la position de la clé
        position_cle = position_cle+1
        if position_cle>=longueur_cle :
            position_cle = 0

        # on determine la ligne et la colonne a utiliser dans la table de Vigenere
        ligne = indexAlphabet(lettre_cle)
        colonne = indexAlphabet(lettre)
        code = code + findInTable(ligne, colonne)

    return code 


# decode le texte selon la clé
def decode(texte, cle):
    longueur_cle = len(cle)
    lettre_cle = ""
    position_cle = 0
    decode = ""

    # on itere sur toutes les lettres du texte
    for lettre in texte:
        # on determine la lettre de la clé
        lettre_cle = cle[position_cle]

        # on fait avancer la position de la clé
        position_cle = position_cle+1
        if position_cle >= longueur_cle:
            position_cle = 0

        # on determine la ligne et la colonne a utiliser dans la table de Vigenere
        ligne = indexAlphabet(lettre_cle)
        colonne = table[ligne].index(lettre)
        decode = decode + alphabet[colonne]

    return decode


def main():
    print("Code de Vigenere")
    print("alphabet : {} de taille {}".format(alphabet, len(alphabet)))
    # initialise la table de Vigenere
    creeTableVigenere()



if __name__ == "__main__":
    # execute only if run as a script
    main()
