import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    ("  déjà   propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("Bonjour MONDE", "bonjour monde"),
    ("PYTHON", "python"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree", [123, None])
def test_nettoyer_texte_type_invalide(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


def test_nettoyer_texte_est_idempotent():
    une_fois = nettoyer_texte("  BONJOUR   monde  ")
    assert nettoyer_texte(une_fois) == une_fois
