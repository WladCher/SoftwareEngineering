# собственное исключение, если строка пустая
class EmptyTextError(Exception):
    """Ошибка: пустой текст"""
    pass


# первая функция — проверяет имя пользователя
def check_name(name):
    if not name.strip():  # если пусто или только пробелы
        raise EmptyTextError("Имя не может быть пустым")
    print(f"Имя принято: {name}")


# вторая функция — проверяет комментарий
def check_comment(comment):
    if not comment.strip():
        raise EmptyTextError("Комментарий не должен быть пустым")
    print("Комментарий сохранён:", comment)


if __name__ == "__main__":
    try:
        check_name("  ")  # вызывает исключение
    except EmptyTextError as e:
        print("Ошибка:", e)

    try:
        check_comment("Hello world!")  # всё хорошо
    except EmptyTextError as e:
        print("Ошибка:", e)