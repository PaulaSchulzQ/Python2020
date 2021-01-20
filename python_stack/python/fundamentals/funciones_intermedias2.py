#1.- Actualiza los valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


    #Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0]=15
print(x)

    #Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students[0]["first_name"]="Bryant"
print(students)

    #En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory["soccer"][0]="Andres"
print(sports_directory)

    #Camba el valor 20 en z a 30
z[0]["y"]=30
print(z)

#2.- Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios,
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterateDictionary(students):
    for i in students:
        print("first_name -", i["first_name"]+", " "last_name -", i["last_name"],)
print(iterateDictionary(students))

#3.- Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función 
#imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
#Michael
#John
#Mark
#KB
#Y iterateDictionary2('last_name', students) debería generar:
#Jordan
#Rosales
#Guillen
#Tonel
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
def iterateDictionary2(key_name, some_list)
    for i in some_list:
        print(i[key_name])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


#4.- Itera a través de un diccionario con valores de listas
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre 
#de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave.

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#printInfo(dojo)
# output:
#7 LOCATIONS
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
    
#8 INSTRUCTORS
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for each_list_value in some_dict[key]:
            print(each_list_value)
        print("")

print(printInfo(dojo))