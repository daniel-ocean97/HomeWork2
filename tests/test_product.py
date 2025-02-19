def test_product1(prod1):
    assert prod1.name == "cucumber"
    assert prod1.description == "green"
    assert prod1.price == 35.2
    assert prod1.quantity == 3


def test_product2(prod2):
    assert prod2.name == "tomatoes"
    assert prod2.description == "red"
    assert prod2.price == 15.2
    assert prod2.quantity == 5


def test_categories_number(cat1):
    assert cat1.number_of_categories == 1


def test_category(cat1, prod1, prod2):
    assert cat1.name == "vegetables"
    assert cat1.description == "for salad"
    assert cat1.products == [prod1, prod2]


def test_products_number(cat1):
    assert cat1.number_of_products == 2
