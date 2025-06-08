import time


def countdown(minutes: int, seconds: int = 0):
    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f'{mins:02d}:{secs:02d}'
        print(f'\r⏳ Таймер: {timer_display}', end='')
        time.sleep(1)
        total_seconds -= 1

    print('\r⏰ ВРЕМЕТО ИЗТЕЧЕ!           ')


if __name__ == '__main__':
    print('🕒 Countdown Timer')
    try:
        mins = int(input('Въведи минути: ') or 0)
        secs = int(input('Въведи секунди: ') or 0)
        print('Започва отброяване...\n')
        countdown(mins, secs)
    except ValueError:
        print('❌ Моля, въведи валидни числа.')
