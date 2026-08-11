import flet as ft

def main(pagina:ft.Page):
    pagina.title = "Conversor de Temperatura🌡"
    pagina.bgcolor = "#F2D5E2"
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #pagina.horizontal_alignment = "center"



    def converter_temperatura():
        valor = float(campo_valor.value)
        de = campo_de.value
        para = campo_para.value

        if de == "c" and para == "k":
            resultado = valor + 273.15
        elif de == "c" and para == "f":
            resultado = (valor * 1.8) + 32
        elif de == "c" and para == "c" or de == "f" and para == "f" or de == "k" and para == "k":
            resultado = valor
        elif de == "k" and para == "c":
            resultado = valor - 273.15
        elif de == "k" and para == "f":
            resultado = (valor -273.15)*1.8 + 32
        elif de == "f" and para == "c":
             resultado = (valor - 32)/1.8
        elif de == "f" and para == "k":
            resultado = (valor - 32*1.8) +273.15 

        campo_resultado.value = resultado
    



    titulo = ft.Text(value="Temperatura",
                     size=40,
                     font_family="Georgia",
                     weight=ft.FontWeight.BOLD,
                     color="#A03163")

    campo_valor = ft.TextField(label="Valor",
                         border_color= "#7D264D",
                         border_radius= 8,
                         border_width= 2.5)

    campo_de = ft.Dropdown(width = 180,
                     label="de",
                     border_color= "#7D264D",
                     border_radius= 8,
                     border_width= 2.5,
                     options= [
                         ft.DropdownOption(key="f",text="Fahrenheit"),
                         ft.DropdownOption(key="c",text="Celsius"),
                         ft.DropdownOption(key="k",text="Kelvin")
                         ])

    campo_para = ft.Dropdown(width = 180,
                     label="Para",
                     border_color= "#7D264D",
                     border_radius= 8,
                     border_width= 2.5,
                     options= [
                         ft.DropdownOption(key="f",text="Fahrenheit"),
                         ft.DropdownOption(key="c",text="Celsius"),
                         ft.DropdownOption(key="k",text="Kelvin")
                         ])


    botao = ft.Button(content="Calcular",
                      height=100,
                      color= "#E3A5C1",
                      bgcolor="#A03163",
                      on_click= converter_temperatura)



    campo_resultado= ft.TextField(read_only=True,
                                  label="Resultado",
                                  border_color= "#7D264D",
                                  border_radius= 8,
                                  border_width= 2.5)

    
    coluna = ft.Column(controls=[campo_de,
                                 campo_para])

    linha = ft.Row(controls=[coluna,
                             botao],

                             alignment="center",
                             spacing= 20)

    


    pagina.controls = [titulo,
                       campo_valor,
                       linha,
                       campo_resultado,
                       ]

    pagina.spacing = 15

    pagina.update()




ft.run(main)