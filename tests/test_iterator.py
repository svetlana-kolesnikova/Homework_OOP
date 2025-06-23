from typing import Any

import pytest


def test_iterator(product_iterator) -> Any:
    """Тест итератора"""
    iter(product_iterator)  # переопределение индекса для гарантии, что индекс переопределится на 0
    assert product_iterator.index == 0  # проверка нулевого индекса
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"  # проверка выдачи результата итератора
    assert next(product_iterator).name == "Iphone 15"  # проверка выдачи результата итератора
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"  # проверка выдачи результата итератора
    assert next(product_iterator).name == '55" QLED 4K'  # проверка выдачи результата итератора
    assert next(product_iterator).name == '65" QLED 2K'  # проверка выдачи результата итератора

    with pytest.raises(StopIteration):  # проверка отлова ошибки при окончании работы итератора
        next(product_iterator)
