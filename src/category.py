from src.product import Product

class Category:
    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = [] if products is None else products
        Category.category_count += 1
        self.product_count = len(self.__products)
        Category.product_count += self.product_count

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product.")

    @property
    def products(self):
        """Возвращает строку с информацией о всех продуктах."""
        return '\n'.join(str(product) for product in self.__products)

    def get_products_list(self):
        """Возвращает исходный список объектов продуктов."""
        return self.__products

    def __str__(self):
        """Строковое представление категории с суммой quantity."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
