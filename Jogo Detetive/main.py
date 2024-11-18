import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame

pygame.mixer.init()

pygame.mixer.music.load("musica.mp3")

pygame.mixer.music.play(loops=-1) 


#DEF PRA FAZER O OUTLINE NO TEXTO
def draw_outlined_text(canvas, x, y, text, font, fill_color, outline_color, outline_width):
    for dx in range(-outline_width, outline_width+1):
        for dy in range(-outline_width, outline_width+1):
            if dx != 0 or dy != 0:
                canvas.create_text(x + dx, y + dy, text=text, font=font, fill=outline_color)
    canvas.create_text(x, y, text=text, font=font, fill=fill_color)

class jogo:
    
    def __init__(self) -> None:
        self.ja_inicio = None
        self.text = None
        self.titulo = None
        self.img_fundo = None
        self.image_label = None
        self.ja_segundo = None
        self.img_fundo2 = None
        self.image_label2 = None
        self.text2 = None
        self.img_fundo3 = None
        self.image_label3 = None
        self.ja_terceiro = None
        self.bt1 = None
        self.bt2 = None
        self.bt3 = None
        self.bt4 = None
        self.img_fundo4 = None
        self.text4 = None
        self.text42 = None
        self.image_label4 = None
        self.ja_quarto = None
        self.vencedor = None
        self.titulo4 = None
        self.imagem_inicio1 = None

