def append_record(file_path):
    cat = input("Введите категорию: ")
    cost = float(input("Введите сумму: "))
    comment = input("Добавьте комментарий: ")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{cat},{cost},{comment}\n")

def display_records(file_path):
    with open(file_path, encoding="utf-8") as file:
        for record in file:
            cat, cost, comment = record.rstrip().split(",")
            print(f"{cat}: {cost} руб. — {comment}")

if __name__ == "__main__":
    append_record("expenses.txt")
    print("\nСписок расходов:")
    display_records("expenses.txt")