import pytest
from unittest.mock import Mock
from app.moderation import decider


def test_decider_bloque_le_spam():
    modele = Mock()
    modele.predict.return_value = "spam"
    assert decider(modele, "Offre miracle") == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_decider_autorise_message_normal():
    modele = Mock()
    modele.predict.return_value = "normal"
    assert decider(modele, "Bonjour") == "autoriser"


def test_decider_propage_erreur_modele():  # bonus
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")
    with pytest.raises(RuntimeError):
        decider(modele, "Bonjour")
