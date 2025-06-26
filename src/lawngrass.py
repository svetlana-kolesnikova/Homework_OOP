from typing import Any

from src.products import Product


class LawnGrass(Product):
    """Подкласс для создания продуктов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> float:
        """Метод возвращает результат сложения сумм всех товаров категории"""
        # Проверка при сложении на принадлежность объекта other на принадлежность к классу LawnGrass
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
