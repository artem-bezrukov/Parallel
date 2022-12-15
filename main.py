import tkinter as tk
from tkinter import ttk
from time import sleep
class Main(tk.Frame):
    a = 0
    label_money = None


    def __init__(self, root):
        super().__init__(root)
        self.label_money = tk.Label(root, text=self.a, font=('Arial', 14))
        self.label_money.place(x=550, y=50)

        label_message = tk.Label(root, text='Автомат с газировкой', font=('Arial', 14))
        label_message.place(x=320, y=50)

        nosirop_checkbutton = ttk.Checkbutton(text="Без сиропа")
        nosirop_checkbutton.place(x=500, y=200)

        lemonsirop_checkbutton = ttk.Checkbutton(text="Лимонный сироп")
        lemonsirop_checkbutton.place(x=500, y=220)

        cherysirop_checkbutton = ttk.Checkbutton(text="Вишнёвый сироп")
        cherysirop_checkbutton.place(x=500, y=240)
        if self.a>0:
            btn_go = tk.Button(root, text='Налить', command=self.progress)
            btn_go.place(x=500, y=260)
# Хочу сдать мартынова
        btn_money = tk.Button(root, text='Пополнить баланс', command=self.money_get)
        btn_money.place(x=500, y=290)



    def money_get(self):
        self.a = self.a+10
        self.label_money.config(text=self.a)

    def progress(self):
        self.a = self.a-10
        self.label_money.config(text=self.a)
        label_message_done = tk.Label(root, text='Напиток готов', font=('Arial', 14))
        progress_bar = ttk.Progressbar(self, orient="vertical", mode="determinate", maximum=100, value=0)
        progress_bar.pack()
        label_message_progress = tk.Label(root, text='Напиток наливается', font=('Arial', 14))
        label_message_progress.pack()
        for i in range(101):
            progress_bar.configure(value=i)
            progress_bar.update()
            sleep(0.05)
        progress_bar.pack_forget()
        label_message_progress.pack_forget()
        label_message_done.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Хочу пить")
    root.geometry("800x800+500+200")
    root.resizable(False, False)
    root.mainloop()