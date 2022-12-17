import tkinter as tk
from tkinter import ttk
from time import sleep


class Main(tk.Frame):
    a = 0
    label_money = None
    no_sirop = False

    def __init__(self):
        super().__init__()
        self.initUI()
        self.master.title('Газировка')
        self.master.geometry('250x400+900+500')

    def initUI(self):
        self.columnconfigure([0, 1, 2, 3], weight=1, minsize=400, pad=3)
        self.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=250, pad=3)

        self.label_money = tk.Label(root, text=self.a, font=('Arial', 14))
        self.label_money.grid(row=7, column=3)
        #label_message = tk.Label(root, text='Автомат с газировкой', font=('Arial', 14))
        #label_message.place(x=320, y=50)

        nosirop_checkbutton = tk.Checkbutton(text="Без сиропа")
        nosirop_checkbutton.grid(row=3, column=3, sticky='w')

        lemonsirop_checkbutton = tk.Checkbutton(text="Лимонный сироп")
        lemonsirop_checkbutton.grid(row=4, column=3, sticky='w')

        cherysirop_checkbutton = tk.Checkbutton(text="Вишнёвый сироп")
        cherysirop_checkbutton.grid(row=5, column=3, sticky='w')

        # Хочу сдать мартынова
        btn_money = tk.Button(root, text='Пополнить баланс', command=self.money_get)
        btn_money.grid(row=8, column=3, sticky='s')

    def money_get(self):
        self.a += 10
        self.label_money.config(text=self.a)

        if self.a > 0:
            btn_go = tk.Button(root, text='Налить', command=self.progress)
            btn_go.grid(row=6, column=3, sticky='s')

    def progress(self):
        progress_bar = ttk.Progressbar(root, orient="vertical", mode="determinate", maximum=100, value=0)
        progress_bar.grid(row=10, column=5)
        self.a -= 10
        self.label_money.config(text=self.a)
        for i in range(101):
            progress_bar.configure(value=i)
            progress_bar.update()
            sleep(0.05)
        sleep(5)
        progress_bar.grid_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main()
    root.mainloop()
