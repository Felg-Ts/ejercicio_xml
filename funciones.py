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
