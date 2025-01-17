import msvcrt

print("Hola, como estas")

name= str(input("Ingresa tu nombre \n"))
print(f"tu nombre es:{name}")

print("Presiona cualquier tecla para continuar...")
msvcrt.getch()  # Esto espera una tecla sin necesidad de presionar Enter

'''
Tipos básicos (primitivos):

    int: Números enteros.
        Ejemplo: 10, -5, 0
    float: Números decimales o de punto flotante.
        Ejemplo: 3.14, -2.5, 0.0
    complex: Números complejos (con parte real e imaginaria).
        Ejemplo: 3 + 5j, -1j
    str: Cadenas de texto (secuencia de caracteres).
        Ejemplo: "Hola", 'Python'
    bool: Valores lógicos (verdadero o falso).
    Ejemplo: True, False


    Estructuras de datos (colecciones):

    list: Lista (mutable, ordenada, permite duplicados).
        Ejemplo: [1, 2, 3], ["a", "b", "c"]
    tuple: Tupla (inmutable, ordenada, permite duplicados).
        Ejemplo: (1, 2, 3), ("a", "b", "c")
    set: Conjunto (mutable, no ordenado, no permite duplicados).
        Ejemplo: {1, 2, 3}, {"a", "b", "c"}
    frozenset: Conjunto inmutable.
        Ejemplo: frozenset({1, 2, 3})
    dict: Diccionario (clave-valor, mutable, no ordenado en versiones <3.7).
        Ejemplo: {"clave": "valor", "a": 1, "b": 2}

Tipos binarios:

    bytes: Secuencia de bytes (inmutable).
        Ejemplo: b"Hola"
    bytearray: Secuencia de bytes (mutable).
        Ejemplo: bytearray(b"Hola")
    memoryview: Vista en memoria de un objeto binario.
        Ejemplo: memoryview(b"Hola")

'''
