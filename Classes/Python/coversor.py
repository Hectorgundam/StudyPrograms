# Welcome message
print("Bienvenido al conversor de millas a kilometros")

# Asking the user to enter a number of miles 
# Using input() to obtain user input 
# Keep in mind that input() returns a string that will need to be converted
# For this we use the float() function 
print("Escribe un numero de millas: ")
millas = float(input())

# Here we are processing the conversion of miles to kilometers 
kilometros = millas * 1.609

print("Millas ingresadas:" , millas , ".")

print("Esto equivale a46" , kilometros, "kilometros. ")