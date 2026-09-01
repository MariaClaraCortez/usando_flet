import flet as ft

class Campo_Tarefa(ft.Row):
    def __init__(self,texto_tarefa):
        super().__init__()

        def alterar_cor ():
            if self.caixa_certinho.value == True:
                self.container_tarefa.bgcolor = "#C3E6A3"
                self.texto_caixa.value="Concluido"
            else:
                self.container_tarefa.bgcolor = "#a46e66"
                self.texto_caixa.value = "Pendente"

        self.caixa_certinho = ft.CupertinoCheckbox(on_change=alterar_cor,
                                                   value=False)
        

        self.caixa_tarefa = ft.TextField(value=texto_tarefa,
                                         label="",
                                         border_color="#60162d",
                                         border_radius=20,
                                         border_width=1.5)
        
        
        self.texto_caixa = ft.Text(value="Pendente")
        

        self.botao_delete = ft.FloatingActionButton(icon=ft.Icon(icon=ft.CupertinoIcons.DELETE),
                                                    width=30,height=30)
        

        self.botao_editar = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.CREATE),
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
                                       bgcolor="#a46e66",
                                       padding=10,
                                       border=ft.Border.all(2,color="#781f25"),
                                       width=390,
                                       border_radius=10,
                                       animate= ft.Animation(duration=400))
        


        self.controls = [self.container_tarefa]

        



        


    @property
    def value(self):
        return self.caixa_tarefa.value