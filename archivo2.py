
# titulo= "clima de hoy"
# diames=13
# mes=4

# temp=22.3

# llueve=False

# print(titulo)
# print(temp)
# print(diames, mes)

# if llueve == True:
#     print("u have to carry an umbrella")
# else:
#     print("It's a sunny day")

# pedir password y pin
# pida al usuario en palabra que debe ser "Temu"
# adema pida el pin que debe ser "3435"
# los 2 deben ser correctos para acceder al sytem
# contraseña = "Temu"
# pin = 3435
# print("escribe tu contraseña")

# contraseñaE = input()
# print("escribe tu pin ahora")
# pinE = int(input())

# if contraseña == contraseñaE and pin == pinE:
#     print("Bienvenido Bro")
# elif contraseña != contraseñaE and pin ==pinE:
#     print("pusiste mal la contraseña")
# elif contraseña == contraseñaE and pin != pinE:
#     print("pusiste mal el pin")
# else:
#     print("pusiste mal ambos")

# ingreso = int(input("Pon tus ingresos"))
# if ingreso <500000:
#     print("no es suficiente")
# elif ingreso >=500000 and ingreso <=1000000:
#     credito = 300000
# elif ingreso >=1000000 and ingreso <=1500000:
#     credito = 650000
# elif ingreso >=1500001:
#     credito = 1000000

# educacion = input("cual educacion tienes? Basico, Medio o Superior")
# if educacion == "Basico" or educacion == "basico" or educacion == "basica" or educacion == "Basica":
#    credito = credito*1
# elif educacion == "medio" or educacion == "Medio" or educacion == "Media" or educacion == "media":
#     credito = credito*1.3
# elif educacion == "superior" or educacion == "Superior":
#     credito = credito*1.5
# else:
#     print("invalido")
# nacion = input("cual es tu nacionalidad? Chilena o Extranjero?")
# if nacion == "chile" or nacion == "chilena" or nacion =="Chile" or nacion =="Chilena" or nacion =="Chileno" or nacion == "chileno":
#     credito = credito+300000
# elif nacion == "extranjero" or nacion =="extranjera" or nacion =="Extranjero" or nacion=="Extranjera":
#     credito =credito+0
# else:
#     print("invalido")

# print(credito)

print("escribe 3 num")
n1 = input()
n2 = input()
n3 = input()


if n1> n2 and n1>n3:
    print(n1, "es mayor")
elif n2> n1 and n2>n3:
    print(n2, "es mayor")
elif n3>n1 and n3>n2:
    print(n3, "es mayor")
