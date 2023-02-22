"""
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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate as tab
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(data_type):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(data_type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Tipo de estructura de dato")
    print("10- Obtener dato dado un ID")
    print("11- Ordenamiento de datos")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    print()
    print("1. Small")
    print("2. 5%")
    print("3. 10%")
    print("4. 20%")
    print("5. 30%")
    print("6. 50%")
    print("7. 80%")
    print("8. Large")
    size = int(input("Elija el tamaño del archivo: \n"))
    print("Cargando información de los archivos ....\n")
    files=["small.csv","5pct.csv","10pct.csv","20pct.csv","30pct.csv","50pct.csv","80pct.csv", "large.csv"]
    return controller.load_data(control, files[size-1])
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_seleccion_lista(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print()
    print("1. ARRAY_LIST")
    print("2. SINGLE_LINKED")
    data_type = int(input("Seleccione el tipo de representación de la lista: \n"))
    control = new_controller(data_type)
    return control, data_type


def print_ordenamiento(control):
    print()
    print("1. Shell Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    sort_type = int(input("Seleccione el tipo de ordenamiento: \n"))
    return controller.sort(control, sort_type)

# Se crea el controlador asociado a la vista
data_type = 1
control = new_controller(data_type)

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                filas = load_data(control)
                print("Se cargaron " + str(filas) + " filas")
                carga = {"Año":[], "Código actividad económica":[], "Nombre actividad económica":[], "Código sector económico":[],
                         "Nombre sector económico":[], "Código subsector económico":[], "Nombre subsector económico":[],
                         "Total ingresos netos":[], "Total costos y gastos":[], "Total saldo a pagar":[], "Total saldo a favor":[]}
                if data_type == 1:
                    for fila in [0,1,2,filas-3,filas-2,filas-1]:
                        for llave in carga:
                            carga[llave].append(control['data']['elements'][fila][llave])
                    print(tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,10,15], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,10,15]))
                else:
                    fila = 0
                    for elemento in lt.iterator(control['data']):
                        if fila in [0,1,2,filas-3,filas-2,filas-1]:
                            for llave in carga:
                                carga[llave].append(elemento[llave])
                        fila+=1
                    print(tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,12,15], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,12,15]))

            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                control, data_type = print_seleccion_lista(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)
                
            elif int(inputs) == 11:
                datos, time, sort_type = print_ordenamiento(control)
                print()
                print("El tiempo tardado en ordenar los datos usando el algoritmo de " + str(sort_type) + " es de: \n" + str(time) + " milisegundos")

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
                
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
