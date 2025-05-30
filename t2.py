import random
import math

# Función para calcular la distancia al origen
def distancia_origen(coord):
    x, y = coord
    return math.sqrt(x**2 + y**2)

# Divide y vencerás para encontrar la coordenada más alejada con X > 0 e Y < 0
def mas_alejada(coords):
    if len(coords) == 0:
        return None
    if len(coords) == 1:
        x, y = coords[0]
        if x > 0 and y < 0:
            return coords[0]
        else:
            return None
    
    mid = len(coords) // 2
    izquierda = mas_alejada(coords[:mid])
    derecha = mas_alejada(coords[mid:])
    
    if izquierda and derecha:
        return izquierda if distancia_origen(izquierda) > distancia_origen(derecha) else derecha
    return izquierda or derecha

# Función principal
def main():
    try:
        n = int(input("Ingrese la cantidad de pares de coordenadas: "))
        coordenadas = [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]
        
        print("\nCoordenadas generadas:")
        for coord in coordenadas:
            print(coord)
        
        resultado = mas_alejada(coordenadas)
        
        if resultado:
            print("\nLa coordenada más alejada con X > 0 e Y < 0 es:", resultado)
            print("Distancia al origen:", round(distancia_origen(resultado), 2))
        else:
            print("\nNo se encontró ninguna coordenada con X > 0 e Y < 0.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
