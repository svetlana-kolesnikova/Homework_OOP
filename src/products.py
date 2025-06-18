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
