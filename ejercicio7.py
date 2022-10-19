mis_datos = {}
print("Ingrese sus datos")
mis_datos['nombre'] = input("Ingrese su nombre: ")
mis_datos['apellido'] = input("Ingrese su apellido: ")
mis_datos['edad'] = int(input("Ingrese su edad: "))

print(f"Hola mi nombre es {mis_datos['nombre']} {mis_datos['apellido']}, y tengo {mis_datos['edad']} años")