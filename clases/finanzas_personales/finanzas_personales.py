class finanzas:
    def __init__(self):
        self.historial = list()
     
    #* Crear un registro nuevo y almacenarlo en una lista
    def crear_transaccion(self,tipoTransaccion):
        
        try :
            descripcion = input("Escriba la descripcion de la transaccion: ")
            monto = input("Ingrese el monto de la transaccion: ").strip()
            if monto.isdigit():
                registro = dict()
                registro.setdefault("id",len(self.historial)+1)
                registro.setdefault("moneda","cordoba")
                registro.setdefault("descripcion",descripcion)
                registro.setdefault("tipoTransaccion",tipoTransaccion)
                registro.setdefault("monto",int(monto))
                self.historial.append(registro)
            else:
                print("Caracteres invalidos")
        except ValueError as e:
            print("Error de entrada",e)
        except Exception as e:
            print("Ocurrió un error inesperado",e)

      
    #? Editar un registro    
    def editar_registro(self):
        if len(self.historial) == 0:
                print("No hay transacciones registradas.")
        try:
            idItem = input("Ingrese el id del registro a traer: ").strip()
            if not idItem.isdigit():
                print("id inválido. Debe ser un número.")
                return
            idItem = int(idItem)

            for item in self.historial:
                if item["id"] == idItem:
                    print("Moneda del registro:", item["moneda"], "| Descripción:", item["descripcion"], "| Monto:", item["monto"])
                    
                    # Actualización de datos
                    descripcion = input("Escriba la descripción de la transacción (actual: {}): ".format(item["descripcion"])).strip() or item["descripcion"]
                    monto = input("Ingrese el monto de la transacción (actual: {}): ".format(item["monto"])).strip()
                    tipoTransaccion = input("Ingrese el tipo de transacción (actual: {}, ejem: ingreso o egreso): ".format(item["tipoTransaccion"])).strip().lower()

                    if monto and not monto.isdigit():
                        print("El monto debe ser un número.")
                        return
                    
                    # Validaciones finales
                    item["descripcion"] = descripcion
                    item["monto"] = int(monto) if monto else item["monto"]
                    item["tipoTransaccion"] = tipoTransaccion if tipoTransaccion in ["ingreso", "egreso"] else item["tipoTransaccion"]

                    print("El registro se ha actualizado satisfactoriamente!")
                    return
            print("No se encontró un registro con ese id.")
        except Exception as e:
            print("Ocurrió un error inesperado:", e)


    #* Historial de tipo de transaccion ya sea ingreo o egreso
    def historial_tipo_transaccion(self, tipoTransaccion):
            
            # Valida si la lista de historial está vacia
            if len(self.historial) == 0:
                print("No hay transacciones de tipo {} registradas.".format(tipoTransaccion))

            # Usa un contador para asignar un numero creciente por cada registro encontrado 
            counter = 1                      
            for item in self.historial:                
                if(item["tipoTransaccion"] == tipoTransaccion):
                    print(counter,"- Moneda de la transaccion: ",item["moneda"]," Descripcion de la transaccion: ",item["descripcion"]," Monto: ",item["monto"]," Tipo de transaccion: ",item["tipoTransaccion"])
                    counter +=1


    #! Borrar un Registro
    def borrar_registro(self):
        # Valida si la lista de historial está vacia
        if len(self.historial) == 0:
                print("No hay transacciones registradas.")
        try:
            # Se ingresa el id correcto y se valida para su postrior borrado
            idItem = input("Ingrese el id del registro a traer: ").strip()
            if not idItem.isdigit():
                print("id inválido. Debe ser un número.")
                return
            idItem = int(idItem)

            for item in self.historial:
                if item["id"] == idItem:
                    self.historial.remove(item)
                    print("El registro ha sido borrado exitoamente")
        except Exception as e:
            print("Ocurrió un error inesperado:", e)
