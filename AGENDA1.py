# Rozendoxxxxxxxxxxxxxxxxxxxx


import sqlite3

conn = sqlite3.connect('AGENDA.db')

# -----------------------------------------------------------------
# CRIANDO AS TABELAS SQL

# $TABELA SEGUNDA FEIRA
conn.execute('''CREATE TABLE SEGUNDA
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO1 INT NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INT NOT NULL,
            MATERIA2 INT NOT NULL);''')

# $TABELA TERCA FEIRA
conn.execute(''' CREATE TABLE TERCA
            ( id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO1 INT NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INT NOT NULL,
            MATERIA2 INT NOT NULL);''')

# $TABELA QUARTA FEIRA
conn.execute(''' CREATE TABLE QUARTA
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO1 INTEGER NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INTEGER NOT NULL,
            MATERIA2 TEXT NOT NULL);''')

# $TABELA QUINTA FEIRA
conn.execute(''' CREATE TABLE QUINTA
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO1 INTEGER NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INTEGER NOT NULL,
            MATERIA2 TEXT NOT NULL); ''')

# $TABELA SEXTA FEIRA
conn.execute(''' CREATE TABLE SEXTA
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO1 INTEGER NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INTEGER NOT NULL,
            MATERIA2 TEXT NOT NULL);''')

# $TABELA SABADO
conn.execute(''' CREATE TABLE SABADO
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORARIO INTEGER NOT NULL,
            MATERIA1 TEXT NOT NULL,
            HORARIO2 INTEGER NOT NULL,
            MATERIA2 TEXT NOT NULL);''')


# -----------------------------------------------------------------
# PARTE DO CODIGO PARA DAR UPDATE NAS TABELAS DE TODAS AS INFORMAÇÕES


def updateSEG():
    connseg = sqlite3.connect('AGENDA.db')
    cursor = connseg.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    # Solicita o novo valor para a coluna "HORARIO1"
    nv_h1 = input("Digite o novo valor para HORARIO1")
    # Solicita o novo valor para a coluna "MATERIA2"
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    # Solicita o novo valor para a coluna "HORARIO2"
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza as colunas de todos os registros da tabela "SEGUNDA"
    cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connseg.commit()

    # Fecha a conexão com o banco de dados
    connseg.close()


def updateTER():
    connter = sqlite3.connect('AGENDA.db')
    cursor = connter.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    # Solicita o novo valor para a coluna "HORARIO1"
    nv_h1 = input("Digite o novo valor para HORARIO1")
    # Solicita o novo valor para a coluna "MATERIA2"
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    # Solicita o novo valor para a coluna "HORARIO2"
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza as colunas de todos os registros da tabela "TERCA"
    cursor.execute("UPDATE TERCA SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE TERCA SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE TERCA SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE TERCA SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connter.commit()

    # Fecha a conexão com o banco de dados
    connter.close()


def updateQUA():
    connqua = sqlite3.connect('AGENDA.db')
    cursor = connqua.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    # Solicita o novo valor para a coluna "HORARIO1"
    nv_h1 = input("Digite o novo valor para HORARIO1")
    # Solicita o novo valor para a coluna "MATERIA2"
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    # Solicita o novo valor para a coluna "HORARIO2"
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza as colunas de todos os registros da tabela "QUARTA"
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connqua.commit()

    # Fecha a conexão com o banco de dados
    connqua.close()


def updateQUI():
    connqui = sqlite3.connect('AGENDA.db')
    cursor = connqui.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    # Solicita o novo valor para a coluna "HORARIO1"
    nv_h1 = input("Digite o novo valor para HORARIO1")
    # Solicita o novo valor para a coluna "MATERIA2"
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    # Solicita o novo valor para a coluna "HORARIO2"
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza as colunas de todos os registros da tabela "QUARTA"
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connqui.commit()

    # Fecha a conexão com o banco de dados
    connqui.close()


def updateSEX():
    connsex = sqlite3.connect('AGENDA.db')
    cursor = connsex.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    # Solicita o novo valor para a coluna "HORARIO1"
    nv_h1 = input("Digite o novo valor para HORARIO1")
    # Solicita o novo valor para a coluna "MATERIA2"
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    # Solicita o novo valor para a coluna "HORARIO2"
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza as colunas de todos os registros da tabela "SEXTA"
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE QUARTA SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connsex.commit()

    # Fecha a conexão com o banco de dados
    connsex.close()


def updateSAB():
    connsab = sqlite3.connect('AGENDA.db')
    cursor = connsab.cursor()

    # Solicita o novo valor para a coluna "MATERIA1"
    nv_m1 = input("Digite o novo valor para MATERIA1: ")
    nv_h1 = input("Digite o novo valor para HORARIO1")
    nv_m2 = input("Digite o novo valor para MATERIA2: ")
    nv_h2 = input("Digite o novo valor para HORARIO2")

    # Atualiza a coluna "MATERIA1" de todos os registros da tabela "SABADO"
    cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_m1,))
    cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_h1,))
    cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_m2,))
    cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_h2,))

    # Salva as alterações
    connsab.commit()

    # Fecha a conexão com o banco de dados
    connsab.close()


