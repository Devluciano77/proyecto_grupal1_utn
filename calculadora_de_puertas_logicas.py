def ingresarDosBinariosValidos():
    num1 = int(input("ingresar el primer numero binario"))
    num2 = int(input("ingresar el segundo numero binario"))

    # si los valores ingresados son mayores a 1 o son menores a 0 se ejecuta el while y se pide que se reingrese el valor incorrecto
    # el while se ejecuta hasta que se ingrese el valor correcto (0 o 1)
    while num1 > 1 or num2 < 0:
        num1 = int(input(f"error {num1} no es un numero binario , ingrese un 0 o un 1"))

    while num2 > 1 or num2 < 0:    
        num2 = int(input(f"error {num2} no es un numero binario , ingrese un 0 o un 1"))

    # se envía los valores verificados a la funcion simuladorDeCompuertas
    seleccionarOperacion(num1, num2)

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
    return 1 - (num1 | num2 )

def seleccionarOperacion(num1, num2):
     operacion = input("ingresar la operacion que quieres realizar (AND, OR, NOT, NAND, NOR, XOR)")

     while True:
        if operacion.upper() == "AND":
            print(f"Puerta AND {AND(num1, num2)}")
            break
        elif operacion.upper() == "OR":
            print(f"Puerta OR {OR(num1, num2)}") 
            break
        elif operacion.upper() == "NOT":  
            print(f"Primer valor NOT {NOT(num1)}")
            print(f"Segundo valor NOT {NOT(num2)}")
            break
        elif operacion.upper() == "NAND":  
            print(f"Puerta NAND {NAND(num1, num2)}")
            break
        elif operacion.upper() == "NOR":   
            print(f"Puerta NOR {NOR(num1, num2)}")
            break
        elif operacion.upper() == "XOR":   
            print(f"Puerta XOR {XOR(num1, num2)}")
            break
        else:
            operacion = input(f"la operacion ingresada {operacion} es incorrecta, ingresar la operacion que quieres realizar (AND, OR, NOT, NAND, NOR, XOR)")
        

ingresarDosBinariosValidos()