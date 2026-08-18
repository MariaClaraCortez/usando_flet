import flet as ft

def main (pagina:ft.Page):
    pagina.title = "Calculo de Média"
    pagina.bgcolor = "#F2FAEB"
    pagina.horizontal_alignment = "center"
    pagina.spacing = 30



    titulo = ft.Text(value="Calculo Média",
                     size = 45,
                     font_family="Georgia",
                     weight=ft.FontWeight.BOLD,
                     color="#ACDC7F")
    

    lista_campo_notas = []


    def adicionar_campo_nota():
        lista_campo_notas.append(ft.TextField(label=ft.Text("Nota",
                                              color= "#508023"),
                                              bgcolor="#DCF0C9",
                                              border_color="#C3E6A3",
                                              border_width= 2,
                                              border_radius=20))
        

    def calcular_media ():
        soma = 0
        contador_notas= 0

        for campo in lista_campo_notas:
            nota = float(campo.value)
            soma += nota
            contador_notas += 1
        resultado = soma / contador_notas
        campo_resutado.value = resultado


    botao_ico = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.ADD,
                                                     color= "#508023",),
                                        bgcolor="#ACDC7F",
                                        hover_color="#94D25B",
                                        on_click=adicionar_campo_nota)


    botao_resultado = ft.FloatingActionButton(content=ft.Text("Calcular média",
                                           color="#508023"),
                                           width=150,
                                           height=50,
                                           bgcolor="#DCF0C9",
                                           hover_color="#94D25B",
                                           on_click=calcular_media)


    campo_resutado = ft.TextField(value=0,
                                  color="#508023",
                                  label=ft.Text("Resultado",
                                                color="#508023",
                                                weight=ft.FontWeight.BOLD),
                                  read_only=True,
                                  text_align="center",
                                  border_color="#C3E6A3",
                                  border_radius= 10,
                                  border_width= 2,
                                  bgcolor= "#DCF0C9",)
    

    coluna_notas = ft.Column(controls=lista_campo_notas,
                             expand=True,
                             wrap=True,
                             scroll=ft.ScrollMode.AUTO)
    

    linha_bc = ft.Row(controls=[botao_resultado,
                                campo_resutado],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20)


    pagina.controls = [titulo,
                       botao_ico,
                       coluna_notas,
                       linha_bc]

    

    pagina.update()
ft.run(main)