# ------------------------------------------------------------------
# PARTE DO CODIGO DE FUNÇÕES PARA DELETAR OS DADOS DAS TABELAS

def deletSEG():
    conndelseg = sqlite3.connect('AGENDA.DB')
    cursor = conndelseg.cursor()

    # EXCLUI TODOS OS DADOS DA TABELA SEGUNDA
    cursor.execute("DELETE FROM SEGUNDA;")

    # SALVA AS ALTERAÇÕES
    conndelseg.commit()

    # FECHA A CONEXÃO COM O BANCO DEDADOS
    conndelseg.close()


def deletTER():
    conndelter = sqlite3.connect('AGENDA.DB')
    cursor = conndelter.cursor()

    cursor.execute("DELETE FROM TERCA;")

    conndelter.commit()

    conndelter.close()


def deletQUA():
    conndelqua = sqlite3.connect('AGENDA.DB')
    cursor = conndelqua.cursor()

    cursor.execute("DELETE FROM QUA;")

    conndelqua.commit()

    conndelqua.close()


def deletQUI():
    conndelqui = sqlite3.connect('AGENDA.DB')
    cursor = conndelqui.cursor()

    cursor.execute("DELETE FROM QUI;")

    conndelqui.commit()

    conndelqui.close()


def deletSEX():
    conndelsex = sqlite3.connect('AGENDA.DB')
    cursor = conndelsex.cursor()

    cursor.execute("DELETE FROM SEX;")

    conndelsex.commit()

    conndelsex.close()


def deletSAB():
    conndelsab = sqlite3.connect('AGENDA.DB')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM SAB;")

    conndelsab.commit()

    conndelsab.close()


# -------------------------------------------------------------------
# ADICIONAR COLUNA ÀS COLUNAS

def adicionarCol():
    connadd = sqlite3.connect('AGENDA.DB')
    cursor = connadd.cursor()

    tabela = input("DIGITE O NOME DA TABELA")

    coluna = input("DIGITE O NOME DA COLUNA")

    tipo_dado = input("DIGITE O TIPO DE DADO DA COLUNA:")

    # concatena as informações na string da consulta SQL
    sql_query = f"ALTER TABLE{tabela}ADD COLUMN {coluna} {tipo_dado}"

    cursor.execute(sql_query)

    connadd.commit()

    connadd.close()


# -------------------------------------------------------------------
# DELETAR ESPECIFICAMENTE UMA COLUNA
def apagar_coluna():
    connapgcol = sqlite3.connect('AGENDA.DB')
    cursor = connapgcol.cursor()

    tabela = input("DIGITE O NOME DA TABELA:")
    coluna = input("DIGITE O NOME DA COLUNA A SER EXCLUÍDA:")

    sql_query = f"ALTER TABLE {tabela} DROP COLUMN {coluna}"

    cursor.execute(sql_query)

    connapgcol.commit()

    connapgcol.close()


# -------------------------------------------------------------------
# ADICIONAR TABELAS NO BDD

def add_tabble():
    connaddtable = sqlite3.connect('AGENDA.DB')
    cursor = connaddtable.cursor()

    # SOLICITA O NOVO NOME DA TABELA QUE IREMOS CRIAR
    nome_tabela = input("INFORME O NOME DA NOVA TABELA")

    # CRIA UMA STRING DE CONSULTA SQL PARA CRIAR UMA NOVA TABELA, COM AS COLUNAS QUE JA EXISTEM NAS OUTRAS TABELAS
    sql_query = f"CREATE TABLE {nome_tabela} (" \
                f"ID INTEGER PRIMARY KET AUTOINCREMENT MATERIA1 TEXT, HORARIO1 TEXT, MATERIA2 TEXT, HORARIO2 TEXT)"
    cursor.execute(sql_query)

    connaddtable.commit()

    connaddtable.close()


