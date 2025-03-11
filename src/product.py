from src.base_product import BaseProduct
from src.exceptions import ZeroQuantityError
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс описывающий Продукты"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных классов")
        return round(self.__price * self.quantity + other.__price * other.quantity, 2)

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    """Класс описывающий Категории товаров"""

    name: str
    description: str
    __products: list

    number_of_categories = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.number_of_categories += 1
        self.product_count = len(products)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name.title()}, количество продуктов: {total_quantity}"

    @property
    def products_in_list(self):
        return self.__products

    def add_product(self, product):
        try:
            if isinstance(product, Product):
                if product.quantity > 0:
                    self.__products.append(product)
                    self.product_count += 1
                else:
                    raise ZeroQuantityError(
                        "Товар с нулевым количеством не может быть добавлен"
                    )
            else:
                raise ValueError(
                    "Передаваемы аргумент должен быть экземпляром Product или его наследником"
                )

        except ZeroQuantityError as e:
            print(e)
        except ValueError as e:
            print(e)
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += str(product)
        return result

    def middle_price(self):
        try:
            return round(
                sum([product.price for product in self.__products])
                / self.product_count,
                2,
            )
        except ZeroDivisionError:
            return 0


class ProductIterator:
    """Класс итератор для перебора продуктов в классе Category"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):
    """Дочерний класс Product для смартфонов"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Дочерний класс Product для газонной травы"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
