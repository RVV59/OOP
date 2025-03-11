import pytest
from src.category import Category
from src.product import Product


# Фикстура для сброса счетчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


# Тест на корректную инициализацию объекта Category
def test_category_initialization():
    products = [
        Product("Product 1", "Description 1", 100.0, 10),
        Product("Product 2", "Description 2", 200.0, 5)
    ]
    category = Category("Test Category", "This is a test category", products)

    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert len(category.products) == 2
    assert category.product_count == 2


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
