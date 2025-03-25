from abc import ABC, abstractmethod


class ReprMixin:
    def __init__(self):
        print(repr(self))


    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"


class BaseProduct(ABC):
    @abstractmethod
    def new_product(cls, product_data):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, ReprMixin):
    def __init__(self, name, description, price, quantity):
        if price < 0:
            # raise ValueError("Price cannot be negative")
            raise ValueError("Цена должна быть положительной")
        if quantity < 0:
            # raise ValueError("Quantity cannot be negative")
            raise ValueError("Количество должно быть положительным")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        if value < self._price:
            raise ValueError("Цена не может быть меньше текущей")
        self._price = value

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать разные классы")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color