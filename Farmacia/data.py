from datetime import datetime
import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root",password="",database="farmacia")
cursor1 = conexion1.cursor()



def mainTens():
    menu = '''
    1-Ingresar receta y usuario
    2-Buscar Medicamentos
    3-Modificar Medicamentos
    4-Familias de Medicamentos
    5-Salir
    '''
    print(menu)



def mainBodeguero():
    menu = '''
    1-Control de Stock
    2-Ingresar Medicamento
    3-Salir
    '''
    print(menu)



def mainJefe():
    menu = '''
    1-Visualizar medicamentos 
    2-Ver empleados
    3-Ingresar empleado
    4-Modificar Empleado
    5-Eliminar Empleado
    6-Salir    
    '''
    print(menu)



def res():
    sw=True
    while sw:
        try:
            res=int(input('escoja una accíon: '))
            while (res<1 or res>6):
                res=int(input('escoja una accíon: '))
            sw=False
        except ValueError:
            print('Digito Invalido!')  
    return res 





#FUNCIONES TENS






def ingReceta():
    try:
        print('Para volver Oprimir CTRL + C')
        print('formato: YYYY-MM-DD')
        sw = True
        while sw:
            try:
                fecha = input('Ingrese La Fecha de la receta : ')
                datetime.strptime(fecha, '%Y-%m-%d')
                sw= False
            except ValueError:
                print('Formato Invalido')
        print('Datos Cliente:')
        rut=input('Rut: ')
        while (len(rut)< 9):
            rut=input('Rut: ')

        Nombre=input('Nombre: ')
        while Nombre == '':
            print('No puede quedar en Blanco')
            Nombre=input('Nombre: ')

        sNombre=input('Segundo Nombre: ')
        while sNombre == '':
            print('No puede quedar en Blanco')
            sNombre=input('Segundo Nombre: ')


        aP=input('Apellido Paterno: ')
        while aP == '':
            print('No puede quedar en Blanco')
            aP=input('Apellido Paterno: ')
            
        aM=input('Apellido Materno: ') 
        while aM == '':
            print('No puede quedar en Blanco')
            aM=input('Apellido Materno: ') 

        sql = 'Insert into receta (fecha) value (%s)'
        datos = (fecha,)
        cursor1.execute(sql,datos)
        conexion1.commit()
        sql = 'Insert into usuario (rut,primerNombre,segundoNombre,apellidoPaterno,apellidoMaterno) value (%s,%s,%s,%s,%s)'
        datos = (rut,Nombre,sNombre,aP,aM)
        cursor1.execute(sql,datos)
        conexion1.commit()
    except KeyboardInterrupt:
        print('Cancelaste Operacion')




def buscarMedic():

    try:
        print('Para volver Oprimir CTRL + C')
        buscar= '''
        Buscar por:

        1-Nombre
        2-ID
        
        '''


        print(buscar)

        op=int(input('Opcion: '))

        if op == 1:
                
            sql = 'select * from medicamentos'
            cursor1.execute(sql)
            lis = []
            for i in cursor1:
                lis.append(i[1])
            sw= True
            while sw:
                try:
                    nom = input('Nombre de medicamento a buscar: ')
                    while nom not in lis:
                        print('Nombre no encontrada')
                        nom = input('Nombre de medicamento a buscar: ')
                    sw=False
                except ValueError:
                    print('Valor Invalido!')
            
            else:
                sql = 'select * from medicamentos where nombre=%s'
                d= (nom,)
                cursor1.execute(sql,d)
                for i in cursor1:
                    print('ID:',i[0],' Nombre: ',i[1],' Familia Medicamentos: ',i[2])


        elif op == 2:
                
            sql = 'select * from medicamentos'
            cursor1.execute(sql)
            lis = []
            for i in cursor1:
                lis.append(i[0])
            sw= True
            while sw:
                try:
                    id = int(input('Id de medicamento a buscar: '))
                    while id not in lis:
                        print('id no encontrada')
                        id = int(input('Id de medicamento a buscar: '))
                    sw=False
                except ValueError:
                    print('Valor Invalido!')
            
            else:
                sql = 'select * from medicamentos where id=%s'
                d= (id,)
                cursor1.execute(sql,d)
                for i in cursor1:
                    print('ID:',i[0],' Nombre: ',i[1],' Familia Medicamentos: ',i[2])
    except KeyboardInterrupt:
        print('Cancelaste Operacion')    


