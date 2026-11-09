import pytest
from unittest.mock import patch
from app.surveillance import surveiller


def test_surveiller_taux_eleve():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.15) == "alerte"
        notifier.assert_called_once_with("Taux eleve")


def test_surveiller_taux_faible():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.05) == "ok"
        notifier.assert_not_called()


def test_surveiller_taux_exactement_0_10():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.10) == "ok"
        notifier.assert_not_called()


def test_surveiller_propage_panne_notification():  # bonus
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service non configure")
        with pytest.raises(RuntimeError):
            surveiller(0.15)
