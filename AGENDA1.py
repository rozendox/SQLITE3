#ROZENDOXXXXXXXXXXXXXXXX

import sqlite3


# FIXME: REALIZAR AS SEGUNTES ALTERAÇÕES PARA TESTES FUTUROS===========
# FIXME: ALTERAR A VARIAVEL DAS FUNÇÃO DE CONEXÃO DE BANCO DE DADOS PARA GLOBAL
# FIXME: ALTERAR O CURSOR DAS FUNÇÕES PARA GLOBAL

# -----------------------------------------------------------------
# CRIANDO AS TABELAS SQL

# $TABELA SEGUNDA FEIRA
# conn.execute('''CREATE TABLE SEGUNDA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INT NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INT NOT NULL,
#            MATERIA2 INT NOT NULL);''')

# $TABELA TERCA FEIRA
# conn.execute(''' CREATE TABLE TERCA
#            ( id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INT NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INT NOT NULL,
#            MATERIA2 INT NOT NULL);''')

# $TABELA QUARTA FEIRA
# conn.execute(''' CREATE TABLE QUARTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')

# $TABELA QUINTA FEIRA
# conn.execute(''' CREATE TABLE QUINTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#           MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL); ''')

# $TABELA SEXTA FEIRA
# conn.execute(''' CREATE TABLE SEXTA
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO1 INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')

# $TABELA SABADO
# conn.execute(''' CREATE TABLE SABADO
#            (id INTEGER PRIMARY KEY AUTOINCREMENT,
#            HORARIO INTEGER NOT NULL,
#            MATERIA1 TEXT NOT NULL,
#            HORARIO2 INTEGER NOT NULL,
#            MATERIA2 TEXT NOT NULL);''')


# -----------------------------------------------------------------

# VER AGENDA:
def verSEG():
    try:
        connverseg = sqlite3.connect('AGENDA.db')

        # Criar um cursor
        cur = connverseg.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM SEGUNDA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverseg.close()

        # Retornar mensagem de sucesso
        return "Operação ver Segunda-Feira bem-sucedida"
    except Exception as e:
        # Retornar mensagem de erro
        return "Operação ver Segunda-Feira não-sucedida. Erro: {}".format(e)


def verTER():
    try:
        connverter = sqlite3.connect('AGENDA.db')

        # Criar um cursor
        cur = connverter.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM TERCA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverter.close()
        return "Operação bem sucedida."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


def verQUA():
    try:
        connverseg = sqlite3.connect('AGENDATESTE.db')

        # Criar um cursor
        cur = connverseg.cursor()

        # Executar o SELECT
        cur.execute("SELECT * FROM QUARTA")

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        # Fechar o cursor e a conexão
        cur.close()
        connverseg.close()
        return "Operação bem sucedida.."
    except:
        return "operação não sucedida..."


def verQUI():
    try:
        connverqui = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connverqui.cursor()

        # Obter todos os Resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connverqui.close()
        return "Operação bem sucedida."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA."


def verSex():
    try:
        connversex = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connversex.cursor()

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connversex.close()
        return "OPERAÇÃO BEM SUCEDIDA"
    except:
        return "OPERAÇÃO NAO SUCEDIDA"


def verSAB():
    try:
        connversab = sqlite3.connect('AGENDA.DB')

        # Criar um cursor
        cur = connversab.cursor()

        # Obter todos os resultados
        resultados = cur.fetchall()

        # Percorrer os resultados e imprimir cada linha
        for linha in resultados:
            print(linha)

        cur.close()
        connversab.close()
        return "OPERAÇÃO BEM SUCEDIDA"
    except:
        return "OPERAÇÃO NÃO SUCEDIDA"


# -----------------------------------------------------------------
# PARTE DO CODIGO PARA DAR UPDATE NAS TABELAS DE TODAS AS INFORMAÇÕES


