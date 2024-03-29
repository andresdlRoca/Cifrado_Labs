import math
import collections

alphabet = "abcdefghijklmnñopqrstuvwxyz"

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

def afin_bruteforce(cipher, k):
    results = []
    m = len(alphabet)
    for a in range(1,m):
        if math.gcd(a, m) == 1:
            for b in range(m):
                result = desencriptar_afin(cipher, a, b)
                metric = calc_metrics(result)
                results.append((metric, result, [a, b]))
    
    results.sort(key=lambda x: x[0])

    return results[:k]

def desencriptar_afin(cipher, a, b):

    m = len(alphabet)

    a_inv = pow(a, -1, m)
    texto_desencriptado = ""

    for letra in cipher:
        if letra in alphabet:
            y = alphabet.index(letra)
            x = a_inv * (y - b) % m
            texto_desencriptado += alphabet[x]
        else:
            texto_desencriptado += letra

    return texto_desencriptado

def main():
    with open("cipher2.txt", "r") as file:
        cipher = file.read()

    ciphertext = cipher.lower()
    results = afin_bruteforce(ciphertext, 5)

    print("Mejores resultados:")
    counter = 1
    for result in results:
        print(f"Resultado {counter}, Llaves {result[2]}: {result[1]}")
        print(f"Distancia euclidiana: {result[0]}")
        print('\n')
        counter += 1

main()