import random

"""
Generacion de archivo cost_transpose.txt
"""
# 26x26
matriz_distancia = [[0] * 26 for _ in range(26)]

# Este ciclo calcula las distancias circulares entre letras
for i in range(26):
    for j in range(26):
        # Se calcula la distancia en ambos sentidos y toma el menor
        distancia_directa = abs(i - j)
        distancia_circular = 26 - distancia_directa
        matriz_distancia[i][j] = min(distancia_directa, distancia_circular)

# Guarda la matriz
with open("cost_transpose.txt", "w") as archivo:
    for fila in matriz_distancia:
        archivo.write(" ".join(map(str, fila)) + "\n")



"""
Generacion de archivo cost_replace.txt
"""
# 26x26
matriz_cost_replace = [[0] * 26 for _ in range(26)]

# Llena la matriz con valores aleatorios entre 0 y 13, asegurando simetría y costo 0 para reemplazo propio
for i in range(26):
    for j in range(i, 26):
        if i == j:
            matriz_cost_replace[i][j] = 0  # Costo 0 para reemplazarse a sí mismo
        else:
            costo = random.randint(1, 13)  # Costo entre 1 y 13
            matriz_cost_replace[i][j] = costo
            matriz_cost_replace[j][i] = costo

# Guarda la matriz
with open("cost_replace.txt", "w") as archivo:
    for fila in matriz_cost_replace:
        archivo.write(" ".join(map(str, fila)) + "\n")



"""
Generacion de archivo cost_insert.txt
"""
# Genera un arreglo de 26 valores aleatorios entre 1 y 13
arreglo_costos = [random.randint(1, 13) for _ in range(26)]

# Guarda el arreglo
with open("cost_insert.txt", "w") as archivo:
    archivo.write(" ".join(map(str, arreglo_costos)) + "\n")


"""
Generacion de archivo cost_delete.txt
"""
# Genera un arreglo de 26 valores aleatorios entre 1 y 13
arreglo_costos = [random.randint(1, 13) for _ in range(26)]

# Guarda el arreglo
with open("cost_delete.txt", "w") as archivo:
    archivo.write(" ".join(map(str, arreglo_costos)) + "\n")
