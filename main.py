import os
from library_manager import Library

def clear_console():
    """Очищает консоль."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    library = Library()
    while True:
        print("\nМеню:\n"
              "1. Добавить книгу\n"
              "2. Удалить книгу\n"
              "3. Искать книгу\n"
              "4. Отобразить все книги\n"
              "5. Изменить статус книги\n"
              "6. Выйти")
        action = input("Выберите действие: ")

        clear_console()
        if action == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
            except ValueError:
                print('Введите год издания корректно!')
            library.add_book(title, author, year)
        elif action == '2':
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                is_book = library.search_book_id(book_id)
                if is_book:
                    library.delete_book(book_id)
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            except ValueError:
                print('Введите корректный ID!')
        elif action == '3':
            field_input = input("Искать по (1 - по названию/2 - по автору /3 - по году выпуска): ")
            if field_input == '1':
                field = 'title'
            elif field_input == '2':
                field = 'author'
            elif field_input == '3':
                field = 'year'
            else:
                print('Введите корректное значение!')
            query = input("Введите запрос для поиска: ")
            results = library.search_books(query, field)
            if results:
                for book in results:
                    print(
                        f"ID: {book['id']}\nНазвание: {book['title']}\nАвтор: {book['author']}\nГод: {book['year']}\nСтатус: {book['status']}")
            else:
                print('Книга не найдена по запросу!')
        elif action == '4':
            library.display_books()
        elif action == '5':
            try:
                book_id = int(input("Введите ID книги для изменения статуса: "))
                is_book = library.search_book_id(book_id)
                if is_book:
                    new_status_input = input("Введите новый статус (1 - в наличии/2 - выдана): ")
                    if new_status_input == '1':
                        new_status = 'в наличии'
                    elif new_status_input == '2':
                        new_status = 'выдана'
                    else:
                        print('Введите корректное значение!')
                    library.change_status(book_id, new_status)
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            except ValueError:
                print('Введите корректный ID!')
        elif action == '6':
            print("Завершение работы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()