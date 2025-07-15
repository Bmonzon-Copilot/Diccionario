estudiante={} #Nombre del diccionario
cantidad=int(input(f"\nIngrese cantidad de estudiantes: "))
for i in range(cantidad):               #Pedimos los datos del estudiante
    print(f"\n Estudiante #{i+1}")
    carnet=input("Ingrese Carnet: ")
    nombre = input("Ingrese Nombre: ")
    edad = input("Ingrese Edad: ")
    carrera = input("Ingrese Carrera: ")

    estudiante[carnet]={      #Creacion del diccionario con clave principal carnet
        "nombre":nombre,
        "edad":edad,
        "carrera":carrera
    }
print(f"\nLista de estudiantes:")
for carnet, datos in estudiante.items(): #recorre la lista de estudiantes y devuelve los datos
    print(f"Carnet: {carnet}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Edad: {datos["edad"]}")
    print(f"Carrera: {datos["carrera"]}")

print(f"\nBuscar Estudiante")
buscando= input("Ingrese carnet: ")
if buscando in estudiante:
    print(f"Nombre: {estudiante[buscando]["nombre"]}")
    print(f"Edad: {estudiante[buscando]["edad"]}")
    print(f"Carrera: {estudiante[buscando]["carrera"]}")
else:
    print("Estudiante no encontrado")

