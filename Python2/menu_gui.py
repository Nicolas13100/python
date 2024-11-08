# -*-coding:Latin-1 -*

import tkinter as tk

# Importing all TP modules
import TP1.TP1_1_tkinter_app as tp1_1
import TP1.TP1_2_tkinter_app as tp1_2
import TP1.TP1_3_tkinter_app as tp1_3
import TP1.TP1_4_tkinter_app as tp1_4
import TP1.TP1_5_tkinter_app as tp1_5
import TP2.TP2_1_tkinter_app as tp2_1
import TP2.TP2_2_tkinter_app as tp2_2
import TP2.TP2_3_tkinter_app as tp2_3
import TP2.TP2_4_tkinter_app as tp2_4
import TP2.TP2_5_tkinter_app as tp2_5
import TP3.TP3_4_tkinter_app as tp3_4


def main_menu():
    main_window = tk.Tk()
    main_window.title("Main Menu")

    tk.Label(main_window, text="Select a TP Module", font=("Arial", 16)).pack(pady=10)

    tk.Button(main_window, text="TP1 Menu", command=tp1_menu, width=20).pack(pady=5)
    tk.Button(main_window, text="TP2 Menu", command=tp2_menu, width=20).pack(pady=5)
    tk.Button(main_window, text="TP3 Menu", command=tp3_menu, width=20).pack(pady=5)
    tk.Button(main_window, text="Exit", command=main_window.quit, width=20).pack(pady=20)

    main_window.mainloop()


def tp1_menu():
    tp1_window = tk.Toplevel()
    tp1_window.title("TP1 Menu")

    tk.Label(tp1_window, text="Select a TP1 Module", font=("Arial", 14)).pack(pady=10)

    tk.Button(tp1_window, text="TP1_1", command=tp1_1.tp1_1_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp1_window, text="TP1_2", command=tp1_2.tp1_2_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp1_window, text="TP1_3", command=tp1_3.tp1_3_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp1_window, text="TP1_4", command=tp1_4.tp1_4_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp1_window, text="TP1_5", command=tp1_5.tp1_5_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp1_window, text="Back to Main Menu", command=tp1_window.destroy, width=20).pack(pady=20)


def tp2_menu():
    tp2_window = tk.Toplevel()
    tp2_window.title("TP2 Menu")

    tk.Label(tp2_window, text="Select a TP2 Module", font=("Arial", 14)).pack(pady=10)

    tk.Button(tp2_window, text="TP2_1", command=tp2_1.tp2_1_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp2_window, text="TP2_2", command=tp2_2.tp2_2_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp2_window, text="TP2_3", command=tp2_3.tp2_3_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp2_window, text="TP2_4", command=tp2_4.tp2_4_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp2_window, text="TP2_5", command=tp2_5.tp2_5_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp2_window, text="Back to Main Menu", command=tp2_window.destroy, width=20).pack(pady=20)


def tp3_menu():
    tp3_window = tk.Toplevel()
    tp3_window.title("TP3 Menu")

    tk.Label(tp3_window, text="Select a TP3 Module", font=("Arial", 14)).pack(pady=10)

    tk.Button(tp3_window, text="TP3_4", command=tp3_4.tp3_4_tkinter_app, width=20).pack(pady=5)
    tk.Button(tp3_window, text="Back to Main Menu", command=tp3_window.destroy, width=20).pack(pady=20)


if __name__ == "__main__":
    main_menu()
