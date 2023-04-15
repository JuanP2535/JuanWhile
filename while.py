import math

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

continuar = True

while continuar:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    opcion = ''

    while opcion != '9':
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potenciación")
        print("6. Factorial")
        print("7. Raíz cuadrada")
        print("8. Cambiar números")
        print("9. Salir")
    
        opcion = input("Ingrese una opción: ")
    
        if opcion == '1':
            resultado = numero1 + numero2
            print("El resultado de la suma es:", resultado)
        elif opcion == '2':
            resultado = numero1 - numero2
            print("El resultado de la resta es:", resultado)
        elif opcion == '3':
            resultado = numero1 * numero2
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == '4':
            if numero2 == 0:
                print("No se puede dividir entre cero")
            else:
                resultado = numero1 / numero2
                print("El resultado de la división es:", resultado)
        elif opcion == '5':
            resultado = numero1 ** numero2
            print("El resultado de la potenciación es:", resultado)
        elif opcion == '6':
            if numero1 < 0:
                print("El número debe ser positivo")
            else:
                resultado = factorial(int(numero1))
                print("El factorial de", numero1, "es:", resultado)
        elif opcion == '7':
            if numero1 < 0:
                print("El número debe ser positivo")
            else:
                resultado = math.sqrt(numero1)
                print("La raíz cuadrada de", numero1, "es:", resultado)
        elif opcion == '8':
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
        elif opcion == '9':
            respuesta = input("¿Desea continuar (s/n)? ")
            if respuesta.lower() == 's':
                opcion = '0'
            else:
                continuar = False
                print("Adiós!")
        else:
            print("Opción inválida")
