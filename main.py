from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import pandas as pd
import tkinter as tk
from PIL import Image, ImageTk
import openpyxl



root= Tk()



class Funcs():
    def limpar(self):
        self.questt.delete(0,END)
        self.tentt.delete(0,END)
        self.respe.delete(0, END)
    def conbancod(self):
        self.conn=sq.connect("envios.bd")
        self.cursor=self.conn.cursor()
    def desconbancod(self):
        self.conn.close()
    def monta(self):
        self.conbancod()
        self.cursor.execute("DROP TABLE IF EXISTS envios;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS envios (
                quest INTEGER,
                tent INTEGER,
                resp REAL,
                feedback CHAR(10),
                score INTEGER
            );
        """)
        self.conn.commit()
        self.desconbancod()
    def enviar(self):
        self.questtex = self.questt.get()
        quest=int(self.questtex)
        self.tenttex = self.tentt.get()
        tent = int(self.tenttex)
        self.resptex = self.respe.get()
        resp=float(self.resptex)

        df = pd.read_excel("respostas.xlsx")
        linha = df[df['quest'] == quest]

        feedback = ""
        score = int()

        if not linha.empty:
            pont = linha['scorei'].values[0]
            respp = linha['resp'].values[0]
            if pont == 3:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=3
                    else:
                        feedback = "incorreto"
                        score=0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score=1
                    else:
                        feedback = "incorreto"
                        score= 0
            elif pont == 4:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=4
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score = 3
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score=1
                    else:
                        feedback = "incorreto"
                        score = 0
            elif pont == 5:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=5
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score = 3
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback == "incorreto"
                        score=0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score=1
                    else:
                        feedback = "incorreto"
                        score = 0
            elif pont == 6:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=6
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score=4
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score = 3
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 4:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score=1
                    else:
                        feedback = "incorreto"
                        score = 0
            elif pont==7:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=7
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score=5
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score = 3
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 4:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score = 1
                    else:
                        feedback = "incorreto"
                        score = 0
            elif pont==8:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score = 8
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score=5
                    else:
                        feedback == "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score = 4
                    else:
                        feedback = "incorreto"
                        score= 0
                elif tent == 4:
                    if resp == respp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto!"
                        score=1
                    else:
                        feedback = "incorreto"
                        score = 0
            elif pont==9:
                if tent == 1:
                    if resp == respp:
                        feedback = "correto!"
                        score=9
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 2:
                    if resp == respp:
                        feedback = "correto!"
                        score=6
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 3:
                    if resp == respp:
                        feedback = "correto!"
                        score=4
                    else:
                        feedback = "incorreto"
                        score = 0
                elif tent == 4:
                    if resp ==resp:
                        feedback = "correto!"
                        score=2
                    else:
                        feedback = "incorreto"
                        score = 0
                else:
                    if resp == respp:
                        feedback = "correto! +1pt"
                        score=1
                    else:
                        feedback = "incorreto"
                        score = 0
        else:
            print("Questão não encontrada")

        print(quest, " ", tent, " ", resp, " ", feedback, " ", score)
        self.conbancod()

        self.cursor.execute("""
            INSERT INTO envios (quest, tent, resp, feedback, score) VALUES (?, ?, ?, ?, ?)
        """, (quest, tent, resp, feedback, score))
        self.conn.commit()

        self.desconbancod()

        self.select()
        self.limpar()
    def select(self):
        self.listaa.delete(*self.listaa.get_children())
        self.conbancod()
        lista=self.cursor.execute("""SELECT quest, tent, feedback FROM envios""")
        for i in lista:
            self.listaa.insert("", END, values=i)
        self.desconbancod()
    def pontuacao(self):
        self.conbancod()
        self.cursor.execute("SELECT SUM(score) AS total_score FROM envios")
        total_score = self.cursor.fetchone()[0]

        msg = f'a pontuação total é {total_score} pontos'

        messagebox.showinfo("Pontuação", msg)

        self.desconbancod()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.interacao()
        self.lista()
        self.root.after(100, self.logo)
        self.monta()
        root.mainloop()
    def tela(self):
        self.root.title("Physics Brawl")
        self.root.configure(background= '#00ae6b')
        self.root.geometry("800x600")
    def frames(self):
        self.framee=Frame(self.root, bd=4, bg='#D3D3D3',  highlightbackground= '#90EE90', highlightthickness=1.5)
        self.framee.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.6)
    def interacao(self):
        self.envio = Button(self.framee, text="Envia", font=('verdana', 8, 'bold'), command=self.enviar)
        self.envio.place(relx=0.2, rely=0.52, relwidth=0.12, relheight=0.1)
        self.pontos=Button(self.framee, text="Mostrar pontuação", font=('verdana', 8, 'bold'), command=self.pontuacao)
        self.pontos.place(relx=0.02, rely=0.80, relwidth=0.30, relheight=0.1)
        self.limpa=Button(self.framee,text="Limpar", font=('verdana', 8, 'bold'), command=self.limpar)
        self.limpa.place(relx=0.2, rely=0.32,relwidth=0.12,relheight=0.1)

        self.lb_1=Label(self.framee, text="Número da questão", font=('verdana', 8, 'bold'))
        self.lb_1.place(relx=0.02,rely=0.05)
        self.lb_2 = Label(self.framee, text="Quantidade de tentativas", font=('verdana', 8, 'bold'))
        self.lb_2.place(relx=0.02, rely=0.25)
        self.lb_3 = Label(self.framee, text="Resposta", font=('verdana', 8, 'bold'))
        self.lb_3.place(relx=0.02, rely=0.45)
        self.lb_4=Label(self.framee,text="Pontuação",font=('verdana', 8, 'bold'))
        self.lb_4.place(relx=0.02, rely=0.73)

        self.questt=Entry(self.framee)
        self.questt.place(relx=0.02, rely=0.12, relwidth=0.16, relheight=0.1)
        self.tentt = Entry(self.framee)
        self.tentt.place(relx=0.02, rely=0.32, relwidth=0.16, relheight=0.1)
        self.respe = Entry(self.framee)
        self.respe.place(relx=0.02, rely=0.52, relwidth=0.16, relheight=0.1)
    def lista(self):
        self.listaa=ttk.Treeview(self.framee, height=3, column=("col1","col2","col3","col4"))
        self.listaa.heading("#0",text=" ")
        self.listaa.heading("#1",text="Número da questão")
        self.listaa.heading("#2", text="Tentativa")
        self.listaa.heading("#3", text="Feedback")

        self.listaa.column("0",width=1)
        self.listaa.column("1", width=83)
        self.listaa.column("2", width=83)
        self.listaa.column("3", width=83)

        self.listaa.place(relx=0.45,rely=0.05,relwidth=0.5,relheight=0.85)

        self.scroll=Scrollbar(self.framee,orient='vertical')
        self.listaa.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=0.94,rely=0.05,relwidth=0.01,relheight=0.85)
    def logo(self):
        pil_image = Image.open("logo.png")
        # Ajuste a largura e altura da label com base na área disponível
        max_width = int(self.root.winfo_width() * 0.6)
        max_height = int(self.root.winfo_height() * 0.1)
        pil_image.thumbnail((max_width, max_height), Image.LANCZOS)

        self.logo_image = ImageTk.PhotoImage(pil_image)

        self.imagem = Label(self.root, image=self.logo_image, bg='#00ae6b')
        self.imagem.place(relx=0.2, rely=0.76, relwidth=0.6, relheight=0.1)

Application()