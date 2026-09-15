from database.conexao_tarefa import conectar_bd

def inserir_tarefa(texto_tarefa):
     conexao, cursor = conectar_bd()
     cursor.execute  ("""
                     INSERT INTO tarefas(tarefa,status)
                     VALUES (?, ?);
                       """,
                     [texto_tarefa,"Pendente"])
     conexao.commit()
     cod_tarefa = cursor.lastrowid
     conexao.close()
     return cod_tarefa


def recuperar_tarefas():
     conexao, cursor = conectar_bd()
     cursor.execute  ("""
                        SELECT * FROM tarefas;
                        """)

     tarefas = cursor.fetchall()
     conexao.close()
     return tarefas


def deletar_tarefa(cod_tarefas):
     conexao, cursor = conectar_bd()
     cursor.execute("""
                     DELETE FROM tarefas
                     WHERE cod_tarefas = ?;
                    """,
                    [cod_tarefas])
     conexao.commit()
     conexao.close()
