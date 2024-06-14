
from enum import Enum

class user_types(Enum):
    ADMIN = 1
    USER = 2
    GUEST = 3

class user_menu(Enum):
    LOAN = 1
    RETURN = 2
    DISPLAY_BOOKS = 3
    SEARCH_BOOK = 4

class admin_menu(Enum):
    ADD_CUSTOMER = 1

class book_types(Enum):
    TEN_DAYS = 10
    FIVE_DAYS = 5
    TWO_DAYS = 2

