import json
from pathlib import Path

from src.product import Category, Product

data_file_path = Path(__file__).resolve().parent.parent / "data" / "products.json"


def read_from_json(path):
    """Функция, которая берёт информацию из json и преобразует в Python объект"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Создаёт объекты классов из данных, подгруженных из Json файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        categories.append(Category(**category))
    return categories
