from conversiones import *
from cuento import mostrar_cuento
from operaciones import *

def main():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Operaciones matemáticas")
    print("2. Conversiones")
    print("3. Mostrar cuento")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        print("Suma:", sumar(a, b))
        print("Resta:", restar(a, b))
        print("Multiplicación:", multiplicar(a, b))
        print("División:", dividir(a, b))

    elif opcion == "2":
        km = float(input("Ingrese kilómetros: "))
        print(f"{km} kilómetros son {kilometros_a_millas(km):.2f} millas")

    elif opcion == "3":
        mostrar_cuento()

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
