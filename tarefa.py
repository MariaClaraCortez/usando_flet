import flet as ft
from component_tarefa.classe_campo_tarefa import Campo_Tarefa

def main(pagina:ft.Page):
    pagina.title = "Tarefas"
    pagina.bgcolor = "#e5c9bb"
    pagina.horizontal_alignment = "center"
    pagina.spacing = 30

    pagina.update()

    titulo = ft.Text(value="Tarefas do Ano",
                     size=50,
                     font_family="Georgia",
                     weight=ft.FontWeight.BOLD,
                     color= "#781f25")
    
    lista_campo_tarefa = []

    def adicionar_campo_tarefa():
        lista_campo_tarefa.append(Campo_Tarefa())
    
    campo_tarefa = ft.TextField(label=ft.Text("Tarefa",
                                              color="#60162d"),
                                border_color="#60162d",
                                border_radius=20,
                                border_width=1.5)
    
    botao_incluir = ft.Button(content=ft.Text("Incluir",
                                              color="#480a0b"),
                                              bgcolor="#ab6c65",
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