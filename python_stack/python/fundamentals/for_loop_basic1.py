#Básico : imprime todos los enteros del 0 al 150.
for x in range (151):
    print (x)

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for y in range(0, 1001, 5):
    print (y)

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5,
# imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for z in range (0,101):
    if z%5==0:
        if z%10==0: 
            print ("Coding dojo")
        else:
            print("coding")
    else:
        print (z)


#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
varsum = 0 
for i in range (500001):
    if i%2!=0:
        varsum=varsum+i
print(varsum)

#Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.
for h in range (2018, 0, -4):
    print (h)
#Contador flexible : establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
#Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lownum = 2
highnum = 9
mult = 3
for i in range (lownum, highnum+1, 1):
    if i%3==0:
        print (i)