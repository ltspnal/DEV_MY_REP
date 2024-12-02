def calculate_bmi():
    try:
        m = float(input("Введите массу тела в кг: "))
        h = float(input("Введите рост в метрах: "))

        if m <= 0 or h <= 0:
            raise ValueError("Вес и рост должны быть положительными числами")

        h = h / 100
        i = m / (h ** 2)

        if i < 18.5:
            print("Недостаточная (дефицит) масса тела")
        elif i > 18.5 and i < 25:
            print("Норма")
        elif i > 25 and i < 30:
            print("Избыточная масса тела")
        else:
            print("Ожирение")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except ZeroDivisionError:
        print("Рост не может быть равен нулю.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    calculate_bmi()
