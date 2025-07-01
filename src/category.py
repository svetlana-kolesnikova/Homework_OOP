from typing import Any

from src.products import Product


class Category:
    """Класс для создания категорий"""

    name: str
    description: str
    products: list

    product_count = 0  # Инициализация атрибута класса
    category_count = 0  # Инициализация атрибута класса

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products  # if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def __str__(self) -> str:
        """Метод возвращает строку содержимого категории в заданном формате"""
        # сумма количества всех продуктов в категории
        summ_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {summ_products} шт."

    def get_category_count(self) -> Any:
        """Возвращает общее количество категорий"""
        return Category.category_count

    def get_product_count(self) -> Any:
        """Возвращает общее количество продуктов"""
        return Category.product_count

    @property
    def products_str(self) -> str:
        """Предоставление возможность просмотра товаров"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product) -> Any:
        """Добавление нового продукта с проверкой на наличие такого
        продукта и решением конфликта цены в сторону большей"""
        if isinstance(product, Product):
            for p in self.__products:
                if p.name == product.name:
                    if p.price >= product.price:
                        product.price = p.price
                    elif p.price < product.price:
                        p.price = product.price
                    p.quantity += product.quantity
                    Category.product_count += product.quantity
                    return
        else:
            raise TypeError

        self.__products.append(product)
        Category.product_count += product.quantity

    @property
    def products(self) -> list:
        """Геттер возвращает приватный атрибут __products"""
        return self.__products

    def middle_price(self) -> Any:
        """Метод для подсчета средней цены товаров в категории"""
        try:
            return round((sum([product.price for product in self.__products]) / len(self.__products)), 2)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    p5 = Product('65" QLED 2K', "Фоновая подсветка отсутствует", 100000.0, 100)

    category1 = Category("Категория 1", "Описание", [p1, p2])
    category2 = Category("Категория 2", "Описание", [p3, p4, p5])

    p6 = Product("Samsung QLED 2K", "Фоновая подсветка отсутствует", 110000.0, 0)

    print(p1)
    print(p6)
    category1.add_product(p6)
    print(category1)
    p1.quantity = 0
    print(p1)

    print(category1)
    print(category2)
    print(Category.product_count)
