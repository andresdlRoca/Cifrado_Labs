import math
import collections

def calc_metrics(texto):
    frecuencias_castellano = {
        'a': 0.125,
        'b': 0.022,
        'c': 0.045,
        'd': 0.058,
        'e': 0.119,
        'f': 0.017,
        'g': 0.017,
        'h': 0.007,
        'i': 0.062,
        'j': 0.005,
        'k': 0.001,
        'l': 0.049,
        'm': 0.031,
        'n': 0.067,
        'ñ': 0.003,
        'o': 0.093,
        'p': 0.022,
        'q': 0.009,
        'r': 0.065,
        's': 0.079,
        't': 0.046,
        'u': 0.029,
        'v': 0.010,
        'w': 0.004,
        'x': 0.001,
        'y': 0.009,
        'z': 0.005,
    }

    frecuencias_texto = calc_frequency(texto)
    distance = calc_euclidian_distance(frecuencias_texto, frecuencias_castellano)

    return distance

def calc_frequency(texto):
    frecuencias = collections.Counter(texto)
    return frecuencias

def calc_euclidian_distance(frecuencias_texto, frecuencias_castellano):
    distance = math.sqrt(sum((frecuencias_texto.get(letra, 0) - frecuencias_castellano.get(letra, 0))**2 for letra in set(frecuencias_texto) | set(frecuencias_castellano)))
    return distance

def vigenere_bruteforce(cipher, k):
    return 0

def main():
    with open("cipher2.txt", "r") as file:
        cipher = file.read()

    ciphertext = cipher.lower()
    results = vigenere_bruteforce(cipher, 5)

    print("Mejores resultados:")
    counter = 1
    for result in results:
        print(f"Resultado {counter}: {result[1]}")
        print(f"Distancia euclidiana: {result[0]}")
        print('\n')
        counter += 1

main()