class Soda:
    def __init__(self, flavor=None):
        """Инициализация объекта Soda с параметром flavor (вкус)"""
        self.flavor = flavor

    def __str__(self):
        """Метод строкового представления объекта"""
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"


soda1 = Soda("клубничным")
print(soda1)

soda2 = Soda()
print(soda2)
