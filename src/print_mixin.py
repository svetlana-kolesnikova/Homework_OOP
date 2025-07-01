class PrintMixin:
    """Класс-миксин для вывода информации о параметрах создаваемого объекта"""

    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса"""
        print(repr(self))

    def __repr__(self) -> str:
        """печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
