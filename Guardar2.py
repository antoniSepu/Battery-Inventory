# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:26:12 2019

@author: AntoniSepu
"""

from GestorBat_1_12 import *
import time

class Guardar:
    selff = 0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master)
        self.archivos = getArchivos()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=3, columnspan=3)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        labelx=tk.Label(self.frame, text='Elegir batería para guardar:', bg='white')
        labelx.grid(row=0, column=1, pady=2, padx=150)

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

        arrayBateria = leer()
        self.aux, counter = filtrar_nombre(arrayBateria)
        if len(self.aux) == 0:
            labelNo = tk.Label(self.interior, text='No hay baterías fuera del cajón', bg='white')
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
        Maestra.windowGuardar2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Guardar2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.numBat = getBateria()
        self.numBate = getBatElegida()
        self.baterias = getArchivos()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.yes = tk.PhotoImage(file='Tick2.gif')
        self.no = tk.PhotoImage(file='Cross2.gif')
        self.home = tk.PhotoImage(file='home.gif')
        self.frame.pack()

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=5, columnspan=4)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        labelbat = tk.Label(self.frame, text='Guardando batería: ' + escribirNombre(self.baterias[self.numBate]), bg='white', width=52)
        labelbat.grid(row=0, column=1, pady=2, padx=85, columnspan=2)

        label2 = tk.Label(self.frame, text="¿Está en storage la batería?", bg='white')
        label2.grid(row=1, column=1, pady=2, columnspan=2)

        self.buttonSi = tk.Button(self.frame, image=self.yes, command=lambda: self.clickSi())
        self.buttonSi.grid(row=2, column=1, pady=4, padx=8, stick='E')

        self.buttonNo = tk.Button(self.frame, image=self.no, command=lambda: self.clickNo())
        self.buttonNo.grid(row=2, column=2, pady=4, padx=8, stick='W')

        self.button = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        self.button.grid(row=0, column=0, pady=2)

        self.label3 = tk.Label(self.frame, text='Por favor, antes de guardar asegurar la batería en modo storage', bg='red', fg='white', width=61)
        self.label3.config(font=16)

        buttonSalir =tk.Button(self.frame, image=self.home, command = lambda: self.destruirTodo())
        buttonSalir.grid(row=0, column=3, pady=4)

    def clickSi(self):
        guardarBateria(self.numBat)
        self.destruirTodo()

    def clickNo(self):
        self.buttonNo.destroy()
        self.buttonSi.destroy()

        self.label3.grid(row=2, column=1, pady=4, columnspan = 2)

    def destruirTodo(self):
        self.master.destroy()
        Guardar.close_windows()
