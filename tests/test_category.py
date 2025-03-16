import pytest
from src.product import Product
from src.category import Category

# Фикстура для сброса счетчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_category_initialization():
    products = [
        Product("Product 1", "Description 1", 100.0, 10),
        Product("Product 2", "Description 2", 200.0, 5)
    ]
    category = Category("Test Category", "This is a test category", products)

    # Проверяем атрибуты категории
    assert category.name == "Test Category"
    assert category.description == "This is a test category"

    # Проверяем количество товаров
    assert len(category.get_products_list()) == 2, "Ожидается 2 товара в категории."

    # Проверяем вывод через геттер products
    expected_output = (
        "Product 1, 100.0 руб. Остаток: 10 шт.\n"
        "Product 2, 200.0 руб. Остаток: 5 шт.\n"
    )
    assert category.products == expected_output, "Ошибка в выводе списка товаров."


# Тест на подсчет количества категорий
def test_category_count():
    products1 = [Product("Product 1", "Description 1", 100.0, 10)]
    category1 = Category("Category 1", "Description 1", products1)

    products2 = [Product("Product 2", "Description 2", 200.0, 5)]
    category2 = Category("Category 2", "Description 2", products2)

    assert Category.category_count == 2


# Тест на подсчет количества продуктов
def test_product_count():
    products1 = [Product("Product 1", "Description 1", 100.0, 10)]
    category1 = Category("Category 1", "Description 1", products1)

    products2 = [
        Product("Product 2", "Description 2", 200.0, 5),
        Product("Product 3", "Description 3", 300.0, 7)
    ]
    category2 = Category("Category 2", "Description 2", products2)

    assert Category.product_count == 3


# Тест на корректность подсчета продуктов в конкретной категории
def test_product_count_in_category():
    products = [
        Product("Product 1", "Description 1", 100.0, 10),
        Product("Product 2", "Description 2", 200.0, 5)
    ]
    category = Category("Test Category", "This is a test category", products)

    assert category.product_count == 2


# Тесты для класса Category
def test_category():
    # Создаем категорию
    category = Category("Еда", "Продукты питания")

    # Создаем продукты
    product1 = Product("Хлеб", "Свежий хлеб", 50, 10)
    product2 = Product("Молоко", "Свежее молоко", 80, 5)

    # Добавляем продукты в категорию
    category.add_product(product1)
    category.add_product(product2)

    # Проверяем вывод списка товаров
    expected_output = "Хлеб, 50 руб. Остаток: 10 шт.\nМолоко, 80 руб. Остаток: 5 шт.\n"
    assert category.products == expected_output, "Ошибка в выводе списка товаров."

    # Проверяем счетчики
    assert category.product_count == 2, "Ошибка в счетчике продуктов."
    assert Category.product_count == 2, "Ошибка в общем счетчике продуктов."



