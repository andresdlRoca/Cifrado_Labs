import unicodedata
import re
from prettytable import PrettyTable


def eliminar_tildes(s):
    s = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        unicodedata.normalize( "NFD", s), 0, re.I
    )

    return unicodedata.normalize("NFC", s)

def calcular_dist(texto_cifrado):
    # Calcular la distribucion de los caracteres

    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    m = len(alfabeto)

    distribucion = {letra: 0 for letra in alfabeto}

    total_caracteres = 0
    for letra in texto_cifrado:
        if letra.isalpha():
            distribucion[letra] += 1
            total_caracteres += 1
    
    for letra in distribucion:
        distribucion[letra] = (distribucion[letra] / total_caracteres) * 100

    return distribucion

def mostrar_dist(distribucion):
    # Mostrar la distribucion de los caracteres

    tabla = PrettyTable()
    tabla.field_names = ["Letra", "Frecuencia"]

    for letra, frecuencia in distribucion.items():
        tabla.add_row([letra, "{:.2f}".format(frecuencia)])

    print(tabla)

def comparar_dist(distribucion):

    # Distribucion de caracteres en español
    dist_espanol = {
        'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70, 'i': 6.25,
        'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68, 'p': 2.51, 'q': 0.88,
        'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.02, 'x': 0.22, 'y': 0.90, 'z': 0.52
    }

    tabla = PrettyTable()
    tabla.field_names = ["Letra", "Frecuencia", "Frecuencia español"]

    for letra, frecuencia in distribucion.items():
        tabla.add_row([letra, "{:.2f}".format(frecuencia), "{:.2f}".format(dist_espanol[letra])])

    print(tabla)

def main():
    run = True

    while run:
        print("\nCifrado Vigenere")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if(opcion == 1):
            texto = input("Ingrese el texto a encriptar: ")
            clave = input("Ingrese la clave: ")
            texto_encriptado = encriptartexto(texto, clave)
            print("Texto encriptado: " + texto_encriptado)
            print("\nDistribucion de caracteres: ")
            mostrar_dist(calcular_dist(texto_encriptado))
            print("\nComparacion con distribucion de caracteres en español: ")
            comparar_dist(calcular_dist(texto_encriptado))

        elif(opcion == 2):
            texto = input("Ingrese el texto a desencriptar: ")
            clave = input("Ingrese la clave: ")
            print("Texto desencriptado: " + desencriptartexto(texto, clave))
        elif(opcion == 3):
            run = False
            break
        else:
            print("Opcion no valida")

def encriptartexto(texto, clave):
    # Encriptar texto con cifrado vigenere

    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    m = len(alfabeto)

    texto = texto.lower()
    texto = eliminar_tildes(texto)
    texto_encriptado = ""

    clave_repetida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        # Concatenar caracteres especiales
        if texto[i].isalpha():
            x = alfabeto.index(texto[i])
            y = alfabeto.index(clave_repetida[i])
            texto_encriptado += alfabeto[(x + y) % m]
        else:
            texto_encriptado += texto[i]

    return texto_encriptado

def desencriptartexto(texto, clave):
    # Desencriptar texto con cifrado vigenere

    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    m = len(alfabeto)

    texto = texto.lower()
    texto = eliminar_tildes(texto)
    texto_encriptado = ""

    clave_repetida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]

    for i in range(len(texto)):
        # Concatenar caracteres especiales
        if texto[i].isalpha():
            y = alfabeto.index(texto[i])
            x = alfabeto.index(clave_repetida[i])
            texto_encriptado += alfabeto[(y - x) % m]
        else:
            texto_encriptado += texto[i]

    return texto_encriptado

main()