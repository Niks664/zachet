import time

while total_seconds >= 0:
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    
    print(f"Осталось времени: {h:02d}:{m:02d}:{s:0  2d}", end="\r")
    
    time.sleep(1) 
    total_seconds -= 1

print("\n\nВремя вышло! Таймер остановлен.")
