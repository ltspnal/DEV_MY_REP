class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        return len(self) % len(s) == 0 and self == s * (len(self) // len(s))

    def is_palindrom(self):
        """
        Проверяет, является ли текущая строка палиндромом (без учета регистра).
        Возвращает True, если да, иначе False.
        """
        normalized_str = self.lower()
        return normalized_str == normalized_str[::-1]


s = SuperStr("abcabcabc")
print(s.is_repeatance("abc"))
print(s.is_repeatance("abcd"))

s2 = SuperStr("radar")
print(s2.is_palindrom())

s3 = SuperStr("hello")
print(s3.is_palindrom())
