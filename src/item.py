import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        """
        Метод, инициализирующий экземпляры класса Item данными из файла items.csv.
        Если список экземпляров класса не пуст - очищает его
        """
        if len(Item.all) != 0:
            Item.all = []

        with open(os.path.join(os.path.dirname(__file__), 'items.csv')) as f:
            items = csv.DictReader(f)
            for i in items:
                cls(name=i['name'], price=float(i['price']), quantity=int(i['quantity']))

    @staticmethod
    def string_to_number(string):
        """
        Метод, возвращающий число из числа-строки
        """
        return int(float(string)) if '.' in string else int(string)
