import random

# Функція для перевірки парності числа
def is_even(number):
    return number % 2 == 0

# Порогова функція (поріг чутливості)
def threshold_function(x, threshold):
    return 1 if x >= threshold else 0

# Генеруємо випадкові ваги і поріг
random.seed(0)
weights = [random.random() for _ in range(12)]
threshold = random.random()

# Вхідні дані для чисел від 0 до 9
inputs = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],  # 1
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # 2
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 3
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0],  # 4
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],  # 5
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],  # 6
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 7
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],  # 8
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],  # 9
]

# Відповіді для чисел від 0 до 9 (1 - парне, 0 - непарне)
answers = [is_even(i) for i in range(10)]

# Гіперпараметри навчання
learning_rate = 0.1
epochs = 10

# Навчання персептрона
for epoch in range(epochs):
    errors = 0
    for i in range(10):
        # Обчислюємо вихід персептрона
        dot_product = sum(inputs[i][j] * weights[j] for j in range(12))
        output = threshold_function(dot_product, threshold)
        
        # Рахуємо помилку і коригуємо ваги
        error = answers[i] - output
        for j in range(12):
            weights[j] += learning_rate * error * inputs[i][j]
        threshold += learning_rate * error
        
        # Якщо була помилка, збільшуємо лічильник помилок
        if error != 0:
            errors += 1

    # Виводимо кількість помилок на поточній епосі
    print(f"Епоха {epoch + 1}, Кількість помилок: {errors}")

# Виводимо остаточні ваги та поріг
print("Остаточні ваги:", weights)
print("Остаточний поріг:", threshold)

# Перевірка результатів для чисел від 0 до 9
for i in range(10):
    dot_product = sum(inputs[i][j] * weights[j] for j in range(12))
    output = threshold_function(dot_product, threshold)
    if output == 1:
        print(f"Цифра {i} є парна.")
    else:
        print(f"Цифра {i} є непарна.")