#----------------------------------------------------------------------------------HISTORIA DO JOGO--------------------------------------------------------------------------------------------------------------------

    def inicio(self):
        root.destroy()
        self.ja_segundo = ctk.CTk()
        self.ja_segundo.title("Pense bem...")
        self.ja_segundo.geometry("1280x720")

        imagem_inicio = ImageTk.PhotoImage(file="vultonovo.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        draw_outlined_text(can, 640, 100, text="A história do jogo", font=("Bernard MT Condensed", 70), fill_color="white", outline_color="black", outline_width=4)
        can.pack(fill="both", expand=True)
        
        textao = """
Em uma cidade envolta em mistérios, a Mansão Arnésh se destacava como um símbolo de dor 
e perda. 
A ordem de Acheron se dedicava a investigar fenômenos sobrenaturais, enquanto 
enfrentava o peso de uma tragédia: 
muitos de seus agentes haviam perdido a vida nas tentativas de desvendar os segredos 
da mansão. 
A última missão resultou no sequestro de uma das agentes, chamada Sofia, por várias entidades 
obscuras que habitavam o lugar. 
A ordem estava determinada a resgatar Sofia, e entender o que se escondia no que chamam de
 "elemento nulo".
        """
        
        draw_outlined_text(can, 650, 400, text=textao, font=("Bernard MT Condensed", 25), fill_color="white", outline_color="black", outline_width=4)

        self.botao_prox = ctk.CTkButton(self.ja_segundo, text="Próximo", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.primeira_fase)
        self.botao_prox.place(x=580, y=650)
        
        self.ja_segundo.mainloop()

#----------------------------------------------------------------------------------ESCOLHA DE PERSONAGEM--------------------------------------------------------------------------------------------------------------------

    def primeira_fase(self):
        
        for widget in self.ja_segundo.winfo_children():
            widget.destroy()
            
        imagem_inicio = ImageTk.PhotoImage(file="sala1.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        can.pack(fill="both", expand=True)
        draw_outlined_text(can, 640, 420, text="Escolha com qual personagem deseja jogar", font=("Bernard MT Condensed", 25), fill_color="white", outline_color="black", outline_width=4)
        
        draw_outlined_text(can, 650, 50, "Jorge Bittencourt", font=("Bernard MT Condensed", 25), fill_color="white", outline_color="black", outline_width=4) #Jorge
        
        draw_outlined_text(can, 140, 300, "Dilma Rouseff", font=("Bernard MT Condensed", 25), fill_color="white", outline_color="black", outline_width=4) #Dilma
        
        draw_outlined_text(can, 1100, 300, "Carioca", font=("Bernard MT Condensed", 25), fill_color="white", outline_color="black", outline_width=4) #Carioca
        
        haha1 = ctk.CTkImage(light_image=Image.open("cariocateste.png"), dark_image=Image.open("cariocateste.png"), size=(250, 150))
        haha2 = ctk.CTkImage(light_image=Image.open("dilmateste.jpeg"), dark_image=Image.open("dilmateste.jpeg"), size=(250, 150))
        haha3 = ctk.CTkImage(light_image=Image.open("jorgecerto.jpeg"), dark_image=Image.open("jorgecerto.jpeg"), size=(250, 150))

        self.botao_21 = ctk.CTkButton(self.ja_segundo, text="", image=haha1, width=250, height=150, hover_color="gray", text_color="black", fg_color="white", corner_radius=0, font=("Arial", 30), command=self.carioca01_00)  #colocar a def do carioca
        self.botao_21.place(x=990, y=330) #Carioca
        
        self.botao_22 = ctk.CTkButton(self.ja_segundo, text="", image=haha2, width=250, height=150, hover_color="gray", text_color="black", fg_color="white", corner_radius=0, font=("Arial", 30), command=self.Dilma01_01) #colocar a def da Dilma
        self.botao_22.place(x=30, y=330) #Dilma
        
        self.botao_23 = ctk.CTkButton(self.ja_segundo, text="", image=haha3, width=250, height=150, hover_color="gray", text_color="black", fg_color="white", corner_radius=0, font=("Arial", 30), command=self.jorge01_01)
        self.botao_23.place(x=520, y=80) #Jorge
        
        self.ja_segundo.mainloop()
        
#----------------------------------------------------------------------------------JORGE----------------------------------------------------------

#----------------------------------------------------------------------------------INICIO PRIMEIRA FASE--------------------------------------------------------------------------------------------------------------------

    def jorge01_01(self):         #TELA QUE MOSTRA A PRIMEIRA "QUEST" DO PERSONAGEM
        for widget in self.ja_segundo.winfo_children():
            widget.destroy()
        
        imagem_inicio = ImageTk.PhotoImage(file="salãonovo.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        can.pack(fill="both", expand=True)
        
        draw_outlined_text(can, 640, 70, text="1º fase:", font=("Bernard MT Condensed", 30), fill_color="white", outline_color="black", outline_width=4)
        
        textao2 = """
    Jorge, finalmente estava no salão da mansão. Ele não sabia como tinha chegado ali, 
    mas a ameaça iminente era quase certa: 
    algo monstruoso o perseguia, e ele tinha que encontrar uma maneira de escapar. 
    Um gramado alto e mal iluminado se estendia à sua frente, 
    e o som das criaturas malditas ecoava pela imensa escuridão.

    Ele saiu apressadamente e deu de cara com uma porta, que tinha o levava para uma 
    sala com uma caixa no centro, ao chegar mais perto da caixa a porta se tranta automaticamente.
    Vendo atentamente a caixa jorge percebe uma escrita estranha e uma especie de mensagem 
    em um dos cantos da caixa, como se fosse escrito para ele:

    "Para abrir esta caixa, complete a tabela verdade para a expressão lógica: (A ∧ B) ∨ ¬C."

    Jorge respirou fundo. Ele tinha aprendido sobre lógica proposicional durante as aulas do Dani 
    e agora teria que usar esse conhecimento para sobreviver. A expressão parecia simples, mas 
    cada detalhe era crucial.
        """
        
        draw_outlined_text(can, 650, 400, text=textao2, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)

        botao_prox12 = ctk.CTkButton(self.ja_segundo, text="Responder", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.jorge01_02)
        botao_prox12.place(x=1080, y=650)
        
        self.ja_segundo.mainloop()

    def jorge01_02(self):    #TELA QUE MOSTRA A GAMA DE OPCOES DO PERSONAGEM
        for widget in self.ja_segundo.winfo_children():
            widget.destroy()
        
        self.choices = ["0 | 1 | 1 | 0 | 1 | 0 | 0 | 1", "1 | 0 | 1 | 0 | 1 | 0 | 1 | 1", "1 | 0 | 1 | 1 | 0 | 0 | 1 | 1", "0 | 0 | 1 | 0 | 1 | 0 | 1 | 1"]
        
        self.escolhas = random.sample(self.choices, 4)
        
        self.esc_titulo = ctk.CTkLabel(self.ja_segundo, text="Escolha a sequência correta!", width=200, height=100,font=("Arial", 80))
        self.esc_titulo.place(x=130, y=50)
        
        self.vencedor = "1 | 0 | 1 | 0 | 1 | 0 | 1 | 1"
        
        self.bt1 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhas[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge1(self.escolhas[0]))
        self.bt1.place(x = 290, y = 570)
        
        self.bt2 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhas[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge1(self.escolhas[1]))
        self.bt2.place(x = 290, y = 650)
        
        self.bt3 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhas[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge1(self.escolhas[2]))
        self.bt3.place(x = 650, y = 570)
        
        self.bt4 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhas[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge1(self.escolhas[3]))
        self.bt4.place(x = 650, y = 650)
        
        self.img_fundo4 = ctk.CTkImage(light_image=Image.open("tabela1.jpg"), dark_image=Image.open("tabela1.jpg"), size=(860, 350))
        self.image_label4 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo4, text="")
        self.image_label4.place(x=200, y=180)
        
        self.ja_segundo.mainloop()
        
    def verifica_jorge1(self, texto_botao): #VERIFICA SE O PERSONAGEM GANHOU OU NAO
        if texto_botao == self.vencedor:  #TELA - CASO O PERSONAGEM TENHA ACERTADO
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="portanova.png")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            draw_outlined_text(can, 640, 70, text="2º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            self.bt_prox = ctk.CTkButton(self.ja_segundo, text="Proxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.jorge02_01)
            self.bt_prox.place(x=1100, y=650)
        
            textao4 = """
Jorge conseguiu o primeiro desafio e viu um medalhão, ao olhar atentamente para a mesa embaixo
da caixa, descobre uma escotilha com o mesmo formato do medalhão, som das garras do monstro 
ecoava atrás da escotilha, e o tempo estava se esgotando, pois sofia estava quase morta. 
Seu coração batia forte, mas ele sabia que precisava manter a calma para superar os desafios que 
viriam. Enquanto corria, avistou uma porta grande, desta vez com um enigma ainda mais complexo.
Na porta estava escrito:

"Complete a tabela verdade para: (A ∨ ¬B) ∧ (¬A ∨ C)."

Jorge se aproximou e viu uma tabela verdade parcialmente preenchida. Ele sabia que precisava
resolver para cada combinação de A, B, e C:
        """
        
            draw_outlined_text(can, 640, 350, text=textao4, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            self.ja_segundo.mainloop()
        else:  #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO   
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio23 = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio23, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Jorge, um bravo guerreiro", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text4 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text4.place(x=78, y=225)
            
            textao3 = """Jorge começou a preencher a tabela, mas suas mãos tremiam tanto que ele hesitou. O suor escorria por seu rosto enquanto ele digitava a última combinação de valores. A lógica, que sempre havia sido seu refúgio, agora parecia escorregar por entre seus dedos. Ele apertou o botão para submeter a resposta.

Por um breve momento, nada aconteceu. O silêncio tomou conta do corredor, exceto pela aproximação constante da fera. Lucas olhou desesperado para o painel, esperando ver a porta se abrir. Mas então, um som frio e metálico ecoou:

SEQUENCIA ERRADA!.

Lucas congelou.

O monstro estava ali, na escuridão atrás dele. Antes que pudesse reagir, sentiu as garras rasgando sua pele. O grito de dor preencheu o ar enquanto o monstro o arrastava para a escuridão. A luz do painel piscou uma última vez, apagando-se enquanto Lucas desaparecia para sempre nas profundezas do abismo.

O labirinto, cruel e implacável, ficaria esperando por sua próxima vítima."""
            
            self.text4.insert("0.0", textao3)
            self.text4.configure(state="disable")
            
            self.ja_segundo.mainloop()

#----------------------------------------------------------------------------------FIM PRIMEIRA FASE--------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------INICIO SEGUNDA FASE--------------------------------------------------------------------------------------------------------------------

    def jorge02_01(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
        
        esc_titulo12 = ctk.CTkLabel(self.ja_segundo, text="Seja sabio, Jorge", width=200, height=100,font=("Arial", 80))
        esc_titulo12.place(x=350, y=50)
        
        self.choices2 = ["0 | 1 | 1 | 0 | 1 | 0 | 0 | 1", "1 | 1 | 0 | 0 | 0 | 1 | 0 | 1", "1 | 0 | 1 | 1 | 0 | 0 | 1 | 1", "0 | 0 | 1 | 0 | 1 | 0 | 1 | 1"]
        
        self.escolhas2 = random.sample(self.choices2, 4)
        
        self.vencedor2 = "1 | 1 | 0 | 0 | 0 | 1 | 0 | 1"
        
        self.bt12 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhas2[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge2(self.escolhas2[0]))
        self.bt12.place(x = 290, y = 570)
        
        self.bt22 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhas2[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge2(self.escolhas2[1]))
        self.bt22.place(x = 290, y = 650)
        
        self.bt32 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhas2[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge2(self.escolhas2[2]))
        self.bt32.place(x = 650, y = 570)
        
        self.bt42 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhas2[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_jorge2(self.escolhas2[3]))
        self.bt42.place(x = 650, y = 650)
        
        self.img_fundo5 = ctk.CTkImage(light_image=Image.open("tabela2.jpg"), dark_image=Image.open("tabela2.jpg"), size=(860, 350))
        self.image_label5 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo5, text="")
        self.image_label5.place(x=200, y=180)
        
        self.ja_segundo.mainloop()
        
        
    def verifica_jorge2(self, botao_texto):      #VERIFICA SE O PERSONAGEM GANHOU OU NAO
        if botao_texto == self.vencedor2:    #TELA - CASO O PERSONAGEM TENHA ACERTADO
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="porão.jpeg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            #can.create_text(640, 50, text="Voce esta fugindo, por enquanto...", font=("Arial", 50), fill="white")
            draw_outlined_text(can, 640, 70, text="3    º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            self.bt_prox = ctk.CTkButton(self.ja_segundo, text="Proxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.jorge02_02)
            self.bt_prox.place(x=1100, y=650)
        
            textao4 = """
Essa era a tao esperada hora, finalmente a ele conseguiu achar o quarto onde Sofia
estava trancada. Quando jorge chegou perto da porta do quarto, ainda conseguiu ouvir
os gemidos aguniantes de Sofia, dando seus ultimos suspiros de vida. Ele, entao, sabia
que deveria agir de forma rapida e agil, se quisesse encontra-la ainda com vida.
Jorge entao abriu a ultima carta, da ultima porta, e nela estava escrito:

"Resolva: (P∨Q)∧(¬P∨Q)"

Ele sabia, que aquele era o momento, o resumo de toda sua historia e carreira. Sofia
seria finalmente salva ou ela morreria ali mesmo, e se tornaria mais uma criatura
das sombras?
        """
        
            draw_outlined_text(can, 650, 400, text=textao4, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            self.ja_segundo.mainloop()
        else:   #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO
            
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Jorge, um bravo guerreiro", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text42 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text42.place(x=78, y=225)
            
            textao32 = """Jorge começou a preencher a tabela, mas suas mãos tremiam tanto que ele hesitou. O suor escorria por seu rosto enquanto ele digitava a última combinação de valores. A lógica, que sempre havia sido seu refúgio, agora parecia escorregar por entre seus dedos. Ele apertou o botão para submeter a resposta.

Por um breve momento, nada aconteceu. O silêncio tomou conta do corredor, exceto pela aproximação constante da fera. Lucas olhou desesperado para o painel, esperando ver a porta se abrir. Mas então, um som frio e metálico ecoou:

SEQUENCIA ERRADA!.

Lucas congelou.

O monstro estava ali, na escuridão atrás dele. Antes que pudesse reagir, sentiu as garras rasgando sua pele. O grito de dor preencheu o ar enquanto o monstro o arrastava para a escuridão. A luz do painel piscou uma última vez, apagando-se enquanto Lucas desaparecia para sempre nas profundezas do abismo.

O labirinto, cruel e implacável, ficaria esperando por sua próxima vítima."""
            
            self.text42.insert("0.0", textao32)
            self.text42.configure(state="disable")
            
            self.ja_segundo.mainloop()
            
    def jorge02_02(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
        
        esc_titulo12 = ctk.CTkLabel(self.ja_segundo, text="Qual sequencia completa a ultima coluna?", width=200, height=100,font=("Arial", 50))
        esc_titulo12.place(x=170, y=50)
        
        self.choices22 = ["0 | 1 | 1 | 0", "1 | 1 | 0 | 0", "1 | 0 | 1 | 0", "0 | 0 | 1 | 0"]
        
        self.escolhas22 = random.sample(self.choices22, 4)
        
        self.vencedor22 = "1 | 0 | 1 | 0"
        
        self.bt122 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhas22[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_jorge3(self.escolhas22[0]))
        self.bt122.place(x = 330, y = 570)
        
        self.bt222 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhas22[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_jorge3(self.escolhas22[1]))
        self.bt222.place(x = 330, y = 650)
        
        self.bt322 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhas22[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_jorge3(self.escolhas22[2]))
        self.bt322.place(x = 700, y = 570)
        
        self.bt422 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhas22[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_jorge3(self.escolhas22[3]))
        self.bt422.place(x = 700, y = 650)
        
        self.img_fundo52 = ctk.CTkImage(light_image=Image.open("tabel3.png"), dark_image=Image.open("tabel3.png"), size=(860, 350))
        self.image_label52 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo52, text="")
        self.image_label52.place(x=200, y=180)
        
        self.ja_segundo.mainloop()
        
    def verifica_jorge3(self, botao_texto):
        if botao_texto == self.vencedor22:
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="porão.jpeg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            draw_outlined_text(can, 640, 70, text="Finalmente...", font=("Bernard MT Condensed",50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
        
            textao4 = """
Jorge ao abrir a porta se depara com uma escada para o porão e paulatinamente desce as escadas,
degrau por degrau,a cada passo o ar parecia cada vez faltar mais. Ao chegar na porta no fim 
da escada Jorge respira fundo e abre a porta, ao abrir ele se depara com Sofia encima de um altar, 
Dilma e Matheus enforcados, sem seus olhos, e a criatura em forma de homem com olhos brancos.
Uma voz ecoa sobre o local: "Jorge , existe algo pior doque a dor e a morte? Tudo tem sido tão leve
até aqui, até mesmo aqueles que morreram não poderiam ter sido salvos por você, ou poderia? 
Você não tem culpa doque aconteceu até agora, ou tem? O que poderia ser pior doque a dor e a morte 
cada vez mais perto? A história só esta começando, você só estava vindo atrás de uma agente perdida. 
Não é? Será o desespero eterno? A solidão fria? O que é pior doque a dor e a morte? aaah, entendi, 
você é o mais forte, não importa o desafio, né? Você eventualmente vai conseguir superar, 
você nunca estará sozinho enquanto estiver aqui. Você está pronto para entender o que é pior do que
a dor e a morte? Você vai querer morrer, vai querer sofrer e você não vai ter nenhuma dessas coisas,
por que eu estou aqui."
        """
        
            draw_outlined_text(can, 650, 400, text=textao4, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            boltin = ctk.CTkButton(self.ja_segundo, text="Proximo", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=self.primeira_fase)
            boltin.place(x = 1100, y = 640)
            
            self.ja_segundo.mainloop()
        else:
            
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Jorge, um bravo guerreiro", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text42 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text42.place(x=78, y=225)
            
            textao32 = """Jorge começou a preencher a tabela, mas suas mãos tremiam tanto que ele hesitou. O suor escorria por seu rosto enquanto ele digitava a última combinação de valores. A lógica, que sempre havia sido seu refúgio, agora parecia escorregar por entre seus dedos. Ele apertou o botão para submeter a resposta.

Por um breve momento, nada aconteceu. O silêncio tomou conta do corredor, exceto pela aproximação constante da fera. Lucas olhou desesperado para o painel, esperando ver a porta se abrir. Mas então, um som frio e metálico ecoou:

SEQUENCIA ERRADA!.

Jorge congelou.

O monstro estava ali, na escuridão atrás dele. Antes que pudesse reagir, sentiu as garras rasgando sua pele. O grito de dor preencheu o ar enquanto o monstro o arrastava para a escuridão. A luz do painel piscou uma última vez, apagando-se enquanto Lucas desaparecia para sempre nas profundezas do abismo.

O labirinto, cruel e implacável, ficaria esperando por sua próxima vítima."""
            
            self.text42.insert("0.0", textao32)
            self.text42.configure(state="disable")
            
            self.ja_segundo.mainloop()

    def volta_volta(self):
        self.haha.destroy()
        self.primeira_fase()

#----------------------------------------------------------------------------------FIM PRIMEIRA FASE--------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------DILMA--------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------INICIO PRIMEIRA FASE---------------------------------------------------------------------------------------------------------

    def Dilma01_01(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
        
        imagem_inicio = ImageTk.PhotoImage(file="bibliotecanova.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        can.pack(fill="both", expand=True)
            
        draw_outlined_text(can, 640, 70, text="1º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
        
        TextoD1 = """
        Dilma foi enviada para investigar a biblioteca da mansão, um lugar antigo,
    com livros empoeirados, móveis pesados, e um grande candelabro que ilumina fracamente
    o ambiente. Ao entrar, Dilma derruba acidentalmente uma pilha de livros antigos,
    revelando uma passagem secreta que estava escondida sob as prateleiras. Sem perceber
    o que fez, ela decide ignorar a passagem e seguir vasculhando, tropeçando em um tapete e quase
    derrubando o candelabro, mas ao cair percebe uma espécie de puzzle com alguns botões embaixo.


    "Para resolver o puzzle, complete a tabela verdade para a expressão lógica: (P∨Q)∧¬Q."

    Dilma começou a pensar muito como resolver o puzzle, e tentou lembra
    dos ensinamentos de Dani, porem não conseguiu por ficar pensando em como
    plantar mandioca ao invés de prestar atenção nos ensinamentos de Dani,
    então decidiu ir no chute.
            """
        draw_outlined_text(can, 650, 400, text=TextoD1, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)

        botao_prox12 = ctk.CTkButton(self.ja_segundo, text="Responder", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.Dilma01_02)
        botao_prox12.place(x=1080, y=650)
            
        self.ja_segundo.mainloop()
    def Dilma01_02(self):    #TELA QUE MOSTRA A GAMA DE OPCOES DO PERSONAGEM
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
            self.op1 = ["1 | 1 | 0 | 0 ", "0 | 1 | 0 | 1 ", "0 | 0 | 1 | 1 ", "1 | 0 | 0 | 1 "]
            
            self.operacoes_1 = random.sample(self.op1, 4)
            
            self.op1_t1 = ctk.CTkLabel(self.ja_segundo, text="Escolha a sequência correta!", width=200, height=100,font=("Arial", 80))
            self.op1_t1.place(x=130, y=50)
            
            self.v_1 = "0 | 1 | 0 | 1 "
            
            self.bot1 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.operacoes_1[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_dilma1(self.operacoes_1[0]))
            self.bot1.place(x = 290, y = 570)
            
            self.bot2 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.operacoes_1[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_dilma1(self.operacoes_1[1]))
            self.bot2.place(x = 290, y = 650)
            
            self.bot3 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.operacoes_1[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_dilma1(self.operacoes_1[2]))
            self.bot3.place(x = 650, y = 570)
            
            self.bot4 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.operacoes_1[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_dilma1(self.operacoes_1[3]))
            self.bot4.place(x = 650, y = 650)
            
            self.fundo_1 = ctk.CTkImage(light_image=Image.open("ex1.png"), dark_image=Image.open("ex1.png"), size=(860, 350))
            self.imagem_l1 = ctk.CTkLabel(self.ja_segundo, image=self.fundo_1, text="")
            self.imagem_l1.place(x=200, y=180)
            self.ja_segundo.mainloop()
        
    def verifica_dilma1(self, texto_botao): #VERIFICA SE O PERSONAGEM GANHOU OU NAO
        if texto_botao == self.v_1:  #TELA - CASO O PERSONAGEM TENHA ACERTADO
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="pasecreta.png")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            draw_outlined_text(can, 640, 70, text="2º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            self.btD1_prox = ctk.CTkButton(self.ja_segundo, text="Proxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.Dilma02_01)
            self.btD1_prox.place(x=1100, y=650)
            
            TextoD2 = """
            Resolvendo o problema por pura sorte e apertando o botão correto
            Dilma abre uma passagem secreta na biblioteca, indo então em direção 
            a passagem secreta Dilma se depara com uma sala muito diferente da biblioteca 
            e com uma estante dourada com livros com símbolos semelhantes ao puzzle anterior,
            e como Dilma é pilantra ela vai correndo em direção a estante para resolver o problema
            na esperança de achar algo de valor.
            
            "Para resolver o problema diga qual é a ordem certa de livros na estante
            de acordo com os símbolos na estante: (P∧Q)∨¬R "
            
            """
            draw_outlined_text(can, 650, 400, text=TextoD2, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
                
            self.ja_segundo.mainloop()
        else:  #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO
            
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1)
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Dilma,a pilantra ", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            text42 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            text42.place(x=78, y=225)
            
            TextoD3 = """
            Dilma tentou chutar a resposta mas Dilma não deveria ter sido
            tão ignorante em relação as aulas de dani, e agora pagara o preço.
            Errando as sequências de botões a biblioteca se tranca completamente e começa 
            a sair das prateliras infinitas carteiras de trabalhos fazendo Dilma 
            ter um ataque cardíaco por conta de ter medo de trabalhar.
            
            Descanse em paz Dilma.
            Já vai tarde. """
            

            text42.insert("0.0", TextoD3)
            text42.configure(state="disable")
            
            self.ja_segundo.mainloop()

#-------------------------------------------------------------------------------------------INICIO SEGUNDA FASE---------------------------------------------------------------------------------------------------------

    def Dilma02_01(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
        
        titulo_pergunta2 = ctk.CTkLabel(self.ja_segundo, text="Boa sorte, Dilma", width=200, height=100, font=("Arial", 80))
        titulo_pergunta2.place(x=350, y=50)
        
        self.opcoes_resposta2 = ["1 | 1 | 0 | 1 | 0 | 1 | 0 | 1", "1 | 0 | 1 | 1 | 0 | 1 | 0 | 0", "0 | 1 | 1 | 0 | 1 | 0 | 1 | 1", "1 | 1 | 1 | 0 | 0 | 0 | 1 | 1"]
        self.escolhas_aleatorias2 = random.sample(self.opcoes_resposta2, 4)
        
        self.resposta_correta2 = "1 | 1 | 0 | 1 | 0 | 1 | 0 | 1"
        
        self.botao_opcao_A = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhas_aleatorias2[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor="w", font=("Arial", 25), command=lambda: self.verifica_Dilma2(self.escolhas_aleatorias2[0]))
        self.botao_opcao_A.place(x=290, y=570)
        
        self.botao_opcao_B = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhas_aleatorias2[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor="w", font=("Arial", 25), command=lambda: self.verifica_Dilma2(self.escolhas_aleatorias2[1]))
        self.botao_opcao_B.place(x=290, y=650)
        
        self.botao_opcao_C = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhas_aleatorias2[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor="w", font=("Arial", 25), command=lambda: self.verifica_Dilma2(self.escolhas_aleatorias2[2]))
        self.botao_opcao_C.place(x=650, y=570)
        
        self.botao_opcao_D = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhas_aleatorias2[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor="w", font=("Arial", 25), command=lambda: self.verifica_Dilma2(self.escolhas_aleatorias2[3]))
        self.botao_opcao_D.place(x=650, y=650)
        
        self.img_fundo_pergunta2 = ctk.CTkImage(light_image=Image.open("ex2.png"), dark_image=Image.open("ex2.png"), size=(860, 350))
        self.label_imagem_pergunta2 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo_pergunta2, text="")
        self.label_imagem_pergunta2.place(x=200, y=180)
        
        self.ja_segundo.mainloop()
            
    def verifica_Dilma2(self, botao_texto):  # VERIFICA SE O PERSONAGEM GANHOU OU NÃO
        if botao_texto == self.resposta_correta2:  # TELA - CASO O PERSONAGEM TENHA ACERTADO
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_fundo = ImageTk.PhotoImage(file="biblioteca2.png")
            canvas = Canvas(self.ja_segundo, width=1280, height=720)
            canvas.create_image(0, 0, image=imagem_fundo, anchor=NW)
            draw_outlined_text(canvas, 640, 70, text="3ª fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            canvas.pack(fill="both", expand=True)
            self.botao_proxima_fase = ctk.CTkButton(self.ja_segundo, text="Próxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.Dilma02_03)
            self.botao_proxima_fase.place(x=1100, y=650)
            
            TextoD4="""
            Enquanto ela mexia nos livros, uma figura misteriosa
            começa a se formar atrás dela. Mas como coisa ruim não dura pouco
            Dilma, completamente inconsciente do perigo
            vira de costas e espirra tão alto que a entidade se dispersa momentaneamente.
            Ela então encontra uma chave misteriosa dentro de um dos livros chamado 
            Voynich, acreditando ser uma pista,coloca no bolso. 
            Na verdade, essa chave é crucial para o funcionamento do "Elemento Nulo"
            
            Por um momento Dilma esquece que está em uma missão e decide ir embora 
            pois esqueceu de saudar a mandioca e o milho
            esse dia ao tentar sair da biblioteca todas as portas se fecham e
            uma daquelas tarefas aparece no meio do cômodo: P∨(Q∧¬R)                                             
            """
            
            draw_outlined_text(canvas, 650, 400, text=TextoD4, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            self.ja_segundo.mainloop()
        
        else:  #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO
            
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1)
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Dilma,a pilantra ", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text421 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text421.place(x=78, y=225)
            
            TextoD3 = """
        Dilma tentou chutar a resposta mas Dilma não deveria ter sido
        tão ignorante em relação as aulas de dani, e agora pagara o preço.
        Errando as sequências de botões a biblioteca se tranca completamente e começa 
        a sair das prateliras infinitas carteiras de trabalhos fazendo Dilma 
        ter um ataque cardíaco por conta de ter medo de trabalhar.
        
        Descanse em paz Dilma.
        Já vai tarde. """
            

            self.text421.insert("0.0", TextoD3)
            self.text421.configure(state="disable")
            
            self.ja_segundo.mainloop()
            
    def Dilma02_03(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()

        titulo_questao_pergunta = ctk.CTkLabel(self.ja_segundo, text="Qual sequencia completa a ultima coluna?", width=200, height=100, font=("Arial", 50))
        titulo_questao_pergunta.place(x=170, y=50)

        opcoes_respostas_disponiveis = ["1 | 1 | 1 | 1 | 1 | 1 | 0 | 1", "1 | 1 | 0 | 1 | 0 | 1 | 0 | 1", "1 | 1 | 1 | 1 | 1 | 0 | 0 | 1", "1 | 0 | 1 | 1 | 0 | 0 | 0 | 1"]

        respostas_selecionadas = random.sample(opcoes_respostas_disponiveis, 4)

        self.vencedor225 = "1 | 1 | 1 | 1 | 1 | 0 | 0 | 1"

        botao_opcao_a = ctk.CTkButton(self.ja_segundo, text=f"A) {respostas_selecionadas[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_Dilma3(respostas_selecionadas[0]))
        botao_opcao_a.place(x=330, y=570)

        botao_opcao_b = ctk.CTkButton(self.ja_segundo, text=f"B) {respostas_selecionadas[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_Dilma3(respostas_selecionadas[1]))
        botao_opcao_b.place(x=330, y=650)

        botao_opcao_c = ctk.CTkButton(self.ja_segundo, text=f"C) {respostas_selecionadas[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_Dilma3(respostas_selecionadas[2]))
        botao_opcao_c.place(x=700, y=570)

        botao_opcao_d = ctk.CTkButton(self.ja_segundo, text=f"D) {respostas_selecionadas[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_Dilma3(respostas_selecionadas[3]))
        botao_opcao_d.place(x=700, y=650)

        imagem_de_fundo = ctk.CTkImage(light_image=Image.open("ex3.png"), dark_image=Image.open("ex3.png"), size=(860, 350))
        label_da_imagem_fundo = ctk.CTkLabel(self.ja_segundo, image=imagem_de_fundo, text="")
        label_da_imagem_fundo.place(x=200, y=180)

        self.ja_segundo.mainloop()
        
    def verifica_Dilma3(self, botao_texto):
        if botao_texto == self.vencedor225:
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
        
            imagem_de_fundo = ImageTk.PhotoImage(file="biblioteca2.png")
            canvas_desenho = Canvas(self.ja_segundo, width=1280, height=720)
        
            draw_outlined_text(canvas_desenho, 640, 70, text="Finalmente...", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
        
            canvas_desenho.pack(fill="both", expand=True)

                
            TextoDf="""
            Pouco depois, as luzes da biblioteca começam a piscar, e as estantes de
            livros se fecham rapidamente ao redor dela.Dilma tenta escapar, mas o chão cede 
            e ela cai em um poço escuro, desaparecendo para sempre, sem que ninguém
            saiba o que realmente aconteceu com ela.
            
            """
            draw_outlined_text(canvas_desenho, 650, 400, text=TextoDf, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            boltin = ctk.CTkButton(self.ja_segundo, text="Proximo", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=self.primeira_fase)
            boltin.place(x = 1100, y = 640)
            
            self.ja_segundo.mainloop()
        else:
            
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1)
            
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Dilma,a pilantra ", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text4212 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text42.place(x=78, y=225)
            
            TextoD3 = """
            Dilma tentou chutar a resposta mas Dilma não deveria ter sido
            tão ignorante em relação as aulas de dani, e agora pagara o preço.
            Errando as sequências de botões a biblioteca se tranca completamente e começa 
            a sair das prateliras infinitas carteiras de trabalhos fazendo Dilma 
            ter um ataque cardíaco por conta de ter medo de trabalhar.
        
            Descanse em paz Dilma.
            Já vai tarde. """
            

            self.text4212.insert("0.0", TextoD3)
            self.text4212.configure(state="disable")
            
            self.ja_segundo.mainloop()
    
#----------------------------------------------------------------CARIOCA----------------------------------------------------------------------------

#-------------------------------------------------------------------PRIMEIRA FASE------------------------------------------------------------------

    def carioca01_00(self):         
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
        imagem_inicio = ImageTk.PhotoImage(file="quartodopanico.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        can.pack(fill="both", expand=True)
            
        draw_outlined_text(can, 640, 70, text="Introdução", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
        textaocarioca = """
Matheus carioca é designado para investigar um cômodo selado, uma espécie de “quarto do pânico”
escondido na mansão. Ao adentrar o espaço, ele nota que o ambiente é antigo, com mobiliário pesado
e paredes acolchoadas, como se fosse um local de contenção mental. 
Contudo, seu instinto lhe diz que há algo mais ali, algo que não pode ser visto com os olhos comuns. 
É então que ele decide usar uma de suas invenções: 
A Juditi, seu binóculo. Esse binóculo é capaz de enxergar o que o olho humano não consegue perceber.
Com a Juditi, Matheus vê um lado oculto da realidade. As paredes acolchoadas estão cobertas
de desenhos macabros de olhos que o observam, pintados com sangue e tinta, e frases escritas em uma 
língua morta aparecem e desaparecem na escuridão, como se fossem sussurros visuais.
Alguns dos dizeres falam do “Elemento Nulo” e do destino cruel daqueles que o procuram. 
Enquanto investiga com o binóculo, ele percebe que os desenhos e símbolos não são apenas decorações,
mas parte de um antigo ritual para aprisionar a entidade que domina a mansão. 
Ele se dá conta de que algo muito maior está em jogo. E então ele se depara com 3 símbolos nos quais
ele já tinha visto uma vez, parecia familiar.
        """   
        draw_outlined_text(can, 650, 400, text=textaocarioca, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)  
        botao_avancar = ctk.CTkButton(self.ja_segundo, text="Avançar", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.carioca01_01)
        botao_avancar.place(x=1080, y=650)
            
        self.ja_segundo.mainloop()
        
    def carioca01_01(self):         
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
        imagem_inicio = ImageTk.PhotoImage(file="quartodopanico.png")

        can = Canvas(self.ja_segundo, width=1280, height=720)
        can.create_image(0, 0, image=imagem_inicio, anchor=NW)
        can.pack(fill="both", expand=True)
            
        draw_outlined_text(can, 640, 70, text="1º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
        textaocarioca1 = """
        Matheus se depara com três símbolos enigmáticos gravados na parede. 
        Ele reconhece os símbolos de suas pesquisas anteriores sobre cultos antigos e artefatos místicos.
        Cada símbolo possui um significado profundo e uma história única: 
        Símbolo da Serpente(S): Representa o conhecimento proibido. Símbolo do Círculo com Triângulo(C):
        Significa proteção e equilíbrio. Símbolo do Olho(O): Representa a vigilância eterna.
        Matheus sabe que, para desvendar o mistério dos símbolos e liberar o caminho à frente,
        ele deve resolver um enigma baseado em lógica. Os símbolos formam uma combinação que se traduz 
        em uma expressão lógica complexa. Matheus decide utilizar uma tabela verdade para solucionar
        o enigma. A expressão lógica é dada como:((S v C ^ O) <-> (¬C ^ S))
        """
        draw_outlined_text(can, 605, 400, text=textaocarioca1, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)

        botao_resolucao1 = ctk.CTkButton(self.ja_segundo, text="Responder", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.carioca01_02)
        botao_resolucao1.place(x=1080, y=650)
            
        self.ja_segundo.mainloop()

    def carioca01_02(self):    #TELA QUE MOSTRA A GAMA DE OPCOES DO PERSONAGEM
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
        self.choicescarioca = ["1 | 1 | 0 | 1 | 1 | 0 | 1 | 1", "1 | 0 | 1 | 0 | 0 | 1 | 0 | 1", "1 | 0 | 0 | 1 | 0 | 1 | 1 | 0", "0 | 0 | 1 | 1 | 0 | 1 | 1 | 1"]
            
        self.escolhascarioca = random.sample(self.choicescarioca, 4)
            
        self.esc_titulo = ctk.CTkLabel(self.ja_segundo, text="Escolha a sequência correta!", width=200, height=100,font=("Arial", 80))
        self.esc_titulo.place(x=130, y=50)
            
        self.vencedorcarioca = "0 | 0 | 1 | 1 | 0 | 1 | 1 | 1"
            
        self.btca1 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhascarioca[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca1(self.escolhascarioca[0]))
        self.btca1.place(x = 290, y = 570)
            
        self.btca2 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhascarioca[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca1(self.escolhascarioca[1]))
        self.btca2.place(x = 290, y = 650)
            
        self.btca3 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhascarioca[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca1(self.escolhascarioca[2]))
        self.btca3.place(x = 650, y = 570)
            
        self.btca4 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhascarioca[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca1(self.escolhascarioca[3]))
        self.btca4.place(x = 650, y = 650)
            
        self.img_fundo4 = ctk.CTkImage(light_image=Image.open("tabela1.jpg"), dark_image=Image.open("tabela1.jpg"), size=(860, 350))
        self.image_label4 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo4, text="")
        self.image_label4.place(x=200, y=180)
            
        self.ja_segundo.mainloop()
            
    def verifica_carioca1(self, texto_botao): #VERIFICA SE O PERSONAGEM GANHOU OU NAO
        if texto_botao == self.vencedorcarioca:  #TELA - CASO O PERSONAGEM TENHA ACERTADO
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="quartodopanico.png")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            draw_outlined_text(can, 640, 70, text="2º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            self.bt_prox01 = ctk.CTkButton(self.ja_segundo, text="Proxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.carioca02_01)
            self.bt_prox01.place(x=1100, y=650)
            
            textaocarioca2 = """
            Ao alinhar os símbolos corretamente, ele escuta um suave clique, e uma seção da parede se abre, 
            revelando um corredor oculto. Com a Juditi, Matheus avança, ciente de que cada passo o leva mais 
            perto da verdade oculta na mansão. Matheus avança pelo corredor oculto, sentindo a adrenalina 
            aumentar enquanto cada passo o leva mais fundo no mistério da mansão. A Juditi revela 
            mais segredos ocultos conforme ele explora. Logo, ele chega a outro cômodo, ainda mais antigo
            e repleto de símbolos. Ao entrar, Matheus encontra uma grande balança no centro do cômodo.
            Duas pedras brilhantes, cada uma com um símbolo gravado (um leão e uma balança ).
            Uma inscrição ao lado da balança lê:"A verdade é equilibrada quando o poder (P) e a justiça (J),
            se alinham corretamente. Somente a combinação certa revelará o próximo passo.
            "Determine a resultante da expressão: ((¬P v J)->(J ^ P))<->(¬P ^ ¬J)   
            """
            
            draw_outlined_text(can, 600, 400, text=textaocarioca2, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
                
            self.ja_segundo.mainloop()
        else:  #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO
                
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
                
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio23 = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio23, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Matheus, também conhecido como Carioca baitola", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text4 = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text4.place(x=78, y=225)
                
            textaocarioca33 = """
            Matheus está terminando de preencher a tabela e começa a sentir uma presença se aproximando dele.
            Assustado, ele tenta acelerar o processo de resolução, mas acaba se desconcentrando e sente que havia algo de errado.
            O quarto começa a tremer ele escuta vozes sussurrando ao fundo, mas se recusa a deixar o medo tomar conta. 
            Um altar começa a sair do piso do cômodo "Que isso, irmão, isso aqui não vai me pegar não!", ele murmura.
            Ao olhar próximo do seu pé, ele encontra uma foto do agente desaparecido, mas os olhos da foto começam a sangrar.
            Ele rapidamente guarda a foto, sabendo que algo muito errado está acontecendo. Mas, de repente o ar se torna pesado.
            Uma figura grotesca começa a aparecer no espelho da parede. Matheus, apesar do medo, usa uma cadeira para quebrar o espelho, dissipando temporariamente a criatura.
            Ele sabe que está em uma situação crítica e decide recuar, tentando encontrar os outros, mas inesperadamente a criatura aparece em sua frente, sem chances de escape.
            E em um piscar de olhos, a criatura agarra Matheus pelo pescoço e o atira até a parede. O corpo de Matheus cai imóvel no chão, sem vida.
            Qualquer que fosse o segredo escondido naquele quarto, jamais seria revelado...
            """
                
            self.text4.insert("0.0", textaocarioca33)
            self.text4.configure(state="disable")
                
            self.ja_segundo.mainloop()

    #----------------------------------------------------------------------------------FIM PRIMEIRA FASE--------------------------------------------------------------------------------------------------------------------


    #----------------------------------------------------------------------------------INICIO SEGUNDA FASE--------------------------------------------------------------------------------------------------------------------

    def carioca02_01(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
        esc_titulo12 = ctk.CTkLabel(self.ja_segundo, text="Seja astuto, Carioca", width=200, height=100,font=("Arial", 80))
        esc_titulo12.place(x=350, y=50)
            
        self.choicescarioca2 = ["0 | 0 | 1 | 0", " 1 | 1 | 0 | 1", " 0 | 0 | 1 | 1", "0 | 1 | 0 | 1 "]
            
        self.escolhascarioca2 = random.sample(self.choicescarioca2, 4)
            
        self.vencedorcarioca2 = "0 | 0 | 1 | 0"
            
        self.btca11 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhascarioca2[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca2(self.escolhascarioca2[0]))
        self.btca11.place(x = 290, y = 570)
            
        self.btca22 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhascarioca2[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca2(self.escolhascarioca2[1]))
        self.btca22.place(x = 290, y = 650)
            
        self.btca33 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhascarioca2[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca2(self.escolhascarioca2[2]))
        self.btca33.place(x = 650, y = 570)
            
        self.btca44 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhascarioca2[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 25), command=lambda: self.verifica_carioca2(self.escolhascarioca2[3]))
        self.btca44.place(x = 650, y = 650)
            
        self.img_fundo5 = ctk.CTkImage(light_image=Image.open("tableo.png"), dark_image=Image.open("tableo.png"), size=(860, 350))
        self.image_label5 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo5, text="")
        self.image_label5.place(x=200, y=180)
            
        self.ja_segundo.mainloop()
            
            
    def verifica_carioca2(self, botao_texto):      #VERIFICA SE O PERSONAGEM GANHOU OU NAO #PAREI AQUI!!!!!!!!!!!!
        if botao_texto == self.vencedorcarioca2:    #TELA - CASO O PERSONAGEM TENHA ACERTADO 
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="quartodopanico.png")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="", font=("Arial", 50), fill="white")
            draw_outlined_text(can, 640, 70, text="3    º fase:", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            self.bt_prox02 = ctk.CTkButton(self.ja_segundo, text="Proxima fase", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", bg_color="transparent", corner_radius=28, font=("Arial", 20), command=self.carioca02_02)
            self.bt_prox02.place(x=1100, y=650)
            
            textaocarioca4 = """  
            Matheus ativa as pedras de acordo com o resultado da expressão.
            A balança se equilibra perfeitamente, e um painel na parede desliza para o lado,
            revelando outro corredor. Seguindo pelo corredor,
            Matheus encontra uma sala circular cheia de espelhos. No centro da sala,
            há um pedestal com três cristais: um azul, um vermelho e um amarelo.
            Uma inscrição na parede diz: Para revelar a verdade, 
            a luz deve ser refletida corretamente: Use as cores Azul(A), Branco(B) e Roxo(R)
            para montar a tabela verdade da expressão (A^B)v(¬A^R)      
            """
            
            draw_outlined_text(can, 600, 400, text=textaocarioca4, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
                
            self.ja_segundo.mainloop()
        else:   #TELA - CASO O PERSONAGEM NAO TENHA ACERTADO
                
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
                
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Matheus, um bravo guerreiro", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.textca = ctk.CTkTextbox(self.ja_segundo, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.textca.place(x=78, y=225)
                
            textaocarioca5 = """
            Matheus está terminando de preencher a tabela e começa a sentir uma presença se aproximando dele.
            Assustado, ele tenta acelerar o processo de resolução, mas acaba se desconcentrando e sente que havia algo de errado.
            O quarto começa a tremer ele escuta vozes sussurrando ao fundo, mas se recusa a deixar o medo tomar conta. 
            Um altar começa a sair do piso do cômodo "Que isso, irmão, isso aqui não vai me pegar não!", ele murmura.
            Ao olhar próximo do seu pé, ele encontra uma foto do agente desaparecido, mas os olhos da foto começam a sangrar.
            Ele rapidamente guarda a foto, sabendo que algo muito errado está acontecendo. Mas, de repente o ar se torna pesado.
            Uma figura grotesca começa a aparecer no espelho da parede. Matheus, apesar do medo, usa uma cadeira para quebrar o espelho, dissipando temporariamente a criatura.
            Ele sabe que está em uma situação crítica e decide recuar, tentando encontrar os outros, mas inesperadamente a criatura aparece em sua frente, sem chances de escape.
            E em um piscar de olhos, a criatura agarra Matheus pelo pescoço e o atira até a parede. O corpo de Matheus cai imóvel no chão, sem vida.
            Qualquer que fosse o segredo escondido naquele quarto, jamais seria revelado...
            """        
            self.textca.insert("0.0", textaocarioca5)
            self.textca.configure(state="disable")
                
            self.ja_segundo.mainloop()
                
    def carioca02_02(self):
        for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            
        esc_titulo12 = ctk.CTkLabel(self.ja_segundo, text="Qual sequencia completa a ultima coluna?", width=200, height=100,font=("Arial", 50))
        esc_titulo12.place(x=170, y=50)
            
        self.escolhacarioca3 = ["1 | 1 | 0 | 0 | 1 | 0 | 1 | 0", "1 | 1 | 0 | 0 | 1 | 0 | 1 | 0", "1 | 0 | 0 | 1 | 0 | 1 | 1 | 0", "0 | 0 | 1 | 1 | 0 | 1 | 1 | 1"]
            
        self.escolhascarioca3 = random.sample(self.escolhacarioca3, 4)
            
        self.vencedorcarioca3 = "1 | 1 | 0 | 0 | 1 | 0 | 1 | 0"
            
        self.btca5 = ctk.CTkButton(self.ja_segundo, text=f"A) {self.escolhascarioca3[0]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_carioca3(self.escolhascarioca3[0]))
        self.btca5.place(x = 330, y = 570)
            
        self.btca6 = ctk.CTkButton(self.ja_segundo, text=f"B) {self.escolhascarioca3[1]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_carioca3(self.escolhascarioca3[1]))
        self.btca6.place(x = 330, y = 650)
            
        self.btca7 = ctk.CTkButton(self.ja_segundo, text=f"C) {self.escolhascarioca3[2]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_carioca3(self.escolhascarioca3[2]))
        self.btca7.place(x = 700, y = 570)
            
        self.btca8 = ctk.CTkButton(self.ja_segundo, text=f"D) {self.escolhascarioca3[3]}", width=200, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=lambda: self.verifica_carioca3(self.escolhascarioca3[3]))
        self.btca8.place(x = 700, y = 650)
            
        self.img_fundo52 = ctk.CTkImage(light_image=Image.open("tabel3.png"), dark_image=Image.open("tabel3.png"), size=(860, 350))
        self.image_label52 = ctk.CTkLabel(self.ja_segundo, image=self.img_fundo52, text="")
        self.image_label52.place(x=200, y=180)
            
        self.ja_segundo.mainloop()
            
    def verifica_carioca3(self, botao_texto):
        if botao_texto == self.vencedorcarioca3:
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="porão.jpeg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            draw_outlined_text(can, 640, 70, text="Finalmente...", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
            can.pack(fill="both", expand=True)
            
            textaocarioca6 = """
            A luz reflete nos espelhos, criando um padrão que ilumina uma porta secreta, revelando 
            um novo caminho. Dentro da sala final, Matheus encontra um altar com um livro antigo,
            coberto de poeira e simbolismo arcano. Ele sente uma presença poderosa,
            como se o próprio espaço estivesse observando-o. Ao abrir o livro, ele encontra 
            descrições detalhadas sobre o "Elemento Nulo" e as consequências de sua liberação.
            Matheus percebe que sua missão está longe de terminar. Derrepente, 
            o quarto começa a tremer ele escuta vozes sussurrando ao fundo, mas se recusa a
            deixar o medo tomar conta. Ao olhar próximo do seu pé, ele encontra uma foto do 
            agente desaparecido, mas os olhos da foto começam a sangrar. Ele rapidamente guarda a foto, 
            sabendo que algo muito errado está acontecendo. Mas, de repente o ar se torna pesado. 
            Uma figura grotesca começa a aparecer no espelho da parede. Matheus, apesar do medo,
            usa uma cadeira para quebrar o espelho, dissipando temporariamente a criatura. 
            Ele sabe que está em uma situação crítica e decide recuar, tentando encontrar os outros, 
            mas inesperadamente a criatura aparece em sua frente, sem chances de escape.  

            """
            
            draw_outlined_text(can, 640, 400, text=textaocarioca6, font=("Bernard MT Condensed", 23), fill_color="white", outline_color="black", outline_width=4)
            
            boltin = ctk.CTkButton(self.ja_segundo, text="Proximo", width=100, height=50, fg_color="white", hover_color="gray", text_color="black", anchor=("w"), font=("Arial", 30), command=self.primeira_fase)
            boltin.place(x = 1100, y = 640)
                
            self.ja_segundo.mainloop()
        else:
                
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("fim.mp3")
            pygame.mixer.music.play(loops=-1) 
                
            for widget in self.ja_segundo.winfo_children():
                widget.destroy()
            imagem_inicio = ImageTk.PhotoImage(file="lobin.jpg")
            can = Canvas(self.ja_segundo, width=1280, height=720)
            can.create_image(0, 0, image=imagem_inicio, anchor=NW)
            can.create_text(640, 50, text="Aqui jaz Jorge, um bravo guerreiro", font=("Arial", 50), fill="white")
            can.pack(fill="both", expand=True)
            self.text42 = ctk.CTkTextbox(self.haha, width=1102, height=400, font=("Arial", 20), fg_color="#2B2B2B", border_width=0)
            self.text42.place(x=78, y=225)
                
            textaocarioca7 = """
            Matheus está terminando de preencher a tabela e começa a sentir uma presença se aproximando dele.
            Assustado, ele tenta acelerar o processo de resolução, mas acaba se desconcentrando e sente que havia algo de errado.
            O quarto começa a tremer ele escuta vozes sussurrando ao fundo, mas se recusa a deixar o medo tomar conta. 
            Um altar começa a sair do piso do cômodo "Que isso, irmão, isso aqui não vai me pegar não!", ele murmura.
            Ao olhar próximo do seu pé, ele encontra uma foto do agente desaparecido, mas os olhos da foto começam a sangrar.
            Ele rapidamente guarda a foto, sabendo que algo muito errado está acontecendo. Mas, de repente o ar se torna pesado.
            Uma figura grotesca começa a aparecer no espelho da parede. Matheus, apesar do medo, usa uma cadeira para quebrar o espelho, dissipando temporariamente a criatura.
            Ele sabe que está em uma situação crítica e decide recuar, tentando encontrar os outros, mas inesperadamente a criatura aparece em sua frente, sem chances de escape.
            E em um piscar de olhos, a criatura agarra Matheus pelo pescoço e o atira até a parede. O corpo de Matheus cai imóvel no chão, sem vida.
            Qualquer que fosse o segredo escondido naquele quarto, jamais seria revelado...

    """
                
            self.text42.insert("0.0", textaocarioca7)
            self.text42.configure(state="disable")
                
            self.ja_segundo.mainloop()


#------------------------------------------------------------------------JANELA PRINCIPAL-----------------------------------------------------------------------------

root = ctk.CTk()
root.geometry("1280x720")
root.title("Tela inicial")
root.resizable(True, True)

imagem_inicio = ImageTk.PhotoImage(file="kaka12.png")

can = Canvas(root, width=1280, height=720)
can.create_image(0, 0, image=imagem_inicio, anchor=NW)

draw_outlined_text(can,640, 50, text="A Fera do Cálculo: O Labirinto da Mente", font=("Bernard MT Condensed", 50), fill_color="white", outline_color="black", outline_width=4)
can.pack(fill="both", expand=True)

botao_inicio = ctk.CTkButton(root, text="Iniciar jogo", width=150, height=80, font=("Arial", 25), fg_color="white", hover_color="gray", text_color="black", corner_radius=28, command= lambda: jogo().inicio())
botao_inicio.place(x=580, y=550)

root.mainloop()