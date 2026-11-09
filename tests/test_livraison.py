import pytest
from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_juste_sous_le_seuil():
    assert frais_livraison(299) == 25


def test_livraison_gratuite_a_300_inclus():
    # test de non-régression : il a révélé le bug (> au lieu de >=)
    assert frais_livraison(300) == 0


def test_livraison_juste_au_dessus_du_seuil():
    assert frais_livraison(301) == 0


def test_livraison_panier_gratuit_500():
    assert frais_livraison(500) == 0


def test_livraison_panier_zero():
    assert frais_livraison(0) == 25


def test_livraison_montant_negatif():
    with pytest.raises(ValueError):
        frais_livraison(-1)
