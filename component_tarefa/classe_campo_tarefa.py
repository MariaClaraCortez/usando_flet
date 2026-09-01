import flet as ft

class Campo_Tarefa(ft.Row):
    def __init__(self,texto_tarefa,funcao_excluir):
        super().__init__()

        self.funcao_excluir = funcao_excluir

        def alterar_cor ():
            if self.caixa_certinho.value == True:
                self.container_tarefa.bgcolor = "#EAF5F0"
                self.texto_caixa.value="Concluido"
                self.texto_caixa.color = "#2E8B57"
                self.caixa_tarefa.border_color = "#B6DCCB"
            else:
                self.container_tarefa.bgcolor = "#E9F3FB"
                self.texto_caixa.color = "#A9D1E8"
                self.texto_caixa.value = "Pendente"
                self.caixa_tarefa.border_color = "#A9D1E8",
                

        self.caixa_certinho = ft.CupertinoCheckbox(on_change=alterar_cor,
                                                   value=False)
        

        self.caixa_tarefa = ft.TextField(value=texto_tarefa,
                                         label="",
                                         border_color="#5DA9B5",
                                         color="#5DA9B5",
                                         border_radius=20,
                                         border_width=1.5)
        
        
        self.texto_caixa = ft.Text(value="Pendente",
                                   weight=ft.FontWeight.BOLD,
                                   color = "#A9D1E8")
        

        self.botao_delete = ft.FloatingActionButton(icon=ft.Icon(icon=ft.CupertinoIcons.DELETE,color= "#176080"),
                                                    bgcolor= "#FFFFFF",
                                                    width=30,height=30, on_click=lambda:self.funcao_excluir(self))
        

        self.botao_editar = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.CREATE, color= "#176080"),
                                                    bgcolor= "#FFFFFF",
                                                    height=30,width=30)
        

        coluna_botaos = ft.Column(controls=[self.botao_delete,self.botao_editar],
                                  expand=True,
                                  wrap=True,
                                  scroll=ft.ScrollMode.AUTO) 
        
        coluna_escrita = ft.Column(controls=[self.texto_caixa,self.caixa_tarefa],
                                   width=300,
                                   wrap=True,
                                   scroll=ft.ScrollMode.AUTO,
                                   horizontal_alignment= "center")
        

        self.container_tarefa = ft.Container(content=ft.Row(controls=[self.caixa_certinho,coluna_escrita,coluna_botaos],),
                                       bgcolor="#E9F3FB",
                                       padding=10,
                                       border=ft.Border.all(2,color="#A9D1E8"),
                                       width=390,
                                       border_radius=10,
                                       animate= ft.Animation(duration=400))
        


        self.controls = [self.container_tarefa]

        



        


    @property
    def value(self):
        return self.caixa_tarefa.value