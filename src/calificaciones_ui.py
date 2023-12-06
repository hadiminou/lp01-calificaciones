from calificaciones import*
def solicita_notas()->tuple:
    nombre=str(input("Introduzca su nombre: "))
#    notas_teo=[]
 #   for i in range (1,5):
  #      nota=float(input"Introduzca la nota del examen teórico"+i+"0 si no ha presentado: ")
   #     notas_teo.append(nota)
    t1=float(input("Introduzca la nota del examen teórico 1: "))
    t2=float(input("Introduzca la nota del examen teórico 2: "))
    t3=float(input("Introduzca la nota del examen teórico 3: "))
    t4=float(input("Introduzca la nota del examen teórico 4: "))
    p1=float(input("Introduzca la nota del examen practico 1: "))
    p2=float(input("Introduzca la nota del examen practico 2: "))
    global notas
    notas=((t1,t2,t3,t4),(p1,p2))
    return nombre, notas

def mostrar_notas(nombre:str, notas:tuple)->tuple:
    print("Hola", str(nombre) ,"Tus notas del primer cuatrimestre son: ", "teoria ",nota_teoria(notas[0][0],notas[0][1])\
          ,",practica ", notas[1][1] , ",cuatrimestre" , nota_cuatrimestre((notas[0][0],notas[0][1]), notas[1][1]))
