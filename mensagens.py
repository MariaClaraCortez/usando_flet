import flet as ft
import random

def main(pagina:ft.Page):
    #ALTERANDO O TITULO DA JANLA 
    pagina.title = "Super Programa de Mensagens!!"
    #ALTERANDO A COR DA JANELA
    pagina.bgcolor="#EAF3FA"  
    #ALTERANDO A ALTURA DA JANELA
    pagina.window.height = 600
    #ALTERANDO A LARGURA DA JANELA
    pagina.window.width = 1000
    #CENTRALIZANDO O TEXTO
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto_hello =ft.Text(value="Mensagem do Dia",
                        color ="#A0C6E9",
                        font_family="italic",
                        size=60,
                        weight=ft.FontWeight.BOLD,)
                        
    subtitulo =ft.Text(value="Um clique, um destino",
                           color ="#A0C6E9",
                           font_family="consolas",
                           size=40,
                           weight=ft.FontWeight.BOLD,)

    
    def mensagem():
        lista_mensagens = ["Você tentou... e foi isso.",
                        "Sua ideia saiu pela porta dos fundos.",
                        "Você tem um talento especial para complicar o simples.",
                        "Impressionante... mas pelo motivo errado.",
                        "Até um relógio parado acerta duas vezes.",
                        "Sua estratégia foi um verdadeiro mistério.",
                        "Você quase acertou... quase.",
                        "Parece que a sorte estava de folga.",
                        "Você consegue errar com confiança.",
                        "Essa foi uma obra de improviso.",
                        "Você fez o difícil parecer impossível.",
                        "Sua organização tirou férias.",
                        "Foi uma tentativa bem corajosa.",
                        "Você transformou um detalhe em um problemão.",
                        "Sua pressa chegou antes da sua ideia.",
                        "Você tem uma criatividade bem... inesperada.",
                        "Hoje não era o seu dia.",
                        "Seu plano precisava de um plano B.",
                        "Você conseguiu surpreender todo mundo."]

        lista_imagem = ["img/memes/doritos.jpg",
                        "img/memes/hehehe.png",
                        "img/memes/woody.jpg",
                        "img/memes/zoio.jpg",
                        "img/memes/cachorro.jpg"]
        
        sorteio = random.choice(lista_mensagens)
        sorteio_imagem = random.choice(lista_imagem)


        if texto_mensagens.visible ==  True:
            texto_mensagens.visible =False 
            pagina.bgcolor = hex(random.randint(0,16700000))
            texto_mensagens.color = hex(random.randint(0,16700000))



        else:
            texto_mensagens.visible =True
            texto_mensagens.value = sorteio

        if imagem.visible == True:
            imagem.visible = False
        else:
            imagem.visible = True
            imagem.src = sorteio_imagem


    botao = ft.Button(content="Clique Aqui para ver sua mensagem!",
                     color="#7BAFE0",
                     on_click=mensagem)

    imagem =ft.Image(src="img/cachorro.jpg",
                    width=200, 
                    height=200,
                    border_radius=20,
                    visible=False)


    texto_mensagens =ft.Text(value="",
                             color="#0F2763",
                             size=30,
                             visible=False)










    pagina.add(texto_hello)
    pagina.add(subtitulo)
    pagina.add(botao)
    pagina.add(texto_mensagens)
    pagina.add(imagem)
ft.run(main)