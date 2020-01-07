# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:40:24 2019

@author: AntoniSepu
"""

from GestorBat_1_12 import *

class Sacar:
    selff = 0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master, width=800, height=480)
        self.frame.pack()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.lupa = tk.PhotoImage(file='Lupa2.gif')

        self.tipo = 0
        self.numcell = 0
        self.boton1=[]
        self.boton2=[]
        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=8, columnspan=7)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo
        label2 = tk.Label(self.frame, text="Elegir tipo de batería y número de celdas", bg='white')
        label2.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
        for i in range(len(TechBat)):
            clikado1 = lambda x = i: self.clickTipo(x)
            self.boton1.append(tk.Button(self.frame, text=TechBat[i], width= 5, height= 2, command=clikado1, bg='white'))
            self.boton1[i].grid(row=2, column=i+2, padx=10, pady=10)
        for i in range(len(NumCell)):
            clikado2 = lambda x = i: self.clickNum(x)
            self.boton2.append(tk.Button(self.frame, text=NumCell[i], width= 5, height= 2, command=clikado2, bg='white'))
            self.boton2[i].grid(row=3, column=i, padx=10, pady=10)

        buttonSearch = tk.Button(self.frame, image=self.lupa, command= lambda: self.buscar(self.tipo, self.numcell))
        buttonSearch.grid(row=4, column=2, padx=10, pady=10, columnspan=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.place(anchor='nw')
        self.frame.pack()

    def clickTipo(self, num):
        self.tipo=TechBat[num]
        setTipo(self.tipo)
        for i in range(len(TechBat)):
            self.boton1[i].config(bg='white')
        self.boton1[num].config(bg='green')

    def clickNum(self, num):
        self.numcell=NumCell[num]
        setNumc(self.numcell)
        for i in range(len(NumCell)):
            self.boton2[i].config(bg='white')
        self.boton2[num].configure(bg='green')

    def buscar(self, tipo, numcell):
        Maestra.windowSacar2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Sacar2:
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
        self.tipo = getTipo()
        self.numcell = getNumc()
        self.archivos = getArchivos()
        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=3, columnspan=3)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Listado de baterías disponibles:", bg='white')
        label2.grid(row=0, column=1, padx=150)

        self.ventana = tk.Frame(self.frame, bg = 'white', width = 200, height= 600)
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

        arrayBateria = leer()
        self.auxiliar = filtrarTipoNum(arrayBateria, self.tipo, self.numcell)
        if len(self.auxiliar) == 0:
            label3 = tk.Label(self.interior, text='No tenemos baterías con estas características', bg='white')
            label3.pack()
        else:
            for i in range(len(self.auxiliar)):
                clickar = lambda x = i: self.batElegida(x)
                if checkIncidencias(self.archivos[self.auxiliar[i]]):
                    botonBat = tk.Button(self.interior, text=escribirNombre(self.archivos[self.auxiliar[i]]), height= 1, bg='yellow', command=clickar)
                    botonBat.pack(pady=4)
                else:
                    botonBat = tk.Button(self.interior, text=escribirNombre(self.archivos[self.auxiliar[i]]), height= 1, bg='white', command=clickar)
                    botonBat.pack(pady=4)

        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0)
        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=2)
        self.frame.pack()

    def batElegida(self, num):
        setBatElegida(self.auxiliar[num])
        Maestra.windowSacar3(selff2)

    def close_windows():
        global selff2
        selff2.master.destroy()

    def goHome(self):
        self.master.destroy()
        Sacar.close_windows()

class Sacar3:
    selff3 = 0
    def __init__(self, master):
        global selff3
        selff3 = self
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.home = tk.PhotoImage(file='home.gif')
        self.bateria = getBatElegida()
        self.mode = 0
        self.pilot = ''
        self.boton=[]
        self.labelnombres=[]
        self.labelstorages=[]
        self.NamePilots=getNamePilots()

        canva = tk.Canvas(self.frame, bg = 'grey', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=11, columnspan=8)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo
        label2 = tk.Label(self.frame, text="Sacar y añadir un ciclo, o solo sacar:", bg='white')
        label2.grid(row=0, column=1, rowspan=2, columnspan=6)

        self.botonSacar = tk.Button(self.frame, text='Sacar y cargar', height=2, bg='green', command=lambda: self.Saco())
        self.botonSacar.grid(row=2, column=1, columnspan=6, pady=2)

        self.botonSacars = tk.Button(self.frame, text='Sacar sin cargar', height=2, bg='white', command=lambda: self.soloSaco())
        self.botonSacars.grid(row=3, column=1, columnspan=6, pady=2)

        label4 = tk.Label(self.frame, text="¿Quién eres?", bg='white')
        label4.grid(row= 4, column=1, columnspan=6, pady=2)
        varColumn = 1
        self.varRow = 5
        for i in range(len(self.NamePilots)):
            click = lambda x = i: self.pilotoElegido(x)
            self.boton.append(tk.Button(self.frame, text=self.NamePilots[i], height=2, bg='white', command=click))
            self.boton[i].grid(row=self.varRow, column=varColumn, padx=2, pady=2)
            varColumn +=1

            if varColumn > 6 and self.varRow >= 5 :
                varColumn = 1
                self.varRow+=1

        self.botonOk = tk.Button(self.frame, text='Ok, sacamos', height=2, bg='white', command=lambda: self.sacamos(self.mode, self.bateria, self.pilot))
        self.botonOk.grid(row=self.varRow + 1, column=1, columnspan=6, pady=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0, pady=2)
        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=7, pady=2)
        self.LabelAviso = tk.Label(self.frame, text = 'Elegir un piloto por favor', bg='red', fg='white')
        self.LabelAviso.config(font=16)
        self.frame.pack()

    def Saco(self):
        self.mode = 0
        self.botonSacar.config(bg='green')
        self.botonSacars.config(bg='white')

    def soloSaco(self):
        self.mode = 1
        self.botonSacars.config(bg='green')
        self.botonSacar.config(bg='white')

    def pilotoElegido(self, num):
        self.pilot = self.NamePilots[num]
        for i in range(len(self.NamePilots)):
            self.boton[i].config(bg='white')
        self.boton[num].config(bg='green')
        self.LabelAviso.grid_forget()
        self.botonOk.grid(row=self.varRow + 1, column=1, columnspan=6, pady=2)

    def sacamos(self, modo, bateria, piloto):
        if piloto == '':
            self.botonOk.grid_forget()
            self.LabelAviso.grid(row=self.varRow + 1, column=1, columnspan=6, pady=2)
        else:
            setModo(modo)
            setBateria(bateria)
            setPiloto(piloto)
            Maestra.windowSacar4(selff3)

    def goHome(self):
        self.master.destroy()
        Sacar2.close_windows()
        Sacar.close_windows()

    def close_windows():
        global selff2
        selff2.master.destroy()

class Sacar4:
    selff4 = 0
    def __init__(self, master):
        global selff4
        selff4 = self
        self.master = master
        self.frame = tk.Frame(self.master, width=800, height=480)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.ok =tk.PhotoImage(file='Tick2.gif')
        self.no =tk.PhotoImage(file='Cross2.gif')
        self.bateria = getBateria()
        self.mode = getModo()
        self.numcargas = 1
        if self.mode == 1:
            self.numcargas = 0

        self.piloto = getPiloto()
        self.tipo = getTipo()
        self.numcell = getNumc()

        baterias = getArchivos()
        self.bateriaElegida = baterias[self.bateria]

        canva = tk.Canvas(self.frame, bg = 'grey', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=7, columnspan = 2)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo
        label2 = tk.Label(self.frame, text='La batería a sacar es: ' + escribirNombre(self.bateriaElegida), bg='white')
        label2.grid(row=0, column=0, pady=4, columnspan=2)
        label3 =tk.Label(self.frame, text='Sacada por: ' + self.piloto, bg='white')
        label3.grid(row=1, column=0, pady=4, columnspan=2)
        if self.mode == 1:
            label5 = tk.Label(self.frame, text='Sacamos sin cargar', bg='white')
            label5.grid(row=2, column=0, pady=4, columnspan=2)
        else:
            label4 = tk.Label(self.frame, text='Número de cargas: ' + str(self.numcargas), bg='white')
            label4.grid(row=2, column=0, pady=4, columnspan=2)

        label7 = tk.Label(self.frame, text='¿Todo correcto?', bg='white')
        label7.grid(row=3, column=0, pady=4, columnspan=2)
        botonSi = tk.Button(self.frame, image=self.ok, command=lambda: self.clickSi(self.mode, self.bateria, self.piloto, self.numcargas))
        botonSi.grid(row=4, column=0, stick='E', padx=8)
        botonAtras = tk.Button(self.frame, image=self.no, command=lambda: self.master.destroy())
        botonAtras.grid(row=4, column=1, stick='W', padx=8)
        self.frame.pack()

    def goHome(self):
        self.master.destroy()
        Sacar3.close_windows()
        Sacar2.close_windows()
        Sacar.close_windows()

    def clickSi(self, modo, bat, piloto, cargas):
        if modo==1:
            sacar(bat, piloto)
        elif modo==0:
            sacarycargar(bat, piloto, cargas)

        self.goHome()
