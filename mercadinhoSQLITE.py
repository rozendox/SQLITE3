import sqlite3

# cria o banco de dados
conn = sqlite3.connect('supermercado.db')

# cria a tabela 'produtos'
conn.execute('''CREATE TABLE produtos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              preco REAL NOT NULL);''')

# insere alguns produtos
conn.execute("INSERT INTO produtos (nome, preco) VALUES ('Arroz', 10.0)")
conn.execute("INSERT INTO produtos (nome, preco) VALUES ('Feijão', 8.0)")
conn.execute("INSERT INTO produtos (nome, preco) VALUES ('Leite', 5.0)")
conn.execute("INSERT INTO produtos (nome, preco) VALUES ('Pão', 3.0)")
conn.execute("INSERT INTO produtos (nome, preco) VALUES ('Queijo', 15.0)")

# cria a tabela 'clientes'
conn.execute('''CREATE TABLE clientes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              email TEXT NOT NULL);''')

# insere alguns clientes
conn.execute("INSERT INTO clientes (nome, email) VALUES ('João', 'joao@gmail.com')")
conn.execute("INSERT INTO clientes (nome, email) VALUES ('Maria', 'maria@hotmail.com')")
conn.execute("INSERT INTO clientes (nome, email) VALUES ('Pedro', 'pedro@yahoo.com')")

# cria a tabela 'vendas'
conn.execute('''CREATE TABLE vendas
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              data TEXT NOT NULL,
              cliente_id INTEGER NOT NULL,
              FOREIGN KEY (cliente_id) REFERENCES clientes(id));''')

# insere uma venda
conn.execute("INSERT INTO vendas (data, cliente_id) VALUES ('2022-02-19', 1)")

# cria a tabela 'itens_venda'
conn.execute('''CREATE TABLE itens_venda
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              venda_id INTEGER NOT NULL,
              produto_id INTEGER NOT NULL,
              quantidade INTEGER NOT NULL,
              FOREIGN KEY (venda_id) REFERENCES vendas(id),
              FOREIGN KEY (produto_id) REFERENCES produtos(id));''')

# insere alguns itens de venda
conn.execute("INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (1, 1, 2)")
conn.execute("INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (1, 2, 3)")
conn.execute("INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (1, 3, 1)")

# faz uma consulta para obter todos os produtos
produtos = conn.execute("SELECT * FROM produtos")
for produto in produtos:
    print(produto)

# faz uma consulta para obter todas as vendas
vendas = conn.execute("SELECT * FROM vendas")
for venda in vendas:
    print(venda)

# faz uma consulta para obter todos os clientes que fizeram compras
clientes = conn.execute("SELECT DISTINCT clientes.* FROM clientes INNER JOIN vendas ON clientes.id = vendas.cliente_id")
for cliente in clientes:
    print(cliente)

# fecha a conexão com o banco de dados
conn.close()