def updateSEG():
    try:
        connseg = sqlite3.connect('AGENDA.db')
        cursor = connseg.cursor()

        nv_m1, nv_h1, nv_m2, nv_h2 = input("Digite o novo valor para {}: ".format("MATERIA1")), input(
            "Digite o novo valor para {}: ".format("HORARIO1")), input(
            "Digite o novo valor para {}: ".format("MATERIA2")), input(
            "Digite o novo valor para {}: ".format("HORARIO2"))

        # Atualiza a tabela segunda feira
        cursor.execute("UPDATE SEGUNDA SET MATERIA1 = ?, MATERIA2 = ?, MATERIA3 = ?, MATERIA4 = ?",
                       (nv_m1, nv_h1, nv_m2, nv_h2))

        # Salva as alterações
        connseg.commit()

        # Fecha a conexão com o banco de dados
        connseg.close()

        print("OPERAÇÃO BEM SUCEDIDA, UPDATE NA TABELA SEGUNDA FEIRA, FINALIZADA SEM ERROS")
    except:
        print("OPERAÇÃO NÃO SUCEDIDA")

    # Retorna ao menu principal após a atualização
    menu_principal()


def updateTER():
    try:
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
        cursor.execute("UPDATE TERCA SET HORAIO1 = ? ", (nv_h1,))
        cursor.execute("UPDATE TERCA SET MATERIA2 = ? ", (nv_m2,))
        cursor.execute("UPDATE TERCA SET HORARIO2 = ? ", (nv_h2,))

        # Salva as alterações
        connter.commit()

        # Fecha a conexão com o banco de dados
        connter.close()

        return "OPERAÇÃO BEM SUCEDIDA,UPDATE NA TERCA FEIRA FINALIZADA SEM ERROS."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, UPDATE NÃO REALIZADO NA TABELA TERCA FEIRA, TENTE NOVAMENTE"


def updateQUA():
    try:

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
        cursor.execute("UPDATE QUARTA SET HORARIO1 = ? ", (nv_h1,))
        cursor.execute("UPDATE QUARTA SET MATERIA2 = ? ", (nv_m2,))
        cursor.execute("UPDATE QUARTA SET HORARIO2 = ? ", (nv_h2,))

        # Salva as alterações
        connqua.commit()

        # Fecha a conexão com o banco de dados
        connqua.close()
        return "OPERAÇÃO BEM SUCEDIDA, UPDATE REALIZADO NA TABELA QUARTA FEIRA."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, UPDATE NÃO REALIZADO NA TABELA QUARTA FEIRA"


def updateQUI():
    try:
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
        cursor.execute("UPDATE QUARTA SET HORARIO1 = ? ", (nv_h1,))
        cursor.execute("UPDATE QUARTA SET MATERIA2 = ? ", (nv_m2,))
        cursor.execute("UPDATE QUARTA SET HORARIO2 = ? ", (nv_h2,))

        # Salva as alterações
        connqui.commit()

        # Fecha a conexão com o banco de dados
        connqui.close()
        return "OPERAÇÃO BEM SUCEDIDA, UPDATE RALIZADO NA TABELA QUINTA FEIRA"
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, UPDATE NÃO REALIZADO NA TABELA QUINTA FEIRA"


def updateSEX():
    try:
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
        cursor.execute("UPDATE QUARTA SET HORARIO1 = ? ", (nv_h1,))
        cursor.execute("UPDATE QUARTA SET MATERIA2 = ? ", (nv_m2,))
        cursor.execute("UPDATE QUARTA SET HORARIO2 = ? ", (nv_h2,))

        # Salva as alterações
        connsex.commit()

        # Fecha a conexão com o banco de dados
        connsex.close()
        return "OPERAÇÃO SUCEDIDA, UPDATE REALIZADO NA TABELA QUARTAFEIRA"

    except:
        "OPERAÇÃO NÃO SUCEDIDA, UPDATE NÃO REALIZADO NA TABELA QUARTAFEIRA"


def updateSAB():
    try:
        connsab = sqlite3.connect('AGENDA.db')
        cursor = connsab.cursor()

        # Solicita o novo valor para a coluna "MATERIA1"
        nv_m1 = input("Digite o novo valor para MATERIA1: ")
        nv_h1 = input("Digite o novo valor para HORARIO1")
        nv_m2 = input("Digite o novo valor para MATERIA2: ")
        nv_h2 = input("Digite o novo valor para HORARIO2")

        # Atualiza a coluna "MATERIA1" de todos os registros da tabela "SABADO"
        cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_m1,))
        cursor.execute("UPDATE SABADO SET HORARIO1 = ? ", (nv_h1,))
        cursor.execute("UPDATE SABADO SET MATERIA1 = ? ", (nv_m2,))
        cursor.execute("UPDATE SABADO SET HORARIO2 = ? ", (nv_h2,))

        # Salva as alterações
        connsab.commit()

        # Fecha a conexão com o banco de dados
        connsab.close()
        return "OPERAÇÃO BEM SUCEDIDA, TABELA ATUALIZADA"
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, TABELA SÁBADO NÃO ATUALIZADA."


