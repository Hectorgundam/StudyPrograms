def mostrarMenu(): 

    print("Selecciona la opcion que deseas:")
    print("1: Conocer cuantos animales tiene la tienda.")
    print("2: Comprar un animal.")
    print("3: Salir de la tienda.")

def mostrarInventarioAnimales(inventario): 

    print("Actualmente contamos con: ")
    for key, value in inventario.items(): 
        print(f"    - {key}: {value}")

    print("")

    # Learning about basic variable operations 
    # Printing the total sum of animals in the pet shop 
    totalAnimales = 0

    for val in inventario.values(): 
        totalAnimales += val

    print("En total tenemos:", totalAnimales , "animales.")


def comprarAnimal():

    carrito = []

    agregarOtro = 'Si'

    while agregarOtro == 'Si': 

        # Ask the user what animal they would like to buy
        print("¿Que animal deseas comprar?")
        animalEscogido = input()

        # We don't have the selected animal in our store 
        if animalEscogido not in inventario: 

            print("")
            print(f"Lo sentimos, no contamos con el animal {animalEscogido}")
        
        # We have the selected animal in our store but it's no longer in stock
        elif inventario[animalEscogido] == 0:

            print("")

            print(f"Lo sentimos, actualmente no tenemos el animal {animalEscogido} en stock.")

        # If the animal the user inputted is not in the list then we can add it 
        elif animalEscogido not in carrito: 

            carrito.append(animalEscogido)
        
        else: 

            print("Ya tienes ese animal en tu carrito.")

        print("")

        print("Tu carrito contiene:")
        for animal in carrito:
            print(f"    - {animal}")

            # Updating the inventory to reduce the amount of animals the user purchased by 1 
            inventario[animal] -= 1
        
        print("")

        print("Deseas agregar otro animal para comprar?")
        print("Escribe Si o No")
        agregarOtro = input()

        print("")

    print("Has comprado los siguientes animales: ")
    for animal in carrito: 
        print(f"    - {animal}")
    
    print("")

# Learning how to print to screen 
print("*********************************")
print("******* BIENVENIDO A ************")
print("**** LA TIENDA DE MASCOTAS ******")
print("*********************************")

print("")

# Dictionary of animals 
# The key is the animal name group
# The value is the amount of animals in stock 
inventario = {
    "Perro" : 10 ,
    "Gato" : 8 ,
    "Pajaro": 25 ,
    "Iguana" : 2 ,
    "Tortuga" : 0
} 

# Learning about variables and printing them 
# Animales 

# Learning about taking input from user 
# Asking the user for input to personalize program a bit more 
print("Por favor ingresa tu nombre:")
nombre = input()

print("")

print("Por favor escribe tu apellido:")
apellido = input()

print("")

# Learning about concatenation 
# Taking two strings and merge them together so to say 
# When you concatenate there is no space between elements 
# Using " " to add an empty space in between 
nombreCompleto = nombre + " " + apellido 

print("*********************************")

print("Gracias por visitarnos," , nombreCompleto)

print("*********************************")

print("")

# print("*********************************")

opcionEscogida = 0

while opcionEscogida != 3: 

    print("*********************************")

    mostrarMenu()

    opcionEscogida = int(input())

    print("*********************************")

    print("")

    if opcionEscogida == 1: 
        print("*********************************")

        mostrarInventarioAnimales(inventario)

        print("*********************************")

        print("")

    elif opcionEscogida ==2: 

        print("*********************************")

        comprarAnimal()

        print("*********************************")

        print("")


print("*********************************")
print("Gracias por visitar nuestra tienda!")
print("*********************************")
print("")
