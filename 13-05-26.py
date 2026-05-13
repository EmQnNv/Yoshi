# interTF = False


# print("cual es el peso del producto? (en gramos)")
# peso = int(input())
# print("ahora deme el porcentaje de sodio en este")
# sodio = int(input())
# print("tu weaita va a ser internacional? Si o No")
# inter = input().upper()
# if inter == "SI" or "S":
#     InterTF = True

# if peso <= 500:
#     print("tu lata es normal")
# elif peso >=501 and peso <=1500:
#     print("tu lata es mediana")
# elif peso >1501:
#     print("tu lata ta grande")
try:
    inicio = 100000
    print("eu tienes 100.000 pa retirar")
    print("solo puedes sacar o ingresar en multiplos de 5000")
    print("que quiere hacer?") 
    print("1.-Consultar Saldo")
    print("2.-Retirar Dinero") 
    print("3.-Depositar Dinero") 
    print("4.-Salir del Closet")
    op = int(input())
    while op != 4:
        match op:

            case 1:
                    print(f"tienes {inicio} en la cuenta")
                    print("que quiere hacer?" \
                    "1.-Consultar Saldo" \
                    "2.-Retirar Dinero" \
                    "3.-Depositar Dinero" \
                    "4.-Salir del Closet")
                    op = int(input())
            case 2:
                    print("cuanto quieres retirar")
                    ret = int(input())
                    if ret >inicio:
                          print("todo mal wn")
                          op = int(input())
                    elif ret <=inicio:
                        sec = ret %5000 ==0
                        if sec == 1:
                                print(f"Entendido, haz retirado {ret}")
                                inicio-=ret
                                op = int(input())
                        elif sec ==0:
                                print("Error (:)")
                                op = int(input())
                        else:
                          print("algo salio mal")


            case 3:
                    print("cuanto quieres depositar?")
                    dep = int(input())
                    rec = dep %5000 ==0
                    if rec ==1:
                          print(f"entendido, depositando {dep}")
                          inicio +=dep
                          op = int(input())
                    elif rec ==0:
                          print("estas re mal broder")
                          op = int(input())
                    else:
                          print("algo salio mal")
            case 4:
                    print("Saliendo")
            case _:
                    print("Opcion equivocada hermano mio")

except ValueError:
      print("Pusiste algun numero mal")
