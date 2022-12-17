import tkinter as tk
from tkinter import ttk
from time import sleep


class Main(tk.Frame):
    cash = 0
    label_money = None

    no_syrup = "no_syrup"
    cherry = "cherry"
    lemon = "lemon"
    syrup_selected = {"no_syrup": False, 'cherry': False, 'lemon': False}
    price = {"no_syrup": 10, 'cherry': 20, 'lemon': 15}

    def __init__(self):
        super().__init__()
        self.initUI()
        self.master.title('Газировка')
        self.master.geometry('250x400+900+500')

    def initUI(self):

        self.columnconfigure([0, 1, 2, 3], weight=1, minsize=400, pad=3)
        self.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=250, pad=3)

        self.label_money = tk.Label(self.master, text=self.cash, font=('Arial', 14))
        self.label_money.grid(row=7, column=3)
        # label_message = tk.Label(root, text='Автомат с газировкой', font=('Arial', 14))
        # label_message.place(x=320, y=50)

        syrup = tk.StringVar()
        nosyrup_radiobutton = tk.Radiobutton(text=f"Без сиропа {self.price['no_syrup']}", value=self.no_syrup,
                                             variable=syrup,
                                             command=lambda: self.choose_syrup(self.no_syrup))
        nosyrup_radiobutton.grid(row=3, column=3, sticky='w')

        lemonsyrup_radiobutton = tk.Radiobutton(text=f"Лимонный сироп {self.price['lemon']}", value=self.lemon,
                                                variable=syrup,
                                                command=lambda: self.choose_syrup(self.lemon))
        lemonsyrup_radiobutton.grid(row=4, column=3, sticky='w')

        cherrysyrup_radiobutton = tk.Radiobutton(text=f"Вишнёвый сироп {self.price['cherry']}", value=self.cherry,
                                                 variable=syrup,
                                                 command=lambda: self.choose_syrup(self.cherry))
        cherrysyrup_radiobutton.grid(row=5, column=3, sticky='w')

        btn_money = tk.Button(self.master, text='Пополнить баланс', command=self.money_get)
        btn_money.grid(row=8, column=3, sticky='s')

        btn_go = tk.Button(self.master, text='Налить', command=self.fill_glass)
        btn_go.grid(row=6, column=3, sticky='s')

    def money_get(self):
        self.cash += 10
        self.label_money.config(text=self.cash)

    def choose_syrup(self, syrup):
        if (syrup == self.no_syrup):
            self.syrup_selected['no_syrup'] = True
            self.syrup_selected['cherry'] = False
            self.syrup_selected['lemon'] = False
        if (syrup == self.cherry):
            self.syrup_selected['no_syrup'] = False
            self.syrup_selected['cherry'] = True
            self.syrup_selected['lemon'] = False
        if (syrup == self.lemon):
            self.syrup_selected['no_syrup'] = False
            self.syrup_selected['cherry'] = False
            self.syrup_selected['lemon'] = True

    def fill_glass(self):
        if (self.cash > 0):
            color = ' '
            if (self.syrup_selected['no_syrup'] and self.cash >= self.price['no_syrup']):
                color = '#FFEFD5'
                self.cash -= self.price['no_syrup']
            if (self.syrup_selected['lemon'] and self.cash >= self.price['lemon']):
                color = 'yellow'
                self.cash -= self.price['lemon']
            if (self.syrup_selected['cherry'] and self.cash >= self.price['cherry']):
                color = 'red'
                self.cash -= self.price['cherry']
            self.progress(color)

    def progress(self, color):
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TProgressbar', background=color)
        progress_bar = ttk.Progressbar(self.master, style='TProgressbar', orient="vertical", mode="determinate",
                                       maximum=100, value=0)
        progress_bar.grid(row=10, column=5)
        self.label_money.config(text=self.cash)
        for i in range(101):
            progress_bar.configure(value=i)
            progress_bar.update()
            sleep(0.05)
        sleep(5)
        progress_bar.grid_forget()


def main():
    root = tk.Tk()
    app = Main()
    app.mainloop()


if __name__ == "__main__":
    main()
