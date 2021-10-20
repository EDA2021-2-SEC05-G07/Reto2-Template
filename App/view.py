﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - obras en orden cronologico -LABORATORIO-")
    print("3 - total obras nacionalidad-LABORATORIO-")
    print("4 - artistas en orden cronologico -REQ 1-")
    print("5 - obras en orden cronologico -REQ 2-")
    print("6 - clasificar las obras por la nacionalidad de sus creadores-REQ 4-")
    print("8 - costo transporte departamento -REQ 5-")
catalog = None

def initDatos():
    return controller.getiniciarDatos()

def cargarDatos(catalog):
    return controller.cargarDatos(catalog)

def gettopnAntiguas(n:int):
    
    return controller.gettopnAntiguas(listaOrdenada, obras, n)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= initDatos()
        cargarDatos(catalog)

    elif int(inputs[0]) == 2:
        n= input('Ingrese un numero: ')
        medio= input('Ingrese el medio que quiere buscar: ')
        print('las n obras más antiguas de' + str(medio))
        obras = controller.getorgObrasCro(catalog, medio)
        fechas = controller.getlistaFechas(obras)
        listaOrdenada = controller. getordenarlista(fechas)
        nObras = controller.gettopnAntiguas(listaOrdenada, obras, n)

    elif int(inputs[0]) == 3:
        nacionalidad = input('Ingrese la nacionalidad que quiere buscar: ')
        cant = controller.getSizeNatio(catalog, nacionalidad)
        print('El número total de obras de la nacionalidad'+ str(nacionalidad) + 'es: ' + str(cant))
    
    elif int(inputs[0]) == 4:
        inicial=input('Ingrese la fecha inicial: ')
        final=input('Ingrese la fecha final: ')
        totalArtist=controller.getorgartistasCro(catalog, inicial, final)
        print('El número total de artistas es: ' + str(totalArtist))
        primeros3=
        ultimos3=
        print(primeros3)
        print(ultimos3)
        
    elif int(inputs[0]) == 5:
        inicial=input('Ingrese la fecha inicial: ')
        final=input('Ingrese la fecha final: ')
        totalObras=controller.getorgObrasCro(catalog, inicial, final)
        print('El número total de artistas es: ' + str(totalObras))
        primeros3=
        ultimos3=
        print(primeros3)
        print(ultimos3)

    elif int(inputs[0]) == 6:
        id= controller.getidArtists
        cargarNacio = controller.getidyNacio(catalog, id)
        lst_top10_final=controller.getlista_nacionalidades(catalog)
        print('Lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10).' + str(lst_top10_final))
        top10= controller.getTop10(catalog)
        info_obras= controller.getnacioMasObras(top10, catalog)
        print('Información de las obras de la nacionalidad con el mayor numero de obras') + info_obras

    elif int(inputs[0]) == 8:
        departamento = input('Departamento del museo: ')
        total_obras= controller.getcantidadObras(catalog)
        print('Total de obras para transportar: ' + str(total_obras))
        estimado = controller.getcostoEstimado(catalog)
        print('Estimado en USD del precio del servicio: ' + str(estimado))
        peso_estimado = controller.getpesototal(catalog)
        print('Peso estimado de las obras: ' + str(peso_estimado))
        listafechas= controller.getlistafechas(catalog)
        listaOrdenada= controller.getordenarlista(listafechas)
        obras_antiguas = controller.getobrasMasAntiguas(listaOrdenada, catalog)
        print('Las 5 obras mas antiguas a transportar: ' + obras_antiguas)
        listaprecios = controller.getlistaprecios(catalog)
        listaOrdenadaprecios = controller.getordenarlista2(listaprecios)
        obras_costosas = controller.getobrasMasCost(listaOrdenadaprecios, catalog)
        print('Las 5 obras mas costosas para transportar: ' + obras_costosas)

    else:
        sys.exit(0)
sys.exit(0)
