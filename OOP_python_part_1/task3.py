class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start_engine(self):
        print("Автомобиль заведен")

    def stop_engine(self):
        print("Автомобиль заглушен")

    def get_color(self):
        return f"Цвет автомобиля: {self.color}"

    def get_type(self):
        return f"Тип автомобиля: {self.car_type}"

    def get_year(self):
        return f"Год выпуска автомобиля: {self.year}"


my_car = Car("Черный", "Кроссовер", 2019)

print(my_car.get_color())
print(my_car.get_type())
print(my_car.get_year())

my_car.start_engine()

my_car.stop_engine()
