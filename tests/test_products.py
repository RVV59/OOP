import pytest
from src.product import Product
from src.category import Category

def test_product_creation():
    """Проверка создания продукта с валидными данными."""
    product = Product("Тестовый товар", "Описание", 100, 10)
    assert product.name == "Тестовый товар"
    assert product.quantity == 10

def test_invalid_price():
    """Проверка исключения при отрицательной цене."""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", -100, 10)

def test_invalid_quantity():
    """Проверка исключения при отрицательном количестве."""
    with pytest.raises(ValueError):
        Product("Товар", "Описание", 100, -10)

def test_product_addition():
    """Проверка сложения двух продуктов."""
    product_a = Product("A", "Описание", 100, 10)
    product_b = Product("B", "Описание", 200, 2)
    assert product_a + product_b == 1400  # 100*10 + 200*2

def test_add_different_types():
    """Проверка ошибки при сложении с не-Product."""
    product_a = Product("A", "Описание", 100, 10)
    with pytest.raises(TypeError):
        product_a + 123  # Попытка сложить с числом

def test_category_str():
    """Проверка строкового представления категории."""
    product1 = Product("Товар1", "Описание", 100, 5)
    product2 = Product("Товар2", "Описание", 200, 8)
    product3 = Product("Товар3", "Описание", 300, 14)
    category = Category("Категория", "Описание", [product1, product2, product3])
    assert str(category) == "Категория, количество продуктов: 27 шт."  # 5+8+14=27

def test_products_getter():
    """Проверка геттера products в Category."""
    product = Product("Товар", "Описание", 100, 10)
    category = Category("Категория", "Описание", [product])
    expected_str = "Товар, 100 руб. Остаток: 10 шт."
    assert category.products == expected_str
