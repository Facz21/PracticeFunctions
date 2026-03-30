#Importamos las funciones que estamos utlizando, se encuentran alojadas dentro de la carpeta source
from source.functions import ( 
    #Estas son las funciones que realizan operaciones 
        saludar as s, es_par as ep, celsius_to_fahrenheit as ctf, fahrenheit_to_celsius as ftc, area_rectangulo as ar, perimetro_rectangulo as pr,
        presentar as prs, min_to_hours as mth, aplicar_descuento as ap, validar_edad_votación as vev, año_bisiesto as ab
    )
from gui.menu import  (
    #Mostramos funciones que enseñan al usuario menús 
    show_menu as sm, show_welcome_message as swm, show_conversion_menu as scm, show_area_perimetro_rectangulo as sapr
                       )
#Inicializamos una variable para controlar el flujo del programa mediante ciclo while y una comparación de diferencia
iniciar = 1

swm()#Funcíon que enseña en pantalla un mensaje de bienvenida

while iniciar != 0:#Aquí ralizamos validación de diferencia entre nuestra variable que controla la repetición en bucle de nuestro programa
    
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
                g = int(input("Ingresa los grados celsius a convertir: "))
                f = ctf(g)
                print(f"{g}°C son {f}°F")    
            elif op == "2":
                g = int(input("Ingresa los grados fahrenheit a convertir: "))
                c = ftc(g)
                print(f"{g}°F son {c}°C")    
                
            elif op == "0":
                print("Saliendo de conversión")
                
                break
            else:
                print(f"La opción {op} es invalida, intente de nuevo")   
    elif op == "4":
        while True:
            sapr()
            op = input("Digita una opción para continuar: ")
            if op == "1":
                b = int(input("Digite la base del rectangulo: "))    
                h = int(input("Digite la altura del rectangulo: "))
                a = ar(b,h)
                print(f"El area del rectangulo con base {b} y altura {h} es de {a}")    
            elif op == "2":
                b = int(input("Digite la base del rectangulo: "))    
                h = int(input("Digite la altura del rectangulo: "))
                p = pr(b,h)
                print(f"El perimetro del rectangulo con base {b} y altura {h} es de {p}")
            elif op == "0":
                print("Saliendo de conversión")
                
                break
            else:
                print(f"La opción {op} es invalida, intente de nuevo")            
    elif op == "5":
        nombre = str(input("Ingresa tu nombre por favor: "))
        edad = int(input("Ingresa tu edad por favor: "))
        ciudad = str(input("Ingresa tu ciudad de residencia por favor: "))
        presentación = prs(nombre, edad, ciudad)
        print(presentación)
    elif op == "6":
        minutos = int(input("Ingrese la cantidad de minutos: "))        
        formato=mth(minutos)
        print(formato)
    elif op == "7":
        precio = float(input("Ingrese el precio del producto: "))
        descuento = float(input("Ingrese el descuento del a realizar: "))
        total = ap(precio, descuento)
        print(f"""
El precio antes del descuento es de: ${precio}
Con un descuento del {descuento}% queda en: ${total[0]}
El total ahorrado fue: ${total[1]}             
              """)
    elif op == "8":
        edad = int(input("Ingresa tu edad para validar si puedes votar o no: "))
        print(vev(edad))
    elif op == "9":
        año = int(input("Ingrese un año para saber si es bisiesto o no: "))
        if ab(año):
            print(f"{año} es un año bisiesto, tiene 366 días")
        else:
            print(f"{año} no es un año bisiesto, tiene 365 días")
    elif op == "0":
        print("Saliendo del programa...")
        iniciar = 0
    else:
        print(f"La opción {op} es invalida, intente de nuevo")