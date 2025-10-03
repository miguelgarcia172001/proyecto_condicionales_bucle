# Este programa determina si una persona es mayor de edad
# y luego permite ingresar calificaciones hasta que el usuario decida salir.

# Solicita la edad del usuario
edad = int(input("Ingrese su edad: "))

# Estructura condicional para verificar mayoría de edad
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("\nAhora vamos a ingresar calificaciones.")

# Bucle while con condición de salida manual
while True:
    # Entrada del usuario
    entrada = input("Ingresa una calificación (o escribe 'salir' para terminar): ")

    # Verifica si el usuario quiere salir
    if entrada.lower() == 'salir':
        print("Has salido del programa.")
        break

    # Verifica que lo ingresado sea un número válido
    if entrada.isdigit():
        calificacion = int(entrada)

        # Estructura lógica anidada para clasificar la calificación
        if calificacion >= 90:
            print("Excelente")
        elif calificacion >= 80:
            print("Muy bien")
        elif calificacion >= 70:
            print("Bien")
        elif calificacion >= 60:
            print("Suficiente")
        else:
            print("Insuficiente")
    else:
        print("Entrada inválida. Por favor ingresa un número o 'salir'.")
