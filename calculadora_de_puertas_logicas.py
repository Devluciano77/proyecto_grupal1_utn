# -- Calculadora de puertas lógicas --

# Funcion para pedir valor
def ingresar_NumBinario(num):
    while True:
        valor = input(num)
        if valor in ("0", "1"):
            return int(valor)
        print("Por favor, ingresa un número binario que sea 1 o 0.")

# Funciones de las puertas lógicas
def AND(a, b): 
    return a & b
def OR(a, b): 
    return a | b
def NOT(a): 
    return 1 - a
def NAND(a, b): 
    return 1 - (a & b)
def XOR(a, b): 
    return a ^ b
def NOR(a, b): 
    return 1 - (a | b)

# Menu de opciones de puertas logicas
def mostrar_menu():
    print("Opciones disponibles:")
    print("1. AND       4. NAND")
    print("2. OR        5. XOR")
    print("3. NOT       6. NOR      7. Salir")

# Bucle principal
print("=== Calculadora de Puertas Lógicas ===")
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-7): ")

    if opcion == "7":
        print("¡Chau, te esperamos para que vuelvas!")
        break

    elif opcion in ("1", "2", "4", "5", "6"):
        num1 = ingresar_NumBinario("Ingresa el primer número binario: ")
        num2 = ingresar_NumBinario("Ingresa el segundo número binario: ")

        if opcion == "1":
            resultado = AND(num1, num2)
            nombre = "AND"
        elif opcion == "2":
            resultado = OR(num1, num2)
            nombre = "OR"
        elif opcion == "4":
            resultado = NAND(num1, num2)
            nombre = "NAND"
        elif opcion == "5":
            resultado = XOR(num1, num2)
            nombre = "XOR"
        elif opcion == "6":
            resultado = NOR(num1, num2)
            nombre = "NOR"

        print("===================================")
        print(f"Resultado de la puerta {nombre}: {resultado}")
        print("===================================")

    elif opcion == "3":
        num3 = ingresar_NumBinario("Ingresa un número binario (0 o 1): ")
        print("===================================")
        print(f"Resultado de la puerta NOT: {NOT(num3)}")
        print("===================================")

    else:
        print("Opción no válida. Intenta de nuevo.")