# ------------------------------------------------------------------
# PARTE DO CODIGO DE FUNÇÕES PARA DELETAR OS DADOS DAS TABELAS

def deletSEG():
    try:
        conndelseg = sqlite3.connect('AGENDA.DB')
        cursor = conndelseg.cursor()

        # EXCLUI TODOS OS DADOS DA TABELA SEGUNDA
        cursor.execute("DELETE FROM SEGUNDA;")

        # SALVA AS ALTERAÇÕES
        conndelseg.commit()

        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conndelseg.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SEGUNDA APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA SEGUNDA"


def deletTER():
    try:
        conndelter = sqlite3.connect('AGENDA.DB')
        cursor = conndelter.cursor()

        # EXCLUI TODOS OS DADOS DA TABELA TERÇA
        cursor.execute("DELETE FROM TERCA;")

        # SALVA AS ALTERAÇÕES
        conndelter.commit()

        # FECHA A CONEXÃO COM O BANCO DE DADOS
        conndelter.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA TERÇA APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA TERÇA"


def deletQUA():
    try:
        conndelqua = sqlite3.connect('AGENDA.DB')
        cursor = conndelqua.cursor()

        cursor.execute("DELETE FROM QUA;")

        conndelqua.commit()

        conndelqua.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUARTA APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA QUARTA"


def deletQUI():
    try:
        conndelqui = sqlite3.connect('AGENDA.DB')
        cursor = conndelqui.cursor()

        cursor.execute("DELETE FROM QUI;")

        conndelqui.commit()

        conndelqui.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUINTA APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA QUINTA"


def deletSEX():
    try:
        conndelsex = sqlite3.connect('AGENDA.DB')
        cursor = conndelsex.cursor()

        cursor.execute("DELETE FROM SEX;")

        conndelsex.commit()

        conndelsex.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SEXTA APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA SEXTA"


def deletSAB():
    try:
        conndelsab = sqlite3.connect('AGENDA.DB')
        cursor = conndelsab.cursor()

        cursor.execute("DELETE FROM SAB;")

        conndelsab.commit()

        conndelsab.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA SABADO APAGADOS COM SUCESSO."
    except:
        return "OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL APAGAR OS DADOS DA TABELA SABADO"


# -------------------------------------------------------------------
# ADICIONAR COLUNA ÀS COLUNAS

# noinspection PyGlobalUndefined
def adicionarCol():
    global tabelaADC
    try:
        connadd = sqlite3.connect('AGENDA.DB')
        cursor = connadd.cursor()

        tabela = input("DIGITE O NOME DA TABELA")

        coluna = input("DIGITE O NOME DA COLUNA")

        tipo_dado = input("DIGITE O TIPO DE DADO DA COLUNA:")

        # concatena as informações na string da consulta SQL
        sql_query = f"ALTER TABLE{tabelaADC}ADD COLUMN {coluna} {tipo_dado}"

        cursor.execute(sql_query)

        connadd.commit()

        connadd.close()
        return "OPERAÇÃO BEM SUCEDIDA, COLUNA ADICIONADA COM SUCESSO."
    except:
        return F"OPERAÇÃO NÃO SUCEDIDA, NÃO FOI POSSÍVEL ADICIONAR A COLUNA NA TABELA, {tabelaADC}"


# -------------------------------------------------------------------
# DELETAR ESPECIFICAMENTE UMA COLUNA

def apagar_coluna():
    try:
        connapgcol = sqlite3.connect('AGENDA.DB')
        cursor = connapgcol.cursor()

        tabeladc = input("DIGITE O NOME DA TABELA:")
        colunadc = input("DIGITE O NOME DA COLUNA A SER EXCLUÍDA:")

        sql_query = f"ALTER TABLE {tabeladc} DROP COLUMN {colunadc}"

        cursor.execute(sql_query)

        connapgcol.commit()

        connapgcol.close()
        return "OPERAÇÃO BEM SUCEDIDA, DADOS DA TABELA QUARTA APAGADOS COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"

