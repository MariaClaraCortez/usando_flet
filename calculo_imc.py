import flet as ft 

def main(pagina:ft.Page):
    pagina.title = "Tipos de Corpos"
    pagina.bgcolor = "#F6F3EE"
    pagina.horizontal_alignment ="center"
    pagina.spacing = 30


    def calcular_corpo():
        if campo_peso.value == "" and campo_altura.value == "":
            mensagem = ft.SnackBar(content="Os campos devem ser peenchidos",
                                   duration=5000,
                                   show_close_icon=True,)
            pagina.show_dialog(mensagem)
            return
        elif campo_altura.value == "":
            mensagem = ft.SnackBar(content="O campo altura deve ser preenchido",
                                   duration=5000,
                                   show_close_icon=True)
            pagina.show_dialog(mensagem)
            return
            
        elif campo_peso.value == "":
            mensagem = ft.SnackBar(content="O campo peso deve ser preenchido",
                                   duration=5000,
                                   show_close_icon=True)
            pagina.show_dialog(mensagem)
            return



        peso = float (campo_peso.value)
        altura = float(campo_altura.value)
        conta = peso / (altura*altura)

        if conta <= 18.5:
            resultado = "Magreza"
            imagem.src = "img_imc/magreza.png"

        elif conta > 18.5 and conta <=24.9:
            resultado = "Normal"
            imagem.src = "img_imc/normal.png" 

        elif conta > 24.9 and conta <=29.9:
            resultado = "Sobrepeso"
            imagem.src = "img_imc/sobrepeso.png"

        elif conta > 29.9 and conta <=34.9:
            resultado = "Obesidade Grau I"
            imagem.src = "img_imc/obs 1.png"

        elif conta > 34.9 and conta <=39.9:
            resultado = "Obesidade Grau II"
            imagem.src = "img_imc/obs 2.png"

        elif conta >39.9:
            resultado = "Obesidade Grau III"
            imagem.src = "img_imc/obs 3.png"

    
        campo_resultado.value = resultado




    titulo = ft.Text(value="Qual seu tipo de corpo?",
                    size=40,
                    font_family="Georgia",
                    weight=ft.FontWeight.BOLD,
                    color="#B8A075")

    campo_peso = ft.TextField(label="Peso",
                              border_color="#8A7347",
                              border_radius=10,
                              border_width=2.5)

    campo_altura = ft.TextField(label="Altura",
                                border_color="#8A7347",
                                border_radius=10,
                                border_width=2.5)

    linha_ap = ft.Row(controls=[campo_peso,
                             campo_altura],
                             alignment="center",
                             spacing= 20)

    botao = ft.Button(content="Calcular",
                      color="#6C5937",
                      bgcolor="#D9CDB6",
                      on_click=calcular_corpo)

    campo_resultado = ft.TextField(read_only=True,
                                   label="Resultado",
                                   border_color="#8A7347",
                                   border_radius=10,
                                   border_width=2.5)

    imagem =ft.Image(src="#",
                        border_radius=1000,
                        visible=True)



    pagina.controls = [titulo,
                       linha_ap,
                       botao,
                       campo_resultado,
                       imagem]


    pagina.update()



ft.run(main)