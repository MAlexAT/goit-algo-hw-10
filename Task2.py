import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi   # Втановити бібліотеку scipy командою pip install

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()



# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(func, a, b, num_points=100000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Виконуємо обчислення методом Монте-Карло
mc_result = monte_carlo_integration(f, a, b)

# Обчислення аналітичного результату за допомогою функції quad
analytical_result, error = spi.quad(f, a, b)

# Виведення результатів
print(f"Інтеграл (Монте-Карло): {mc_result}")
print(f"Інтеграл (quad): {analytical_result}, з помилкою: {error}")

# Висновки та порівняння результатів в файлі readme.md

