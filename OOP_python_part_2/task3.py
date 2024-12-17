class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []
        self.free_seats_flag = True
        self.seat_map = {i: None for i in range(1, max_seats + 1)}

    def board_passenger(self, *surnames):
        for surname in surnames:
            if None in self.seat_map.values():
                for seat, passenger in self.seat_map.items():
                    if passenger is None:
                        self.seat_map[seat] = surname
                        self.passengers.append(surname)
                        break
            else:
                self.free_seats_flag = False
                print(f"Места в автобусе заполнены. Невозможно посадить {surname}.")

    def disembark_passenger(self, *surnames):
        for surname in surnames:
            if surname in self.passengers:
                self.passengers.remove(surname)
                for seat, passenger in self.seat_map.items():
                    if passenger == surname:
                        self.seat_map[seat] = None
                        break
            else:
                print(f"Пассажир {surname} не найден в автобусе.")
        self.free_seats_flag = any(value is None for value in self.seat_map.values())

    def change_speed(self, delta):
        self.speed = max(0, min(self.max_speed, self.speed + delta))
        print(f"Текущая скорость: {self.speed} км/ч")

    def __contains__(self, surname):
        return surname in self.passengers

    def __iadd__(self, surname):
        self.board_passenger(surname)
        return self

    def __isub__(self, surname):
        self.disembark_passenger(surname)
        return self

    def __str__(self):
        return (f"Скорость: {self.speed} км/ч, Пассажиры: {self.passengers}, "
                f"Свободные места: {sum(1 for seat in self.seat_map.values() if seat is None)}")


if __name__ == "__main__":
    bus = Bus(max_seats=5, max_speed=120)
    print(bus)

    bus += "Иванов"
    bus += "Петров"
    bus.board_passenger("Сидоров", "Кузнецов")
    print(bus)

    print("Иванов" in bus)
    print("Васильев" in bus)

    bus -= "Петров"
    bus.disembark_passenger("Сидоров")
    print(bus)

    bus.change_speed(50)
    bus.change_speed(100)
    bus.change_speed(-30)
    print(bus)

    bus.board_passenger("Васильев", "Козлов")
    print(bus)
