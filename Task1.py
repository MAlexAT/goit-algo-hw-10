# В терміналі встановіть: pip install pulp
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створення моделі задачі
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні: кількість вироблених одиниць "Лимонаду" та "Фруктового соку"
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Мета: максимізувати загальну кількість продуктів
model += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Максимальна кількість Лимонаду: {value(lemonade)}")
print(f"Максимальна кількість Фруктового соку: {value(fruit_juice)}")
print(f"Загальна максимальна кількість вироблених продуктів: {value(model.objective)}")

'''
Пояснення коду
Створення моделі: Задача оптимізації визначена як максимізація.
Змінні: Визначаємо змінні lemonade та fruit_juice, які позначають кількість 
вироблених одиниць "Лимонаду" та "Фруктового соку".
Цільова функція: Мета - максимізувати загальну кількість вироблених одиниць продуктів.
Обмеження: Додаємо обмеження на ресурси:
Вода: обмежена до 100 од.
Цукор: обмежений до 50 од.
Лимонний сік: обмежений до 30 од.
Фруктове пюре: обмежене до 40 од.
Розв'язання та виведення результатів: Задача розв'язується, і виводиться 
оптимальна кількість вироблених одиниць "Лимонаду" та "Фруктового соку" разом із загальною кількістю.

Очікуваний результат
Цей код поверне оптимальну кількість "Лимонаду" та "Фруктового соку", 
яку можна виготовити при максимальному використанні обмежених ресурсів.
'''