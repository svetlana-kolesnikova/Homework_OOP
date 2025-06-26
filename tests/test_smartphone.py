from typing import Any

import pytest

from src.smartphone import Smartphone


def test_smartphone_init(new_product_smartphone1) -> Any:
    """
    Тестирование корректной инициализации продукта
    """
    assert new_product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert new_product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_smartphone1.efficiency == "China"
    assert new_product_smartphone1.color == "Gray"
    assert new_product_smartphone1.memory == "256GB"
    assert new_product_smartphone1.model == "S23"
    assert new_product_smartphone1.price == 180000.0
    assert new_product_smartphone1.quantity == 6


def test_smartphone_init_error() -> Any:
    """
    Тестирование отлова ошибки при инициализации продукта
    """
    with pytest.raises(TypeError):
        s1 = Smartphone("Не продукт")


def test_smartphone_add(new_product_smartphone1, new_product_smartphone2) -> Any:
    """
    Тестирование отлова ошибки при сложении, если объект other является объектом класса LawnGrass
    """
    assert new_product_smartphone1 + new_product_smartphone2 == 3180000.0


def test_smartphone_add_error(new_product_smartphone1) -> Any:
    """
    Тестирование отлова ошибки при сложении, если объект other не является объектом класса LawnGrass
    """
    with pytest.raises(TypeError):
        r = new_product_smartphone1 + "Не продукт"
