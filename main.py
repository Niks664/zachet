import time

def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        
        print(f"Осталось: {h:02d}:{m:02d}:{s:02d}", end="\r")
        
        time.sleep(1) 
        total_seconds -= 1
        
    print("Время вышло!        ")

hours = int(input("Введите часы, если нет, то 0:"))
minutes = int(input("Введите минуты, если нет, то 0:"))
seconds = int(input("Введите секунды, если нет, то 0:"))

timer(hours, minutes, seconds)
