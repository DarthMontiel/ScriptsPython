
from os import system #!Importamos os para limpiar la pantalla y hacer el efecto de carga
from time import time #! Time para poder realizar un conteno del tiempo que queremos que se ejcute el script

start = time() + 259200 #!Cantidad en segundos correspondiente a 72hrs
while time() < start:
    print("/ Loading Niabo backup.")
    system("clear")
    print("| Loading Niabo backup..")
    system("clear")
    print("\ Loading Niabo backup...")
    system("clear")
    print("- Loading Niabo backup")
    system("clear")
    if time() >= start:
        print("Error uploading file. Try again\n\n\n")