# -------------------------------------------------------------------
# ADICIONAR TABELAS NO BDD

def add_tabble():
    try:
        connaddtable = sqlite3.connect('AGENDA.DB')
        cursor = connaddtable.cursor()

        # SOLICITA O NOVO NOME DA TABELA QUE IREMOS CRIAR
        nome_tabela = str(input("INFORME O NOME DA NOVA TABELA"))

        # CRIA UMA STRING DE CONSULTA SQL PARA CRIAR UMA NOVA TABELA, COM AS COLUNAS QUE JA EXISTEM NAS OUTRAS TABELAS
        sql_query = f"CREATE TABLE {nome_tabela} (" \
                    f"ID INTEGER PRIMARY KET AUTOINCREMENT MATERIA1 TEXT, HORARIO1 TEXT, MATERIA2 TEXT, HORARIO2 TEXT)"
        cursor.execute(sql_query)

        connaddtable.commit()

        connaddtable.close()
        return "OPERAÇÃO BEM SUCEDIDA, TABELA ADICIONADA COM SUCESSO."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# DELETAR TABLES DO BANCO DE DADOS
# -------------------------------------------------------------------
def apagar_tabela():
    try:
        conndeltable = sqlite3.connect('AGENDA.DB')
        tabela_at = input("INFORME O NOME DA TABELA...")
        cursor = conndeltable.cursor()
        cursor.execute("DROP TABLE IF EXISTS" + tabela_at)
        conndeltable.commit()
        conndeltable.close()
        return "OPERAÇÃO BEM SUCEDIDA TABELA EXCLUIDA COM SUCESSO..."
    except sqlite3.OperationalError as e:
        return f"Operação não sucedida. Erro: {str(e)}"


