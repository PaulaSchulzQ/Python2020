#1
def a():
    return 5
print(a())
#Mi prediccion: 5
#salida 5

#2
def a():
    return 5
print(a()+a())
#Mi prediccion: 10
#salida 10

#3
def a():
    return 5
    return 10
print(a())
#Mi prediccion: 10
#salida 5

#4
def a():
    return 5
    print(10)
print(a())
#Mi prediccion 10 y 5
#salida 5

#5
def a():
    print(5)
x = a()
print(x)
#Mi prediccion 5 y 5
#salida 5, none

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#Mi prediccion 3, 5 y 8
#salida 3, 5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#Mi prediccion 25
#salida 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
        else
            return 10
    return 7
print(a())
#Mi prediccion 100
#salida 100 y 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#Mi prediccion 7, 14, 21
#salida 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#Mi prediccion 8
#salida 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#Mi prediccion 500 500 300 y 500
#salida 500 500 300 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#Mi prediccion 500 500 300 300 500
#salida 500 500 300 500


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#Mi prediccion 500 500 300 300
#salida 500 500 300 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#Mi prediccion 1
#salida 1 3 2


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#Mi prediccion 1 10 3 5
#salida 1 3 5 10