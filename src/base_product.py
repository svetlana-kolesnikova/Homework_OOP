from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс для класса Product"""

    @abstractmethod
    def __add__(self, *args: Any, **kwargs: Any) -> float:
        """Метод возвращает результат сложения сумм всех товаров категории"""
        pass
