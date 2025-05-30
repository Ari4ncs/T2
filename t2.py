import random
import math

def distancia_origen(coord):
    x, y = coord
    return math.sqrt(x**2 + y**2)

# Función para encontrar la coordenada más alejada de X e Y:
def ca(coords):
    if len(coords) == 0:
        return None
    if len(coords) == 1:
        x, y = coords[0]
        if x > 0 and y < 0:
            return coords[0]
        else:
            return None  
    mid = len(coords) // 2
    izquierda = ca(coords[:mid])
    derecha = ca(coords[mid:])
    
    if izquierda and derecha:
        return izquierda if distancia_origen(izquierda) > distancia_origen(derecha) else derecha
    return izquierda or derecha

# Código principal donde te pide la cantidad de pares que deseas:
def main():
    try:
        n = int(input("Ingrese la cantidad de pares coordenadas: "))
        coordenadas = [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]
        
        print("\nCoordenadas:")
        for coord in coordenadas:
            print(coord)
        
        resultado = ca(coordenadas)
# Resultado del código:
  
        if resultado:
            print("\nLa coordenada más alejada de X e Y es:", resultado)
            print("Distancia al origen:", round(distancia_origen(resultado), 2))
        else:
            print("\nNo se encontró ingreso ninguna coordenada")
    except ValueError:
        print("Debe de ingresar un número entero")
if __name__ == "__main__":
    main()
