def calculator():
    print("Добро пожаловать в калькулятор!")

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            operation = input("Введите операцию (+, -, *, /): ")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно!")
                result = num1 / num2
            else:
                raise ValueError("Неверная операция. Попробуйте снова.")

            print(f"Результат: {result}")

        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
        except ZeroDivisionError as zde:
            print(f"Ошибка: {zde}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        choice = input("Хотите продолжить? (да/нет): ").strip().lower()
        if choice != "да":
            print("Спасибо за использование калькулятора. До свидания!")
            break


if __name__ == "__main__":
    calculator()
