# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:53:26 2019

@author: AntoniSepu
"""

from Nucleo2 import *
import tkinter as tk
from PIL import Image, ImageTk


class Maestra:
    selff = 0
    def __init__(self, master):
        global selff
        selff = self
        self.master = master
        self.frame = tk.Frame(self.master)
        os.chdir(DirPrimario)
        #self.Im = Image.open('background.gif')
        #self.fondo = ImageTk.PhotoImage(self.Im)

        canva = tk.Canvas(self.frame, bg = 'white', width=800, height=480)
        canva.grid(row=0, column=0, rowspan=10, columnspan=5)
        #canva.create_image(0, 0, anchor = 'nw', image=self.fondo)
        #canva.image=self.fondo

        self.titulo = tk.Label(self.frame, text= 'Gestor de baterías', bg='white')
        self.titulo.grid(row=0, column=0, columnspan=5, pady=10)
        self.titulo.config(font=18)
        self.button1 = tk.Button(self.frame, text = 'Sacar', bg='white', height = 4,  command = self.windowSacar)
        self.button1.grid(row=1, column=1)
        self.button2 = tk.Button(self.frame, text = 'Guardar', bg='white', height = 4,  command = self.windowGuardar)
        self.button2.grid(row=1, column=2)
        self.button3 = tk.Button(self.frame, text = 'Cargar', bg='white', height = 4,  command = self.windowCargar)
        self.button3.grid(row=1, column=3)
        self.button4 = tk.Button(self.frame, text = 'Nueva batería',  bg='white', height = 4,  command = self.windowNueva)
        self.button4.grid(row=2, column=0, columnspan=2)
        self.button5 = tk.Button(self.frame, text = 'Revisar baterías', bg='white', height = 4,  command = self.windowCheck)
        self.button5.grid(row=1, column=0)
        self.button6 = tk.Button(self.frame, text = 'Nuevo piloto', bg='white', height = 4,  command = self.windowNuevoP)
        self.button6.grid(row=2, column=3, columnspan=2)
        self.button7 = tk.Button(self.frame, text = 'Incidencia', bg='white', height = 4,  command = self.windowReport1)
        self.button7.grid(row=1, column=4)
        self.button8 = tk.Button(self.frame, text = 'Retirar batería', bg='white', height = 4,  command = self.windowRetirar1)
        self.button8.grid(row=2, column=2)

        self.frame.pack()

    def windowGuardar(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Guardar2.Guardar(self.newWindow)

    def windowGuardar2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Guardar2.Guardar2(selff.newWindow)

    def windowSacar(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Sacar2.Sacar(self.newWindow)

    def windowSacar2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Sacar2.Sacar2(selff.newWindow)

    def windowSacar3(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Sacar2.Sacar3(selff.newWindow)

    def windowSacar4(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Sacar2.Sacar4(selff.newWindow)

    def windowCargar(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Cargar2.Cargar(self.newWindow)

    def windowCargar2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Cargar2.Cargar2(selff.newWindow)

    def windowCargar3(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Cargar2.Cargar3(selff.newWindow)

    def windowNueva(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Nueva2.Nueva(self.newWindow)

    def windowNueva2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Nueva2.Nueva2(selff.newWindow)

    def windowCheck(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Check2.Check(self.newWindow)

    def windowCheck2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Check2.Check2(selff.newWindow)

    def windowNuevoP(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = NuevoP2.NuevoP(self.newWindow)

    def windowReport1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Report2.Report1(self.newWindow)

    def windowReport2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Report2.Report2(selff.newWindow)

    def windowReport3(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Report2.Report3(selff.newWindow)

    def windowRetirar1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry("{0}x{1}+0+0".format(self.newWindow.winfo_screenwidth(), self.newWindow.winfo_screenheight()))
        self.app = Retirar2.Retirar1(self.newWindow)

    def windowRetirar2(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Retirar2.Retirar2(selff.newWindow)

    def windowRetirar3(selff):
        selff.newWindow = tk.Toplevel(selff.master)
        selff.newWindow.geometry("{0}x{1}+0+0".format(selff.newWindow.winfo_screenwidth(), selff.newWindow.winfo_screenheight()))
        selff.app = Retirar2.Retirar3(selff.newWindow)

import Sacar2, Guardar2, Cargar2, Nueva2, Check2, NuevoP2, Report2, Retirar2

def main():
    root = tk.Tk()
    os.chdir(DirPrimario)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.title('Gestor de baterías')
    app = Maestra(root)
    root.mainloop()

if __name__ == '__main__':
    main()
