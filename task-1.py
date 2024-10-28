class Solution:
    def romanToInt(self, s):
        # Створюємо словник для зберігання значень римських цифр
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Ініціалізуємо змінну для зберігання результату
        result = 0
        
        # Проходимо по рядку римських цифр
        for i in range(len(s)):
            # Якщо поточна цифра менша за наступну, віднімаємо її значення з результату
            # Це робиться для таких випадків як IV (4) і IX (9), де I стоїть перед V або X
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            # Інакше додаємо її значення до результату
            else:
                result += roman_values[s[i]]
        
        return result

# Приклади використання функції
sol = Solution()
print(sol.romanToInt("III"))    # Вивід: 3
print(sol.romanToInt("LVIII"))  # Вивід: 58
print(sol.romanToInt("MCMXCIV"))  # Вивід: 1994
