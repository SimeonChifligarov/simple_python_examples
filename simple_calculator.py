import tkinter as tk


def on_button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Грешка')


# 🪟 GUI Setup
window = tk.Tk()
window.title('🧮 Калкулатор')
window.geometry('300x400')

entry = tk.Entry(window, font=('Arial', 20), justify='right', bd=10, relief='sunken')
entry.pack(fill='both', padx=10, pady=10)

# 🔢 Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(window)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')
    for char in row:
        btn = tk.Button(row_frame, text=char, font=('Arial', 18), width=5, height=2,
                        command=(calculate if char == '=' else lambda c=char: on_button_click(c)))
        btn.pack(side='left', expand=True, fill='both')

clear_btn = tk.Button(window, text='🧹 Изчисти', font=('Arial', 14), command=clear)
clear_btn.pack(fill='x', padx=10, pady=5)

window.mainloop()
