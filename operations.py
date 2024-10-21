from copy import copy, deepcopy

example1 = [
    "? mom",  # N
    "+ mom",
    "+ mom",
    "? mom",  # Y
    "- mom",
    "? mom",  # N
    "? dad",  # N
    "+ dog",
    "+ taco cat",
    "- evil olive",
    "? evil olive",  # N
    "+ evil olive",
    "+ evil olive",
    "+ evil olive",
    "? evil olive",  # Y
    "- evil olive",
    "- evil olive",
    "? evil olive",  # N
    "& mom"  # invalid operation, pass
    "+ yo banana boy",
    "+ dad",
    "+ step on no pets",
    "- evil olive"
    "+ no lemon no melon",
    "+ do geese see god",
    "? dad",  # Y
    "+ geese do see god",
    "+ cool geese",
    "+ egad an adage",
    "#",  # further operations wouldn't be performed
    "+ dd",
    "+ aaaa",
    "- aaaa"
]

example2 = ["+ mom", "- mom"] * ((10 ** 6) // 2)

example3 = deepcopy(example2)
example3.append("? mom")  # len = 10^6+1 elements
