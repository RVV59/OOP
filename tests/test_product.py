import pytest
from src.product import Product


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
    assert str(exc_info.value) == "Price cannot be negative"


def test_product_initialization_with_negative_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Test Product", "This is a test product", 99.99, -10)
    assert str(exc_info.value) == "Quantity cannot be negative"


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

    product.price = -10  # Некорректная цена
    assert product.price == 250, "Ошибка: цена изменилась на некорректное значение."

    product.price = 200  # Новая цена ниже текущей
    assert product.price == 250, "Ошибка: цена изменилась на меньшую."
