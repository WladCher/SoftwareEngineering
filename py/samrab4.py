class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__current_page = 0

    def description(self):
        return f"Книга '{self.__title}' написана {self.__author} и содержит {self.__pages} страниц."

    def read(self, pages):
        if pages < 0:
            return "Невозможно прочитать отрицательное количество страниц."
        self.__current_page += pages
        if self.__current_page > self.__pages:
            self.__current_page = self.__pages
        return f"Сейчас вы на странице {self.__current_page}."

    def get_current_page(self):
        return self.__current_page

    def set_current_page(self, page):
        if 0 <= page <= self.__pages:
            self.__current_page = page
            return f"Страница установлена на {self.__current_page}."
        else:
            return "Недопустимый номер страницы."

my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(my_book.description())
print(my_book.read(50))
print(my_book.get_current_page())
print(my_book.set_current_page(200))
print(my_book.get_current_page())
print(my_book.set_current_page(500))
