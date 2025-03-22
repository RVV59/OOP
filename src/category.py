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
        """Добавляет объект класса Product в список товаров."""
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса"
                            " Product.")

    @property
    def products(self):
        """Геттер для приватного атрибута __products.
        Возвращает строку с информацией о всех продуктах."""
        result = ""
        for product in self.__products:
            result += (f"{product.name}, {product.price} руб."
                       f" Остаток: {product.quantity} шт.\n")
        return result

    def get_products_list(self):
        """Возвращает список товаров."""
        return self.__products
