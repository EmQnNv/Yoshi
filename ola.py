#debe preguntar al usuario el nombre de juego
#sin espacio y todo mayuscula
#preguntar percio solo numero positivo y mas de 20 mil pero menos de 40 mil es indie
#si no es de estudio
#mostrar cuantos hay de cada categoria
#clasificacion E para todos +12 adolescentes M +18
#mostrar resumen

# cl_adu = 0
# cl_ado = 0
# cl_e = 0
# ind = 0
# est = 0
# ran = 0


# r = False
# try:
    
#     while r == False:
    
#         indie = False
#         Studio = False
#         E = False
#         adolescente = False
#         adulto = False
#         print("eu dame el name del jueo altoke")
#         name = input().upper()

#         largo = len(name.replace(" ",""))

#         print(f"Mas feo ese nombre, {name}...")
#         try:
#             while largo <5:
                
#                     if len(name) <5:
#                         print("no me gusto, hazlo de nuevo")
#                         name = input()
#                         largo = len(name.replace(" ",""))
#                     else:
#                         print("Que hiciste???")
#                         name = input()
#                         largo = len(name.replace(" ",""))
#         except:
#                 print("algo salio mal broder, reintentalo")
#                 name = input()
#                 largo = len(name.replace(" ",""))

            
#         print("Igual te salio bueno...Supongo")
#         print(f"Bien... Ahora dame el precio de {name}")
#         try:
#             while True:
            
#                 precio = int(input())
#                 if precio <0:
#                     print("Hermano, Como es que tu numero es MENOR a 0???")
#                     print("REINTENTALO")
#                     precio = int(input())
#                 elif precio >=20000 and precio <=40000:
#                     print("Epaaaa un juego INDIE?? Wena")
#                     indie = True
#                     ind+=1
#                     break
#                 elif precio >40000:
#                     print("Mish... Mirenlo, el Estudio")
#                     Studio = True
#                     est+=1
#                     break
#                 elif precio >0 and precio <20000:
#                     print("entendido, eres un random")
#                     ran+=1
#                     break
#         except:
#             print("algo salio mal MAL, Reintentalo")
#             precio = int(input())
                

#         print("Y para finalizarrrrr, QUE CALIFICACION ES TU JUEGO????")
#         print("Es Clasificaion E?")
#         print("Es Clasificaion +12?")
#         print("Es Clasificaion +18?")
#         print("usa de 1 a 3 respectivamente")
#         op = 0
       
#         while True:
#             try:
#                 op = int(input())
                
#                 match op:
#                     case 1:
#                         print("Entendido, tu juego es family friendly")
#                         E = True
#                         cl_e +=1
#                         break
#                     case 2:
#                         print("Oka, pa adolescentes")
#                         adolescente = True
#                         cl_ado +=1
#                         break
#                     case 3:
#                         print("los hijos lo querran pero los adultos lo odiaran... Bien Hecho")
#                         adulto = True
#                         cl_adu +=1
#                         break
#                     case _:
#                         print("eres analfabeta???")
#                         print("intentalo de nuevo")
#                         op = int(input())
#             except:
#                 print("algo salio mal, Reintentalo (:")
#                 op = int(input())
            


#         print("Vamos por los resultados Finales!!!")
#         print(f"Nombre de juego: {name}")
#         print(f"Precio: {precio}")
#         if Studio == True:

#             print(f"Tipo de juego: Studio")
#         elif indie == True:
#             print("Tipo de juego: Indie")
#         else:
#             print("solo un random Lol")
#         if E == True:
#             print("Clasificacion: E")
            
#         elif adolescente == True:
#             print("Clasificacion: E")
            
#         elif adulto == True:
#             print("Clasificacion: E")
#         try:   
#             print("quieres continuar?")
#             cont = input("S/N")
#             if cont.upper() == "S" or cont.upper() == "SI":
#                 print("entendido... Continuando")
#             elif cont.upper() == "N" or cont.upper() == "NO":
#                 print("Entendido")
#                 break
#         except:
#             print("algo salio mal, reintentalo")
#             cont = input("S/N")
#         break

  

# except:
#     print("algo salio re mal")
    
# print(f"hay un total de {ind} indies")
# print(f"hay un total de {est} estudios")
# print(f"hay un total de {ran} de randoms lol")
# print(f"hay un total de {cl_ado} de Clasificacion Adolescente")
# print(f"hay un total de {cl_adu} de Clasificacion de Adultos")
# print(f"hay un total de {cl_e} de Clasificacion de Para Todos")

######almacenaminto de bibbliocteca

#90 espacio
#cada libro usa u espacio
# menu
#historial de ocupaciones
#*mostrar cantidad de libros registrados durante la sesion
#poner +
#sacar -
s = 90
espacio = 90
try:
    while True:
        print("1.- Espacios Disponibles")
        print("2.- Poner Libros")
        print("3.- Sacar Libros")
        print("4.- Historial de ocupaciones")
        print("5.- Salir")
        op = int(input())
        match op:
            case 1:
                print(f"Tienes {espacio} espacios disponibles")
            case 2:
                print(f"Cuantos libros quieres colocar?")
                colocar = int(input())
                if colocar >90 or colocar>espacio:
                    print("Bro estas re mal mal")
                elif colocar 
                    colocar+espacio
                    print("hesho con exito mi broder")
except:


