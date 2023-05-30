import random
import string


def get_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def get_email() -> str:
    return f"{get_string()}@{get_string()}.xyz"


def get_phone_number() -> str:
    template = "({}{}{})-{}{}{}-{}{}{}{}"

    ten_numbers = [random.randint(0, 9) for _ in range(10)]
    return template.format(*ten_numbers)
