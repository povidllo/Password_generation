from enum import Enum
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class Characters(Enum):
    low_case = ascii_lowercase
    up_case = ascii_uppercase
    digits = digits
    spec = punctuation

