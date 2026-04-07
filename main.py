import time

while total_seconds >= 0:
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    
    print(f"Осталось времени: {h:02d}:{m:02d}:{s:0  2d}", end="\r")
    
    time.sleep(1) 
    total_seconds -= 1

print("\n\nВремя вышло! Таймер остановлен.")

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

