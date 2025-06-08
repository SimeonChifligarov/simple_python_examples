import random
import time


def generate_numbers(count=5, max_num=99):
    return random.sample(range(1, max_num + 1), count)


def memory_game():
    print('🧠 Игра за памет: Запомни числата!')
    count = int(input('Колко числа искаш да запомниш? (напр. 5): ') or 5)
    duration = int(input('Колко секунди да се показват числата? (напр. 5): ') or 5)

    numbers = generate_numbers(count)
    print('\nЗапомни тези числа:')
    print(' '.join(str(n) for n in numbers))
    time.sleep(duration)

    # Изчистване на екрана (само визуално)
    print('\n' * 50)

    print('Въведи числата, които запомни, едно по едно:')

    guesses = []
    for i in range(count):
        try:
            guess = int(input(f'Число {i + 1}: '))
            guesses.append(guess)
        except ValueError:
            print('❌ Моля, въведи валидно число.')
            return

    correct = [num for num in guesses if num in numbers]
    print(f'\n🎯 Резултат: {len(correct)}/{count} познати')

    print('Оригинални числа:', numbers)
    print('Твоите отговори:', guesses)


if __name__ == '__main__':
    memory_game()
