# E-commerce

### Электронная система платежей

## Классы
BaseProduct  [base_product.py](src/base_product.py)
- Является абстрактным классом для класса Product

PrintMixin  [print_mixin.py](src/print_mixin.py)
- Класс-миксин. Выводит печатать в консоль информацию о том, 
от какого класса и с какими параметрами был создан объект


Product  [products.py](src/products.py)
- Добавляет новой продукт.
- Проверяет валидность цены. 
- Предоставляет пользователю возможность снизить цену.

Category  [category.py](src/category.py)
- Создает категории.
- Предоставляет возможность просмотра товаров в списке.
- Проверяет товар для исключения дублирования.

ProductIterator  [iterator.py](src/iterator.py)
- Итератор для перебора продуктов в списке продуктов экземпляра класса Category


### Дочерний классы Класса Product

LawnGrass  [lawngrass.py](src/lawngrass.py)
- Добавляет новой продукт с проверкой принадлежности к дочернему классу LawnGrass
- Складывает общую стоимость продуктов дочернего класса LawnGrass


Smartphone  [smartphone.py](src/smartphone.py)
- Добавляет новой продукт с проверкой принадлежности к пдочернему классу Smartphone
- Складывает общую стоимость продуктов дочернего класса Smartphone

## Тесты
- Тесты для модуля [test_category.py](tests/test_category.py)
- Тесты для модуля [test_products.py](tests/test_products.py)
- Тесты для модуля [iterator.py](src/iterator.py)
- Тесты для модуля [test_smartphone.py](tests/test_smartphone.py)
- Тесты для модуля [test_utils.py](tests/test_utils.py)
- Тесты для модуля [test_lawngrass.py](tests/test_lawngrass.py)