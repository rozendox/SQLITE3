import sqlite3


class agenda:
    segunda = []
    terca = ''
    quarta = ''
    quinta = ''
    sexta = ''
    sabado = ''

    def AtribuirSeg(self):
        self.segunda = input("Defina sua grade de segunda")


conn = sqlite3.connect('AGENDA.DB')

conn.execute('''CREATE TABLE SEGUNDA_FEIRA
                (id integer PRIMARY KEY AUTOINCREMENT,
                SEGUNDAX TEXT NOT NULL);''')



num = input("Entre com a sua data")
while num != "Exit":
    if num == "segunda":
        agenda.AtribuirSeg(self= agenda)
        conn.execute("INSERT INTO SEGUNDA_FEIRA (id, SEGUNDAX) VALUES (1,'19:00 - 21:00 Compiladores 21:00 - 23:00 POO')")
        break


"""conn.execute('')"""
