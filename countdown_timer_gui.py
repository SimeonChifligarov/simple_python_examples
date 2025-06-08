import tkinter as tk
from tkinter import messagebox


def start_timer():
    try:
        mins = int(entry_minutes.get() or 0)
        secs = int(entry_seconds.get() or 0)
        total_seconds = mins * 60 + secs
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror('Грешка', 'Моля, въведи валидни числа.')


def countdown(seconds_left):
    mins, secs = divmod(seconds_left, 60)
    time_str = f'{mins:02d}:{secs:02d}'
    label_timer.config(text=time_str)

    if seconds_left > 0:
        window.after(1000, countdown, seconds_left - 1)
    else:
        messagebox.showinfo('Готово', '⏰ Времето изтече!')


# 🪟 GUI Setup
window = tk.Tk()
window.title('⏳ Таймер за обратно броене')
window.geometry('300x200')

label_info = tk.Label(window, text='Въведи време:', font=('Arial', 12))
label_info.pack(pady=5)

frame_inputs = tk.Frame(window)
frame_inputs.pack()

entry_minutes = tk.Entry(frame_inputs, width=5)
entry_minutes.insert(0, '0')
entry_minutes.pack(side='left')
tk.Label(frame_inputs, text='мин').pack(side='left')

entry_seconds = tk.Entry(frame_inputs, width=5)
entry_seconds.insert(0, '10')
entry_seconds.pack(side='left')
tk.Label(frame_inputs, text='сек').pack(side='left')

button_start = tk.Button(window, text='▶️ Старт', command=start_timer)
button_start.pack(pady=10)

label_timer = tk.Label(window, text='00:00', font=('Courier', 36))
label_timer.pack(pady=10)

window.mainloop()
