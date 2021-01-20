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

def printInfo(algun_dicc):
    for i in algun_dicc:
        print(len(algun_dicc[i]))
        for valor_listas in algun_dicc[i]:
            print(valor_listas)
        print("")

print(printInfo(dojo))