class Car:
    def __init__(self, brand, model, year, price, horsepower):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.horsepower = horsepower

    def get_full_name(self):
        return f"{self.brand} {self.model} ({self.year})"

    def calculate_discount(self, percent):
        if 0 < percent < 100:
            discounted_price = self.price * (1 - percent / 100)
            return round(discounted_price, 2)
        return self.price


class CarShowroom:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def filter_by_brand(self, brand_name):
        filtered_cars = []
        for car in self.inventory:
            if car.brand.lower() == brand_name.lower():
                filtered_cars.append(car)
        return filtered_cars

    def sort_cars_by_price(self, reverse=False):
        """Сортира наличните коли по цена."""
        # Ползваме вградената сортировка с ламбда функция по цената
        return sorted(self.inventory, key=lambda car: car.price, reverse=reverse)