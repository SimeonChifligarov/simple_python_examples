import tkinter as tk

# 🧾 Теми
themes = {
    'light': {
        'bg': '#FFFFFF',
        'fg': '#000000',
        'entry_bg': '#F0F0F0',
        'btn': '#E0E0E0',
        'btn_active': '#D0D0D0',
        'accent': '#4CAF50',
        'error': '#E57373'
    },
    'dark': {
        'bg': '#2E2E2E',
        'fg': '#F2F2F2',
        'entry_bg': '#3E3E3E',
        'btn': '#4E4E4E',
        'btn_active': '#5E5E5E',
        'accent': '#4CAF50',
        'error': '#E57373'
    }
}

current_theme = 'dark'  # Начална тема


def apply_theme(theme):
    colors = themes[theme]
    window.configure(bg=colors['bg'])
    entry.configure(bg=colors['entry_bg'], fg=colors['fg'], insertbackground=colors['fg'])
    clear_btn.configure(bg=colors['error'], fg=colors['fg'], activebackground=colors['btn_active'])
    toggle_btn.configure(bg=colors['btn'], fg=colors['fg'], activebackground=colors['btn_active'])

    for row in button_widgets:
        for char, btn in row.items():
            btn.configure(
                bg=colors['accent'] if char == '=' else colors['btn'],
                fg=colors['fg'],
                activebackground=colors['btn_active']
            )


def toggle_theme():
    global current_theme
    current_theme = 'light' if current_theme == 'dark' else 'dark'
    apply_theme(current_theme)


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
window.title('🧮 Калкулатор с тъмна/светла тема')
window.geometry('320x460')

entry = tk.Entry(window, font=('Consolas', 22), justify='right', bd=0)
entry.pack(fill='both', padx=10, pady=10, ipady=10)

# 🔢 Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

button_widgets = []

frame = tk.Frame(window)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')
    row_buttons = {}
    for char in row:
        btn = tk.Button(
            row_frame, text=char, font=('Arial', 16), width=5, height=2,
            command=(calculate if char == '=' else lambda c=char: on_button_click(c))
        )
        btn.pack(side='left', expand=True, fill='both', padx=1, pady=1)
        row_buttons[char] = btn
    button_widgets.append(row_buttons)

# 🧹 Clear Button
clear_btn = tk.Button(window, text='🧹 Изчисти', font=('Arial', 14), command=clear)
clear_btn.pack(fill='x', padx=10, pady=(10, 5))

# 🌗 Toggle Theme Button
toggle_btn = tk.Button(window, text='🌗 Смени тема', font=('Arial', 12), command=toggle_theme)
toggle_btn.pack(fill='x', padx=10, pady=(0, 10))

# 🎨 Apply Initial Theme
apply_theme(current_theme)

window.mainloop()
