t9="111222333444555666777788889999"

# renvoie le chiffre correspondant a une lettre
def lettre_chiffre(x):
    assert 'a'<=x and x<='z'
    return t9[ord(x)-ord("a")]

# renvoie la sequence de chiffres correspondant a un mot
def mot_code(mot):
    return "".join(map(lettre_chiffre, mot))

def predictive_texte(dico):
    freq = {} # freq[p] = poids total des mots de prefixe p

    for mot, poids in dico:
        prefixe=""
        for x in mot:
            prefixe+=x
            if prefixe in freq:
                freq[prefixe]+=poids
            else:
                freq[prefixe]=poids

    # prop[s] = prefixe a afficher sur s
    prop={}
    for prefixe in freq:
        code = mot_code(prefixe)
        if code not in prop or freq[prop[code]] < freq[prefixe]:
            prop[code] = prefixe
    return prop


def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    else:
        return "None"



dico = {"le":10, }
