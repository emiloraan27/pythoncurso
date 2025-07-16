# Input nos va aservir para poder capturar datos que el usuario escriba en el programa

nombre = input("¿Como te llamas? ")
print("Hola " + nombre) #es importante que esta ultima no vaya entre comillas porque no es una cadena, es una variable

edad = input("¿Cuantos años tienes? ")
print(type(edad))
print(f"{nombre!r} tiene {edad}")

# programa que pide dos numeros al usuario y los suma

numero1 = int(input("Introduce un numero porfavor: "))
numero2 = int(input("Introduce otro numero porfavor: "))
numero3 = numero1 + numero2
print(f"El resultado de la suma es {numero3}")

