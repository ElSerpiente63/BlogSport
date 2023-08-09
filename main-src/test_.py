def couper_en_morceaux(chaine, longueur_morceau):
    morceaux = [chaine[i:i+longueur_morceau] for i in range(0, len(chaine), longueur_morceau)]
    return morceaux

chaine = "Ceci est une chaine de caracteres assez longue et devrait etre coupee en morceaux de 50 caracteres."
longueur_morceau = 50

morceaux = couper_en_morceaux(chaine, longueur_morceau)
print(morceaux)
for morceau in morceaux:
    print(morceau)