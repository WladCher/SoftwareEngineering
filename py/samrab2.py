import random

def cube():
    value = random.randint(1, 6)
    print(f"Выпавшее число - {value}")
    
    if value in (5, 6):
        print("Вы победили")
    elif value in (3, 4):
        cube()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    cube()