def modificarMed():
    try:
        print('Para volver Oprimir CTRL + C')

        sql = 'select * from medicamentos'
        lista = []
        cursor1.execute(sql)
        for i in cursor1:
            lista.append(i[0])

        sw= True
        while sw:
            try:
                id = int(input('Ingrese id del medicamento a modificar: '))
                while id not in lista:
                    print('medicamento no encontrado')
                    id = int(input('Ingrese id del medicamento a modificar: '))
                sw=False
            except ValueError:
                print('Digito Invalido!')
                
        sql = 'update medicamentos set nombre=%s where id=%s'
        e= input('Nuevo Nombre : ')
        dato = (e,id)
        cursor1.execute(sql,dato)
        conexion1.commit()
    except KeyboardInterrupt:
        print('Cancelaste Operacion')    


def verFamiliasMed():
    sql = 'select * from familiamedicamentos'
    cursor1.execute(sql)
    for i in cursor1:
        print('ID: ',i[0],' Nombre: ',i[1])









#FUNCIONES BODEGUERO

def controlStock():
    #Esta función permite visualizar toda el stock ingresado en la base da datos
    sql="Select * from medicamentos"

    cursor1.execute(sql)
    for x in cursor1:
        print("ID",x[0],"Nombre",x[1],"Familia Medicamentos",x[2])
    return




def id_familia():
    #Esta función permite ingresar y tambien verificar al momento de ingresar la familia de medicamentos

    print("1.-Analgesicos\n","2.-Antialergico")

    sql="select * from familiamedicamentos"
    cursor1.execute(sql)

    lista=[]
    for x in cursor1:
        lista.append(x[0])
    id=int(input("Ingrese ID de familia de Medicamentos: "))
    while id=="" or id not in lista:
        if id=="":
            print("El campo no puede quedar vacío")
        elif id not in lista:
            print("El ID no se encuentra en la base de datos")
            id=int(input("Ingrese ID nuevamente: "))
    else:
        print("ID seleccionado correctamente")

    return id

def id_medicamentos():
    sql="select * from medicamentos"
    cursor1.execute(sql)

    lista=[]
    for x in cursor1:
        lista.append(x[0])
    sw=True
    while sw:
        try:
            id=int(input("Ingrese ID medicamento: "))
            while id == "" or id  in lista:
                if id=="":
                    print("El campo no puede quedar vacío")
                elif id  in  lista:
                    print("El ID se encuentra en la base de datos")
                    id=int(input("Ingrese ID nuevamente: "))
            else:
                print("Continue con el ingreso")
            sw=False
        except ValueError:
            print('Digito Incorrecto')
    return

def Nombre():
    Nombre=input("Ingrese el nombre de medicamento: ")
    while Nombre=="" or Nombre == (int):
        print("Campo nombre no puede quedar vacío")
        Nombre=input("Ingrese nuevamente: ")
    return Nombre


def ingresarMedicamentos():
    try:
        print('Para volver Oprimir CTRL + C')
        sql="insert into medicamentos (ID,nombre,familiaMedicamentos_ID) values (%s,%s,%s)"
        id=id_medicamentos()
        nombre=Nombre()
        idfamili=id_familia()
        datos=(id,nombre,idfamili)
        cursor1.execute(sql,datos)
        conexion1.commit()
    except KeyboardInterrupt:
        print('Cancelaste Operacion')
    return








#FUNCIONES JEFE

def visualizarMed():



    sql = 'select * from medicamentos'
    cursor1.execute(sql)
    for i in cursor1:
        print('ID: ',i[0],' Nombre: ',i[1],' Familia Medicamentos: ',i[2])

    return

def verEmpleados():
    sql = 'select * from empleados'
    cursor1.execute(sql)
    for i in cursor1:
        if i[6] == 1:
            cargo= 'Tens'
        elif i[6] == 2:
            cargo = 'Bodeguero'
        else:
            cargo = 'Jefe'

        print('Rut: ', i[0],'| Nombre Completo: ',i[1],i[2],i[3],'| Telefono: ',i[4],'| Correo: ',i[5],'| Cargo: ',cargo,'| Contraseña: ',i[7])

    return