# -------------------------------------------------------------------
def menu_principal():
    connMP = sqlite3.connect('AGENDA.db')
    print("\t\t\t\t@====================================@")
    print("\t\t\t\t@==-BEM VINDO À SUA AGENDA ROZENDO-==@")
    print("\t\t\t\t@====================================@")

    # nesta variavel será decidido qual opção o usuario Rozendo irá usar

    print("\t\t@@@====1 - VER AGENDA===@@@")
    print("\t\t@@@====2 - MODIFICAR AGENDA- MODIFICAR POR INTEIRA===@@@")
    print("\t\t@@@====3 - APAGAR DADOS DAS TABELAS COMPLETAMENTE===@@@")
    print("\t\t@@@====4-  ALTERAR TABELA- ADICIONAR COLUNAS===@@@")
    print("\t\t@@@====5 - APAGAR DADOS - REMOVER COLUNAS===@@@")
    print("\t\t@@@====6-  ADICIONAR TABELAS.===@@@")
    print("\t\t@@@====7-  APAGAR TABELAS COMPLETAMENTE===@@@")
    decisao = int(input("Oque deseja fazer?"))
    entrada_especial = ''
    # VER AGENDA
    if decisao == 1:
        print("digite segunda para segunda feira")
        print("digite terça para terça feira")
        print("digite quarta para quarta feira")
        print("digite quinta para quinta feira")
        print("digite sexta para sexta feira")
        print("digite sabado para sabado")
        print("digite outra tabela para acessar outra tabela...")
        entrada = input('DIGITE O DIA DA SEMANA QUE VOCÊ DESEJA VER')
        while entrada != "exit":

            if entrada.lower() == 'segunda':
                try:
                    print(verSEG())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("@@==$OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"Operação não sucedida. Erro: {str(e)}"

            elif entrada.lower() == 'terça':
                try:
                    print(verTER())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("\t@@=#OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"@@@OPERAÇÃO NÃO SUCEDIDA. ERRO: {str(e)}"
            elif entrada == "quarta" or entrada == "QUARTA":
                try:
                    print(verQUA())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("\t@@=#OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"@@@OPERAÇÃO NÃO SUCEDIDA. ERRO: {str(e)}"
            elif entrada == "quinta" or entrada == "QUINTA":
                try:
                    print(verQUI())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("\t@@=#OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"@@@OPERAÇÃO NÃO SUCEDIDA. ERRO: {str(e)}"
            elif entrada == "sexta" or entrada == "SEXTA":
                try:
                    print(verSex())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("\t@@=#OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"@@@OPERAÇÃO NÃO SUCEDIDA. ERRO: {str(e)}"
            elif entrada == "sabado" or entrada == "SABADO":
                try:
                    print(verSAB())
                    print("\t:::DESEJA VOLTAR AO MENU PRINCIPAL? S OU N::::")
                    voltar = str(input("$DIGITE A OPÇÃO DESEJADA$"))
                    if voltar.lower() == 's' or voltar.lower() == 'sim':
                        menu_principal()
                    elif voltar.lower() == 'n' or voltar.lower() == 'nao':
                        print("\t@@=#OPERAÇÃO FINALIZADA COM SUCESSO$==@@")
                        break
                    else:
                        print("\t@@==:$OPERAÇÃO FINALIZADA, ENTRADA DE DADOS ERRADA$:==@@")
                        menu_principal()
                    return "@@==:$OPERAÇÃO BEM SUCEDIDA$:==@@"
                except sqlite3.OperationalError as e:
                    return f"@@@OPERAÇÃO NÃO SUCEDIDA. ERRO: {str(e)}"
            elif entrada == "exit":
                print("OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA.")
                connMP.close()
                break
            elif entrada == 'outra tabela':
                outra_tabela = input("INFORME A OUTRA TABELA A SER ACESSADA")
                
            else:
                raise Exception("ENTRADA DE DADOS ERRADA, TERMINANDO SUA SESSÃO...")

    # MODIFICAR AGENDA- MODIFICAR POR INTEIRA
    elif decisao == 2:
        decisao2 = input("INFORME O DIA DA SEMANA PARA ALTERAR")
        while decisao2 != "exit":
            if decisao2 == "segunda" or decisao2 == 'SEGUNDA':
                updateSEG()
            elif decisao2 == 'terca' or 'TERCA':
                updateTER()
            elif decisao2 == 'quarta' or 'QUARTA':
                updateQUA()
            elif decisao2 == 'quinta' or 'QUINTA':
                updateQUI()
            elif decisao2 == 'sexta' or 'SEXTA':
                updateSEX()
            elif decisao2 == 'sabado' or 'SABADO':
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
            if decisao3 == "segunda" or "SEGUNDA":
                deletSEG()

            elif decisao3 == "terca" or "TERCA":
                deletTER()

            elif decisao3 == "quarta" or "TERÇA":
                deletQUA()

            elif decisao3 == "quinta" or "QUINTA":
                deletQUI()

            elif decisao3 == "sexta" or "SEXTA":
                deletSEX()

            elif decisao3 == "sabado" or "SABADO":
                deletSAB()

            elif decisao3 == "EXIT" or "exit" or "Exit" or "sair" or "SAIR" or "Sair":
                print("$$OBRIGADO POR USAR O SISTEMA DE GERENCIAMENTO DE AGENDA$$")
                break
            else:
                raise Exception("@==DADOS INFORMADOS DE MANEIRA ERRADA==@")

    # ADICIONAR ITENS NA TABELA
    elif decisao == 4:
        print("\t BEM VINDO, ESTA OPÇÃO IRÁ ADICONAR ITENS A TABELA QUE DESEJA-")
        adicionarCol()

    # REMOVER COLUNAS
    elif decisao == 5:
        print("\t BEM VINDO, ESTA OPÇÃO IRÁ REMOVER COLUNAS DA SUA TABELA")
        apagar_coluna()

    # ADICIONAR TABELA
    elif decisao == 6:
        print("\t BEM VINDO, ESTA OPÇÃO IRÁ ADICIONAR UMA TABELA NOVA AO SEU BDD")
        add_tabble()
    elif decisao == 7:
        print("\t BEM VINDO, ESTA OPÇAO IRÁ REMOVER A TABELA DESEJADA-")
        apagar_tabela()
    else:
        raise Exception("------------------ OPÇÃO INVALIDA -------------------------")


menu_principal()

