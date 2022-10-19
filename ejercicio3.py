lista = [15,20,50,80,40,60]
print(f"Lista => {lista}")
elegido = int(input("Elija un número de la lista: "))
lista.remove(elegido)
print(f"Numero {elegido} eliminado")
print(f"Lista => {lista}")