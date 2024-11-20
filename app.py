while True:
    name = input("Введите своё имя (или введите 'выход' для завершения): ")
    if name.lower() == "выход":
        print("До свидания!")
        break
    print(f"Привет, {name}!")