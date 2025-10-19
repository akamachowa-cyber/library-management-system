# test_library.py

import pytest
from book import EBook, PrintedBook

def test_calculate_late_fee_ebook():
    ebook = EBook("EBook Test", "Alice", 10)
    assert ebook.calculate_late_fee(3) == 0

def test_calculate_late_fee_printed_book():
    printed_book = PrintedBook("Printed Test", "Bob", 25)
    assert printed_book.calculate_late_fee(4) == 2.0
