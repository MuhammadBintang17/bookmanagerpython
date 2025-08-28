from typing import List
from book import Book

class BookManager:
    def __init__(self):   # <-- perbaikan, pakai __init__
        self.books = []

    def add_book(self, book: Book) -> None:
        if book is None:
            raise ValueError("Buku tidak boleh kosong")
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
            
        title_lower = title.strip().lower()
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title_lower]
        return len(self.books) < initial_count

    def get_all_books(self) -> List[Book]:
        return self.books.copy()

    def find_books_by_author(self, author: str) -> List[Book]:
        if author is None or not author.strip():
            raise ValueError("Penulis tidak boleh kosong")
            
        author_lower = author.strip().lower()
        return [book for book in self.books if book.author.lower() == author_lower]

    def find_books_by_year(self, year: int) -> List[Book]:
        if year < 2000 or year > 2100:  # aku ubah biar sesuai pesan error
            raise ValueError("Tahun hanya bisa diisi dari tahun 2000 sampai 2100")
            
        return [book for book in self.books if book.year == year]

    def get_book_count(self) -> int:
        return len(self.books)

    def contains(self, title: str) -> bool:
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
            
        title_lower = title.strip().lower()
        return any(book.title.lower() == title_lower for book in self.books)

    def clear_all_books(self) -> None:
        self.books.clear()
