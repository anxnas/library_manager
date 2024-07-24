import unittest
import os
import json
from library_manager import Library
from config import DATA_FILE

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создает тестовую библиотеку и очищает данные перед каждым тестом."""
        self.library = Library()
        self.library.books = []
        self.library.save_book()

    def tearDown(self):
        """Удаляет тестовый файл после каждого теста."""
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Тест 1", "Тест 2", "2024")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0]['title'], "Тест 1")

    def test_delete_book(self):
        """Тест удаления книги."""
        self.library.add_book("Тест 1", "Тест 2", "2024")
        book_id = self.library.books[0]['id']
        self.library.delete_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        """Тест поиска книги."""
        self.library.add_book("Тест 1", "Тест 2", "2024")
        results = self.library.search_books("Тест 1", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Тест 1")

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.library.add_book("Тест 1", "Тест 2", "2024")
        book_id = self.library.books[0]['id']
        self.library.change_status(book_id, "выдана")
        self.assertEqual(self.library.books[0]['status'], "выдана")

    def test_search_book_id(self):
        """Тест поиска книги по ID."""
        self.library.add_book("Тест 1", "Тест 2", "2024")
        book_id = self.library.books[0]['id']
        self.assertTrue(self.library.search_book_id(book_id))
        self.assertFalse(self.library.search_book_id(999))

if __name__ == '__main__':
    unittest.main()