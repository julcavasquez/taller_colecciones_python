
lista = ["Hola","Amigos","Hoy",True]
palabra = input("Ingrese una palabra:")
lista.append(palabra)
# lista = [palabra] + lista
lista.insert(0,palabra)
print(lista)