import pytest
from src.products import Product
from src.category import Category
from src.iterator import ProductIterator


@pytest.fixture
def products():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    p5 = Product('65" QLED 2K', "Фоновая подсветка отсутствует", 100000.0, 10)
    return p1, p2, p3, p4, p5


@pytest.fixture(autouse=True)
def reset_category_count():
    Category.category_count = 0
    yield


@pytest.fixture(autouse=True)
def reset_product_count():
    Category.product_count = 0
    yield


@pytest.fixture
def new_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def new_product1():
    return Product("Apple SE2020", "256GB, Серый цвет, 200MP камера", 60000.0, 6)


@pytest.fixture
def new_product_dict():
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    return new_product


@pytest.fixture
def new_product_dict_price_0():
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 0.0,
        "quantity": 5,
    }
    return new_product


@pytest.fixture
def new_product_price_0():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 0, 5)


@pytest.fixture
def new_price_0():
    return 0


@pytest.fixture
def new_category(products):
    return Category("Категория новая", "Описание", [*products])


@pytest.fixture
def product_iterator(new_category):
    return ProductIterator(new_category)
