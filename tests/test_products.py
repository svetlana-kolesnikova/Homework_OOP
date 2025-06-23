import pytest

from src.products import Product


def test_product_attributes(products):
    """Тест на успешное создание продуктов"""
    p1, p2, p3, p4, p5 = products
    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p2.price == 210000.0
    assert p3.quantity == 14
    assert p4.description == "Фоновая подсветка"
    assert p5.description == "Фоновая подсветка отсутствует"


def test_product_init_price_0():
    """Проверка поведения конструктора Product при нулевой цене"""
    p = Product("Тест", "Описание", 0, 1)
    assert p.name == "Тест"
    assert p.price is None


def test_product_set_price_to_zero(new_product, new_price_0):
    """Проверка, что при попытке установить цену = 0 через сеттер выбрасывается ValueError"""
    with pytest.raises(ValueError, match="Цена должна быть положительной."):
        new_product.price = new_price_0


def test_new_product(new_product_dict):
    """Проверка корректной работы класса Product.new_product при корректных данных"""
    new_product_ = Product.new_product(new_product_dict)
    assert new_product_.name == "Samsung Galaxy S23 Ultra"
    assert new_product_.price == 180000.0


def test_new_product_price_0(capsys, new_product_dict_price_0):
    """Проверка, что Product.new_product возвращает None и выводит предупреждение,
    если цена <= 0"""
    new_product_dict_price_0["price"] = 0
    product = Product.new_product(new_product_dict_price_0)  # вызываем метод

    captured = capsys.readouterr()
    assert product is None
    assert captured.out.strip() == "Ошибка: цена не может быть нулевой или отрицательной. Объект не создан."


def test_price_set_lower_with_user_confirmation_yes(monkeypatch, new_product):
    """Проверка снижения цены с подтверждением пользователя"""
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    new_product.price = new_product.price - 1000
    assert new_product.price == 179000.0


def test_price_set_lower_with_user_confirmation_no(monkeypatch, new_product):
    """Проверка снижения цены с отменой ввода пользователя"""
    monkeypatch.setattr("builtins.input", lambda _: "no")
    new_product.price = new_product.price
    assert new_product.price == new_product.price


def test_product_str(new_product):
    """Проверка вывода строки содержимого продукта в заданном формате"""
    assert str(new_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб., Остаток: 5 шт."


def test_product_add(new_product, new_product1):
    """Тест сложения сумм всех товаром двух продуктов"""
    result = new_product + new_product1
    assert result == 1260000.0


def test_product_add_oter_not_product_obj(new_product):
    """Тест проверки отлова ошибки, если второй продукт не является объектом класса Product"""
    new_product2 = "Samsung Galaxy S23 Ultra, 180000.0 руб., Остаток: 5 шт."
    with pytest.raises(ValueError):
        new_product + new_product2
