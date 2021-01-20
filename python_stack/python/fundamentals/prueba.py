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