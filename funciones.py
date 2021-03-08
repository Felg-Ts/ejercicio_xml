import msvcrt
import os

def listinfo(root):
    for x in root.findall("./tiendas/ciudad"):
        print(x.text)
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    os.system('clear')