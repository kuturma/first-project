from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1
    # проверка что при добавлении книги add_new_book жанр не установлен
    def test_add_new_book_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # 2
    # проверка set_book_genre жанр присвоился книге если она есть в славаре book_genre
    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_set_book_genre_if_name_in_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # 3
    # проверка set_book_genre жанр не присвоился книге, если её нет в славаре book_genre
    @pytest.mark.parametrize('name, genre', [['Зубастая собака', 'Ужасы']])
    def test_set_book_genre_if_name_not_in_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) is None

    # 4
    # проверка получения жанра книги по ее имени get_book_genre
    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Ужасы']])
    def test_get_book_genre_get_genre_of_book_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == 'Ужасы'
    
    # 5
    # проверка вывода списока книг с определённым жанром get_books_with_specific_genre
    def test_get_books_with_specific_genre_get_list_books_for_specific_genre(self):
        collector = BooksCollector()
        list_books = ['Зубастая собака', 'Гордость и предубеждение и зомби']
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == list_books

    # 6
    # проверка get_books_genre выводит текущий словарь books_genre
    def test_get_books_genre_outputs_books_and_genre_of_books_genre(self):
        collector = BooksCollector()
        dictionary_books = {'Зубастая собака':'Ужасы', 'Гордость и предубеждение и зомби':'Ужасы','Смешная собака':'Комедии'}
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        assert collector.get_books_genre() == dictionary_books    

    # 7
    # проверка get_books_for_children возвращает книги, которые подходят детям, у жанра книги не должно быть возрастного рейтинга
    def test_get_books_for_children_return_only_book_for_children(self):    
        collector = BooksCollector()
        list_books = ['Смешная собака']
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        assert collector.get_books_for_children() == list_books

    # 8 
    # проверка add_book_in_favorites добавляет книгу в избранное, книга должна находиться в словаре books_genre
    def test_add_book_in_favorites_add_book_from_dictionary_books_genre_in_favorites(self):
        collector = BooksCollector()
        list_books = ['Смешная собака']
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        collector.add_book_in_favorites('Смешная собака')
        assert collector.get_list_of_favorites_books()== list_books

    # 9 
    # проверка add_book_in_favorites что повторно добавить книгу в избранное нельзя
    def test_add_book_in_favorites_add_book_from_dictionary_books_genre_in_favorites_duplicate_not_add(self):
        collector = BooksCollector()
        list_books = ['Смешная собака']
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        collector.add_book_in_favorites('Смешная собака')
        collector.add_book_in_favorites('Смешная собака')
        assert collector.get_list_of_favorites_books() == list_books

    # 10
    # проверка delete_book_from_favorites удаляет книгу из избранного, если она там есть
    @pytest.mark.parametrize('name, genre', [['Смешная собака', 'Комедии']])
    def test_delete_book_from_favorites_delet_book_from_favarites_book_that_is_on_list(self, name, genre):
        collector = BooksCollector()
        list_books = [name]
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    # 11
    # проверка delete_book_from_favorites ничего не удаляет из избранного, если удаляемой книги нет в избранном
    def test_delete_book_from_favorites_book_not_delet_if_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        collector.add_book_in_favorites('Смешная собака')
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')      
        collector.delete_book_from_favorites('Зубастая собака')
        assert collector.get_list_of_favorites_books() == ['Смешная собака']

    # 12
    # проверяем get_list_of_favorites_books получает список избранных книг
    def test_get_list_of_favorites_books_get_book_only_in_favorites(self):    
        collector = BooksCollector()
        collector.add_new_book('Смешная собака')
        collector.set_book_genre('Смешная собака', 'Комедии')
        collector.add_book_in_favorites('Смешная собака')
        collector.add_new_book('Зубастая собака')
        collector.set_book_genre('Зубастая собака', 'Ужасы')      
        assert collector.get_list_of_favorites_books() == ['Смешная собака']


# проверка вывода списока книг с определённым жанром get_books_with_specific_genre реализована через фикстуру АНАЛОГ 5 теста  
def test_get_books_with_specific_genre_get_list_books_for_specific_genre_by_fixture(collector_with_books):
    list_books = ['Зубастая собака', 'Гордость и предубеждение и зомби']
    assert collector_with_books.get_books_with_specific_genre('Ужасы') == list_books

# проверка get_books_genre выводит текущий словарь books_genre АНАЛОГ 6 теста  
def test_get_books_genre_outputs_books_and_genre_of_books_genre_by_fixture(collector_with_books):
    dictionary_books = {'Зубастая собака':'Ужасы', 'Гордость и предубеждение и зомби':'Ужасы','Смешная собака':'Комедии'}
    assert collector_with_books.get_books_genre() == dictionary_books

# проверка get_books_for_children возвращает книги, которые подходят детям, у жанра книги не должно быть возрастного рейтинга АНАЛОГ 7 теста  
def test_get_books_for_children_return_only_book_for_children_by_fixture(collector_with_books):
    list_books = ['Смешная собака']
    assert collector_with_books.get_books_for_children() == list_books