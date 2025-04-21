# -- Calculadora de puertas lógicas -- 

# ingreso de datos binarios
def ingresar_NumBinario (num):
    while True:
        valor = input(num)
        if valor == "0" or valor == "1":
            # checkea que el valor sea un numero binario
            return int(valor)
        else:
            print("Por favor, ingresa un numero binario que sea 1 o 0")


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

print("=== Calculadora de Puertas Lógicas ===")

# menu de opciones de puertas logicas 
while True:
  print("Opciones disponibles:")
  print("1. AND")
  print("2. OR")
  print("3. NOT")
  print("4. NAND")
  print("5. XOR")
  print("6. NOR")
  print("7. Salir")
  
  opcion = input("Selecciona una opción (1-7): ")

  # proceso de la informacion
  if opcion in ("1","2","4","5","6"): 
      # si esta dentro de estas opciones
      print("Solo puedes ingresar 0 o 1")
      num1 = ingresar_NumBinario("Ingresa el primer número binario: ")
      num2 = ingresar_NumBinario("Ingresa el segundo número binario: ")
  if opcion == '3': 
      # si la opcion elegida es la 3
      print("Solo puedes ingresar 0 o 1")
      num = ingresar_NumBinario("Ingresa un número binario (0 o 1): ")
      print(f"Resultado de la puerta not: {NOT(num)}")
  if opcion == '7':
      # si la opcion elegida es la 7
      print("¡Chau, te esperamos para que vuelvas!")
      break
  if opcion == "1":
     print(f"Resultado de la puerta AND:{AND (num1, num2)}")
  elif opcion == '2':
     print(f"Resultado de la puerta OR: {OR (num1, num2)}")
  elif opcion == '4':
     print(f"Resultado de la puerta NAND: {NAND(num1, num2)}")
  elif opcion == '5':
     print(f"Resultado de la puerta XOR: {XOR(num1, num2)}")
  elif opcion == '6':
     print(f"Resultado de la puertaNOR: {NOR(num1, num2)}")
