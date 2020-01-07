# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:09:36 2019

@author: AntoniSepu
"""
#En este archvivo se encuentran todas las funcionalidades básicas del programa
import os
from datetime import datetime

bol1 = False
bol2 = False
DirPrimario = os.getcwd() #Consigo el directorio actual del script

dirs = os.listdir(DirPrimario)
for i in range(len(dirs)):
    if dirs[i] == 'Archivos':
        bol1 = True
    if dirs[i] == 'Datos':
        bol2 = True
if bol1 != True:
    os.mkdir('Archivos')
if bol2 != True:
    os.mkdir('Datos')

DirDatos = DirPrimario + '/Datos'
os.chdir(DirDatos)
nceldas = open('N_Celdas.txt', 'r+') #Ha de existir un archivo llamado N_Celdas.txt
NumCell = nceldas.read().splitlines()
nceldas.close()
tbaterias = open('Tipos_Baterias.txt', 'r+') #Ha de existir un archivo llamado Tipos_Baterias.txt
TechBat = tbaterias.read().splitlines()
tbaterias.close()

DirTrabajo = DirPrimario + '/Archivos' #Creo el path a la carpeta Archivos

BateriaOperar = 0
TipoElegido = 0
NumElegido = 0
BatElegida = -1
Nombre = ''
Pilot = ''
amperios = ''
numCargas = 0
Modo = 0
Ident = ''

#Setters y getters
def getNamePilots():
    os.chdir(DirDatos)
    npilotos = open('Nombres_Pilotos.txt', 'r+') #Ha de existir un archivo llamado Nombres_Pilotos.txt
    nombres = npilotos.read().splitlines()
    npilotos.close()
    return nombres

def getArchivos():
    files = os.listdir(DirTrabajo)
    return files

def getFecha():
    fecha_str = datetime.strftime(datetime.today(), '%d/%m/%Y')
    return fecha_str

def setTipo(numTipo):
    global TipoElegido
    TipoElegido = numTipo
def getTipo():
    global TipoElegido
    return TipoElegido

def setNumc(numCell):
    global NumElegido
    NumElegido = numCell
def getNumc():
    global NumElegido
    return NumElegido

def setAmp(amps):
    global amperios
    amperios = amps
def getAmp():
    global amperios
    return amperios

def setBateria(numBat):
    global BateriaOperar
    BateriaOperar = numBat
def getBateria():
    global BateriaOperar
    return BateriaOperar

def setPiloto(nombre):
    global Pilot
    Pilot = nombre
def getPiloto():
    global Pilot
    return Pilot

def setBatElegida(numero):
    global BatElegida
    BatElegida = numero
def getBatElegida():
    global BatElegida
    return BatElegida

def setNombreArchivo(name):
    global Nombre
    Nombre = name
def getNombreArchivo():
    global Nombre
    return Nombre

def setNumCargas(numero):
    global numCargas
    numCargas=numero
def getNumCargas():
    global numCargas
    return numCargas

def setModo(num):
    global Modo
    Modo = num
def getModo():
    global Modo
    return Modo

def setIdent(identificador):
    global Ident
    Ident = identificador
def getIdent():
    global Ident
    return Ident

#Funciones del programa
def leer():
    bateria = []
    dmg=[]
    prefijos=[]
    tipos=[]
    numscell=[]
    amps=[]
    nombres=[]
    archivos=getArchivos()
    numArchivos=len(archivos)
    for i in range(numArchivos): #Recorro todos los archivos y almaceno sus atributos en una serie de listas
        bat = archivos[i].split('_')
        if len(bat) == 6:
            prefijos.append(bat[0])
            tipos.append(bat[1])
            numscell.append(bat[2])
            amps.append(bat[3])
            nombres.append(bat[4])
            dmg.append(bat[5])
        elif len(bat) == 5:
            if bat[4] == 'dmg.txt' or bat[4] == 'kia.txt':
                prefijos.append('None')
                tipos.append(bat[0])
                numscell.append(bat[1])
                amps.append(bat[2])
                nombres.append(bat[3])
                dmg.append(bat[4])
            else:
                prefijos.append(bat[0])
                tipos.append(bat[1])
                numscell.append(bat[2])
                amps.append(bat[3])
                nombres.append(bat[4])
                dmg.append('None')
        elif len(bat) == 4:
            prefijos.append('None')
            tipos.append(bat[0])
            numscell.append(bat[1])
            amps.append(bat[2])
            nombres.append(bat[3])
            dmg.append('None')
        else:
            print('Formato del archivo irreconocible')

    bateria.append(prefijos)
    bateria.append(tipos)
    bateria.append(numscell)
    bateria.append(amps)
    bateria.append(nombres)
    bateria.append(dmg)

    return bateria

def filtrar_nombre(bateria):
    conta = 0
    contador = []
    aux = []
    archivos=getArchivos()
    numArchivos=len(archivos)
    for i in range(numArchivos):
        if bateria[0][i] != 'None' and bateria[5][i] != 'kia.txt': #filtro e imprimo
            conta += 1
            aux.append(i)
            contador.append(conta)
    return aux, contador

def filtrar_sinnombre(bateria):
    conta = 0
    aux = []
    archivos=getArchivos()
    numArchivos=len(archivos)
    for i in range(numArchivos):
        if bateria[0][i] == 'None' and bateria[5][i] != 'kia.txt': #filtro e imprimo
            conta += 1
            aux.append(i)
    return aux

def guardarBateria(numBat):
    NamePilots=getNamePilots()
    os.chdir(DirTrabajo)
    arrayBateria = leer()
    aux, counter = filtrar_nombre(arrayBateria)
    for i in range(len(aux)):#Generamos el nombre del archivo elegido, recorro la lista auxiliar para hallar el archivo deseado
        if arrayBateria[5][aux[i]] == 'dmg.txt':
            nombre = arrayBateria[1][aux[i]] + '_' + arrayBateria[2][aux[i]] + '_' + arrayBateria[3][aux[i]] + '_' + arrayBateria[4][aux[i]] + '_' + arrayBateria[5][aux[i]]
        else:
            nombre = arrayBateria[1][aux[i]] + '_' + arrayBateria[2][aux[i]] + '_' + arrayBateria[3][aux[i]] + '_' + arrayBateria[4][aux[i]]
        for j in range(len(NamePilots)):
            if numBat == counter[i] and arrayBateria[0][aux[i]] == NamePilots[j]:
                os.rename(NamePilots[j] + '_' + nombre, nombre)

def filtrarTipoNum(bateria, tipoelegido, cellelegido):
    archivos = getArchivos()
    numArchivos=len(archivos)
    aux=[]
    for i in range(numArchivos):
        if bateria[1][i] == tipoelegido and bateria[2][i] == cellelegido and bateria[0][i] == 'None' and bateria[5][i] != 'kia.txt':
            aux.append(i) #En esta lista auxiliar almaceno el número de los archivos que pasan por el filtro
    return aux

def filtrarhastaAmp(bateria, tipoelegido, cellelegido, ampelegido):
    archivos = getArchivos()
    numArchivos=len(archivos)
    aux=[]
    for i in range(numArchivos):
        if bateria[1][i] == tipoelegido and bateria[2][i] == cellelegido and bateria[3][i] == ampelegido and bateria[5][i] != 'kia.txt':
            aux.append(i) #En esta lista auxiliar almaceno el número de los archivos que pasan por el filtro
    return aux

def filtrarIdentificador(bateria, identificador):
    archivos = getArchivos()
    numArchivos=len(archivos)
    aux = []
    for i in range(numArchivos):
        identificadores = bateria[4][i].split('.')
        if identificadores[0] == identificador and bateria[5][i] != 'kia.txt':
            aux.append(i)
    return aux

def sacar(bateria, piloto):
    os.chdir(DirTrabajo)
    archivos = getArchivos()
    if piloto != '':
        nombreoriginal = archivos[bateria]
        nuevonombre = piloto + '_' + nombreoriginal
        os.rename(nombreoriginal, nuevonombre)

def sacarycargar(bateria, piloto, cargas):
    os.chdir(DirTrabajo)
    archivos = getArchivos()
    if piloto != '':
        nombreoriginal = archivos[bateria]
        nuevonombre = piloto + '_' + nombreoriginal
        os.rename(nombreoriginal, nuevonombre)
        addcicles(nuevonombre, cargas)

def addcicles(name, numc):
    os.chdir(DirTrabajo)
    bol = os.stat(name).st_size == 0
    fecha = getFecha()
    if bol == True:
        log = open(name,'w')
        log.write(fecha + '\n' + str(numc))
        log.close()
    else:
        log = open(name, 'r+')
        mensaje = log.read().splitlines()
        for i in range(len(mensaje)):
            if len(mensaje[i]) < 10:
                numciclos=mensaje[i]
        numciclos_int=int(numciclos)
        if numc > 0:
            for i in range(numc):
                numciclos_int += 1
            log.write('\n' + fecha + '\n' + str(numciclos_int))
            log.close()
        elif numc < 0:
            numc = abs(numc)
            for i in range(numc):
                numciclos_int -= 1
            log.write('\n' + fecha + '\n' + str(numciclos_int))
            log.close()


def cargarBateria(bateria, numBat, piloto, numCargas):
    os.chdir(DirTrabajo)
    arrayBateria = leer()
    aux, counter = filtrar_nombre(arrayBateria)
    for i in range(len(counter)):
        if numBat == counter[i] and bateria[0][aux[i]] == piloto and bateria[5][aux[i]]=='dmg.txt':
            nombre = bateria[0][aux[i]] + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]] + '_' + bateria[5][aux[i]]
            addcicles(nombre, numCargas)
        elif numBat == counter[i] and bateria[0][aux[i]] == piloto:
            nombre = bateria[0][aux[i]] + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]]
            addcicles(nombre, numCargas)
        elif numBat == counter[i] and bateria[5][aux[i]]=='dmg.txt':
            nombreoriginal = bateria[0][aux[i]] + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]] + '_' + bateria[5][aux[i]]
            nuevonombre = piloto + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]]  + '_' + bateria[5][aux[i]]
            os.rename(nombreoriginal, nuevonombre)
            addcicles(nuevonombre, numCargas)
        elif numBat == counter[i]:
            nombreoriginal = bateria[0][aux[i]] + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]]
            nuevonombre = piloto + '_' + bateria[1][aux[i]] + '_' + bateria[2][aux[i]] + '_' + bateria[3][aux[i]] + '_' + bateria[4][aux[i]]
            os.rename(nombreoriginal, nuevonombre)
            addcicles(nuevonombre, numCargas)

def nuevaBateria(tipoe, nume, ampe, namee):
    os.chdir(DirTrabajo)
    arrayBateria = leer()
    archivos = getArchivos()
    etiqueta = namee + '.txt'
    name = tipoe + '_' + nume + '_' + ampe + '_' + namee + '.txt'
    conta = 0
    for i in range(len(archivos)):
        if arrayBateria[1][i]==tipoe and arrayBateria[2][i]==nume and arrayBateria[3][i]==ampe and arrayBateria[4][i]==etiqueta:
            conta += 1

    if conta > 0:
        return True
    else:
        log = open(name, 'w+')
        log.close
        return False

def escribirNombre(string):
    partido = string.split('_')
    if len(partido) == 5 and partido[4] == 'dmg.txt':
        nombre = partido[0] + ' ' + partido[1] + ' ' + partido[2] + ' ' + partido[3]
    elif len(partido) == 5:
        fin = partido[4].split('.')
        nombre = partido[0] + ' ' + partido[1] + ' ' + partido[2] + ' ' + partido[3] + ' ' + fin[0]
    elif len(partido) == 4:
        fin = partido[3].split('.')
        nombre = partido[0] + ' ' + partido[1] + ' ' + partido[2] + ' ' + fin[0]
    elif len(partido) == 6:
        fin = partido[4].split('.')
        nombre = partido[0] + ' ' + partido[1] + ' ' + partido[2] + ' ' + partido[3] + ' ' + fin[0]

    return nombre

def escribirNombre2(string): #Misma función que la anterior pero sin incluir el nombre de la persona a cargo
    partido = string.split('_')
    if len(partido) == 5 and partido[4] == 'dmg.txt':
        nombre = partido[1] + ' ' + partido[2] + ' ' + partido[3]
    elif len(partido) == 5 or len(partido) == 6:
        fin = partido[4].split('.')
        nombre = partido[1] + ' ' + partido[2] + ' ' + partido[3] + ' ' + fin[0]
    elif len(partido) == 4:
        fin = partido[3].split('.')
        nombre = partido[0] + ' ' + partido[1] + ' ' + partido[2] + ' ' + fin[0]

    return nombre

def escribirIncidencia(archivo, texto):
    os.chdir(DirTrabajo)
    fecha = getFecha()
    log = open(archivo, 'r+')
    mensaje = log.read().splitlines()
    log.write('\n' + fecha + '\n' + 'Incidencia: ' + texto)
    log.close()
    NombreOriginal = archivo.split('.')
    NuevoNombre = NombreOriginal[0] + '_dmg.txt'
    if checkIncidencias(archivo) == False:
        os.rename(archivo, NuevoNombre)

def checkIncidencias(nombre):
    bol = False
    partido=nombre.split('_')
    for i in range(len(partido)):
        if partido[i] == 'dmg.txt':
            bol=True
    return bol

def eliminarBateria(archivo, texto):
    os.chdir(DirTrabajo)
    fecha = getFecha()
    log = open(archivo, 'r+')
    mensaje = log.read().splitlines()
    log.write('\n' + fecha + '\n' + 'Batería eliminada: ' + texto)
    log.close()
    NombreOriginal = archivo.split('.')
    NuevoNombre1 = NombreOriginal[0] + '_kia.txt'
    if checkIncidencias(archivo):
        partes = archivo.split('_')
        partes[len(partes)-1]='kia.txt'
        NuevoNombre2 = '_'.join(partes)
        os.rename(archivo, NuevoNombre2)
    else:
        os.rename(archivo, NuevoNombre1)

def checkEliminada(nombre):
    bol = False
    partido=nombre.split('_')
    for i in range(len(partido)):
        if partido[i] == 'kia.txt':
            bol=True
    return bol
