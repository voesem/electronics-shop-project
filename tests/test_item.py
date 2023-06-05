from src.item import Item

item_1 = Item('Смарт-часы', 25000, 20)
item_2 = Item('Робот-пылесос', 12000, 5)


def test_calculate_total_price():
    assert item_1.calculate_total_price() == 500000
    assert item_2.calculate_total_price() == 60000


def test_apply_discount():
    assert 25000 * Item.pay_rate == item_1.price
    Item.pay_rate = 0.5
    item_1.apply_discount()
    assert item_1.price == 12500.0
