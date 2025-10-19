from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Price: ${self.__price}"

    @abstractmethod
    def calculate_late_fee(self, days_late):
        pass


class EBook(Book):
    def calculate_late_fee(self, days_late):
        return 0


class PrintedBook(Book):
    def calculate_late_fee(self, days_late):
        return days_late * 0.5

