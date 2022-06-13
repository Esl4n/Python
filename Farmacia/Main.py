import trabajadoresMenu
import Funtions
import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root",password="",database="farmacia")
cursor1=conexion1.cursor()
#──────▄▀▄─────▄▀▄
#─────▄█░░▀▀▀▀▀░░█▄
#─▄▄──█░░░░░░░░░░░█──▄▄
#█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█

Ini = True
while Ini == True:
    res="no"
    while res=="no":
        Funtions.ini()
        rut=""
        pswrd=""
        fName=""
        sName=""
        aPP=""
        tel=""
        corr=""
        cargo=""
        sw=True
        while sw:
            try:
                opc = int(input('Seleccion: '))
                while not(opc==1 or opc ==2 or opc==3):
                    print('Opcion no valida!')
                    opc = int(input('Seleccion: '))
                sw=False
            except ValueError:
                print('Opcion no Valida!')
        if (opc == 1):
            rut,pswrd=Funtions.login(rut,pswrd)
            sql='select * from empleados'
            cursor1.execute(sql)
            list = []
            plist = []
            for i in cursor1:
                list.append(i[0])

            if rut in list:
                sql='select Contraseña from empleados where rut=%s'
                dato= (rut,)
                cursor1.execute(sql,dato)
                for x in cursor1:
                    plist.append(x[0])
                if pswrd in plist:
                    dato=Funtions.Entrada(rut)
                    if dato == 1:
                        print('Tens') 
                        trabajadoresMenu.tens()
                    elif dato == 2:
                        print('Bodeguero') 
                        trabajadoresMenu.bodeguero()
                    else :
                        print('Jefe') 
                        trabajadoresMenu.jefe()
                else:
                    print("Contraseña Incorrecta")
            else:
                print("Rut Incorrecto")   

        elif (opc == 2):
            try:
                print("__________________________________________")
                print('Para Volver Pulse CTRL + C ')
                rut, fName, sName,aPP,tel,corr,cargo,pswrd=Funtions.register(rut, fName, sName,aPP,tel,corr,cargo,pswrd)
                datos=(rut, fName, sName,aPP,tel,corr,cargo,pswrd)
                insert = "insert into empleados (rut,primerNombre,segundoNombre,apellidoPaterno,telefono,correo,cargo_ID,Contraseña) Value (%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor1.execute(insert,datos)
                conexion1.commit()
            except KeyboardInterrupt:
                print('Cancelaste Operacion')
        
        else:
            Ini=False
            res='si'


conexion1.close()

print('Bye!')
        