from book import EBook, PrintedBook

def test_calculate_late_fee():
    ebook = EBook("EBook Test", "Alice", 10)
    printed_book = PrintedBook("Printed Test", "Bob", 25)
    assert ebook.calculate_late_fee(3) == 0
    assert printed_book.calculate_late_fee(4) == 2.0
