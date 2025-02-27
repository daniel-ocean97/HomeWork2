import pytest

from src.product import Product, ProductIterator


def test_product1(prod1):
    """Первый тест на проверку экземпляра класса Product"""
    assert prod1.name == "cucumber"
    assert prod1.description == "green"
    assert prod1.price == 35.2
    assert prod1.quantity == 3


def test_product2(prod2):
    """Второй тест на проверку экземпляра класса Product"""
    assert prod2.name == "tomatoes"
    assert prod2.description == "red"
    assert prod2.price == 15.2
    assert prod2.quantity == 5


def test_categories_number(cat1):
    """Тест на проверку количества категорий в экземпляре класса Category"""
    assert cat1.number_of_categories == 1


def test_category(cat1, prod1, prod2):
    """Тест, который проверяет корректность инициализации объектов класса Category"""
    assert cat1.name == "vegetables"
    assert cat1.description == "for salad"


def test_category_products(cat1):
    """Проверка геттера products в классе Categories"""
    assert (
        cat1.products
        == "cucumber, 35.2 руб. Остаток: 3 шт.\ntomatoes, 15.2 руб. Остаток: 5 шт.\n"
    )


def test_products_number(cat1, new_product, capsys):
    """Тест, который проверяет подсчет количества продуктов и метод add_product"""
    assert cat1.product_count == 2
    cat1.add_product(new_product)
    assert cat1.product_count == 3
    cat1.add_product("test")
    assert (
        capsys.readouterr().out
        == "Передаваемы аргумент должен быть экземпляром Product или его наследником\n"
    )
    assert cat1.product_count == 3


def test_new_product():
    """Проверка класс-метода nrw_product в классе Product"""
    product = Product.new_product(
        {
            "name": "Смартфон",
            "description": "Новый флагман",
            "price": 999.99,
            "quantity": 5,
        }
    )
    assert product.name == "Смартфон"
    assert product.description == "Новый флагман"
    assert product.price == 999.99
    assert product.quantity == 5


def test_set_new_price(prod1, capsys):
    """Тест метода price класса Product"""
    assert prod1.price == 35.2
    prod1.price = 36
    assert prod1.price == 36
    prod1.price = 0
    assert capsys.readouterr().out == "Цена не должна быть нулевая или отрицательная\n"
    assert prod1.price == 36


def test_product_str(prod1):
    """Тест строкового отображения класса Product"""
    assert str(prod1) == "cucumber, 35.2 руб. Остаток: 3 шт.\n"


def test_category_str(cat1):
    """Тест строкового отображения класса Category"""
    assert str(cat1) == "Vegetables, количество продуктов: 8"


def test_product_add(prod1, prod2):
    """Тест магического метода __add__ класса Product"""
    assert prod2 + prod1 == 181.6


def test_product_iterator(cat1):
    """Тест класса-итератора ProductIterator"""
    iterator = ProductIterator(cat1)
    assert iterator.index == 0
    assert next(iterator).name == "cucumber"
    assert next(iterator).name == "tomatoes"
    with pytest.raises(StopIteration):
        next(iterator)
