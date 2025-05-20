
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fosforo BOOLEAN,
    potassio BOOLEAN,
    ph REAL,
    umidade REAL,
    irrigacao_ativa BOOLEAN
)
''')

# Função CRUD
def inserir_dado(fosforo, potassio, ph, umidade, irrigacao):
    cursor.execute('''
        INSERT INTO sensores (fosforo, potassio, ph, umidade, irrigacao_ativa)
        VALUES (?, ?, ?, ?, ?)
    ''', (fosforo, potassio, ph, umidade, irrigacao))
    conn.commit()

def consultar_dados():
    cursor.execute('SELECT * FROM sensores')
    return cursor.fetchall()

def atualizar_dado(id, campo, novo_valor):
    cursor.execute(f'UPDATE sensores SET {campo} = ? WHERE id = ?', (novo_valor, id))
    conn.commit()

def remover_dado(id):
    cursor.execute('DELETE FROM sensores WHERE id = ?', (id,))
    conn.commit()

# Simulação de inserção
inserir_dado(True, True, 6.8, 35.0, True)
inserir_dado(True, False, 7.2, 42.0, False)

# Exibir resultados
for linha in consultar_dados():
    print(linha)

# Fechar conexão
conn.close()
