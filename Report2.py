from GestorBat_1_12 import *

class Report1:
    selff = 0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entrada = tk.StringVar()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=12, columnspan=20)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Introduzca identificador de la batería:", bg='white')
        label2.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
        label2.config(font=16)


        botones = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e', 'f', 'Del']

        self.entrada = tk.Entry(self.frame, textvariable=self.entrada , width=5)
        self.entrada.grid(row=2, column=0, columnspan=20, pady=10)

        varRow = 3
        varColumn = 7

        for button in botones:

            command = lambda x=button: self.select(x)

            if button == 'Del':
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn, columnspan=2)
            else:
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            varColumn +=1

            if varColumn > 10 and varRow == 6:
                varColumn = 8
                varRow+=1
            elif varColumn > 10 and varRow >= 3:
                varColumn = 7
                varRow+=1

        botonConfirmar = tk.Button(self.frame, text="Confirmar", height=2, bg='white', command=lambda: self.confirm())
        botonConfirmar.grid(row=8, column=0, columnspan=20, pady=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0, pady=2)

        self.frame.pack()

    def select(self, value):
        if value == "Del":
            self.entrada.delete(len(self.entrada.get())-1, tk.END)
        else:
            self.entrada.insert(tk.END,value)

    def confirm(self):
        setIdent(self.entrada.get())
        Maestra.windowReport2(selff)

    def close_windows():
        global selff
        selff.master.destroy()

class Report2:
    selff2 = 0
    def __init__(self, master):
        global selff2
        selff2 = self
        self.master = master
        self.frame = tk.Frame(self.master)
        self.Identificador = getIdent()
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.home = tk.PhotoImage(file='home.gif')
        self.si =tk.PhotoImage(file='Tick2.gif')
        self.no =tk.PhotoImage(file='Cross2.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=12, columnspan=4)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        botonSi = tk.Button(self.frame, image=self.si, command=lambda: self.clickSi())
        botonNo = tk.Button(self.frame, image=self.no, command=lambda: self.master.destroy())

        self.Baterias = leer()
        self.auxiliar = filtrarIdentificador(self.Baterias, self.Identificador)
        self.archivos = getArchivos()
        if len(self.auxiliar) == 1:
            label2 = tk.Label(self.frame, text="¿Incidencia en la batería " + escribirNombre2(self.archivos[self.auxiliar[0]]) + '?', bg='white')
            label2.grid(row=1, column=1, columnspan=2)
            label2.config(font=18)
            botonSi.grid(row=2, column=1, stick='E', padx=8)
            botonNo.grid(row=2, column=2, stick='W', padx=8)
        else:
            label3 = tk.Label(self.frame, text='No existe una batería con el identificador ' + self.Identificador, bg='white', width=65)
            label3.grid(row=1, column=1, columnspan=2)
            label3.config(font=16)

        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0)

        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=3)
        self.frame.pack()

    def goHome(self):
        self.master.destroy()
        Report1.close_windows()

    def close_windows():
        global selff2
        selff2.master.destroy()

    def clickSi(self):
        setNombreArchivo(self.archivos[self.auxiliar[0]])
        Maestra.windowReport3(selff2)


class Report3:
    selff3=0
    def __init__(self, master):
        global selff3
        selff3 = self
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.entrada = tk.StringVar()
        self.cap = False
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)
        self.atras = tk.PhotoImage(file='atras.gif')
        self.home = tk.PhotoImage(file='home.gif')

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=10, columnspan=13)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        label2 = tk.Label(self.frame, text="Describa el problema:", bg='white')
        label2.grid(row=1, column=0, padx=10, pady=10, columnspan=13)

        botones = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','BACK',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','ñ','MAYUS',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', 'SPACE',]

        self.entrada = tk.Entry(self.frame, textvariable=self.entrada , width=80)
        self.entrada.grid(row=2,columnspan=13, pady=10)

        varRow = 3
        varColumn = 1

        for button in botones:

            command = lambda x=button: self.select(x)
            if button == "SPACE" or button == "MAYUS" or button == "BACK":
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            else:
                tk.Button(self.frame,text= button, width=5, height=2, bg="#3c4987", fg="#ffffff",
    				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=2,
    				pady=2, bd=1,command=command).grid(row=varRow,column=varColumn)

            varColumn +=1

            if varColumn > 11 and varRow >= 3:
                varColumn = 1
                varRow+=1

        botonConfirmar = tk.Button(self.frame, text="Anotar problema", height=2, bg='white', command=lambda: self.confirm())
        botonConfirmar.grid(row=7, column=0, columnspan=13, pady=2)
        botonAtras = tk.Button(self.frame, image=self.atras, command=lambda: self.master.destroy())
        botonAtras.grid(row=0, column=0, pady=2)
        botonHome = tk.Button(self.frame, image=self.home, command=lambda: self.goHome())
        botonHome.grid(row=0, column=12, pady=2)

    def select(self, value):
        if value == "BACK":
            self.entrada.delete(len(self.entrada.get())-1, tk.END)
            self.cap = False
        elif value == "SPACE":
            self.entrada.insert(tk.END, ' ')
            self.cap = False
        elif value == "MAYUS":
            self.cap = True
        else:
            if self.cap:
                self.entrada.insert(tk.END,value.upper())
                self.cap = False
            else:
                self.entrada.insert(tk.END,value)
                self.cap = False

    def goHome(self):
        self.master.destroy()
        Report1.close_windows()
        Report2.close_windows()

    def confirm(self):
        nombre = getNombreArchivo()
        escribirIncidencia(nombre, self.entrada.get())
        self.goHome()
