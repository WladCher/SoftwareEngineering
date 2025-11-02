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

class AudioBook(Book):
    def __init__(self, title, author, pages, duration_minutes):
        super().__init__(title, author, pages)
        self.duration_minutes = duration_minutes
        self.current_minute = 0

    def listen(self, minutes):
        self.current_minute += minutes
        if self.current_minute > self.duration_minutes:
            self.current_minute = self.duration_minutes
        return f"Вы прослушали {self.current_minute} из {self.duration_minutes} минут аудиокниги."

    def description(self):
        return f"Аудиокнига '{self.title}' автора {self.author}, длительность: {self.duration_minutes} минут."

paper_book = Book("Мастер и Маргарита", "Михаил Булгаков", 384)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 384, 720)

print(paper_book.description())
print(paper_book.read(50))
print(paper_book.is_long())

print(audio_book.description())
print(audio_book.listen(120))
print(audio_book.listen(300))
