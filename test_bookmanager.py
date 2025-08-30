import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    # =========================
    # Test Case Asli (5 awal)
    # =========================
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
        self.assertEqual(0, self.book_manager.get_book_count())

    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Buku Tidak Ada")
        self.assertFalse(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Pemrograman Python", "Andi", 2020)
        book2 = Book("Basis Data", "Erlangga", 2021)
        book3 = Book("Algoritma", "Andi", 2020)  # Tahun diperbaiki ke 2020
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        books_by_andi = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(books_by_andi))
        books_by_erlangga = self.book_manager.find_books_by_author("Erlangga")
        self.assertEqual(1, len(books_by_erlangga))

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

    # =========================
    # Positive Test Cases
    # =========================
    def test_valid_book_creation(self):
        """Test Valid Book Creation"""
        book = Book("Data Science", "Budi", 2022)
        self.assertEqual(book.title, "Data Science")
        self.assertEqual(book.author, "Budi")
        self.assertEqual(book.year, 2022)

    def test_book_search_by_author(self):
        """Test Book Search by Author"""
        book1 = Book("Python", "Andi", 2020)
        book2 = Book("Java", "Budi", 2021)
        book3 = Book("C++", "Andi", 2022)
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        books = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(books))

    def test_book_search_by_year(self):
        """Test Book Search by Year"""
        book1 = Book("Python", "Andi", 2020)
        book2 = Book("Java", "Budi", 2021)
        book3 = Book("C++", "Andi", 2020)
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        books_2020 = self.book_manager.find_books_by_year(2020)
        self.assertEqual(2, len(books_2020))

    def test_multiple_books_added(self):
        """Test Multiple Books Added"""
        books = [
            Book("A", "Author1", 2020),
            Book("B", "Author2", 2021),
            Book("C", "Author3", 2022)
        ]
        for b in books:
            self.book_manager.add_book(b)
        self.assertEqual(len(self.book_manager.get_all_books()), 3)

    # =========================
    # Negative Test Cases
    # =========================
    def test_invalid_book_title(self):
        """Test Invalid Book Title"""
        with self.assertRaises(ValueError):
            Book("", "Andi", 2020)

    def test_invalid_year(self):
        """Test Invalid Year"""
        with self.assertRaises(ValueError):
            Book("Python", "Andi", 1999)
        with self.assertRaises(ValueError):
            Book("Python", "Andi", 2101)

    def test_remove_non_existent_book(self):
        """Test Remove Non-existent Book"""
        removed = self.book_manager.remove_book("NonExistent")
        self.assertFalse(removed)

    def test_search_non_existent_author(self):
        """Test searching non-existent author"""
        book = Book("Python", "Andi", 2020)
        self.book_manager.add_book(book)
        books = self.book_manager.find_books_by_author("Budi")
        self.assertEqual(len(books), 0)

    # =========================
    # Edge Test Cases
    # =========================
    def test_empty_book_manager(self):
        """Test Empty BookManager"""
        self.assertEqual(self.book_manager.get_book_count(), 0)
        self.assertEqual(len(self.book_manager.get_all_books()), 0)
        removed = self.book_manager.remove_book("Any Book")
        self.assertFalse(removed)

    def test_duplicate_books(self):
        """Test Duplicate Books"""
        book = Book("Python", "Andi", 2020)
        self.book_manager.add_book(book)
        self.book_manager.add_book(book)
        self.assertEqual(self.book_manager.get_book_count(), 2)

    def test_large_dataset(self):
        """Test Large Dataset"""
        for i in range(1000):
            self.book_manager.add_book(Book(f"Book {i}", f"Author {i%10}", 2000 + i%21))
        self.assertEqual(self.book_manager.get_book_count(), 1000)
        author5_books = self.book_manager.find_books_by_author("Author 5")
        self.assertTrue(len(author5_books) > 0)

    def test_case_sensitivity_in_author_search(self):
        """Test Case Sensitivity in Author Search"""
        book1 = Book("Python", "Andi", 2020)
        book2 = Book("Java", "andi", 2021)
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        books = self.book_manager.find_books_by_author("ANDI")
        self.assertEqual(len(books), 2)

if __name__ == '__main__':
    unittest.main()
