import msvcrt
import os

def listinfo(root):
    for x in root.findall("./tiendas/ciudad"):
        print(x.text)
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

def countinfo(root):

    l1 = []
    l2 = []

    for cdd1 in root.findall("./tiendas[1]/ciudad"):
        print(cdd1.text)
        for clt1 in root.findall(f"./tiendas[1]/clientes/nombre"):
            l1.append(clt1)

    print(f"En {cdd1.text} hay {len(l1)} clientes")
    print('')

    for cdd2 in root.findall("./tiendas[2]/ciudad"):
        print(cdd2.text)

        for clt2 in root.findall(f"./tiendas[2]/clientes/nombre"):
            l2.append(clt2)

    print(f"En {cdd2.text} hay {len(l2)} clientes")

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

def searhinfo(root):

    print('''
    1-FIFA
    2-COD
    3-FORTNITE
    4-LOL
    5-OVERWATCH
    6-GTA
    ''')

    ngame = input("Introduce el nombre de un juego: ")

    if ngame == 'FIFA':
        NG1 = root.find("./tiendas/videojuegos[1]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[1]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[1]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')
    elif ngame == 'COD':
        NG1 = root.find("./tiendas/videojuegos[4]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[4]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[4]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')
    elif ngame == 'FORTNITE':
        NG1 = root.find("./tiendas/videojuegos[5]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[5]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[5]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')
    elif ngame == 'LOL':
        NG1 = root.find("./tiendas/videojuegos[6]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[6]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[6]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')
    elif ngame == 'OVERWATCH':
        NG1 = root.find("./tiendas/videojuegos[7]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[7]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[7]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')
    elif ngame == 'GTA':
        NG1 = root.find("./tiendas/videojuegos[8]/nombreVideojuego")
        DG2 = root.find("./tiendas/videojuegos[8]/fechaLanzamiento")
        PG3 = root.find("./tiendas/videojuegos[8]/precioInicial")
        print(f'El videojuego {NG1.text} se lanzo el {DG2.text} y tenia un coste inicial de {PG3.text}.')

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

def searhinfore(root):

    print('''
    1-FIFA
    2-COD
    3-FORTNITE
    4-LOL
    5-OVERWATCH
    6-GTA
    ''')

    ngame = input("Introduce el nombre de un juego: ")

    if ngame == 'FIFA':
        NG1 = root.find("./tiendas/videojuegos[1]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        C2 = root.find("./tiendas[2]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text} y {C2.text}.')
    elif ngame == 'COD':
        NG1 = root.find("./tiendas/videojuegos[4]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        C2 = root.find("./tiendas[2]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text} y {C2.text}.')
    elif ngame == 'FORTNITE':
        NG1 = root.find("./tiendas/videojuegos[5]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text}.')
    elif ngame == 'LOL':
        NG1 = root.find("./tiendas/videojuegos[6]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text}.')
    elif ngame == 'OVERWATCH':
        NG1 = root.find("./tiendas/videojuegos[7]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text}.')
    elif ngame == 'GTA':
        NG1 = root.find("./tiendas/videojuegos[8]/nombreVideojuego")
        C1 = root.find("./tiendas[1]/ciudad")
        C2 = root.find("./tiendas[2]/ciudad")
        print(f'El videojuego {NG1.text} se vende en: {C1.text} y {C2.text}.')

    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')

def searhichamabil(root):

    print('''
    1-Granada
    2-Barcelona
    ''')

    nc = input("Introduce el nombre de una ciudad: ")

    if nc == 'Granada':
        for x1 in root.findall("./tiendas[1]/clientes/nombre"):
            print(x1.text)

    
        cll1 = root.find("./tiendas[1]/clientes[1]/nombre")
        cll2 = root.find("./tiendas[1]/clientes[2]/nombre")
        cll3 = root.find("./tiendas[1]/clientes[3]/nombre")
        cll4 = root.find("./tiendas[1]/clientes[4]/nombre")

        cl1 = input("Dime el nombre de un cliente: ")

        if cl1 == cll1.text:
            n1 = root.find("./tiendas[1]/clientes[1]/nombre")
            c1 = root.find("./tiendas[1]/ciudad")
            g1 = root.find("./tiendas[1]/clientes[1]/videojuegosComprados[1]/nombreVideojuego")
            g2 = root.find("./tiendas[1]/clientes[1]/videojuegosComprados[2]/nombreVideojuego")
            print(f"El cliente {n1.text} de la ciudad {c1.text} tiene los videojuegos: {g1.text} y {g2.text}")
        elif cl1 == cll2.text:
            n1 = root.find("./tiendas[1]/clientes[2]/nombre")
            c1 = root.find("./tiendas[1]/ciudad")
            g1 = root.find("./tiendas[1]/clientes[2]/videojuegosComprados[1]/nombreVideojuego")
            print(f"El cliente {n1.text} de la ciudad {c1.text} tiene los videojuegos: {g1.text}")
        elif cl1 == cll3.text:
            n1 = root.find("./tiendas[1]/clientes[3]/nombre")
            c1 = root.find("./tiendas[1]/ciudad")
            g1 = root.find("./tiendas[1]/clientes[3]/videojuegosComprados[1]/nombreVideojuego")
            print(f"El cliente {n1.text} de la ciudad {c1.text} tiene los videojuegos: {g1.text}")
        elif cl1 == cll4.text:
            n1 = root.find("./tiendas[1]/clientes[4]/nombre")
            c1 = root.find("./tiendas[1]/ciudad")
            g1 = root.find("./tiendas[1]/clientes[4]/videojuegosComprados[1]/nombreVideojuego")
            g2 = root.find("./tiendas[1]/clientes[4]/videojuegosComprados[2]/nombreVideojuego")
            print(f"El cliente {n1.text} de la ciudad {c1.text} tiene los videojuegos: {g1.text} y {g2.text}")

        print("Presione una tecla para continuar...")
        msvcrt.getch()
        os.system('clear')

    elif nc == 'Barcelona':
        for x2 in root.findall("./tiendas[2]/clientes/nombre"):
            print(x2.text)

        cll1 = root.find("./tiendas[2]/clientes[1]/nombre")

        cl1 = input("Dime el nombre de un cliente: ")

        if cl1 == cll1.text:
            n1 = root.find("./tiendas[2]/clientes[1]/nombre")
            c1 = root.find("./tiendas[2]/ciudad")
            g1 = root.find("./tiendas[2]/clientes[1]/videojuegosComprados[1]/nombreVideojuego")
            g2 = root.find("./tiendas[2]/clientes[1]/videojuegosComprados[2]/nombreVideojuego")
            print(f"El cliente {n1.text} de la ciudad {c1.text} tiene los videojuegos: {g1.text} y {g2.text}")

        print("Presione una tecla para continuar...")
        msvcrt.getch()
        os.system('cl')
