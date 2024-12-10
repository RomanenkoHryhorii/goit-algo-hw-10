import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x**2

def monte_carlo_integration(func, a, b, num_points=100000):
    # Генерація випадкових точок
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(0, func(b), num_points)
    
    # Підрахунок точок під кривою
    points_under_curve = y <= func(x)
    
    # Обчислення площі
    total_area = (b - a) * func(b)
    area_under_curve = total_area * np.sum(points_under_curve) / num_points
    
    return area_under_curve

# Параметри інтегрування
a, b = 0, 2
num_points_list = [1000, 10000, 100000, 1000000]

# Аналітичне обчислення
analytic_result = (b**3 - a**3) / 3
print(f"Аналітичний результат: {analytic_result}")

# Обчислення квадратури
quad_result, quad_error = spi.quad(f, a, b)
print(f"Результат quad(): {quad_result}, Похибка: {quad_error}")

# Метод Монте-Карло з різною кількістю точок
print("\nРезультати методу Монте-Карло:")
for num_points in num_points_list:
    mc_result = monte_carlo_integration(f, a, b, num_points)
    print(f"Точки: {num_points}, Інтеграл: {mc_result}")
    print(f"Відхилення від аналітичного: {abs(mc_result - analytic_result)}")

# Демонстрація збіжності методу
plt.figure(figsize=(10, 6))
mc_results = [monte_carlo_integration(f, a, b, num_points) for num_points in num_points_list]
plt.semilogx(num_points_list, mc_results, marker='o')
plt.axhline(y=analytic_result, color='r', linestyle='--', label='Аналітичний результат')
plt.title('Збіжність методу Монте-Карло')
plt.xlabel('Кількість точок')
plt.ylabel('Значення інтеграла')
plt.legend()
plt.grid(True)
plt.show()