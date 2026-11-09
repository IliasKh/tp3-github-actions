def frais_livraison(montant):
    if montant < 0:
        raise ValueError("Montant negatif")
    if montant >= 300:   # correction : 300 inclus => gratuit (bug initial : montant > 300)
        return 0
    return 25
