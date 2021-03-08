import xml.etree.ElementTree as ET
import funciones
opción = '1'

xmldoc = ET.parse('game.xml')
root = xmldoc.getroot()

while opción >= "1" and opción <= "5":

    print('''
    1-Lista los nombres de las ciudades.
    2-Lista el numero de clientes que contiene cada ciudad.
    3-Pide el nombre de un juego y muestra su fecha de lanzamiento, precioInicial.
    4-Pide por teclado el nombre de un juego y muestra en que ciudades se vende.
    5-Pide por teclado el nombre de una ciudad y el de un cliente y muestra 
    por pantalla el nombre de los juegos que tiene.
    ''')

    opción = input("Introduce un número del 1 al 5 para ejecutar una de las 5 funciones: ")

    if opción == '1':
        funciones.listinfo(root)
    elif opción == '2':
        funciones.countinfo(root)
    elif opción == '3':
        funciones.searhinfo(root)
    elif opción == '4':
        funciones.searhinfore(root)
    elif opción == '5':
        funciones.searhichamabil(root)
