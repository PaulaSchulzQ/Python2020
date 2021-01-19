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