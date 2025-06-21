class Product:
    """Класс для создания продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        # if price <= 0:
        #     raise ValueError("Цена не может быть нулевой или отрицательной. Объект не создан.")
        #
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    def __str__(self):
        """Метод возвращает строку содержимого продукта в заданном формате"""
        return f"{self.name}, {self.__price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает результат сложения сумм всех товаров двух категорий"""
        if isinstance(other, Product):  # проверяем, является ли other объектом класса Product
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise ValueError("Other не является объектом класса Product")

    @property
    def price(self):
        """Геттер возвращает приватный атрибут __price"""
        if self.__price <= 0:
            print("Цена не может быть нулевой или отрицательной.")
            return
        return self.__price

    @price.setter
    def price(self, new_price):
        """Проверка цены на ввод положительного числа и числа не равного нулю"""
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной.")
        if new_price < self.__price:
            """предоставление пользователю возможность снизить цену"""
            confirm = input("Действительно ли цена снижена? (yes/no): ")
            if confirm.lower().startswith("y"):
                self.__price = new_price
            else:
                print("Цена осталась прежней.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, dict_product):
        """Создает объект Product, если цена положительная. Иначе возвращает None."""
        if dict_product["price"] <= 0:
            print("Ошибка: цена не может быть нулевой или отрицательной. Объект не создан.")
            return None

        # Если цена корректная — создаем объект
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])


if __name__ == "__main__":

    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    p5 = Product('65" QLED 2K', "Фоновая подсветка отсутствует", 100000.0, 10)

    print(p1)
    print(p3)
    print(p1 + p3)
