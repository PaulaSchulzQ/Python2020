#1.-Crea un nuevo archivo de Python llamado hello_world.py
#Ejecuta el archivo

#2.-Escribe el código para imprimir una cadena literal que diga "Hola mundo" (# 1)
print("Hello world")

#3.-Almacena tu nombre en una variable y luego úsalo para imprimir la cadena "¡Hola {{tu nombre}}!" usando una coma en la función de impresión (# 2a)
#Ejecuta el archivo
x="Paula!"
print("¡Hola", x)

#4.-Almacena tu nombre en una variable y luego úsalo para imprimir la cadena "¡Hola {{tu nombre}}!" usando un + en la función de impresión (# 2b)
#Ejecuta el archivo
y="Paula Schulz"
print("¡Hola" + y)

#5.-Almacena tu número favorito en una variable, y luego úsalo para imprimir la cadena "¡Hola {{num}}!" 
#usando una coma en la función de impresión (# 3a)
#Ejecuta el archivo
z=23
print("¡Hola", z)

#6.-Almacena tu número favorito en una variable, y luego úsalo para imprimir la cadena "¡Hola {{num}}!" 
#usando un + en la función de impresión (# 3b)
#Ejecuta el archivo
z="23"
print("¡Hola" + z)

#7.-NINJA BONUS: descubre cómo resolver el error desde arriba, sin cambiar el signo + a una coma
#---> Le agregue comillas a la variable numero

#8.-Almacena 2 de tus comidas favoritas en variables y luego úsalas para imprimir la cadena
# "Me encanta comer {{food_one}} y {{food_two}}".
#con el método de formato (# 4a)
#Ejecuta el archivo
b="Cazuela"
c="ceviche"
print("Me encanta comer {} y {}".format(b, c) )

#9.-Almacena 2 de tus comidas favoritas en variables y luego úsalas para imprimir la cadena
# "Me encanta comer {{food_one}} y {{food_two}}". con cuerdas f (# 4b)
#Ejecuta el archivo
print(f"Me encanta comer {b} y {c}")


#10.-BONIFICACIÓN DE NINJA: ¡Dedica unos minutos a jugar con otros métodos de cuerda para ver qué hay ahí fuera!
l="probando con title"
print(l.title())

m="devuelve una copia de la cadena con todos los caracteres en mayúscula."
print(m.upper())

n="devuelve una copia de la cadena con todos los caracteres en minúsculas."
print(n.lower())

o="probando substring, devuelve el número de ocurrencias de subcadena en la cadena."
p="este es el substrin"
print(o.count(p))
