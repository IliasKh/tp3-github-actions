import pytest
from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_message_normal_autorise(client):
    r = client.post("/moderate", json={"message": "bonjour"})
    assert r.status_code == 200
    assert r.get_json() == {"decision": "autoriser"}


def test_message_spam_bloque(client):
    r = client.post("/moderate", json={"message": "ceci est du SPAM"})
    assert r.status_code == 200
    assert r.get_json() == {"decision": "bloquer"}


@pytest.mark.parametrize("corps", [{}, {"message": 42}])
def test_message_invalide(client, corps):
    r = client.post("/moderate", json=corps)
    assert r.status_code == 400
    assert r.get_json() == {"error": "Invalid message"}
    

def test_moderate_corps_json_liste_retourne_400(client):
    reponse = client.post("/moderate", json=["spam"])
 
    assert reponse.status_code == 400
    assert reponse.get_json() == {"error": "JSON object required"}
