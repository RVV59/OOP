import pytest
from src.product import Product, Smartphone, LawnGrass


def test_product_initialization():
    product = Product("Test Product", "This is a test product", 99.99, 10)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 99.99
    assert product.quantity == 10


def test_product_initialization_with_zero_quantity():
    product = Product("Test Product", "This is a test product", 99.99, 0)
    assert product.quantity == 0


def test_product_initialization_with_negative_price():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "This is a test product", -99.99, 10)
    assert str(exc_info.value) == "Цена должна быть положительной"


def test_product_initialization_with_negative_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "This is a test product", 99.99, -10)
    assert str(exc_info.value) == "Количество должно быть положительным"


def test_product():
    # Создаем продукт через класс-метод
    product_data = {
        'name': 'Сыр',
        'description': 'Голландский сыр',
        'price': 200,
        'quantity': 7
    }
    product = Product.new_product(product_data)

    # Проверяем атрибуты продукта
    assert product.name == "Сыр", "Ошибка в имени продукта."
    assert product.price == 200, "Ошибка в цене продукта."
    assert product.quantity == 7, "Ошибка в количестве продукта."

    # Проверяем сеттер для цены
    product.price = 250  # Корректная цена
    assert product.price == 250, "Ошибка в установке новой цены."

    # Проверяем обработку некорректной цены
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        product.price = -10  # Некорректная цена

    # Проверяем, что цена не изменилась после некорректной попытки
    assert product.price == 250, "Ошибка: цена изменилась после некорректной попытки."

    # Проверяем запрет уменьшения цены
    with pytest.raises(ValueError, match="Цена не может быть меньше текущей"):
        product.price = 200  # Новая цена ниже текущей

    # Проверяем, что цена не изменилась после попытки уменьшения
    assert product.price == 250, "Ошибка: цена изменилась после попытки уменьшения."
def test_product_addition():
    p1 = Product("Яблоко", "Фрукт", 100, 2)
    p2 = Product("Груша", "Фрукт", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3


def test_price_setter():
    p = Product("Тест", "Описание", 100, 10)

    # Корректное изменение цены
    p.price = 150
    assert p.price == 150

    # Попытка установить отрицательную цену
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        p.price = -50

    # Попытка уменьшить цену
    with pytest.raises(ValueError, match="Цена не может быть меньше текущей"):
        p.price = 100

def test_smartphone_creation():
    phone = Smartphone("iPhone", "Описание", 1000,
                       5, "High", "15", 256,
                       "Black")
    assert phone.memory == 256

def test_lawn_grass_creation():
    grass = LawnGrass("Трава", "Описание", 500,
                      10, "Россия", "14 дней",
                      "Зеленый")
    assert grass.germination_period == "14 дней"


def test_invalid_product_addition():
    p = Product("Яблоко", "Фрукт", 100, 2)
    s = Smartphone("iPhone", "Описание", 1000, 5,
                   "High", "15", 256, "Black")
    with pytest.raises(TypeError, match="Нельзя складывать разные классы"):
        p + s
