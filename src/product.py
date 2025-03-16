class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        """Геттер для приватного атрибута __price."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватного атрибута __price."""
        if new_price <= 0:
            print("Price should not be zero or negative.")
        elif new_price < self.__price:
            print("New price cannot be lower than the current price.")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания объекта из словаря."""
        return cls(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )

    def __add__(self, other):
        """Сложение продуктов по общей стоимости на складе."""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return (self.price * self.quantity) + (other.price * other.quantity)
