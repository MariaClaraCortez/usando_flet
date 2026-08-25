import flet as ft

class Campo_nota(ft.Row):
    def __init__(self):
        super().__init__()
        self.caixa_texto = ft.TextField(label=ft.Text("Nota",
                                              color= "#508023"),
                                              bgcolor="#DCF0C9",
                                              border_color="#C3E6A3",
                                              border_width= 2,
                                              border_radius=20,
                                              width=200)

        self.caixa_selecao = ft.CupertinoCheckbox(on_change=self.alterar_cor,)

        self.container_nota = ft.Container(content=ft.Row(controls=[self.caixa_texto,self.caixa_selecao],),
                                       bgcolor="#F2FAEB",
                                       padding=5,
                                       border=ft.Border.all(2,color="#DCF0C9"),
                                       width=250,
                                       border_radius=10,
                                       animate= ft.Animation(duration=400))

        
        self.controls= [self.container_nota]


    def alterar_cor (self):
            if self.caixa_selecao.value == True:
                self.container_nota.bgcolor = "#C3E6A3"
            else:
                 self.container_nota.bgcolor = "#F2FAEB"

    @property
    def value(self):
         return self.caixa_texto.value