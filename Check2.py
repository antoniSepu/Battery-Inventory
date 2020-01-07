# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:33:18 2019

@author: AntoniSepu
Lo del frame con scroll es copiado de Stack overflow:
dynamic button with scrollbar in tkinter python
"""

from GestorBat_1_12 import *

class Check:
    selff=0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='home.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=6, columnspan=3)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label1 = tk.Label(self.frame, text="Página revisar archivos", bg='white')
        label1.grid(row=0, column=1, pady=4)

        self.label2 = tk.Label(self.frame, text='Baterías sacadas:', bg='white')
        self.label2.grid(row=1, column=0)

        self.label3 = tk.Label(self.frame, text='Baterías guardadas:', bg='white')
        self.label3.grid(row=1, column=2)

        self.botonnombres1=[]
        self.botonnombres2=[]
        self.botonstorages=[]

        self.Baterias = leer()
        self.Aux1, self.Count1 = filtrar_nombre(self.Baterias)
        self.Aux2 = filtrar_sinnombre(self.Baterias)
        self.archivos = getArchivos()

        self.ventana1 = tk.Frame(self.frame, width = 200, height= 600, bg='white')
        self.ventana1.grid(row=2, column=0)

        self.ventana2 = tk.Frame(self.frame, width = 200, height= 600, bg='white')
        self.ventana2.grid(row=2, column=2)

        self.vscrollbar1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.vscrollbar1.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)

        self.vscrollbar2 = tk.Scrollbar(self.ventana2, orient=tk.VERTICAL)
        self.vscrollbar2.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)

        self.canva1 = tk.Canvas(self.ventana1, bd=0, bg= 'white', highlightthickness=0, yscrollcommand=self.vscrollbar1.set)
        self.canva1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.vscrollbar1.config(command=self.canva1.yview)

        self.canva2 = tk.Canvas(self.ventana2, bd=0, bg= 'white', highlightthickness=0, yscrollcommand=self.vscrollbar2.set)
        self.canva2.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.vscrollbar2.config(command=self.canva2.yview)

        self.canva1.xview_moveto(0)
        self.canva1.yview_moveto(0)
        self.canva2.xview_moveto(0)
        self.canva2.yview_moveto(0)

        self.interior1 = tk.Frame(self.canva1, bg='white')
        self.interior1_id = self.canva1.create_window(0,0, window=self.interior1, anchor=tk.NW)

        self.interior2 = tk.Frame(self.canva2, bg='white')
        self.interior2_id = self.canva2.create_window(0,0, window=self.interior2, anchor=tk.NW)

        def configure_interior1(event):
            size1 = (self.interior1.winfo_reqwidth(), self.interior1.winfo_reqheight())
            self.canva1.config(scrollregion='0 0 %s %s' % size1)
            if self.interior1.winfo_reqwidth() != self.canva1.winfo_width():
                self.canva1.config(width=self.interior1.winfo_reqwidth())

        def configure_interior2(event):
            size2 = (self.interior2.winfo_reqwidth(), self.interior2.winfo_reqheight())
            self.canva2.config(scrollregion='0 0 %s %s' % size2)
            if self.interior2.winfo_reqwidth() != self.canva2.winfo_width():
                self.canva2.config(width=self.interior2.winfo_reqwidth())

        self.interior1.bind('<Configure>', configure_interior1)
        self.interior2.bind('<Configure>', configure_interior2)

        def configure_canva1(event):
            if self.interior1.winfo_reqwidth() != self.canva1.winfo_width():
                self.canva1.itemconfigure(self.interior1_id, width=self.canva1.winfo_width())

        def configure_canva2(event):
            if self.interior2.winfo_reqwidth() != self.canva2.winfo_width():
                self.canva2.itemconfigure(self.interior2_id, width=self.canva2.winfo_width())

        self.canva1.bind('<Configure>', configure_canva1)
        self.canva2.bind('<Configure>', configure_canva2)

        for i in range(len(self.Aux1)):
            clickado = lambda x = i: self.click(self.archivos[self.Aux1[x]])
            if checkIncidencias(self.archivos[self.Aux1[i]]):
                self.botonnombres1.append(tk.Button(self.interior1, text=escribirNombre(self.archivos[self.Aux1[i]]), bg='yellow', command = clickado, height=1))
                self.botonnombres1[i].pack()
            else:
                self.botonnombres1.append(tk.Button(self.interior1, text=escribirNombre(self.archivos[self.Aux1[i]]), bg='white', command = clickado, height=1))
                self.botonnombres1[i].pack()

        for i in range(len(self.Aux2)):
            clickado = lambda x = i: self.click(self.archivos[self.Aux2[x]])
            if checkIncidencias(self.archivos[self.Aux2[i]]):
                self.botonnombres2.append(tk.Button(self.interior2, text=escribirNombre(self.archivos[self.Aux2[i]]), bg='yellow', command = clickado, height=1))
                self.botonnombres2[i].pack()
            else:
                self.botonnombres2.append(tk.Button(self.interior2, text=escribirNombre(self.archivos[self.Aux2[i]]), bg='white', command = clickado, height=1))
                self.botonnombres2[i].pack()

        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=3, column=1, pady=4)

        self.frame.pack()


    def click(self, nombre):
        setNombreArchivo(nombre)
        Maestra.windowCheck2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Check2:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.home = tk.PhotoImage(file='home.gif')
        self.nombre = getNombreArchivo()

        canva = tk.Canvas(self.frame, bg = 'grey', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=13, columnspan=3)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo
        label2 = tk.Label(self.frame, text='Ultimas cuatro cargas de: ' + escribirNombre(self.nombre), bg='white')
        label3 = tk.Label(self.frame, text='Ultima carga de: ' + escribirNombre(self.nombre), bg='white')

        os.chdir(DirTrabajo)
        log = open(self.nombre, 'r')
        self.mensaje = log.read().splitlines()

        incidencia=[]
        carga=[]
        for i in range(len(self.mensaje)):
            if len(self.mensaje[i]) > 10:
                incidencia.append(i)
            elif len(self.mensaje[i]) < 10:
                carga.append(i)

        if len(incidencia) > 0:
            labelInc = tk.Label(self.frame, text = 'Esta batería tiene una incidencia:', bg='white',fg='red')
            labelInc.grid(row=0, column=1, padx=140)
            for i in range(2):
                labelx = tk.Label(self.frame, text = self.mensaje[incidencia[len(incidencia)-1]-1 + i], bg='white')
                labelx.grid(row=i+1, column=1, pady=2)
            label3.grid(row=3, column=1, pady=2)
            for i in range(2):
                labely = tk.Label(self.frame, text = self.mensaje[carga[len(carga)-1]-1 + i], bg='white')
                labely.grid(row=i+4, column=1, pady=2)

        elif len(self.mensaje) <= 1:
            label2.grid(row=0, column=1, padx=150, pady=2)
            labelx = tk.Label(self.frame, text = 'No hay registro', bg='white')
            labelx.grid(row=1, column=1, pady=2)

        elif len(self.mensaje) < 8:
            label2.grid(row=0, column=1, padx=150, pady=2)
            for i in range(len(self.mensaje)):
                labelx = tk.Label(self.frame, text = self.mensaje[i], bg='white')
                labelx.grid(row=i+1, column=1, pady=2)
        else:
            label2.grid(row=0, column=1, padx=150, pady=2)
            for i in range(8):
                labelx = tk.Label(self.frame, text = self.mensaje[len(self.mensaje) - 8 + i], bg='white')
                labelx.grid(row=i+1, column=1, pady=2)

        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0)
        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=2)

        self.frame.pack()

    def goHome(self):
        self.master.destroy()
        Check.close_windows()
