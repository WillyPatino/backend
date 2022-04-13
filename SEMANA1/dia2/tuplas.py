# a la tupla no se le puede agregar, es inmutable, es una lista de valores que no se puede modificar
dias=("lunes", "martes", "miercoles","jueves", "viernes")
print(dias)
dias = list(dias)
dias.append("sabado")
print(dias)
dias = tuple (dias)
print(dias)
for i in dias:
  print(i)