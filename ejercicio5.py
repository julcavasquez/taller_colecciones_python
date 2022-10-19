diccionario = {
              'Marcelo' : 1.80,
              'Jose': 1.50,
              'Oscar': 1.70,
              'Jorge':1.40
            }
print(f"Tallas de Personas => {diccionario}")    
nombre = input("Ingrese un nombre: ")
print(f"Su talla es: {diccionario[nombre]:.2f}")