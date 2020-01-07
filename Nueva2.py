# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:44:31 2019

@author: AntoniSepu
"""

from GestorBat_1_12 import *
import random

class Nueva:#hay que conseguir que detecte las baterías que tienen nombre
    selff = 0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.tipo = ''
        self.numcell = ''
        self.amperios = tk.StringVar()
        self.boton1=[]
        self.boton2=[]

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=10, columnspan=9)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Elegir datos de la nueva batería", bg='white')
        label2.grid(row=0, column=1, padx=150, pady=2, columnspan=6)
        for i in range(len(TechBat)):
            clikado1 = lambda x = i: self.clickTipo(x)
            self.boton1.append(tk.Button(self.frame, text=TechBat[i], height=2, bg='white', command=clikado1))
            self.boton1[i].grid(row=1, column=i + 2, padx=2, pady=2, columnspan=3)
        for i in range(len(NumCell)):
            clikado2 = lambda x = i: self.clickNum(x)
            self.boton2.append(tk.Button(self.frame, text=NumCell[i], height=2, bg='white', command=clikado2))
            self.boton2[i].grid(row=2, column=i+1, padx=2, pady=2)

        label3 = tk.Label(self.frame, text="Capacidad[mAh]:", bg='white')
        label3.grid(row=3, column=2, pady=1, padx=2, columnspan = 3)
        self.entryAmp = tk.Entry(self.frame, textvariable=self.amperios, width=8)
        self.entryAmp.grid(row=3, column=4, pady=2, columnspan=3, stick='w')

        botones = ['7','8','9','4','5','6','1','2','3','DEL','0']

        varRow = 4
        varColumn = 3

        for button in botones:

            command = lambda x=button: self.select(x)
            tk.Button(self.frame,text= button, width=5, height=1, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            varColumn +=1

            if varColumn > 5:
                varColumn = 3
                varRow+=1

        buttonCreate = tk.Button(self.frame, text='Añadir batería', height=2, bg='white', command= lambda: self.anadir(self.tipo, self.numcell, self.amperios))
        buttonCreate.grid(row=varRow + 1, column=1, pady=2, columnspan = 6)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0)
        self.frame.pack()

    def select(self, value):
        if value == "DEL":
            self.entryAmp.delete(len(self.entryAmp.get())-1, tk.END)
        else:
            self.entryAmp.insert(tk.END,value)

    def clickTipo(self, num):
        self.tipo=TechBat[num]
        for i in range(len(TechBat)):
            self.boton1[i].config(bg='white')
        self.boton1[num].config(bg='green')

    def clickNum(self, num):
        self.numcell=NumCell[num]
        for i in range(len(NumCell)):
            self.boton2[i].config(bg='white')
        self.boton2[num].config(bg='green')

    def anadir(self, tipoe, nume, ampe):
        setTipo(tipoe)
        setNumc(nume)
        setAmp(ampe.get())
        Maestra.windowNueva2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Nueva2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tipo = getTipo()
        self.numcell = getNumc()
        self.amperios = getAmp()
        self.etiqueta = self.findName()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.yes = tk.PhotoImage(file='Tick2.gif')
        self.no = tk.PhotoImage(file='Cross2.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=9, columnspan=2)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text='Estos son los datos de la nueva batería:', bg='white')
        label2.grid(row=0, column=0, columnspan=2)
        label3 = tk.Label(self.frame, text='Tipo: ' + self.tipo, bg='white')
        label3.grid(row=1, column=0, columnspan=2)
        label4 = tk.Label(self.frame, text='Celdas: ' + self.numcell, bg='white')
        label4.grid(row=2, column=0, columnspan=2)
        label5 = tk.Label(self.frame, text='Capacidad: ' + self.amperios + '[mAh]', bg='white')
        label5.grid(row=3, column=0, columnspan=2)
        label6 = tk.Label(self.frame, text='Etiqueta: ' + self.etiqueta, bg='white')
        label6.grid(row=4, column=0, columnspan=2)
        label7 = tk.Label(self.frame, text='La etiqueta se genera de manera automática', bg='white')
        label7.grid(row=5, column=0, columnspan=2)
        label8 = tk.Label(self.frame, text='¿Todo correcto?', bg='white')
        label8.grid(row=6, column=0, columnspan=2)
        botonSi = tk.Button(self.frame, image=self.yes, command=lambda: self.clickSi(self.tipo, self.numcell, self.amperios, self.etiqueta))
        botonSi.grid(row=7, column=0, padx=8, stick='e')
        botonAtras = tk.Button(self.frame, image=self.no, command=lambda: self.master.destroy())
        botonAtras.grid(row=7, column=1, padx=8, stick='w')

        self.frame.pack()

    def findName(self):
        hexa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        digitos=[]
        for i in range(4):
            digitos.append(random.choice(hexa))
        nombre = digitos[0] + digitos[1] + digitos[2] + digitos[3]
        return nombre

    def clickSi(self, tipoe, nume, ampe, namee):
        bol = nuevaBateria(tipoe, nume, ampe, namee)
        if bol:
            label8 = tk.Label(self.frame, text="Ya existe una batería con esas características")
            label8.pack()
        else:
            self.master.destroy()
            Nueva.close_windows()
