from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class ReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key}={value}" for key,
        value in self.__dict__.items()])
        return f"{class_name}({attributes})"


class Product(BaseProduct, ReprMixin):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        print(f"Создан объект: {self.__repr__()}")

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных"
                            " классов")
        return (self.price * self.quantity) + (other.price *
                                               other.quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных "
                            "классов")
        return (self.__price * self.quantity) + (other.__price
                                                 * other.quantity)

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
            print("New price cannot be lower than the "
                  "current price.")
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

# class Smartphone(Product):
#     def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
#         super().__init__(name, description, price, quantity)
#         self.efficiency = efficiency
#         self.model = model
#         self.memory = memory
#         self.color = color
#
#
# class LawnGrass(Product):
#     def __init__(self, name, description, price, quantity, country, germination_period, color):
#         super().__init__(name, description, price, quantity)
#         self.country = country
#         self.germination_period = germination_period
#         self.color = color
