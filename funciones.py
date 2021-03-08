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
