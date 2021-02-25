#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def tamanio_grande(arr):
    contador = 0
    for i in arr:
        if i > 0:
            arr[contador]="Big"
        contador = contador + 1
    return arr

print(tamanio_grande([-3,2,1,-5]))


#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
# (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def contar_positivos(arr):
    nuevoarr=[]
    for i in arr:
        if i>0:
            nuevoarr.append(i)
            arr[len(arr)-1]=len(nuevoarr)
    return arr

print(contar_positivos([-1,1,1,1]))


#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def suma_total(arr):
    var=(0)
    for i in arr:
        var+=i
    return var

print(suma_total([1,2,3,4]))


#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(arr):
    suma=0
    for i in arr:
        suma+=i
    return suma/len(arr)

print(promedio([1,2,3,4]))

#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
def longitud(arr):
    return len(arr)

print(longitud([37,2,3,4,-1]))

#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
def minimo(arr):
    if len(arr)==0:
        return False
    val_min=arr[0]
    for i in arr:
        if i<=val_min:
            val_min=i
            if i>val_min:
                val_min=val_min
    return val_min

print(minimo([37,1,2,3,-9]))

#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
def maximo(arr):
    if len(arr)==0:
        return False
    val_max=arr[0]
    for i in arr:
        if i>=val_max:
            val_max=i
            if i<val_max:
                val_max=val_max
    return val_max

print(maximo([37,1,2,3,-9]))

#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la 
#suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}
def final(arr):
    diccionario={
        "suma":suma_total(arr),
        "promedio":promedio(arr),
        "minimo":minimo(arr),
        "maximo":maximo(arr),
        "longitud":len(arr)
    }
    return diccionario

print(final([2,3,5,7,4,88,3,-4]))

def ultimate_analysis(list):
    diccionario = {}
    diccionario.update({"suma": suma_total(list)})
    diccionario.update({"promedio": promedio(list)})
    diccionario.update({"minimo": minimo(list)})
    diccionario.update({"maximo": maximo(list)})
    diccionario.update({"longitud": longitud(list)})
    return diccionario
print(ultimate_analysis([37, 2, 1, -9]))


#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. 
#(Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def inversa(arr):
    return arr[::-1]

print(inversa([1,2,3,4,5]))

