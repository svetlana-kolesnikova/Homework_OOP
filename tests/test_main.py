from main import Category, Product


def test_product_attributes(products):
    """Тест на успешное создание продуктов"""
    p1, p2, p3, p4, p5 = products
    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p2.price == 210000.0
    assert p3.quantity == 14
    assert p4.description == "Фоновая подсветка"
    assert p5.description == "Фоновая подсветка отсутствует"
    


def test_category_creation_and_attributes(products):
    """Тест на успешное создание категорий"""
    p1, p2, p3, p4, p5 = products
    category = Category("Смартфоны", "Описание категории", [p1, p2, p3])
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3


def test_category_count_increment(products):
    """Тест не подсчет категорий"""
    p1, p2, p3, p4, p5 = products
    assert Category.category_count == 0
    Category("Категория 1", "Описание", [p1, p2, p3, p4, p5])
    assert Category.category_count == 1
    Category("Категория 2", "Описание", [p1, p2, p3, p4, p5])
    assert Category.category_count == 2


def test_product_count_property(products):
    """Тест на получение общего количества единиц продуктов"""
    p1, p2, p3, p4, p5 = products
    
    Category("Смартфоны", "Описание", [p1, p2, p3])
    Category("Телевизоры", "Описание", [p4, p5])
    assert Category.product_count == 5 + 8 + 14 + 7 + 10
    


def test_product_count_empty_category():
    """Тест на отсутствие категорий и продуктов"""
    category = Category("Пустая категория", "Нет продуктов", [])
    assert category.product_count == 0
    

def test_category_and_product_counts():
    """Тест на подсчёт количества категорий и количества продуктов"""
    Category.category_count = 0
    Category.product_count = 0
    
    p1 = Product("Товар 1", "Описание", 100.0, 2)  # поменял порядок, см ниже
    p2 = Product("Товар 2", "Описание", 200.0, 3)

    cat1 = Category("Категория 1", "Описание", [p1])
    cat2 = Category("Категория 2", "Описание", [p2])

    assert cat1.get_category_count() == 2
    assert cat2.get_product_count() == 5
    
