from re import A
import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root",password="",database="farmacia")
cursor1 = conexion1.cursor()

def ini():
    print("__________________________________________")
    print('Farmacia')
    print("1.-Iniciar Sesion")
    print("2.-Registrarse")
    print("3.-Cerrar")
    return

def qst():
    res=input("Salir del programa? si|no : ")
    while not(res=="si" or res=="no"):
        res=input("Salir del programa? si|no : ")
    return res

def login(rut,pswrd):
    print("Login")
    print("__________________________________________")
    rut=input("Ingrese su rut: ")
    pswrd=input("Ingrese su contraseña: ")
    return rut,pswrd

def register(rut, fName, sName,aPP,tel,corr,cargo,pswrd):
    exc_1=True
    exc_2=True
    lst=[]
    sw=True
    print("Registrate")
    print('Ej:(12345678-9)')
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
    while (fName ==''):
        fName=str(input("Ingrese primer nombre: "))
    
    
    sName=str(input("Ingrese segundo nombre: "))
    while (sName == ''):
        sName=str(input("Ingrese segundo nombre: "))

    
    aPP=str(input("Ingrese apellido paterno: "))
    while (aPP == '') :
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
    while pswrd == '' :
        pswrd=input("Ingrese contraseña: ")

    return rut, fName, sName,aPP,tel,corr,cargo,pswrd




def Entrada(rut):
    sql='select * from empleados where rut=%s'
    r = rut
    datos = (r,)
    print(datos)
    cursor1.execute(sql,datos)
    for i in cursor1:
        dato = i[6]

    return dato
   
    



print('TODO OK')