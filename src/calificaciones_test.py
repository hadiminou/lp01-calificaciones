from calificaciones import*
from calificaciones_ui import *
def test_nota_teoria():
    print("nota de bloque teorico es: ", nota_teoria(9.1 ,7.2))
    print("nota de bloque teorico es: ", nota_teoria(4.0 ,6.0))
    print("nota de bloque teorico es: ", nota_teoria(4.0 ,3.0))
    print("nota de bloque teorico es: ", nota_teoria(None ,3.0))
    print("nota de bloque teorico es: ", nota_teoria(9.0 ,None))

def test_nota_cuatrimestre():    
    print("nota de cuatrimestre es: ", nota_cuatrimestre((9.1 ,7.2), 8.1))
    print("nota de cuatrimestre es: ", nota_cuatrimestre((4.0 ,6.0), 5.0))
    print("nota de cuatrimestre es: ", nota_cuatrimestre((4.0 ,3.0), None))
    print("nota de cuatrimestre es: ", nota_cuatrimestre((None ,3.0), None))
    print("nota de cuatrimestre es: ", nota_cuatrimestre((9.0 ,None), 4.5))

def test_nota_continua():
    print(("nota continua es: "), nota_continua((9.6 ,9.9 ,10.0 ,9.8),(9.7 ,9.5)))
    print(("nota continua es: "), nota_continua((4.4 ,4.9 ,5.1 ,4.7),(4.6 ,4.8)))
    print(("nota continua es: "), nota_continua((4.0, 6.0, 4.0, 3.0),(5.0, None)))
    print(("nota continua es: "), nota_continua((9.0, None, 4.0, 3.0),(4.5, None)))

if __name__=="__main__":
    test_nota_teoria()
    test_nota_cuatrimestre()
    test_nota_continua()
    nombre, tupla_notas = solicita_notas()
    mostrar_notas(nombre, tupla_notas)