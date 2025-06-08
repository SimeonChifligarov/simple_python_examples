import random
import string


def generate_password(length=12, use_special_chars=True):
    if length < 4:
        raise ValueError('Паролата трябва да е поне 4 символа дълга.')

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Гарантираме, че има поне по един от всеки тип
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    print('🔐 Генератор на пароли 🔐')
    try:
        length = int(input('Въведи желана дължина на паролата (по подразбиране 12): ') or 12)
        use_special = input('Да се включват ли специални символи? (y/n): ').lower() != 'n'
        password = generate_password(length, use_special)
        print(f'\n✅ Генерирана парола: {password}')
    except ValueError as e:
        print('❌ Грешка:', e)
