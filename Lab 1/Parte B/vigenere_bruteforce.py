import math
import collections
import itertools
import textwrap

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

def vigenere_bruteforce(cipher, k):
    results = []
    m = len(alphabet)

    key_length = 1
    while key_length <= len(cipher):
        for key in generate_keys(key_length):
            result = ""
            clave_repetida = (key * (len(cipher) // key_length)) + key[:len(cipher) % key_length]
            for i in range(len(cipher)):
                if cipher[i] in alphabet:
                    decrypted_letter = descifrar_letra_vigenere(cipher[i], clave_repetida[i], alphabet)
                    result += decrypted_letter
                else:
                    result += cipher[i]
            metric = calc_metrics(result)
            results.append((metric, result, key))

        key_length += 1

    results.sort(key=lambda x: x[0])

    return results[:k]

def generate_keys(key_length):
    return [''.join(p) for p in itertools.product(alphabet, repeat=key_length)]

def descifrar_letra_vigenere(letra_cifrada, letra_clave, alfabeto):
    indice_letra_cifrada = alfabeto.index(letra_cifrada)
    indice_letra_clave = alfabeto.index(letra_clave)
    indice_letra_original = (indice_letra_cifrada - indice_letra_clave) % len(alfabeto)
    return alfabeto[indice_letra_original]

def desencriptar_vigenere(cipher, key):
    m = len(alphabet)

    result = ""
    clave_repetida = (key * (len(cipher) // len(key))) + key[:len(cipher) % len(key)]

    for i in range(len(cipher)):
        if cipher[i] in alphabet:
            y = alphabet.index(cipher[i])
            x = alphabet.index(clave_repetida[i])
            result += alphabet[(y - x) % m]
        else:
            result += cipher[i]

    return result


def main():
    with open("cipher3.txt", "r") as file:
        cipher = file.read()

    ciphertext = cipher.lower()
    ciphertext = textwrap.wrap(ciphertext, 50)
    print(ciphertext[0])
    results = vigenere_bruteforce(ciphertext[0], 5)

    print("Mejores resultados:")
    counter = 1
    for result in results:
        print(f"Resultado {counter}: {result[1]}")
        print(f"Distancia euclidiana: {result[0]}")
        print('\n')
        counter += 1

main()