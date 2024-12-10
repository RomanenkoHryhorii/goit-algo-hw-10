import pulp

def optimize_beverage_production():
    # Створення моделі лінійного програмування
    model = pulp.LpProblem(name="beverage-production-optimization", sense=pulp.LpMaximize)

    # Змінні рішення - кількість вироблених напоїв
    lemonade = pulp.LpVariable(name="Lemonade", lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable(name="FruitJuice", lowBound=0, cat='Integer')

    # Цільова функція - максимізація загальної кількості вироблених напоїв
    model += lemonade + fruit_juice, "Total_Production"

    # Обмеження на ресурси
    # Вода: 2 од. на лимонад, 1 од. на фруктовий сік, всього 100 од.
    model += (2 * lemonade + fruit_juice <= 100, "Water_Constraint")
    
    # Цукор: 1 од. на лимонад, 0 на фруктовий сік, всього 50 од.
    model += (lemonade <= 50, "Sugar_Constraint")
    
    # Лимонний сік: 1 од. на лимонад, 0 на фруктовий сік, всього 30 од.
    model += (lemonade <= 30, "Lemon_Juice_Constraint")
    
    # Фруктове пюре: 0 на лимонад, 2 од. на фруктовий сік, всього 40 од.
    model += (2 * fruit_juice <= 40, "Fruit_Puree_Constraint")

    # Розв'язання моделі
    model.solve()

    # Виведення результатів
    print("Статус оптимізації:", pulp.LpStatus[model.status])
    print("Кількість Лимонаду:", lemonade.varValue)
    print("Кількість Фруктового соку:", fruit_juice.varValue)
    print("Загальна кількість вироблених напоїв:", 
          lemonade.varValue + fruit_juice.varValue)

    # Перевірка використання ресурсів
    print("\nВикористання ресурсів:")
    print(f"Вода: {2 * lemonade.varValue + fruit_juice.varValue}/100")
    print(f"Цукор: {lemonade.varValue}/50")
    print(f"Лимонний сік: {lemonade.varValue}/30")
    print(f"Фруктове пюре: {2 * fruit_juice.varValue}/40")

# Виклик функції оптимізації
optimize_beverage_production()