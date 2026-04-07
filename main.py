import time

def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        
        print(f"Осталось: {h:02d}:{m:02d}:{s:02d}", end="\r")
        
        total_seconds -= 1
        
    print("Время вышло!        ")

timer(1, 30, 10)
