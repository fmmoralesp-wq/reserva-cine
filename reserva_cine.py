# 1. Crear una matriz de 3 filas por 4 columnas (inicializada en 0)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 2. Pedir al usuario la fila y la columna del asiento que desea reservar
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# 3. Marcar el asiento como reservado asignándole el valor 1
asientos[fila][columna] = 1

# 4. Mostrar la matriz completa en formato de tabla usando bucles anidados
print("\nEstado de la sala de cine:")
for i in range(len(asientos)):
    for j in range(len(asientos[i])):
        print(asientos[i][j], end=" ")
    print()  # Salto de línea al terminar cada fila
