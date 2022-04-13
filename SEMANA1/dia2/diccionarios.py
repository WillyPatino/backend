# estructura de datos similar a JSON
capitales = {
    'Perú': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
}

print(capitales)

# agregando nuevo valor al diccionario
nuevaCapital1 = {'Brasil': 'Brasilia'}
capitales.update(nuevaCapital1)
print(capitales)

# eliminar valores de un diccionario
c = capitales.pop('Colombia', 'No existe ese país en mi diccionario')
print(c)
print(capitales)
### RECORRER CAPITALES ###
for capital in capitales:
    print(capital+" : "+capitales[capital])
print(capitales.keys())
print(capitales.values())
print(capitales.items())
for clave in capitales.keys():
    print(clave+"=>"+capitales[clave])

for clave, valor in capitales.items():
    print(clave+" __ "+valor)


#### BASE DE DATOS DE ALUMNOS ####
alumno1 = {
    'Nombre': 'Juan',
    'Edad': 20,
    'Nota': 13,
    'Aprobado': True,
    'Cursos': ['JavaScript', 'Python', 'C#']
}

alumno2 = {
    'Nombre': 'Lucia',
    'Edad': 20,
    'Nota': 19.5,
    'Aprobado': True,
    'Cursos': ['Java', 'Swift', 'Kotlin']
}
alumnos=[alumno1,alumno2]
print("*"*100)
for columna in alumno1:
  print(columna, end = '     | ')
print()
print("*"*100)
for alumno in alumnos:
    for clave, valor in alumno.items():
        print(valor,end='     |   ')
    print()