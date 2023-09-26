from string import digits, ascii_uppercase

from random import choices, shuffle

def generate_key():
    key = []
    for _ in range(3):
        key_part = choices(digits, k=2) + choices(ascii_uppercase, k=3)
        shuffle(key_part)

        key.append(''.join(key_part))

    return '-'.join(key)
