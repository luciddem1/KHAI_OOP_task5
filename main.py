import tkinter as tk
from tkinter import messagebox

def IsPower5(K):
    if K <= 0:
        return False

    while K > 1:
        if K % 5 != 0:
            return False
        K /= 5

    return True

def count_powers():
    try:
        numbers_str = entry_numbers.get()
        numbers = list(map(int, numbers_str.split(',')))
        count = sum(IsPower5(number) for number in numbers)
        result_label.config(text=f"Кількість ступенів числа 5 у наборі: {count}")
    except ValueError:
        result_label.config(text="Помилка: Введіть коректний набір чисел")

def calculate_y(k, y_prev, U, T0, T, K):
    return (1 - T0 / T) * y_prev + (T0 / T) * K * U

def show_task1():
    # Приховання елементів головного меню
    menu_frame.pack_forget()

    # Відображення елементів для завдання 1
    task1_frame.pack()

def return_to_menu():
    # Приховання елементів завдання 1
    task1_frame.pack_forget()

    # Відображення елементів головного меню
    menu_frame.pack()

# Створення головного вікна
root = tk.Tk()
root.title("Меню завдань")

# Створення меню
menu_frame = tk.Frame(root)

button_task1 = tk.Button(menu_frame, text="Завдання 1", command=show_task1)
button_task1.pack()

menu_frame.pack(pady=20)

# Завдання 1
task1_frame = tk.Frame(root)

label_numbers = tk.Label(task1_frame, text="Введіть набір чисел (розділені комами):")
label_numbers.pack()

entry_numbers = tk.Entry(task1_frame)
entry_numbers.pack()

calculate_button = tk.Button(task1_frame, text="Обчислити", command=count_powers)
calculate_button.pack()

return_button = tk.Button(task1_frame, text="Повернутися в меню", command=return_to_menu)
return_button.pack()

result_label = tk.Label(task1_frame, text="")
result_label.pack()

# Завдання 2
def show_task2_window():
    task2_window = tk.Toplevel(root)
    task2_window.title("Завдання 2")

    # Зміни для завдання 2...
    label_T = tk.Label(task2_window, text="Введіть T:")
    label_T.pack()

    entry_T = tk.Entry(task2_window)
    entry_T.pack()

    label_K = tk.Label(task2_window, text="Введіть K:")
    label_K.pack()

    entry_K = tk.Entry(task2_window)
    entry_K.pack()

    label_U0 = tk.Label(task2_window, text="Введіть початкове значення U:")
    label_U0.pack()

    entry_U0 = tk.Entry(task2_window)
    entry_U0.pack()

    label_y0 = tk.Label(task2_window, text="Введіть початкове значення y:")
    label_y0.pack()

    entry_y0 = tk.Entry(task2_window)
    entry_y0.pack()

    plot_button = tk.Button(task2_window, text="Побудувати графік", command=lambda: plot_graph(entry_T.get(), entry_K.get(), entry_U0.get(), entry_y0.get()))
    plot_button.pack()

def plot_graph(T, K, U0, y0):
    try:
        T = float(T)
        K = float(K)
        U0 = float(U0)
        y0 = float(y0)

        U_values = [U0]
        y_values = [y0]

        for k in range(1, 11):
            y_k = calculate_y(k, y_values[-1], U_values[-1], T, T, K)
            U_values.append(U_values[-1] + 1)
            y_values.append(y_k)

        # Побудова графіку за допомогою Canvas
        graph_window = tk.Toplevel(root)
        graph_window.title("Графік функції")

        canvas = tk.Canvas(graph_window, width=400, height=300)
        canvas.pack()

        # Нормалізуємо значення для масштабування на Canvas
        max_U = max(U_values)
        max_y = max(y_values)
        normalized_U = [u / max_U * 380 for u in U_values]
        normalized_y = [300 - (y / max_y * 280) for y in y_values]

        for i in range(1, len(normalized_U)):
            canvas.create_line(normalized_U[i - 1], normalized_y[i - 1], normalized_U[i], normalized_y[i], fill="blue", width=2)

    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа.")

# Створення головного вікна
root = tk.Tk()
root.title("Меню завдань")

# Створення меню
menu_frame = tk.Frame(root)

button_task1 = tk.Button(menu_frame, text="Завдання 1", command=count_powers)
button_task1.pack()

button_task2 = tk.Button(menu_frame, text="Завдання 2", command=show_task2_window)
button_task2.pack()

menu_frame.pack(pady=20)

# Створення і запуск головного циклу Tkinter
root.mainloop()
