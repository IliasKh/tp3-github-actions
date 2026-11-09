import pytest
from app.notifications import envoyer_notification


def test_envoyer_notification_service_non_configure():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Taux eleve")
