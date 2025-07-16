# Ejemplos de la funcion print

# print ("Hola mundo")
# print ("Hola mundo" , "otra vez")
# print ("Son las" , 9, "de la mañana")
# print ("El resultado de 3 * 4 es:" , 3*4)

# Ejemplos de cadenas formateadas
# print("El numero 15 en sistema decimal es %d, en el sistema octal es %o, en el sistema hexadecimal es %x" %(15, 15, 15))

# pi = 3.141592
# r = 5
# print(f"El radio de un circulo es{r} y el area de ese circulo es {pi*r**2 : .2f}" )
# se va a poner una f al principio para especificar que queremos hacer una cadena formateada
#Como queremos el resultado en un formato de punto decimal pero que solo este redondeado a dos decimales se indican( : .2f), la f por el tipo de formato

# Impresion de caracteres especiales
# print("La letra beta es: \n\t \u03B2")
# Para hacer un salto de linea se pone \n y podemos pedir una tabulacion con \t, la tabulacion por defecto es por 4 espacios
# podemos pedirle que imprima la letra beta por medio de su codificacion en el sistema ascii y siempre despues de \

# Caracteres de escape
print("Hola mundo",end = " ")
print("otra vez", end = "\t")
print("y otra vez")