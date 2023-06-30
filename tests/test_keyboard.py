import pytest

from src.keyboard import KeyBoard

keyboard = KeyBoard('SmartBuy', 1500.0, 20)


def test_keyboard_attributes():
    assert keyboard.name == 'SmartBuy'
    assert keyboard.price == 1500.0
    assert keyboard.quantity == 20
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'
