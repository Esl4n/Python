import data
import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root",password="",database="farmacia")
cursor1 = conexion1.cursor()


def tens():
    ini = True
    while ini:
        try:    
            sw=True
            while sw:
                data.mainTens()
                res=data.res()
                if res== 1:
                    print("__________________________________________")

                    data.ingReceta()
                    print("__________________________________________")

                elif res==2:
                    print("__________________________________________")

                    data.buscarMedic()
                    print("__________________________________________")

                elif res==3:
                    print("__________________________________________")

                    data.modificarMed()
                    print("__________________________________________")

                elif res==4:
                    print("__________________________________________")

                    data.verFamiliasMed()
                    print("__________________________________________")

                else:
                    print('adios')
                    sw=False
                    ini=False
        except KeyboardInterrupt:
            print('Esa Funcion no existe')
        
    return


def bodeguero():
    ini=True
    while ini:
        try:
            sw=True
            while sw:
                data.mainBodeguero()
                res=data.res()
                if res== 1:
                    print("__________________________________________")

                    data.controlStock()
                    print("__________________________________________")

                elif res==2:
                    print("__________________________________________")

                    data.ingresarMedicamentos()
                    print("__________________________________________")

                else:
                    print('adios')
                    sw=False
                    ini=False
        except KeyboardInterrupt:
            print('Esa Funcion no existe')

    return




def jefe():
    ini=True
    while ini:
        try:
            sw=True
            while sw:
                data.mainJefe()
                res=data.res()    
                
                if res== 1:
                    print("__________________________________________")
                    print('Medicamentos:')
                    data.visualizarMed()

                    print("__________________________________________")

                elif res==2:
                    print("__________________________________________")
                    print('Empleados: ')

                    
                    data.verEmpleados()

                    print("__________________________________________")

                elif res==3:

                    print("__________________________________________")

                    data.ingEmpleados()
                    print("__________________________________________")

                elif res==4:
                    print("__________________________________________")

                    data.modicarEmpelado()
                    print("__________________________________________")

                elif res==5:
                    print("__________________________________________")

                    data.eliminarEmpleado()
                    print("__________________________________________")

                else:
                    sw=False
                    ini=False
        except KeyboardInterrupt:
            print('Esa Funcion no existe')
    return 