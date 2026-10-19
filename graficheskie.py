import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Импортируем из вашего файла functionalnie.py
import functionalnie

class ProgressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система сопровождения вычислений прогрессий")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        tk.Label(root, text="Выберите тип прогрессии:").place(x=20, y=20)
        self.prog_type = tk.StringVar(value="arithmetic")
        tk.Radiobutton(root, text="Арифметическая", variable=self.prog_type, value="arithmetic").place(x=180, y=20)
        tk.Radiobutton(root, text="Геометрическая", variable=self.prog_type, value="geometric").place(x=320, y=20)

        tk.Label(root, text="Первый член (a1/b1):").place(x=20, y=60)
        self.entry_a1 = tk.Entry(root, width=20)
        self.entry_a1.place(x=200, y=60)

        tk.Label(root, text="Шаг или знаменатель (d/q):").place(x=20, y=100)
        self.entry_step = tk.Entry(root, width=20)
        self.entry_step.place(x=200, y=100)

        tk.Label(root, text="Номер элемента (n):").place(x=20, y=140)
        self.entry_n = tk.Entry(root, width=20)
        self.entry_n.place(x=200, y=140)

        tk.Label(root, text="Результат вычислений:").place(x=20, y=180)
        self.entry_result = tk.Entry(root, width=40, state="readonly")
        self.entry_result.place(x=200, y=180)

        tk.Button(root, text="Рассчитать", width=18, command=self.on_calculate).place(x=20, y=230)
        tk.Button(root, text="Сохранить профиль", width=18, command=self.on_save_profile).place(x=180, y=230)
        tk.Button(root, text="Пакетный расчет файла", width=22, command=self.on_file_process).place(x=340, y=230)

        tk.Label(root, text="Управление конфигурацией и резервным копированием (ПМ 06):").place(x=20, y=290)
        tk.Button(root, text="Создать резервную копию (Бэкап)", width=32, command=self.on_backup).place(x=20, y=330)
        tk.Button(root, text="Восстановить из бэкапа", width=32, command=self.on_restore).place(x=270, y=330)

    def on_calculate(self):
        try:
            a1 = float(self.entry_a1.get())
            step = float(self.entry_step.get())
            n = int(self.entry_n.get())

            if n <= 0:
                messagebox.showerror("Ошибка", "Номер элемента n должен быть целым числом больше 0")
                return

            if self.prog_type.get() == "arithmetic":
                res = functionalnie.calculate_arithmetic_member(a1, step, n)
            else:
                res = functionalnie.calculate_geometric_member(a1, step, n)

            self.entry_result.config(state="normal")
            self.entry_result.delete(0, tk.END)
            self.entry_result.insert(0, str(res))
            self.entry_result.config(state="readonly")
        except ValueError:
            messagebox.showerror("Ошибка", "Введены некорректные символы. Допускаются только числа.")

    def on_save_profile(self):
        try:
            a1 = float(self.entry_a1.get())
            step = float(self.entry_step.get())
            name = f"profile_{datetime.now().strftime('%H%M%S')}"
            if functionalnie.save_profile(name, self.prog_type.get(), a1, step):
                messagebox.showinfo("Успешно", f"Профиль '{name}' сохранен в файл.")
            else:
                messagebox.showerror("Ошибка", "Не удалось записать файл профилей.")
        except ValueError:
            messagebox.showerror("Ошибка", "Заполните параметры числами.")

    def on_file_process(self):
        input_path = filedialog.askopenfilename(title="Выберите входной файл JSON", filetypes=[("JSON файлы", "*.json")])
        if not input_path:
            return
        output_path = filedialog.asksaveasfilename(title="Сохранить результат как...", filetypes=[("JSON файлы", "*.json")], defaultextension=".json")
        if not output_path:
            return
        if os.path.exists(input_path):
            try:
                with open(input_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                p_type = data.get("type", "arithmetic").lower()
                first_member = float(data.get("first_member", 0))
                step = float(data.get("step", 0))
                n = int(data.get("n", 1))
                if n <= 0:
                    raise ValueError("Номер n должен быть больше 0.")
                if p_type in ["arithmetic", "1"]:
                    result = functionalnie.calculate_arithmetic_member(first_member, step, n)
                    p_name = "Арифметическая"
                else:
                    result = functionalnie.calculate_geometric_member(first_member, step, n)
                    p_name = "Геометрическая"
                output_data = {
                    "progression_type": p_name,
                    "first_member": first_member,
                    "step_or_denominator": step,
                    "element_number_n": n,
                    "result_value": result,
                    "calculated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(output_data, f, ensure_ascii=False, indent=4)
                messagebox.showinfo("Успешно", f"Расчет файла завершен.")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка: {e}")

    def on_backup(self):
        success, info = functionalnie.create_backup()
        if success:
            messagebox.showinfo("Успешно", f"Резервная копия создана:\n{info}")
        else:
            messagebox.showerror("Ошибка", f"Не удалось выполнить бэкап:\n{info}")

    def on_restore(self):
        success, info = functionalnie.restore_backup()
        if success:
            messagebox.showinfo("Успешно", f"Система восстановлена из файла:\n{info}")
        else:
            messagebox.showerror("Ошибка", f"Ошибка восстановления:\n{info}")


