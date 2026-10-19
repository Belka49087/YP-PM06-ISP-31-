import tkinter as tk
from graficheskie import ProgressionApp

def main():
    """Точка входа в исполнительную систему программы"""
    root = tk.Tk()
    app = ProgressionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

