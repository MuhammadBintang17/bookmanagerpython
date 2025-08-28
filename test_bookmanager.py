import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())  # Diperbaiki dari 'o' menjadi '0'

    # Unit Test dibawah untuk buku yang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Buku Tidak Ada")
        self.assertFalse(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    # Unit Test dibawah untuk mencari buku berdasarkan penulis
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Pemrograman Python", "Andi", 2020)
        book2 = Book("Basis Data", "Erlangga", 2021)
        book3 = Book("Algoritma", "Andi", 2019)
        
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        
        books_by_andi = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(books_by_andi))
        
        books_by_erlangga = self.book_manager.find_books_by_author("Erlangga")
        self.assertEqual(1, len(books_by_erlangga))

    # Unit Test dibawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Pemrograman Python", "Andi", 2020)
        book2 = Book("Basis Data", "Erlangga", 2021)
        
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        
        all_books = self.book_manager.get_all_books()
        self.assertEqual(2, len(all_books))
        self.assertIn(book1, all_books)
        self.assertIn(book2, all_books)

if __name__ == '_main_':
    unittest.main()