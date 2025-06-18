from src.products import Product


class Category:
    """Класс для создания категорий"""

    name: str
    description: str
    products: list

    product_count = 0  # Инициализация атрибута класса
    category_count = 0  # Инициализация атрибута класса

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products  # if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def get_category_count(self):
        """Возвращает общее количество категорий"""
        return Category.category_count

    def get_product_count(self):
        """Возвращает общее количество продуктов"""
        return Category.product_count

    @property
    def products_str(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product):
        """Добавление нового продукта с проверкой на наличие такого
        продукта и решением конфликта цены в сторону большей"""
        for p in self.__products:
            if p.name == product.name:
                if p.price >= product.price:
                    product.price = p.price
                elif p.price < product.price:
                    p.price = product.price
                p.quantity += product.quantity
                Category.product_count += product.quantity
                return

        self.__products.append(product)
        Category.product_count += product.quantity

    @property
    def products(self):
        """Геттер возвращает приватный атрибут __products"""
        return self.__products
