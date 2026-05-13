print("Bienvenido al cajero automático")
saldo = 1000

while True:
    print("Menu del cajero")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("Tu saldo es: " + str(saldo))
    
    elif opcion == "2":
        deposito = input("¿Cuánto quieres depositar? ")
        deposito = int(deposito)
        saldo = saldo + deposito
        print("Depósito realizado este es su nuevo saldo: " + str(saldo))
    
    elif opcion == "3":
        retiro = input("Cuanto deseas retirar ")
        retiro = int(retiro)
        
        if retiro > saldo:
            print("No hay saldo suficiente")
        elif retiro < 0:
            print("Cantidad no valida")
        else:
            saldo = saldo - retiro
            print("Retiro hecho: " + str(saldo))
    
    elif opcion == "4":
        print("Cajero apagado")
        break
    
    else:
        print("Opción no válida")