class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.category_count = Category.category_count + 1
        self.product_count = len(products)
        Category.product_count += self.product_count
