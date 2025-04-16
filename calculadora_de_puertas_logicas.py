# -- Calculadora de puertas lógicas -- 

# Funciones de las puertas logicas
def AND(num1, num2):
    return num1 & num2
def OR(num1, num2):
    return num1 | num2
def NOT(num1):
    return 1 - num1
def NAND(num1, num2):
    return 1 - (num1 & num2)
def XOR(num1, num2):
    return num1 ^ num2
def NOR(num1, num2):
    return 1 - (num1 | num2)
# Pedir los valores
print("=== Calculadora de Puertas Lógicas ===")
print("Solo puedes ingresar 0 o 1")

# los print son de prueba para las funciones
print(XOR(1,0))
print(XOR(1,1))
print(XOR(0,1))
print(XOR(0,0))
# Menú de operaciones


# Procesar la operación
