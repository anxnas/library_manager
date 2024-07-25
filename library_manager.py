import json
import os
from config import DATA_FILE

class Library:

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Загружает книги из файла."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_book(self):
        """Сохраняет данные в файл."""
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)

    def generate_id(self):
        """Генерирует уникальный идентификатор для новой книги."""
        if self.books:
            return max(book['id'] for book in self.books) + 1
        return 1

    def add_book(self, title, author, year):
        """Добавляет новую книгу в библиотеку."""
        new_book = {
            'id': self.generate_id(),
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        self.save_book()
        print(f"Книга '{title}' добавлена в библиотеку.")

    def delete_book(self, book_id):
        """Удаляет книгу из библиотеки по ID."""
        self.books = [book for book in self.books if book['id'] != book_id]
        self.save_book()
        print(f"Книга с ID {book_id} удалена из библиотеки.")

    def search_books(self, query, field):
        """Ищет книги по заданному полю и запросу."""
        return [book for book in self.books if query.lower() in book[field].lower()]

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if self.books:
            for book in self.books:
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
        else:
            print('База пуста.')

    def change_status(self, book_id, new_status):
        """Изменяет статус книги по ID."""
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_book()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_book_id(self, book_id):
        """Ищем книгу по ID."""
        for book in self.books:
            if book['id'] == book_id:
                return True
        return False