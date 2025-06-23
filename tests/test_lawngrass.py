from typing import Any

import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(new_product_lawngrass1) -> Any:
    """
    Тестирование корректной инициализации продукта
    """
    assert new_product_lawngrass1.name == "Газонная трава"
    assert new_product_lawngrass1.description == "Элитная трава для газона"
    assert new_product_lawngrass1.country == "Россия"
    assert new_product_lawngrass1.color == "Зеленый"
    assert new_product_lawngrass1.germination_period == "7 дней"
    assert new_product_lawngrass1.price == 500.0
    assert new_product_lawngrass1.quantity == 20


def test_lawngrass_init_error() -> Any:
    """
    Тестирование отлова ошибки при инициализации продукта
    """
    with pytest.raises(TypeError):
        s1 = LawnGrass("Не продукт")


def test_lawngrass_add(new_product_lawngrass1, new_product_lawngrass2) -> Any:
    """
    Тестирование отлова ошибки при сложении, если объект other является объектом класса LawnGrass
    """
    assert new_product_lawngrass1 + new_product_lawngrass2 == 16750.0


def test_lawngrass_add_error(new_product_lawngrass1) -> Any:
    """
    Тестирование отлова ошибки при сложении, если объект other не является объектом класса LawnGrass
    """
    with pytest.raises(TypeError):
        r = new_product_lawngrass1 + "Не продукт"
