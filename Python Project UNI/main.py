from models import Car, CarShowroom

from tabulate import tabulate


def display_cars_table(title, car_list):
    print(f"\n=== {title.upper()} ===")
    if not car_list:
        print("Няма намерени коли по тези критерии.")
        return

    headers = ["Марка", "Модел", "Година", "Мощност (к.с.)", "Цена (лв.)", "Цена с 10% отстъпка"]
    table_data = []

    for car in car_list:
        table_data.append([
            car.brand,
            car.model,
            car.year,
            car.horsepower,
            f"{car.price:,.2f}",
            f"{car.calculate_discount(10):,.2f}"
        ])

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def main():

    showroom = CarShowroom("Premium Auto Sofia")


    showroom.add_car(Car("BMW", "M5 E39 (Старата мечка М5)", 2002, 45000, 400))
    showroom.add_car(Car("Audi", "RS6", 2021, 160000, 600))
    showroom.add_car(Car("VW", "Golf 4 1,4i (Наказателя на Дизел с чип от замунда)", 2003, 2500, 120 ))
    showroom.add_car(Car("BMW", "335i E92", 2008, 22000, 306))
    showroom.add_car(Car("Mercedes", "E55 AMG (Дядо Мерц)", 2002, 95000, 469))

    print(f"Добре дошли в {showroom.name}!")


    all_sorted = showroom.sort_cars_by_price(reverse=False)
    display_cars_table("Всички налични коли (Сортирани по цена възходящо)", all_sorted)

    target_brand = "BMW"
    bmw_cars = showroom.filter_by_brand(target_brand)
    display_cars_table(f"Филтрирано по марка: {target_brand}", bmw_cars)


if __name__ == "__main__":
    main()
