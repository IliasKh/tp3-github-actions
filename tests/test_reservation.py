import pytest
from app.reservation import Stock, Reservation


@pytest.fixture
def stock():
    return Stock(5)


def test_reservation_confirmee(stock):
    assert Reservation(stock).reserver(2) == "confirmee"
    assert stock.quantite == 3


def test_reservation_refusee_stock_insuffisant(stock):
    assert Reservation(stock).reserver(6) == "refusee"
    assert stock.quantite == 5


def test_reservation_de_tout_le_stock(stock):
    assert Reservation(stock).reserver(5) == "confirmee"
    assert stock.quantite == 0


def test_reservation_quantite_nulle(stock):
    with pytest.raises(ValueError):
        Reservation(stock).reserver(0)
    assert stock.quantite == 5
