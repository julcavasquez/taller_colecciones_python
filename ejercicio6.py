diccionario = {
              'Marcelo' : 1.80,
              'Jose': 1.50,
              'Oscar': 1.70,
              'Jorge':1.40
            }
print(f"Tallas de Personas => {diccionario}")  
lista_keys = list(diccionario.keys())
lista_valores = list(diccionario.values())  
print(f"Keys => {lista_keys}")
print(f"Valores => {lista_valores}")
talla = float(input("Ingrese la talla: "))
indice = lista_valores.index(talla)
print(f"Persona con dicha talla: {lista_keys[indice]}")