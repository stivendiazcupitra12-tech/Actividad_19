seleccionmenu = 0
while seleccionmenu != 3: 
    print("Menu Principal")
    print("1. Par o Impar")
    print("2. Tablas de multiplicar")
    print("3. Salir")

    
    seleccionmenu = int(input("Elija una opción: "))

    if seleccionmenu == 1:
        submenu = 0
        while submenu != 2:
            print("Menu Par o Impar")
            print("1. Ingresar un número")
            print("2. Volver")
            submenu = int(input("Elija una opción: "))
            if submenu == 1:
                numero = int(input("Ingrese el número: "))
                if numero % 2 == 0:
                    print(f"El número {numero} es par")
                else:
                    print(f"El número {numero} es impar")

    elif seleccionmenu == 2:
        submenu = 0
        while submenu != 2:
            print("Menu Tabalas De Multiplicar")
            print("1. Generar tabla")
            print("2. Volver") 
            submenu = int(input("Elija una opción: "))
            if submenu == 1:
                numero = int(input("Ingrese el número: "))
                print(f"Tabla del {numero}:")
                for a in range(1, 11):
                    print(f"{numero} * {a} = {numero * a}")
            elif submenu == 2:
                break 

    elif seleccionmenu == 3:
        print("Adios")
    else:
        print("Opción no válida")
#No debe tener ningun fallo
