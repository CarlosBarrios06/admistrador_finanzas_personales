from clases.finanzas_personales.finanzas_personales import finanzas

# Se asigna la clase a una variable
registro_finanzas = finanzas()
while True:
    
    print("Elige una opcion:")
    print("1- Ingreso")
    print("2- Egreso")
    print("3- Historial")
    print("4- Historial de Ingresos")
    print("5- Historial de Egresos")
    print("6- Editar Registro")
    print("7- Borrar Registro")
    print("8- Balance General")
    print("0- Salir")   
    
   
    try:   
        opc = input("Ingresa la opcion deseada: ").strip()
        if not opc.isdigit():
            print("Entrada inválida. Por favor, ingresa un número.")
            continue
        opc = int(opc)

        if(opc == 0):
            exit()

        elif(opc > 8):
            print("Opcion fuera de rango!")

        elif(opc == 1):
          registro = registro_finanzas.crear_transaccion("ingreso")
        
        elif(opc == 2):
           registro = registro_finanzas.crear_transaccion("egreso")
        elif(opc == 3):
            historial = registro_finanzas.historial
            if len(historial) == 0:
                print("No hay transacciones registradas.")
            counter = 1
            for item in historial:
                print(counter,"- Moneda de la transaccion: ",item["moneda"]," Descripcion de la transaccion: ",item["descripcion"]," Monto: ",item["monto"]," Tipo de transaccion: ",item["tipoTransaccion"]) 
                counter +=1
        elif(opc == 4):
            historicoIngresos = registro_finanzas.historial_tipo_transaccion("ingreso")
        elif(opc == 5):
            historicoIngresos = registro_finanzas.historial_tipo_transaccion("egreso")       
        elif(opc == 6):
           registro_finanzas.editar_registro()
        elif(opc == 7):
           registro_finanzas.borrar_registro()
        else:
            ingreso = list()
            egreso = list()

            for item in registro_finanzas.historial:
                if (item["tipoTransaccion"] == "ingreso"):
                    ingreso.append(item["monto"])
                else:
                    egreso.append(item["monto"])
            balance = sum(ingreso) - sum(egreso)
            print(f"El balance general actual es: {balance}")
    except Exception as e:
        print("Opcion Invalida",e)
        