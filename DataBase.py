import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS DataBase (water integer, gas integer, lemon integer, cherry integer)''')
        self.conn.commit()
    def update(self):
        print('1')

    def read_db(self):
        self.c.execute('''SELECT * FROM DataBase''')
        records = self.DB.c.fetchall()
        water = 1
        gas = 3
        cherry = 3
        lemon = 0
        print(records)
        for column in records:
            water=column[0]
            gas=column[1]
        print(water, gas, cherry, lemon)

        return {'water' : water, 'gas' : gas, 'cherry':cherry, 'lemon':lemon}