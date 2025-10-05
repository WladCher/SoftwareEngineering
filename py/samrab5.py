from triangle import f_heron

if __name__ == "__main__":
    a = float(input("Cторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    
    area = f_heron(a, b, c)
    print("Площадь треугольника равна - ", area)