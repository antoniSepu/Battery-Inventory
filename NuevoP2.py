# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:08:45 2019

@author: AntoniSepu
@keyboard author: Ajinkya Padwad
"""

from GestorBat_1_12 import *

class NuevoP:#hay que conseguir que detecte las baterías que tienen nombre
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entrada = tk.StringVar()
        self.cap = False
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='home.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=12, columnspan=12)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Introduzca un nombre:", bg='white')
        label2.grid(row=1, column=0, padx=10, pady=10, columnspan=15)


        botones = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','BACK',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','ñ','SHIFT',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', 'SPACE',]

        self.entrada = tk.Entry(self.frame, textvariable=self.entrada , width=50)
        self.entrada.grid(row=2,columnspan=15, pady=10)

        varRow = 3
        varColumn = 0

        for button in botones:

            command = lambda x=button: self.select(x)
            if button == "SPACE" or button == "SHIFT" or button == "BACK":
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            else:
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            varColumn +=1

            if varColumn > 10 and varRow == 3:
                varColumn = 0
                varRow+=1
            if varColumn > 10 and varRow == 4:
                varColumn = 0
                varRow+=1
            if varColumn > 10 and varRow == 5:
                varColumn = 0
                varRow+=1

        botonConfirmar = tk.Button(self.frame, text="Confirmar", height=2, bg='white', command=lambda: self.confirm())
        botonConfirmar.grid(row=7, column=0, columnspan=15, pady=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=8, column=0,columnspan=15, pady=2)

        self.frame.pack()

    def select(self, value):
        if value == "BACK":
            self.entrada.delete(len(self.entrada.get())-1, tk.END)
            self.cap = False
        elif value == "SPACE":
            self.entrada.insert(tk.END, ' ')
            self.cap = False
        elif value == "SHIFT":
            self.cap = True
        else:
            if self.cap:
                self.entrada.insert(tk.END,value.upper())
                self.cap = False
            else:
                self.entrada.insert(tk.END,value)
                self.cap = False

    def confirm(self):
        os.chdir(DirDatos)
        log = open('Nombres_Pilotos.txt', 'r+')
        nombres = log.readlines()
        nuevo = self.entrada.get()
        log.write('\n' + nuevo)
        log.close()
        self.master.destroy()
