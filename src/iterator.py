from typing import Iterator, Any

from src.category import Category
from src.products import Product


class ProductIterator(Iterator):
    """Итератор для перебора продуктов в списке продуктов экземпляра класса Category"""

    def __init__(self, product_object: Any):
        self.category = product_object  # объект класса - экземпляр класса Category
        self.index = 0  # стартовая точка итерации

    def __iter__(self) -> "ProductIterator":
        self.index = 0  # чтоб каждый новый вызов итератора начинался сначала
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products):
            product = self.category.products[self.index]  # обращаемся к экземпляру products экземпляра category
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    p5 = Product('65" QLED 2K', "Фоновая подсветка отсутствует", 100000.0, 10)

    category1 = Category("Категория 1", "Описание", [p1, p2, p3, p4, p5])

    print(p1)
    print(category1)
    print()

    iterator = ProductIterator(category1)
    for i in iterator:
        print(i)

    print()

    iterator = ProductIterator(category1)
    for i in iterator:
        print(i)
