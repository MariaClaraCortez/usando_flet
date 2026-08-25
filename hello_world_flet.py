import flet as ft

def main(pagina:ft.Page):
    #ALTERANDO O TITULO DA JANLA 
    pagina.title = "Super Programa de Hello World!!"
    #ALTERANDO A COR DA JANELA
    pagina.bgcolor="#EAF3FA"  
    #ALTERANDO A ALTURA DA JANELA
    pagina.window.height = 650
    #ALTERANDO A LARGURA DA JANELA
    pagina.window.width = 1200
    #CENTRALIZANDO O TEXTO
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #CRIANDO UM TEXTO
    texto_hello =ft.Text(value="Olá Pessoal!!",
                        color ="#A0C6E9",
                        font_family="italic",
                        size=50,
                        weight=ft.FontWeight.BOLD,)
                        
    subtitulo =ft.Text(value="Sejam Bem Vindos a Minha Fliricultira!",
                       color ="#A0C6E9",
                       font_family="consolas",
                       size=30,
                       weight=ft.FontWeight.BOLD,)
    #FUNÇAO PARA O BOTAO
    def mostar_imagem():
        if imagem.visible == True:
            imagem.visible =False 
        else:
            imagem.visible =True

           
    #CRIANDO BOTAO 
    botao =ft.Button(content="Clique Aqui",
                     color="#C5DCF1",
                     on_click=mostar_imagem)
    #CRIANDO UMA IMAGEM
    imagem =ft.Image(src="img/flor/tulipa.jpg",
                    width=150,
                    height=150,
                    border_radius =20,
                    visible=False)
    #ADICIONANDO O TEXTO PA PAGINA
    pagina.add(texto_hello)
    pagina.add(subtitulo)
    pagina.add(botao)
    pagina.add(imagem)
    pagina.update()







ft.run(main)
