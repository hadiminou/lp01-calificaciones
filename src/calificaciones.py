from collections import namedtuple
def a_cero(variable):
    if variable==None:
        variable=0
    return variable    

def nota_teoria(examen1, examen2)->float:
    '''_summary_

    :param examen1: Nota del primer examen teoria
    :type examen1: float
    :param examen2: Nota del primer examen teoria
    :type examen2: float
    :return: _description_
    :rtype: float
    '''
    '''if examen1==None:
        examen1=0
    if examen2==None:
        examen2=0
    res=(examen1+examen2)/2
    return res'''
    # examen1= a_cero(examen1)
    # examen2= a_cero(examen2)
    return ((a_cero(examen1))+(a_cero(examen2)))/2

def nota_cuatrimestre(teoricos:tuple, practico)->float:
    '''_summary_

    :param teoricos: notas de teoricos
    :type teoricos: tuple
    :param practico: nota de practico
    :type practico: float
    :return: la nota de cuatrimestre
    :rtype: float
    '''
    teoricos1= a_cero(teoricos[0])
    teoricos2= a_cero(teoricos[1])
    if nota_teoria(teoricos1,teoricos2)>=4:
        res=0.1*(teoricos1+teoricos2)+0.8*(practico)
    else:
        res=0
    return res

def nota_continua(teoricos:tuple, practicos:tuple)->float:
    teor0=a_cero(teoricos[0])
    teor1=a_cero(teoricos[1])
    teor2=a_cero(teoricos[2])
    teor3=a_cero(teoricos[3])
    prac0=a_cero(practicos[0])
    prac1=a_cero(practicos[1])
    notacontinua1=nota_cuatrimestre((teor0,teor1),(prac0))
    notacontinua2=nota_cuatrimestre((teor2,teor3),(prac1))
    if notacontinua1>=4 and notacontinua2>=4:
        notacontinua=(notacontinua1+notacontinua2)/2
    else:
        notacontinua=min(4,(notacontinua1 + notacontinua2)/2)
    return notacontinua 