# while True:
#     try:

#         nym=int(input())
#         if nym <5:

#             break 
#     except ValueError as e:
#         print("Solo se aceptan numeros enteros")
#         print(e)
#         print("ola")
# import random
# while True:
#     try:
#         ip=random.randint(1,10)
#         print(ip)
#         if ip %2!=0: #si no es par va a romper el codigo
#             break
#     except:
#         print("algo")
# while True:
#     try:
#         n1=int(input())
#         nu+=n1
#         if n1==0:
#             break
#     except:
#         print("solo entero")
# print(nu)
######## try es para evitar el crasheo el excpet es para detectar que paso exactamente

### seccion sacada de Python 
# op = 0
# total = 0
# cant=0
# while op != 4:
#     try:
#         print("1.- Radio Stereo Sony $70.000")
#         print("2.- LGTV 55 Pulgadas Super TV del Futuro Max Waos $500.000")
#         print("3.- PS5 $480.000")
#         print("4.- Salir")
#         op=int(input())
#         match op:
#             case 1:
#                 print("Tienes que pagar ", round(70000*1.19))
#                 total += 70000*1.19
#                 cant+=1
#             case 2:
#                 print("Tienes que pagar ", round(500000*1.19))
#                 total += 500000*1.19
#                 cant+=1
#             case 3:
#                 print("Tienes que pagar ", round(480000*1.19))
#                 total += 480000*1.19
#                 cant+=1
#             case 4:
#                 print("Saliendo")
#                 print(f"su total es ", {round(total)})
#                 print(f"la cantidad de productos es de {cant}")
#             case _: #para NUMERO NO valido
#                 print("mas invalido que yo")
#     except:
#         print("oye tienes que poner un numero no una letra aweonao") #para CUALQUIER cosa NO VALIDA

# proc=int(input("ingresa porcentaje de rucos en su comuna"))

# if proc>100 or proc<=-1:
#     print("error intenta de nuevo")
#     proc=int(input("ingresa porcentaje de rucos en su comuna"))
# elif proc<=100:
#     print("gud")