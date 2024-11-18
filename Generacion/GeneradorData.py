# Generar datasets más específicos basados en las nuevas instrucciones del usuario
import os
import random
import string

# Funciones para generar cadenas y casos
def random_string(length):
    """Genera una cadena aleatoria de longitud especificada."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_equal_length_cases(n):
    """Genera casos donde las cadenas tienen el mismo largo de 1 a 15, creciendo gradualmente."""
    cases = []
    cont = 1
    for length in range(1, 16):
        if cont == 1:
            cases.append((random_string(length), random_string(length)))
            cont-=1
        cases.append((random_string(length), random_string(length)))
    return cases

def generate_empty_and_random_cases1(n):
    """Genera casos con un string vacío y otro string aleatorio, con longitudes crecientes."""
    cases = []
    cont = 1
    for length in range(0, n + 1):
        str1 = ""
        str2 = random_string(length)  # Longitud creciente de 1 a n
        if cont == 1:
            cases.append((str1, str2))
            cont -=1
        cases.append((str1, str2))
    return cases

def generate_empty_and_random_cases2(n):
    """Genera casos con un string vacío y otro string aleatorio, con longitudes crecientes."""
    cases = []
    cont = 1
    for length in range(0, n + 1):
        str2 = ""
        str1 = random_string(length)  # Longitud creciente de 1 a n
        if cont == 1:
            cases.append((str1, str2))
            cont-=1
        cases.append((str1, str2))
    return cases


def generate_transposed_cases(n):
    """Genera casos con transposiciones de a pares, con longitudes crecientes."""
    cases = []
    cont = 1
    for length in range(2, n + 1, 2):  # Longitudes crecientes de a 2
        # Crear una cadena base con caracteres aleatorios
        str1 = ''.join(random.choices(string.ascii_lowercase, k=length))
        str2 = list(str1)
        
        # Realizar transposiciones de cada par consecutivo
        for i in range(0, length, 2):
            str2[i], str2[i + 1] = str2[i + 1], str2[i]
        
        # Agregar el caso generado a la lista
        if cont:
            cases.append((str1, ''.join(str2)))
            cont = 0
        cases.append((str1, ''.join(str2)))
    return cases

def generate_repeted_cases(n, total_length=13, min_substr_len=1, max_substr_len=13):
    """Genera casos con cadenas que repiten la misma letra aleatoria y crecen en longitud."""
    cases = []
    cont = 1
    # Incrementar el tamaño de las cadenas en cada caso, desde 5 hasta 13
    for i in range(n):
        # El tamaño de la cadena crece de 5 a 13 en cada caso
        substr_len = min_substr_len + i  # Esto asegura que el tamaño vaya de 5 a 13
        
        # Elegir una letra aleatoria minúscula
        letra = random.choice(string.ascii_lowercase)
        
        # Generamos las dos cadenas con la misma letra repetida
        cadena = letra * substr_len
        
        # Agregamos el caso a la lista
        if cont:
            cases.append((cadena, cadena))
            cont = 0
        cases.append((cadena, cadena))

    return cases

# Generar y guardar los datasets
def write_dataset(filename, cases):
    """Escribe un dataset en un archivo."""
    with open(filename, "w") as f:
        f.write(f"{len(cases)}\n")
        for str1, str2 in cases:
            f.write(f"{len(str1)} {len(str2)}\n")
            f.write(f"{str1}\n{str2}\n")

# Generar los datasets según lo solicitado
datasets = {
    "IgualLargo.txt": generate_equal_length_cases(10),
    "VacioS2.txt": generate_empty_and_random_cases2(14),
    "VacioS1.txt": generate_empty_and_random_cases1(14),
    "Transposiciones.txt": generate_transposed_cases(15),
    "LetrasRepetidas.txt": generate_repeted_cases(15),
}

output_dir = "/home/moonturtle/algoco/T23/Datasets"
os.makedirs(output_dir, exist_ok=True)

for filename, cases in datasets.items():
    write_dataset(os.path.join(output_dir, filename), cases)

output_dir
