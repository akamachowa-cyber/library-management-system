from book import EBook, PrintedBook
from payment import CashPayment, CreditCardPayment
from library_service import LibraryService

if __name__ == "__main__":
    ebook = EBook("Digital Python", "Alice Smith", 10)
    printed_book = PrintedBook("Python Basics", "John Doe", 25)

    print(ebook.get_details())
    print(f"Late fee for ebook: ${ebook.calculate_late_fee(5)}")

    print(printed_book.get_details())
    print(f"Late fee for printed book: ${printed_book.calculate_late_fee(5)}")

    cash_service = LibraryService(CashPayment())
    cash_service.pay_fine(5)

    card_service = LibraryService(CreditCardPayment())
    card_service.pay_fine(10)
