def saludar(n):
    
    return f"¡Hola, {n} Bienvenido."

def es_par(n):
    if n % 2 == 0:
        return f"El numero {n} si es par", True
    else:
        return f"El numero {n} no es par", False