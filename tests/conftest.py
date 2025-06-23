from typing import Any

import pytest

from src.category import Category
from src.iterator import ProductIterator
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def products() -> Any:
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    p5 = Product('65" QLED 2K', "Фоновая подсветка отсутствует", 100000.0, 10)
    return p1, p2, p3, p4, p5


@pytest.fixture(autouse=True)
def reset_category_count() -> Any:
    Category.category_count = 0
    yield


@pytest.fixture(autouse=True)
def reset_product_count() -> Any:
    Category.product_count = 0
    yield


@pytest.fixture
def new_product() -> Any:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def new_product1() -> Any:
    return Product("Apple SE2020", "256GB, Серый цвет, 200MP камера", 60000.0, 6)


@pytest.fixture
def new_product_dict() -> Any:
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    return new_product


@pytest.fixture
def new_product_dict_price_0() -> Any:
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 0.0,
        "quantity": 5,
    }
    return new_product


@pytest.fixture
def new_product_price_0() -> Any:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0, 5)


@pytest.fixture
def new_price_0() -> Any:
    return 0


@pytest.fixture
def new_category(products: tuple) -> Any:
    return Category("Категория новая", "Описание", [*products])


@pytest.fixture
def product_iterator(new_category: dict) -> Any:
    return ProductIterator(new_category)


@pytest.fixture
def new_product_smartphone1() -> Any:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 6, "China", "S23", "256GB", "Gray")


@pytest.fixture
def new_product_smartphone2() -> Any:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 10, "China", "15", "512GB", "Gray space")


@pytest.fixture
def new_product_lawngrass1() -> Any:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def new_product_lawngrass2() -> Any:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