def ingEmpleados():
    exc_1=True
    exc_2=True
    lst=[]
    sw=True
    print('Para volver Oprimir CTRL + C')
    print('Ej:(12345678-9)')
    try:
        while sw:
            rut=str(input("Ingrese Rut a registrar: "))
            while (len(rut)< 9):
                print('rut invalido')
                rut=str(input("Ingrese Rut a registrar: "))
            sql='select rut from empleados'
            cursor1.execute(sql)
            for i in cursor1:
                lst.append(i[0])
            if rut in lst:
                print('Rut ya registrado!')
            else:
                sw=False
        fName=str(input("Ingrese primer nombre: "))
        sName=str(input("Ingrese segundo nombre: "))
        aPP=str(input("Ingrese apellido paterno: "))
        while exc_1:
            try:
                tel=int(input("Ingrese Telefono : "))
                exc_1=False
            except ValueError:
                print("Valor Ingresado Invalido!")


        cargos="""
            1-Tens
            2-Bodeguero
            3-Jefe
        """
        print(cargos)
        while exc_2:
            try:    
                cargo=int(input("Ingrese cargo: "))
                while not(cargo==1 or cargo==2 or cargo==3):
                    print('Por favor ingrese el codigo correspondiente')
                    cargo=int(input("Ingrese cargo: "))
                exc_2=False
            except ValueError:
                print("Valor Ingresado Invalido!!")
        corr=str(input("Ingrese su correo: "))
        pswrd=input("Ingrese contraseña: ")
        datos=(rut, fName, sName,aPP,tel,corr,cargo,pswrd)
        insert = "insert into empleados (rut,primerNombre,segundoNombre,apellidoPaterno,telefono,correo,cargo_ID,Contraseña) Value (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor1.execute(insert,datos)
        conexion1.commit()
    except KeyboardInterrupt:
        print('Salir')
    return








def modicarEmpelado():
    try:
        print('Para volver Oprimir CTRL + C')
        sql = 'select * from empleados'
        cursor1.execute(sql)
        list=[]
        for i in cursor1:
            list.append(i[0])
        rut = input('Ingrese el rut del empleado a modificar: ')
        while (rut not in list):
            if (rut not in list) :
                print('rut no encontrado')
                rut = input('ingrese rut existente: ')
        else:
            swPrincipal = True
            while swPrincipal:
                    select= '''
                    1-Cambiar Nombre
                    2-Cambiar Segundo Nombre
                    3-Cambiar Apellido
                    4-Cambiar Telefono  
                    5-Cambiar Correo
                    6-Cambiar Contraseña
                    7-Salir
                    '''

                    print(select)

                    sw = True
                    while sw:
                        try:
                            op = int(input('Que desea Modificar?: '))
                            while not (op== 1 or op == 2 or op== 3 or op== 4 or op== 5 or op== 6 or op== 7):
                                print('Opcion invalida!')
                                op = int(input('Que desea Modificar?: '))
                            sw= False
                        except ValueError:
                            print('Valor Incorrecto!')


                    if op == 1:
                        sql= 'update empleados set primerNombre=%s where rut=%s'
                        cambio= input('Nuevo Nombre: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                    elif op == 2:
                        sql= 'update empleados set segundoNombre=%s where rut=%s'
                        cambio= input('Nuevo Segundo Nombre: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                        conexion1.commit()
                    elif op == 3:
                        sql= 'update empleados set apellidoPaterno=%s where rut=%s'
                        cambio= input('Nuevo Apellidos: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                        conexion1.commit()

                    elif op == 4:
                        sql= 'update empleados set telefono=%s where rut=%s'
                        cambio= input('Nuevo Telefono: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                        conexion1.commit()
                    elif op == 5:
                        sql= 'update empleados set correo=%s where rut=%s'
                        cambio= input('Nuevo Correo: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                        conexion1.commit()
                    elif op == 6:
                        sql= 'update empleados set Contraseña=%s where rut=%s'
                        cambio= input('Nueva Contraseña: ')
                        datos=(cambio,rut)
                        cursor1.execute(sql,datos)
                        conexion1.commit()    
                    else:
                        print('Volviste al menu')
                        swPrincipal=False
    except KeyboardInterrupt:
        print('Saliste')                    
    return
        

def eliminarEmpleado():
    try:
        print('Para volver Oprimir CTRL + C')
        sql = 'select rut from empleados'
        cursor1.execute(sql)
        list=[]
        for i in cursor1:
            list.append(i[0])
        rut = input('Ingrese el rut del empleado a eliminar: ')
        while rut not in list:
            print('Rut No Existente!')
            rut = input('Ingrese el rut del empleado a eliminar: ')
        else:    
            sql = 'Delete from empleados where rut=%s'
            dato= (rut,)
            cursor1.execute(sql,dato)
            conexion1.commit()
    except KeyboardInterrupt:
        print('Cancelaste La Operecion')