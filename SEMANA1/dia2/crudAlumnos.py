import tabulate
# PROGRAMA PARA CREAR UN CRUD DE ALUMNOS
# CREATE => C
# READ => R
# UPDATE => U
# DELETE => D
print("-"*50)
print("|"+" "*9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "*8 + "|")
print("-"*50)
print("|"+" "*9 + "MENU DE OPCIONES      " + " "*18 + "|")
print("|"+" "*9 + "[1] REGISTRA ALUMNO   " + " "*18 + "|")
print("|"+" "*9 + "[2] MOSTRAR ALUMNO    " + " "*18 + "|")
print("|"+" "*9 + "[3] ACTUALIZAR ALUMNO " + " "*18 + "|")
print("|"+" "*9 + "[4] ELIMINAR ALUMNO   " + " "*18 + "|")
print("|"+" "*9 + "[5] SALIR ALUMNO      " + " "*18 + "|")
print("-"*50)
opcion = 0
alumnos = [{'NOMBRE':'cesar mayta','EMAIL':'cesarmayta@gmail.com','CELULAR':'232323'}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")