# explicacion for

# for i in range(5): #de 0 a 5
#     print(i+1) #imprimime el rango de la i, de 0 a 5

# print("dame 1 numero")
# num = int(input())

# for num in range(num):
#     print("ola master") #dependiendo de que numero me de el usuario va a aparecer esa cantidad de veces este mensaje
    

# print("dame un numero y te lo multiplicare")

# n = int(input())

# for i in range(11):
#     print(n, "x", i, "=", n*i)
    
# #otra forma
# for i in range(10):
#     print(n, "x", i+1, "=", n*i, (1+i))
# #otra forma
# for i in range(1,11):
#     print(n, "x", i, "=", n*i)
    

#pedr nmer al usuario 
#mostrar la suma de este numero
#desde el 1 hasta ese numero

# print("dame un numero")
# n = int(input())
# for i in range(n):
#     print(n, "+", i+1, "=", i+n)


# #pedir cantidad de notas al usuario
# #luego pedir cada nota individualmente
# #calcular el promedio de todas las notas
# #mostrar si aprueba o no

# print("dame 3 notas tuya")

# n1 = float(input()) #float es para decimales (el codigo sabra que los decimales seran incluidos)
# n2 = float(input())
# n3= float(input())

# promedio = (n1+n2+n3)/3

# if promedio <4.0 and promedio >=1:
#     print("reprobaste bro, tienes un", promedio)
# elif promedio >= 4.0 and promedio <= 7.0:
#     print("wenaa pasaste con", promedio)
# elif promedio > 7.0 or promedio <1.0:
#     print("seguro que no pusiste algo mal?, tienes un", promedio)

# como lo hizo el profe

# notas=int(input(" escribe la cantidad de notas"))
# suma=0
# for i in range(notas):
#     n=float(input(" ingresa tus notas"))
#     suma=suma+n
# prom=suma/notas
# if prom>=4:
#     print("pasaste")
# elif prom<4:
#     print("reprobado")

# nombre=input("escribe tu nombre")
# cant=0
# conso =0

# for i in nombre:
    
#     print(i)
#     if i in "aeiouAEIOU":
#         cant=cant+1
#     else:
#         conso += 1

# print("la cntidad de vocales es", cant)
# print("la cntidad de vocales es", conso)
        
#pida la cantidad de alumnos
#por cada alumno pida la cant
#de notas
#saca el promedio y si aprueba o no

alumn = int(input("ingresa la cant de alumnos")) #me dio error aca???
cant = 0
notas = 0
for i in range(alumn):
    print("notas de alumno", i+1)
   
    cant = int(input("cual es la cantidad de notas?"))
    for i in range(cant):
        notas1 = int(input())
        notas2 = int(input())
        notas3 = int(input())

print(notas1)