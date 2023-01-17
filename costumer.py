import sqlite3 


connect = sqlite3.connect('data.db')


#comando para dropar a tabela se ela existir

connect.execute("DROP TABLE IF EXISTS COSTUMER")

#comando basico para criação de uma tabela

connect.execute('''CREATE TABLE COSTUMER 
            (ID INT PRIMARY KEY NOT NULL,
            NAME CHAR NOT NULL,
             AGE INT NOT NULL);''')


#adicionar valores na tabela
connect.execute("INSERT INTO COSTUMER ( ID, NAME, AGE)  VALUES(1, 'ROZENDO', 99) ") 

#all_data = connect.execute(''' SELECT * FROM COSTUMER''')


connect.close
