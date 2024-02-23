import sqlite3

# Conecta-se ao banco de dados
banco = sqlite3.connect("dbContatos.db")

# Cria um cursor para executar comandos SQL
cursor = banco.cursor()

# Cria a tabela Contatos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    email TEXT,
    endereco TEXT
);
""")

# Salva as alterações
banco.commit()
