class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def description(self):
        return f"Книга '{self.title}' написана {self.author} и содержит {self.pages} страниц."

    def is_long(self):
        return self.pages > 300

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        return f"Сейчас вы на странице {self.current_page}."


my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)

print(my_book.description())
print("Это длинная книга." if my_book.is_long() else "Это короткая книга.")
print(my_book.read(50))
print(my_book.read(100))