from database.conexao_tarefa import conectar_bd

def criar_bd():
    # criando a tabela de tarefas no banco de dados SQLITE3
        conexao, cursor = conectar_bd()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS tarefas(
                       cod_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                       tarefa TEXT,
                       status TEXT);
                       """)  #cursor executa esse comando para criar a tabela
        
        conexao.commit() #salvando alterações
        conexao.close() #fechando conexão