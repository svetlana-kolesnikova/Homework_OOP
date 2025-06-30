from typing import Any

from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys) -> Any:
    """Тест на печать в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""
    Product("Apple SE2020", "256GB, Серый цвет, 200MP камера", 60000.0, 6)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Apple SE2020, 256GB, Серый цвет, 200MP камера, 60000.0, 6)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 10, "China", "15", "512GB", "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 10)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
