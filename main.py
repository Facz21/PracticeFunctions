#Importamos las funciones que estamos utlizando, se encuentran alojadaas dentro de la carpeta source
from source.functions import (
    #Estas son las funciones que realizan operaciones 
    saludar as s, es_par as ep, celsius_to_farenheit as ctf
    )
from gui.menu import  (
    #Mostramos funcione que enseñan al usario menús 
    show_menu as sm, show_welcome_message as swm, show_conversion_menu as scm
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
        while True:
            scm()
            op = input("Digita una opción para continuar: ")
            if op == "1":
                grados = int(input("Ingresa los grados celsius a convertir: "))
                ctf(grados)
                f = ctf(grados)
                print(f"{grados}°C son {f}°F")    
            elif op == "2":
                print("Conversión a Fahrenheit")
            elif op == "0":
                print("Saliendo de conversíon")
                
                break
            else:
                print(f"La opción {op} es invalida, itente de nuevo")
    elif op == "0":
        print("Saliendo del programa...")
        iniciar = 0
    else:
        print(f"La opción {op} es invalida, intente de nuevo")