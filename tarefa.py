import flet as ft
from component_tarefa.classe_campo_tarefa import Campo_Tarefa
import sqlite3

def main(pagina:ft.Page):
    pagina.title = "Tarefas"
    pagina.bgcolor = "#EFF7F6"
    pagina.horizontal_alignment = "center"
    pagina.spacing = 30

    pagina.update()

    titulo = ft.Text(value="Tarefas do Ano",
                     size=50,
                     font_family="Georgia",
                     weight=ft.FontWeight.BOLD,
                     color= "#256D85")
    
    lista_campo_tarefa = []

    # criando a tabela de tarefas no banco de dados SQLITE3
    conexao = sqlite3.connect("bd_tarefa.sqlite") #conectando ao banco de dados
    cursor = conexao.cursor() #criando cursor
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tarefas(
                   cod_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                   tarefa TEXT,
                   status TEXT);
                   """)  #cursor executa esse comando para criar a tabela
    
    conexao.commit() #salvando alterações
    conexao.close() #fechando conexão

    def excluir_tarefa(campo_tarefa):
        lista_campo_tarefa.remove(campo_tarefa)

    def adicionar_campo_tarefa():
        lista_campo_tarefa.append(Campo_Tarefa(texto_tarefa=campo_tarefa.value,
                                               funcao_excluir=excluir_tarefa))

        conexao = sqlite3.connect("bd_tarefa.sqlite")
        cursor = conexao.cursor()
        cursor.execute ("""
                        INSERT INTO tarefas(tarefa,status)
                        VALUES (?, ?);
                           """,
                             [campo_tarefa.value,"Pendente"])
        conexao.commit()
        conexao.close()
        campo_tarefa.value = ""
        
    
    campo_tarefa = ft.TextField(label=ft.Text("Tarefa",
                                              color="#6B7280"),
                                              bgcolor="#FFFFFF",
                                border_color = "#A9D1E8",
                                border_radius=20,
                                border_width=1.5)
    
    botao_incluir = ft.Button(content=ft.Text("Incluir",
                                              color="#FFFFFF"),
                                              bgcolor="#84C69B",
                                              on_click=adicionar_campo_tarefa)

    linha_incluir = ft.Row(controls=[campo_tarefa,botao_incluir],
                           alignment="center")
    
    coluna_tarefas = ft.Column(controls=lista_campo_tarefa,
                             expand=True,
                             wrap=True,
                             scroll=ft.ScrollMode.AUTO)

    

    
    pagina.controls = [titulo,
                       linha_incluir,
                       coluna_tarefas]


ft.run(main)