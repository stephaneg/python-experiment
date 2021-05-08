# calcul de dictionnaire de frequence en français

ponctuation = ["'", ",", ".", ";"]

def filter(text):
    ls = text.lower()
    res=""
    for letter in ls :
        print("traitement de l'élément {}".format(letter))
        res+=letter
    return ls
    


input="Nous et nos partenaires traitons les données personnelles telles que l'adresse IP, l'identifiant unique, les données de navigation. Certains partenaires ne demandent pas votre consentement pour traiter vos données, mais se fondent sur leur intérêt commercial légitime. Consultez notre liste de partenaires pour voir les raisons pour lesquelles ils estiment avoir un intérêt légitime et et comment vous y opposer. Nous et nos partenaires pouvons utiliser vos données aux fins suivantes, vous pouvez gérer vos choix en cliquant sur Gérer les options. Vous pouvez modifier vos paramètres à tout moment, y compris en retirant votre consentement, en cliquant sur l'icône "

print("traitement de l'entrée : {}".format(input))
res = filter(input)
print("resultat: {}".format(res))

