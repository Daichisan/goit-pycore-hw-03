import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    if cleaned_number.startswith("+"):
        return cleaned_number
    elif cleaned_number.startswith("380"):
        return "+" + cleaned_number[1:]
    else:
        return "+38" + cleaned_number

raw_numbers = [
    "095\\b123 6677",
    "(066) 123-5678\\b",
    "+380 44 123 4567",
    "380951237777",
    "    +38(095)223-23-34",
    "     0505651884",
    "(050)6669801",
    "38044-321-00-11",
    "38063 123 21 10   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)