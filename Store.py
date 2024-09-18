class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Пустой словарь для товаров

    def add_item(self, item_name, price_per_kg):
        """Добавить товар в ассортимент."""
        self.items[item_name] = price_per_kg

    def remove_item(self, item_name):
        """Удалить товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Получить цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price_per_kg):
        """Обновить цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price_per_kg

    def __str__(self):
        """Вывести информацию о магазине."""
        return f'Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}'

# Создадим несколько объектов класса Store

store1 = Store("Продукты у Дома", "ул. Пушкина, д. 10")
store1.add_item("яблоки", 120)  # Цена за килограмм в рублях
store1.add_item("бананы", 80)

store2 = Store("Фермерские товары", "ул. Ленина, д. 5")
store2.add_item("молоко", 50)
store2.add_item("сыр", 300)

store3 = Store("Мясная лавка", "ул. Советская, д. 25")
store3.add_item("говядина", 500)
store3.add_item("свинина", 400)

# Выведем информацию о магазинах
print(store1)
print(store2)
print(store3)

# Тестирование методов на первом магазине

# Получим цену яблок
print(f'Цена яблок за кг: {store1.get_price("яблоки")} руб.')

# Обновим цену бананов
store1.update_price("бананы", 90)
print(f'Обновленная цена бананов: {store1.get_price("бананы")} руб.')

# Удалим яблоки из ассортимента
store1.remove_item("яблоки")
print(f'После удаления яблок: {store1}')
