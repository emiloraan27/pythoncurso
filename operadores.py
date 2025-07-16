# operadores aritmeticos
print(2+2) # suma
print(4-2) # resta
print(3*7) # multiplicacion
print(15/2) # division
print(11%4) # modulo es el residuo que queda en la division, en este caso 4 solo cabe dos veces en el 11, y su residuo es 3
print(11//4) # division de piso es la mayor cantidad de veces que cabe el 4 en el 11
print(2**3) # con el doble asterisco (**) podemos elevar un numero a x potencia

#operadores en cadenas de texto (strings)
print("Hola" + "mundo") # Concatenacion (mo se le llama suma ne cadenas de texto)
print("Hola" * 3) # Repeticion
print("Hola" + "mundo"*3)
print(("Hola" + "mundo")*3)

#print("Hola" + 3) 
# no va

# operadores de comparacion
print("Hola" == "hola") # doble signo de igualdad (==) representa el igual que
print("Hola" != 'hola') # distinto que
print(3>11) # mayor que, menor que
print(11>=10) # mayor o igual que
print(10<=10) #menor o igual que

# operadores de existencia (Verificar si un elemento existe dentro de otro elemento)
print("ola" in "Hola") # De existencia
print("ola" not in "Hola") # De inexistencia

# operadores booleanos
print(True or False) # or verifica que se cumpla solo una de las condiciones
print(True and False) # and verifica que se cumplan ambas condiciones

# operadores de asignacion (asigna un nuevo valor a una variable ya definida)
x = 1 # operador de asignacion estandar
x += 2 # operador de asignacion suma
x *= 3 #operador de asignacion multiplicacion
x %= 4 # opeerador de asignacion modulo
print(x)

X = 6 * 5 + 8 / 2 ** 4
print(X)

#Tambien se pueden separar listas por medio de sep=", "
print("manzana", "platano", "cereza", sep=", ")