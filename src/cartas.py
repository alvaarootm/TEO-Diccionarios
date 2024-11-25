"""
:author: reinaqu_2
"""

from typing import NamedTuple
import statistics
Carta = NamedTuple("Carta", [("palo",str),("valor",int)])

def crear_dicc_conteo_valores (cartas:list[Carta])->dict[int, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas (frecuencia) con ese valor
    :rtype: {int:int}
    '''
    dicc = dict()
    for carta in cartas:
        if carta.valor in dicc:
            dicc[carta.valor] = dicc[carta.valor] + 1
        else:
            dicc[carta.valor] = 1
    return dicc

def crear_dicc_valores_por_palos (cartas:list[Carta])->dict[str, list[int]]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los palos y como valores una lista con los valores de las cartas de ese palo
    :rtype: {str:[int]}
    '''
    dicc = dict()
    for carta in cartas:
        clave = carta.palo
        if clave in dicc:
            dicc[clave] += carta.valor
        else:
            dicc[clave] = [carta.valor]
    return dicc

def obtener_clave_mayor(dicc:dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}       
    Devuelve:
    :return: La clave con valor mayor, según el orden natural
    :rtype: int
    '''
    return max(dicc)

def obtener_valor_mayor_frecuencia(dicc:dict[int, int])->int:
    '''
    Recibe:
    :param dicc: Un diccionario que tiene como clave los valores de las cartas y como valores el número de cartas con ese valor
    :type: {int:int}
    Devuelve:
    :return: El valor mayor, que en ese caso es el valor de carta con una frecuencia mayor
    :rtype: int
    '''
    return max(dicc, key=dicc.get())

def obtener_media_valores_por_palos(cartas:list[Carta])->dict[str, float]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, la media de los valores de las cartas de ese palo
    :rtype: {str:float} 
    '''
    d_aux = crear_dicc_valores_por_palos(cartas)
    # res = dict()
    # for palo, lista_valores in d_aux.items():
    #     # res[palo] = sum(lista_valores)/len(lista_valores)
    #     res[palo] = statistics.mean(lista_valores)
    # return res
    return {palo: statistics.mean (lista_valores) for palo, lista_valores in d_aux}

def obtener_max_valores_por_palos(cartas:list[Carta])->dict[str, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]       
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    :rtype: {str: int}
    '''
    res = dict()
    for carta in cartas:
        clave = carta.palo
        if clave in res:
            res [clave] = max (res[clave],carta.valor)
            # if res[clave]< carta.valor:
            # res[clave] = carta.valor
        else:#clave no en diccionario
            res[clave] = carta.valor
    return res

def obtener_max_valores_por_palos2(cartas:list[Carta])->dict[str, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]       
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    :rtype: {str: int}
    '''

    d_aux = crear_dicc_valores_por_palos(cartas)
    res = dict ()
    for palo, conj_valores in d_aux.items():
        res [palo] = max (conj_valores)
    return res

def obtener_max_valores_por_palos2_comp(cartas:list[Carta])->dict[str, int]:
    '''
    Recibe:
    :param cartas: una lista de tuplas Carta(palo, valor)
    :type cartas: [Carta(str,int)]       
    Devuelve:
    :return: Un diccionario en el que la clave son los palos y los valores, el mayor valor de una carta de ese palo
    :rtype: {str: int}
    '''
    d_aux = crear_dicc_valores_por_palos(cartas)
    return {palo:max(conj_valores) for palo, conj_valores in d_aux.items}