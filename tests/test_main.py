from main import Category


def test_product_attributes(products):
    """Тест на успешное создание продуктов"""
    p1, p2, p3 = products
    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p2.price == 210000.0
    assert p3.quantity == 14


def test_category_creation_and_attributes(products):
    """Тест на успешное создание категорий"""
    p1, p2, p3 = products
    category = Category("Смартфоны", "Описание категории", [p1, p2, p3])
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3


def test_category_count_increment():
    """Тест не подсчет категорий"""
    assert Category.category_count == 0
    Category("Категория 1", "Описание")
    assert Category.category_count == 1
    Category("Категория 2", "Описание")
    assert Category.category_count == 2


def test_product_count_property(products):
    """Тест на получение общего количества единиц продуктов"""
    p1, p2, p3 = products
    category = Category("Смартфоны", "Описание", [p1, p2, p3])
    assert category.product_count == (5 + 8 + 14)


def test_product_count_empty_category():
    """Тест на отсутствие категорий и продуктов"""
    category = Category("Пустая категория", "Нет продуктов")
    assert category.product_count == 0
