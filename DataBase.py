import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS DataBase (
            water integer, gas integer, lemon integer, cherry integer
            )''')
        self.conn.commit()
        self.conn.close()
    #def update(self):
    #    print('1')

    def read_db(self):
        self.conn = sqlite3.connect('DataBase.db')
        self.c = self.conn.cursor()
        self.c.execute('''SELECT * FROM DataBase''')
        records = self.c.fetchall()
        water = 0
        gas = 0
        cherry = 0
        lemon = 0
        for column in records:
            water=column[0]
            gas=column[1]
            cherry = column[2]
            lemon = column[3]
        return {'water' : water, 'gas' : gas, 'cherry':cherry, 'lemon':lemon}
        self.conn.close()
