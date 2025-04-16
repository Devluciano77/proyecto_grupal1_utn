def ingresarDosBinariosValidos():
    num1 = int(input("ingresar el primer numero binario"))
    num2 = int(input("ingresar el segundo numero binario"))

    # si los valores ingresados son mayores a 1 o son menores a 0 se ejecuta el while y se pide que se reingrese el valor incorrecto
    # el while se ejecuta hasta que se ingrese el valor correcto (0 o 1)
    while num1 > 1 or num2 < 0:
        num1 = int(input(f"error {num1} no es un numero binario , ingrese un 0 o un 1"))

    while num2 > 1 or num2 < 0:    
        segundoValor = int(input(f"error {segundoValor} no es un numero binario , ingrese un 0 o un 1"))

    # se envía los valores verificados a la funcion simuladorDeCompuertas
    simuladorDePuertasLogicas(num1, num2)
  

def simuladorDePuertasLogicas(num1, num2):
        print(f"Compuerta AND {num1 and num2}")
        print(f"Compuerta OR {num1 or num2}")
        print(f"Primer valor NOT {1 - num1}")
        print(f"Segundo valor NOT {1 - num2}")
        print(f"Compuerta NAND {1 - (num1 and num2)}")
        print(f"Compuerta NOR {1 - (num1 or num2)}")
        print(f"Compuerta XOR {num1 ^ num2}")
        

ingresarDosBinariosValidos()