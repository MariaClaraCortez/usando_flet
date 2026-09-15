import flet as ft
import sqlite3
from component_tarefa.classe_campo_tarefa import Campo_Tarefa
from database.conexao_tarefa import conectar_bd
from database.create_database import criar_bd
from model import model_tarefa 


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

    criar_bd()

    

    def excluir_tarefa(campo_tarefa):
        model_tarefa.deletar_tarefa(campo_tarefa.cod_tarefa)
        lista_campo_tarefa.remove(campo_tarefa)

    def adicionar_campo_tarefa():
        cod_tarefas = model_tarefa.inserir_tarefa(campo_tarefa.value)
        lista_campo_tarefa.append(Campo_Tarefa(texto_tarefa=campo_tarefa.value,
                                               funcao_excluir=excluir_tarefa,
                                               cod_tarefa=cod_tarefas))
        campo_tarefa.value = ""

    tarefas_bd = model_tarefa.recuperar_tarefas()
    for tarefa in tarefas_bd:
        lista_campo_tarefa.append(Campo_Tarefa(texto_tarefa=tarefa["tarefa"],
                                               funcao_excluir=excluir_tarefa,
                                               cod_tarefa=tarefa["cod_tarefas"]))
        
    
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