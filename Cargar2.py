# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:43:02 2019

@author: AntoniSepu
"""

from GestorBat_1_12 import *

class Cargar:
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
        self.archivos = getArchivos()
        self.numero = 0

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=4, columnspan=4)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Elegir batería para cargar", bg='white')
        label2.grid(row=0, column=1, pady=4, padx=150)

        self.ventana = tk.Frame(self.frame, bg = 'white', width = 250, height= 480)
        self.ventana.grid(row=1, column=1)

        self.vscrollbar = tk.Scrollbar(self.ventana, orient=tk.VERTICAL)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)

        self.canva = tk.Canvas(self.ventana, bd=0, bg = 'white', highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.vscrollbar.config(command=self.canva.yview)

        self.canva.xview_moveto(0)
        self.canva.yview_moveto(0)

        self.interior = tk.Frame(self.canva, bg= 'white')
        self.interior_id = self.canva.create_window(0,0, window=self.interior, anchor=tk.NW)

        def configure_interior(event):
            size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
            self.canva.config(scrollregion='0 0 %s %s' % size)
            if self.interior.winfo_reqwidth() != self.canva.winfo_width():
                self.canva.config(width=self.interior.winfo_reqwidth())

        self.interior.bind('<Configure>', configure_interior)

        def configure_canva(event):
            if self.interior.winfo_reqwidth() != self.canva.winfo_width():
                self.canva.itemconfigure(self.interior_id, width=self.canva.winfo_width())

        self.canva.bind('<Configure>', configure_canva)

        self.arrayBateria = leer()
        self.aux, counter = filtrar_nombre(self.arrayBateria)
        if len(self.aux) == 0:
            labelNo = tk.Label(self.interior, text='No hay baterías fuera del cajón', bg = 'white')
            labelNo.pack()
        else:
            for i in range(len(counter)):
                clikado = lambda x = i: self.click(x)
                if checkIncidencias(self.archivos[self.aux[i]]):
                    boton=tk.Button(self.interior, text=escribirNombre(self.archivos[self.aux[i]]), height=2, bg='yellow', command=clikado)
                    boton.pack(pady=4)
                else:
                    boton=tk.Button(self.interior, text=escribirNombre(self.archivos[self.aux[i]]), height=2, bg='white', command=clikado)
                    boton.pack(pady=4)

        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0)
        self.frame.pack()

    def click(self, num):
        self.numero=num + 1
        setBateria(self.numero)
        setBatElegida(self.aux[num])
        setPiloto(self.arrayBateria[0][self.aux[num]])
        Maestra.windowCargar2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Cargar2:
    selff2 = 0
    def __init__(self, master):
        global selff2
        selff2 = self
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.home = tk.PhotoImage(file='home.gif')
        self.bateria = getBateria()
        self.numcargas = tk.IntVar()
        self.int_numcargas = 1
        self.pilot = getPiloto()
        self.boton=[]
        self.NamePilots = getNamePilots()

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=10, columnspan=8)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Elegir número de cargas:", bg='white')
        label2.grid(row=0, column=1, rowspan=2, columnspan=6)
        self.entrada = tk.Entry(self.frame, textvariable=self.numcargas, width = 4)
        self.entrada.grid(row=2, column=3, columnspan=2, pady=2)
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, 1)
        self.entrada.config(justify=tk.CENTER)
        botonMas = tk.Button(self.frame, text = '+', height=2, bg='white', command = lambda: self.mas())
        botonMas.grid(row=2, column=5, columnspan=2,  sticky='w', pady=2)
        botonMenos = tk.Button(self.frame, text = '-', height=2, bg='white', command = lambda: self.menos())
        botonMenos.grid(row=2, column=1, columnspan=2, sticky='e', pady=2)

        label4 = tk.Label(self.frame, text="¿Quién eres?", bg='white')
        label4.grid(row= 4, column=1, columnspan=6, pady=2)
        varColumn = 1
        varRow = 5
        for i in range(len(self.NamePilots)):
            click = lambda x = i: self.pilotoElegido(x)
            self.boton.append(tk.Button(self.frame, text=self.NamePilots[i], height=2, bg='white', command=click))
            self.boton[i].grid(row=varRow, column=varColumn, padx=2, pady=2)
            varColumn +=1

            if varColumn > 6 and varRow >= 5 :
                varColumn = 1
                varRow+=1

        botonOk = tk.Button(self.frame, text='Ok, cargamos', height=2, bg='white', command=lambda: self.ok())
        botonOk.grid(row=varRow + 1, column=1, columnspan=6, pady=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0, pady=2)
        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=7, pady=2)
        self.frame.pack()


    def ok(self):
        self.int_numcargas = self.numcargas.get()
        setNumc(self.int_numcargas)
        Maestra.windowCargar3(selff2)

    def goHome(self):
        self.master.destroy()
        Cargar.close_windows()

    def mas(self):
        self.int_numcargas = self.numcargas.get()
        self.entrada.delete(0, tk.END)
        self.int_numcargas += 1
        self.entrada.insert(0, self.int_numcargas)

    def menos(self):
        self.int_numcargas = self.numcargas.get()
        self.entrada.delete(0, tk.END)
        self.int_numcargas -= 1
        self.entrada.insert(0, self.int_numcargas)

    def pilotoElegido(self, num):
        self.pilot = self.NamePilots[num]
        setPiloto(self.pilot)
        for i in range(len(self.NamePilots)):
            self.boton[i].config(bg='white')
        self.boton[num].config(bg='green')

    def close_windows():
        global selff2
        selff2.master.destroy()

class Cargar3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.yes = tk.PhotoImage(file='Tick2.gif')
        self.no = tk.PhotoImage(file='Cross2.gif')

        self.numBat = getBateria()
        self.numBate = getBatElegida()
        self.baterias = getArchivos()
        self.pilot = getPiloto()
        self.numcargas = getNumc()
        self.nombre_bien = escribirNombre(self.baterias[self.numBate])

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=6, columnspan=2)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text='Cargando batería: ' + self.nombre_bien, bg = 'white')
        label2.grid(row=0, column=0, columnspan=2)
        label3 = tk.Label(self.frame, text='Con ' + str(self.numcargas) + ' cargas', bg = 'white')
        label3.grid(row=1, column=0, columnspan=2)
        label4 = tk.Label(self.frame, text='Siendo ' + self.pilot + ' la persona a cargo', bg = 'white')
        label4.grid(row=2, column=0, columnspan=2)
        label5 = tk.Label(self.frame, text='¿Es esto correcto?', bg = 'white')
        label5.grid(row=3, column=0, columnspan=2)
        botonOk = tk.Button(self.frame, image=self.yes, command=lambda: self.cargamos(self.numBat, self.pilot, self.numcargas))
        botonOk.grid(row=4, column=0, padx=8, stick='E')
        botonAtras = tk.Button(self.frame, image=self.no, command=lambda: self.master.destroy())
        botonAtras.grid(row=4, column=1, padx=8, stick='W')

    def cargamos(self, numBat, piloto, cargas):
        arrayBateria = leer()
        cargarBateria(arrayBateria, numBat, piloto, cargas)
        self.master.destroy()
        Cargar2.close_windows()
        Cargar.close_windows()
