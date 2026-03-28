def saludar(n):
    
    return f"¡Hola, {n} Bienvenido."

def es_par(n):
    if n % 2 == 0:
        return f"El numero {n} si es par", True
    else:
        return f"El numero {n} no es par", False
    
def celsius_to_farenheit(c):
    f = c * 9/5 + 32
    return f

def farenheit_to_celsius(f):
    c = (f-32) * 5/9 
    return c

def area_rectangulo(b,h):
    a = b * h 
    return a
    
def perimetro_rectangulo(b,h):
    p = 2 * (b + h)
    return p