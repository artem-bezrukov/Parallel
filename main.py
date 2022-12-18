import tkinter as tk
from tkinter import ttk
from time import sleep
import DataBase as DB


class Main(tk.Frame):
    cash = 0
    storage={}
    label_money = None
    DB = DB.DB()
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
        self.get_data()


        syrup = tk.StringVar()
        nosyrup_radiobutton = tk.Radiobutton(text=f"Без сиропа {self.price['no_syrup']}", value=self.no_syrup,
                                             variable=syrup,
                                             command=lambda: self.choose_syrup(self.no_syrup))
        nosyrup_radiobutton.grid(row=3, column=1, sticky='w')

        lemonsyrup_radiobutton = tk.Radiobutton(text=f"Лимонный сироп {self.price['lemon']}", value=self.lemon,
                                                variable=syrup,
                                                command=lambda: self.choose_syrup(self.lemon))
        lemonsyrup_radiobutton.grid(row=4, column=1, sticky='w')

        cherrysyrup_radiobutton = tk.Radiobutton(text=f"Вишнёвый сироп {self.price['cherry']}", value=self.cherry,
                                                 variable=syrup,
                                                 command=lambda: self.choose_syrup(self.cherry))
        cherrysyrup_radiobutton.grid(row=5, column=1, sticky='w')

        self.label_money = tk.Label(self.master, text=f'баланс: \n{self.cash}')
        self.label_money.grid(row=10, column=1)
        lbl_get_money = tk.Label(self.master, text='Пополнить баланс')
        lbl_get_money.grid(row=8, column=1, sticky='sw')
        btn_money_2 = tk.Button(self.master, text='+2', command=self.add2_cash)
        btn_money_2.grid(row=9, column=1, sticky='w')
        btn_money_5 = tk.Button(self.master, text='+5', command=self.add5_cash)
        btn_money_5.grid(row=10, column=1, sticky='w')
        btn_money_10 = tk.Button(self.master, text='+10', command=self.add10_cash)
        btn_money_10.grid(row=11, column=1, sticky='w')

        btn_go = tk.Button(self.master, text='Налить', command=self.fill_glass)
        btn_go.grid(row=12, column=1, sticky='')

        btn_get_change = tk.Button(self.master, text='Получить сдачу', command=self.get_change)
        btn_get_change.grid(row=13, column=1, sticky='s')

    def add2_cash(self):
        self.cash += 2
        self.label_money.config(text=f'баланс:\n {self.cash}')

    def add5_cash(self):
        self.cash += 5
        self.label_money.config(text=f'баланс:\n {self.cash}')

    def add10_cash(self):
        self.cash += 10
        self.label_money.config(text=f'баланс:\n {self.cash}')

    def get_change(self):
        self.cash = 0
        self.label_money.config(text=f'баланс:\n {self.cash}')

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
        if self.storage['water'] <= 0:
            self.destroy()
    def get_data(self):
        self.storage = self.DB.read_db()
    def fill_glass(self):
        if (self.cash > 0):
            color = ' '
            if (self.syrup_selected['no_syrup'] and self.cash >= self.price['no_syrup']):
                color = '#FFEFD5'
                self.cash -= self.price['no_syrup']
                self.progress(color)
                self.storage['water']--1
                print(self.storage['water'])
            if (self.syrup_selected['lemon'] and self.cash >= self.price['lemon']):
                color = 'yellow'
                self.cash -= self.price['lemon']
                self.progress(color)
            if (self.syrup_selected['cherry'] and self.cash >= self.price['cherry']):
                color = 'red'
                self.cash -= self.price['cherry']
                self.progress(color)

    def progress(self, color):
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TProgressbar', background=color)
        progress_bar = ttk.Progressbar(self.master, style='TProgressbar', orient="vertical", mode="determinate",
                                       maximum=100, value=0, length=50)
        progress_bar.grid(row=14, column=2)
        self.label_money.config(text=f'баланс:\n {self.cash}')
        for i in range(101):
            progress_bar.configure(value=i)
            progress_bar.update()
            sleep(0.05)

        progress_bar.grid_forget()

    DB.read_db()

def main():

    root = tk.Tk()
    root.resizable(False, False)
    app = Main()
    root.mainloop()


if __name__ == "__main__":
    main()