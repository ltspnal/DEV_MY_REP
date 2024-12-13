class Math:
    def addition(self, a, b):
        print(f"Результат сложения {a} + {b} = {a + b}")

    def subtraction(self, a, b):
        print(f"Результат вычитания {a} - {b} = {a - b}")

    def multiplication(self, a, b):
        print(f"Результат умножения {a} * {b} = {a * b}")

    def division(self, a, b):
        if b != 0:
            print(f"Результат деления {a} / {b} = {a / b}")
        else:
            print("Ошибка: деление на ноль!")


math = Math()

math.addition(5, 3)
math.subtraction(10, 4)
math.multiplication(7, 8)
math.division(20, 4)
math.division(10, 0)
