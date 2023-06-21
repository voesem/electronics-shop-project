from src.phone import Phone

phone_1 = Phone('Samsung', 12500.0, 20, 2)


def test_phone_attributes():
    assert phone_1.name == 'Samsung'
    assert phone_1.price == 12500.0
    assert phone_1.quantity == 20
    assert phone_1.number_of_sim == 2
