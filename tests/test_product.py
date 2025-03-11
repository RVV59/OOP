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
