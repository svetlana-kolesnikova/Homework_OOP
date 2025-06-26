from typing import Any

import pytest

from src.category import Category
from src.products import Product


def test_category_creation_and_attributes(products) -> Any:
    """
    Тест на успешное создание категорий
    """
    p1, p2, p3, p4, p5 = products

    category = Category("Смартфоны", "Описание категории", [p1, p2, p3])
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3


def test_category_count_increment(products) -> Any:
    """
    Тест на подсчет категорий
    """
    p1, p2, p3, p4, p5 = products
    assert Category.category_count == 0
    Category("Категория 1", "Описание", [p1, p2, p3, p4, p5])
    assert Category.category_count == 1
    Category("Категория 2", "Описание", [p1, p2, p3, p4, p5])
    assert Category.category_count == 2


def test_product_count_property(products) -> Any:
    """
    Тест на получение общего количества единиц продуктов
    """
    p1, p2, p3, p4, p5 = products

    Category("Смартфоны", "Описание", [p1, p2, p3])
    Category("Телевизоры", "Описание", [p4, p5])
    assert Category.product_count == 5 + 8 + 14 + 7 + 10


def test_product_count_empty_category() -> Any:
    """
    Тест на отсутствие категорий и продуктов
    """
    category = Category("Пустая категория", "Нет продуктов", [])
    assert category.product_count == 0


def test_category_and_product_counts() -> Any:
    """
    Тест на подсчёт количества категорий и количества продуктов
    """
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание", 100.0, 2)  # поменял порядок, см ниже
    p2 = Product("Товар 2", "Описание", 200.0, 3)

    cat1 = Category("Категория 1", "Описание", [p1])
    cat2 = Category("Категория 2", "Описание", [p2])

    assert cat1.get_category_count() == 2
    assert cat2.get_product_count() == 5


def test_add_duplicate_product_lower_price_keeps_higher(products) -> Any:
    """
    Тест: добавление дубликата с меньшей ценой — сохраняется более высокая цена
    """
    p1 = Product("Продукт", "Описание", 1000.0, 5)
    category = Category("Категория", "Описание", [p1])

    cheaper_product = Product("Продукт", "Описание", 800.0, 2)
    category.add_product(cheaper_product)

    updated_product = next(p for p in category.products if p.name == "Продукт")  # Перебор по списку продуктов
    assert updated_product.price == 1000.0  # цена осталась старой (высокой)
    assert updated_product.quantity == 7  # количество увеличилось


def test_add_duplicate_product_higher_price_overwrites(products) -> Any:
    """
    Тест: добавление дубликата с более высокой ценой — цена обновляется
    """
    p1 = Product("Продукт", "Описание", 1000.0, 5)
    category = Category("Категория", "Описание", [p1])

    more_expensive_product = Product("Продукт", "Описание", 1200.0, 2)
    category.add_product(more_expensive_product)

    updated_product = next(p for p in category.products if p.name == "Продукт")  # Перебор по списку продуктов
    assert updated_product.price == 1200.0  # цена обновилась на более высокую
    assert updated_product.quantity == 7


def test_products_str_output_format(products) -> Any:
    """
    Тест строкового представления товаров в категории
    """
    category = Category("Смартфоны", "Описание", products[:2])
    output = category.products_str

    expected_line_1 = f"{products[0].name}, {products[0].price} руб. Остаток: {products[0].quantity} шт."
    expected_line_2 = f"{products[1].name}, {products[1].price} руб. Остаток: {products[1].quantity} шт."

    assert expected_line_1 in output
    assert expected_line_2 in output


def test_category_str(new_category) -> Any:
    """
    Тест на возвращение строи содержимого категории в заданном формате
    """
    assert str(new_category) == "Категория новая, количество продуктов: 44 шт."


def test_add_product(new_product_smartphone1) -> Any:
    """
    Тестирование отлова ошибки при добавлении в категорию объекта, не являющегося объектом класса Product
    """
    p1 = Product("Продукт", "Описание", 1000.0, 5)
    p2 = Product("Продукт2", "Описание2", 1000.0, 5)
    category = Category("Категория", "Описание", [p1])
    with pytest.raises(TypeError):
        category.add_product("Не продукт")

    category.add_product(p2)
    assert Category.product_count == 10
