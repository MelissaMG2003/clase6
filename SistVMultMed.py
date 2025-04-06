class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
   
from datetime import datetime  # al inicio del archivo

def main():
    caninos = {}
    felinos = {}

    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            total_mascotas = len(caninos) + len(felinos)
            fecha = input("Ingrese la fecha de ingreso (dia/mes/año): ")
            try:
                datetime.strptime(fecha, "%d/%m/%Y")
                break  # fecha válida, salir del ciclo
            except ValueError:
                 print("Formato de fecha inválido. Use dd/mm/aaaa (por ejemplo: 06/04/2025)")
            if total_mascotas >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if historia in caninos or historia in felinos:
                print("ya existe la mascota con ese numero de historia clinica")
                continue
            nombre=input("Ingrese el nombre de la mascota: ")
            tipo=input("Ingrese el tipo de mascota (felino o canino): ")
            peso=int(input("Ingrese el peso de la mascota: "))
            fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
            nm=int(input("Ingrese cantidad de medicamentos: "))
            lista_med=[]

            for i in range(nm):
                while True: 
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    nombres_existentes = [med.verNombre().lower() for med in lista_med]
                    if nombre_medicamentos.lower() in nombres_extistentes:
                        print("Ya se ha asignado un medicamento con este nombre, ingrese uno diferente")
                        continue

                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    break

            mas= Mascota()
            mas.asignarNombre(nombre)
            mas.asignarHistoria(historia)
            mas.asignarPeso(peso)
            mas.asignarTipo(tipo)
            mas.asignarFecha(fecha)
            mas.asignarLista_Medicamentos(lista_med)
            
            if tipo == "canino":
                caninos[historia] = mas

            elif tipo == "felinos":
                felinos[historia] = mas


            else:
                print("Tipo de mascota invalido, ingrese nuevamente canino/felino")

        elif menu==2: # Ver fecha de ingreso
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            mascota = caninos.get(historia) or felinos.get(historia)
            # if servicio_hospitalario.verificarExiste == True
            if mascota:
                print("La fecha de ingreso de la mascota es: " mascota.verFecha())
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            total = len(caninos) + len(felinos)
            print("El número de pacientes en el sistema es: ", total)

        elif menu==4: # Ver medicamentos que se están administrando
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            mascota= caninos.get(historia) or felinos.get(historia)
            if mascota: 
                meds = mascota.verLista_medicamentos()
                print("Los medicamentos suministrados son: ")
                for m in meds:   
                    print(f"\n- {m.verNombre()} (dosis: {m.dosis()})")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            if historia in caninos:
                del caninos[historia]
                print("Mascota eliminada del sistema con exito")
            elif historia in felinos:
                del felinos[historia]
                print("Mascota eliminada del sistema con exito")

            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                


