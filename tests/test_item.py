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


def test_name_setter():
    item_1.name = 'Смартфон'
    assert item_1.name == 'Смартфон'
    item_1.name = 'Холодильник'
    assert item_1.name == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('7.5') == 7


def test_repr():
    assert repr(item_1) == "Item('Смартфон', 12500.0, 20)"


def test_str():
    assert str(item_1) == 'Смартфон'
