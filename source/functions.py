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