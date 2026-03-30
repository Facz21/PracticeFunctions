def saludar(n):
    
    return f"¡Hola, {n} Bienvenido."

def es_par(n):
    if n % 2 == 0:
        return f"El número {n} si es par"
    else:
        return f"El número {n} no es par"
    
def celsius_to_fahrenheit(c):
    f = c * 9/5 + 32
    return f

def fahrenheit_to_celsius(f):
    c = (f-32) * 5/9 
    return c

def area_rectangulo(b,h):
    a = b * h 
    return a
    
def perimetro_rectangulo(b,h):
    p = 2 * (b + h)
    return p

def presentar(n,e,c):
    return f"Mi llamo {n}, tengo {e} años y soy de {c}"

def min_to_hours(minutos):
    horas = minutos//60
    minutos_restantes = minutos%60
    
    h = "hora" if horas == 1 else "horas"
    m = "minuto" if minutos_restantes == 1 else "minutos"
    return f"{horas} {h} y {minutos_restantes} {m}"

def aplicar_descuento (precio, descuento):
    total = precio - (precio * descuento / 100)
    descontado = precio * descuento / 100
    return total, descontado

def validar_edad_votación (edad):
    
    if edad < 1:
        return"Edad invalida"
    elif edad < 18:
        return"Aun no puedes votar"
    else:
        return"Tu edad es valida para participar en votaciones"

def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False