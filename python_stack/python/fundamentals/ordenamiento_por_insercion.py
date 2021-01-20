#Construye un algoritmo para la ordenación por inserción.
# Mira el video aquí para comprender cómo funciona la ordenación por inserción e implementar el código. 
#Básicamente, este orden funciona comenzando en el índice 1, desplazando ese valor a la izquierda 
#hasta que se ordena en relación con todos los valores a la izquierda, y 
#luego pasando a la siguiente posición del índice y realizando los mismos cambios hasta el final de la lista. alcanzado. 


def insercion(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if(arr[j-1] > arr[j]):
                aux=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=aux
    return arr
arr=[2,5,12,1,0,8]
print(insercion(arr))
