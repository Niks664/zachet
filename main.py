def get_input(prompt):
    while True:
        text = input(prompt)
        if text.isdigit():
            return int(text)
        print("Ошибка! Введи число.")

print("Настройка Таймера")
hours = get_input("Введите часы: ")
minutes = get_input("Введите минуты: ")
seconds = get_input("Введите секунды: ")

total_seconds = hours * 3600 + minutes * 60 + seconds

print("\nТаймер запущен!")
