import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


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

    def test_smartphone_initialization():
        smartphone = Smartphone("Samsung", "Описание", 100000, 10, "Высокая", "S23", 256, "Черный")
        assert smartphone.name == "Samsung"
        assert smartphone.efficiency == "Высокая"

    def test_lawn_grass_initialization():
        grass = LawnGrass("Трава", "Описание", 500, 20, "Россия", "14 дней", "Зеленый")
        assert grass.country == "Россия"

    def test_repr_mixin():
        product = Product("Test Product", "Description", 100, 10)
        assert repr(product) == "Product(name=Test Product, description=Description, price=100, quantity=10)"

    def test_add_products():
        p1 = Product("Product1", "Desc1", 100, 2)
        p2 = Product("Product2", "Desc2", 200, 3)
        total = p1 + p2
        assert total == (100 * 2 + 200 * 3)

    def test_add_different_classes():
        p = Product("Product", "Desc", 100, 2)
        s = Smartphone("Samsung", "Desc", 100000, 1, "High", "S23", 256, "Black")
        with pytest.raises(TypeError):
            p + s

    def test_category_add_product():
        category = Category("Test Category", "Description")
        product = Product("Test Product", "Description", 100, 10)
        category.add_product(product)
        assert len(category.get_products_list()) == 1

    def test_category_add_invalid_product():
        category = Category("Test Category", "Description")
        with pytest.raises(TypeError):
            category.add_product("Not a product")
