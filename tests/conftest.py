import pytest

from src.product import Category, Product


@pytest.fixture
def prod1():
    return Product(name="cucumber", description="green", price=35.2, quantity=3)


@pytest.fixture
def prod2():
    return Product(name="tomatoes", description="red", price=15.2, quantity=5)


@pytest.fixture
def cat1(prod1, prod2):
    return Category(name="vegetables", description="for salad", products=[prod1, prod2])


@pytest.fixture
def new_product():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