# -------------------------------------------------------------------

print("\t\t\t\t************************************")
print("\t\t\t\t**-BEM VINDO À SUA AGENDA ROZENDO-**")
print("\t\t\t\t************************************")

# nesta variavel será decidido qual opção o usuario Rozendo irá usar

print("\t1 - VER AGENDA")
print("\t2 - MODIFICAR AGENDA- MODIFICAR POR INTEIRA")
print("\t3 - APAGAR DADOS DAS TABELAS COMPLETAMENTE")
print("\t4-  ALTERAR TABELA- ADICIONAR COLUNAS")
print("\t5 - APAGAR DADOS - REMOVER COLUNAS")
print("\t6-  ADICIONAR TABELAS.")
print("\t7-  APAGAR TABELAS COMPLETAMENTE")
decisao = int(input("Oque deseja fazer?"))

# VER AGENDA
if decisao == 1:
    entrada = input('DIGITE O DIA DA SEMANA QUE VOCÊ DESEJA VER')
    while entrada != "exit":

        if entrada == "segunda":
            conn.execute("SELECT * FROM SEGUNDA ")
            for segunda in segunda:
                print(segunda)

        elif entrada == "terca":
            conn.execute("SELECT * FROM TERCA_FEIRA")
            for terca in terca:
                print(terca)

        elif entrada == "quarta":
            conn.execute("SELECT * FROM QUARTA_FEIRA")
            for quarta in quarta:
                print(quarta)

        elif entrada == "quinta":
            conn.execute("SELECT * FROM QUINTA_FEIRA")
            for quinta in quinta:
                print(quinta)

        elif entrada == "sexta":
            conn.execute("SELECT * FROM SEXTA-FEIRA")
            for sexta in sexta:
                print(sexta)

        elif entrada == "sabado":
            conn.execute("SELECT * FROM SABADO")
            for sabado in sabado:
                print(sabado)

        if entrada == "exit":
            print("OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA.")
            conn.close()

    else:
        raise Exception("ENTRADA DE DADOS ERRADA, TERMINANDO SUA SESSÃO...")
# MODIFICAR AGENDA- MODIFICAR POR INTEIRA
elif decisao == 2:
    decisao2 = input("INFORME O DIA DA SEMANA PARA ALTERAR")
    while decisao2 != "exit":
        if decisao2 == "segunda":
            updateSEG()

        elif decisao2 == 'terca':
            updateTER()

        elif decisao2 == 'quarta':
            updateQUA()

        elif decisao2 == 'quinta':
            updateQUI()

        elif decisao2 == 'sexta':
            updateSEX()

        elif decisao2 == 'sabado':
            updateSEX()

        elif decisao2 == 'exit':
            print("OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA, FINALIZANDO...")
            break
    else:
        raise Exception("ENTRADA DE DADOS ERRADA, TERMINANDO A SESSÃO...")

# APAGAR TODOS OS DADOS DA TABELA
elif decisao == 3:
    print("\tBEM VINDO, ESTA OPÇÃO IRÁ APAGAR A TABELA COMPLETAMENTE")
    print("escreva o dia ou escreva -EXIT- para sair")
    decisao3 = input("INFORME -[]- ")

    while decisao3 != "EXIT":
        if decisao3 == "segunda":
            deletSEG()

        elif decisao3 == "terca":
            deletTER()

        elif decisao3 == "quarta":
            deletQUA()

        elif decisao3 == "quinta":
            deletQUI()

        elif decisao3 == "sexta":
            deletSEX()

        elif decisao3 == "sabado":
            deletSAB()

        elif decisao3 == "EXIT":
            print("OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA")
            break
    else:
        raise Exception("*-DADOS INFORMADOS DE MANEIRA ERRADA-*")

# ADICIONAR ITENS NA TABELA
elif decisao == 4:
    print("\t BEM VINDO, ESTA OPÇÃO IRÁ ADICONAR ITENS A TABELA QUE DESEJA-")
    adicionarCol()

# REMOVER COLUNAS
elif decisao == 5:
    print("\t BEM VINDO, ESTA OPÇÃO IRÁ REMOVER COLUNAS DA SUA TABELA")
    apagar_coluna()

# ADICIONAR TABELAS
elif decisao == 6:
    print("\t BEM VINDO, ESTA OPÇÃO IRÁ ADICIOONAR UMA TABELA NOVA AO SEU BDD")
    add_tabble()

else:
    raise Exception("------------------ OPÇÃO INVALIDA -------------------------")

