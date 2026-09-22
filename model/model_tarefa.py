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



def atualizar_status(cod_tarefas, novo_status):
     conexao, cursor = conectar_bd()
     cursor.execute("""
                     Update tarefas
                    set status = ?
                    where cod_tarefas = ?;
                    """, 
                    [novo_status, cod_tarefas])
     conexao.commit()
     conexao.close()

def atualizar_tarefas(cod_tarefa, novo_texto):
     conexao, cursor = conectar_bd()
     cursor.execute("""
                     Update tarefas
                    set tarefa = ?
                    where cod_tarefa = ?;
                    """
                    [novo_texto,cod_tarefa])
     conexao.commit()
     conexao.close()



