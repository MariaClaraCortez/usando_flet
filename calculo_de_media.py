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

    botao_ico = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.ADD,
                                                     color= "#508023",),
                                        bgcolor="#ACDC7F",
                                        hover_color="#67A42D")

    #campo_calculo = ft.TextField(label="Calculo",
                                # border_color="#ACDC7F",
                                # border_radius= 10,
                                # border_width= 2,
                                # bgcolor= "#DCF0C9")

    botao_resultado = ft.FilledTonalButton(content="Calcular média",
                                           color="#508023",
                                           bgcolor="#DCF0C9")


    campo_resutado = ft.TextField(value=0,
                                  color="#7DC837",
                                  label="Resultado",
                                  read_only=True,
                                  text_align="center",
                                  border_color="#ACDC7F",
                                  border_radius= 10,
                                  border_width= 2,
                                  bgcolor= "#DCF0C9")

    linha_bc = ft.Row(controls=[botao_resultado,
                                campo_resutado],
                                alignment="center",
                                spacing=20)


    pagina.controls = [titulo,
                       botao_ico,
                       linha_bc,]

    

    pagina.update()
ft.run(main)