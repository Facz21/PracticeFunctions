from utils.functions import (
    saludar as s, es_par as ep
    )
from gui.menu import  (
    show_menu as sm, show_welcome_message as swm
                       )
iniciar = 1

swm()

while iniciar != 0:
    
    sm()
    op = input("Seleccione una opción: ")
    
    if op == "1":
        nombre = str(input("Ingresa tu nombre: "))
        saludo =s(nombre)
        print(saludo)
    elif op == "2":
        num = int(input("Digita un número para comprobar si es par: "))
        par_prueba = ep(num)
        print(par_prueba)
    elif op == "3":
        print("Saliendo del programa...")
        iniciar = 0
    else:
        print(f"La opción {op} es invalida intente de nuevo")