from main import BooksCollector
import pytest

# @pytest.fixture создаем 3 книги и присваиваем им жанры, из них 2 с одинаковым жанром
@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    collector.add_new_book('Зубастая собака')
    collector.set_book_genre('Зубастая собака', 'Ужасы')
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Смешная собака')
    collector.set_book_genre('Смешная собака', 'Комедии')
    return collector