from typing import Any

from src.products import Product


class Smartphone(Product):
    """Подкласс для создания продуктов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> float:
        """Метод возвращает результат сложения сумм всех товаров категории"""
        if type(other) is Smartphone:  # проверяем, является ли other объектом класса Smartphone
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
