cuentas = {
    "1234"
    "5678"
    "3274"
}

while True: 
    print("CAJERO AUTOMATICO")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print()"6". Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: {saldo} dolares")
    elif opcion == "2":
        monto = int(input("Ingrese el monto a retirar."))
        if monto > saldo:
            print(f"Su saldo es insuficiente. Tu saldo actual es, {saldo}")

        else: 
            saldo -= monto 
            print(f"Su retiro fue exitoso. su saldo retante es de: {saldo} ")

    elif opcion == "3":
        deposito = float(input("Ingrese el valor a depositar."))

        if deposito <= 0: 
            print("Su deposito debe ser mayor a 0")
        else:
            saldo += deposito
            print(f"su deposito fue exitoso. su nuevo saldo es. {saldo}")

    elif opcion =="4":
        print("Gracias por utilizar nuestros servicios, Hasta pronto")
        break
    else: 
        print("Opcion invalida intentelo de nuevo")