peliculas = ["1: Tora! Tora! Tora! (1970)", "2: Dunkerque (Dunkirk, 2017)", "3: Greyhound (2020)", "4: Battleship (2012)", "5: The Hunt for Red October (1990)"]
reservas = []
boletos = 150
precio_boletos = 44
def nombre_cliente():
    while True:
        nombre = (input("Ingrese el nombre del cliente: \n")).capitalize().strip()
        if nombre == "":
            print("Ingrese un nombre valido (Error: nombre vacio)\n")
        else:
            return nombre
            
def ver_funciones():
    print("Funciones disponibles:")
    for pelis in peliculas:
        print(pelis)
            
def Atencion_cliente():
    global boletos
    
    while True:
        ver_funciones()
        try:
            funcion = int(input("ingrese el numero de la función que va a ver:\n"))
            if funcion < 1 or funcion > len(peliculas):
                raise IndexError("El número ingresado está fuera del rango permitido.")
            else:
                print("función seleccionada:", peliculas[funcion-1])
        except ValueError:
            print("caracter invalido, ingrese caracteres numericos enteros")
            continue
        nombre = nombre_cliente()
        while True:
            try:
                comprar = int(input("Ingrese la cantidad de boletos que desea comprar:\n"))
                if comprar < 0:
                    print("No se pueden comprar boletos negativos")
                else:
                    total = precio_boletos*comprar
                    print("Cantidad de boletos comprada: ", comprar, "\nPrecio total a pagar: Q", total ,"\nCantidad de boletos restantes: ", boletos-comprar)
                    break
            except ValueError:
                print("Valor invalido, ingrese solamente numeros enteros")
        print("\tResumen del pedido:\nfunción:", peliculas[funcion-1], "\nCantidad de boletos: ", comprar, "\nprecio a pagar: ", total, "\n")
        resumen = {
            "Nombre": nombre,
            "Función": peliculas[funcion - 1],
            "Boletos comprados": comprar,     
            "Precio a pagar": total        
        }
        reservas.append(resumen)
        continuar = input("Desea hacer otra compra? (s/n): ").lower()
        if continuar != 's':
            break
def mostrar_reserva():
    for i, r in enumerate(reservas, 1):
        print(f"#{i} \nCliente: {r['Nombre']} \nFunción: {r['Función']} \nBoletos: {r['Boletos comprados']} \nTotal: Q{r['Precio a pagar']}")
        
def menu():
    while True:
        print("\tSistema CineFácil\n1: ver funciones\n2: comprar boletos\n3:Mostrar reserva\n4: salir")
        try:
            opcion = int(input("Ingrese la opcion que desea elegir:\n "))
            if opcion == 1:
                ver_funciones()
            elif opcion == 2:
                Atencion_cliente()
            elif opcion == 3:
                mostrar_reserva()
            elif opcion == 4:
                print("saliendo del sistema")
                break
            else:
                print("ingrese una de las opciones disponibles (1-4)") 
        except ValueError:
            print("Ingrese valores numericos")

menu()