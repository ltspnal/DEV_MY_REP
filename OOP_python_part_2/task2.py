class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.__bee_part = bee_part
        self.__elephant_part = elephant_part

    def fly(self):
        return self.__bee_part >= self.__elephant_part

    def trumpet(self):
        return "tu-tu-doo-doo" if self.__elephant_part >= self.__bee_part else "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.__elephant_part = max(0, self.__elephant_part - value)
            self.__bee_part = min(100, self.__bee_part + value)
        elif meal == "grass":
            self.__bee_part = max(0, self.__bee_part - value)
            self.__elephant_part = min(100, self.__elephant_part + value)

    def __str__(self):
        return f"Пчела: {self.__bee_part}, Слон: {self.__elephant_part}"


if __name__ == "__main__":
    creature = BeeElephant(30, 50)
    print("Начальное состояние:", creature)

    print("Может летать?", creature.fly())

    print("Звук:", creature.trumpet())

    creature.eat("nectar", 20)
    print("После поедания нектара (20):", creature)

    creature.eat("grass", 30)
    print("После поедания травы (30):", creature)

    creature.eat("nectar", 100)
    print("После поедания нектара (100):", creature)

    creature.eat("grass", 150)
    print("После поедания травы (150):", creature)
