'''
@author: reinaqu
'''
l_bso = {("Thriller",1982), 
             ("Back in Black",1980), 
             ("The Dark Side of the Moon", 1973), 
             ("The Bodyguard",1992), 
             ("Bat Out of Hell",1977), 
             ("Their Greatest Hits (1971-1975)", 1976), 
             ("Saturday Night Fever",1977), 
             ("Rumours",1977)}

def crear_dicc_titulos_anyos(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    return {bso:anyo for bso, anyo in bsos}

def crear_dicc_titulos_anyos2(bsos:list[tuple[str,int]])->dict[str, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los títulos y como valores los años
    :rtype: {str:int}
    '''
    res = {}
    for bso, anyo in bsos:
        res[bso] = anyo
    return res

def crear_dicc_anyos_conteo_titulos (bsos:list[tuple[str,int]])->dict[int, int]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores el número de títulos
          de ese año
    :rtype: {int:int}
    '''
    años = [año for _, año in bsos]
    return {año: años.count(año) for año in set(años)}

def crear_dicc_anyos_lista_titulos (bsos:list[tuple[str,int]])->dict[int, list[str]]:
    '''
    Recibe:
    :param bsos: una lista de tuplas (titulo, año)
    :type: [(str, int)]
    Devuelve:
    :return: Un diccionario que tiene como clave los años y como valores una lista con los títulos
          de ese año
    :rtype:{int:[str]}
    '''
    resultado = {}
    for titulo, año in bsos:
        if año not in resultado:
            resultado[año] = []
        resultado[año].append(titulo)
    return resultado

def obtener_clave_mayor(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: La clave con valor mayor, segun el orden natural
    :rtype: str
    '''
    max_anyo = max(dicc_bso.values())
    for titulo, anyo in dicc_bso.items():
        if anyo == max_anyo:
            return titulo

def obtener_valor_mayor(dicc_bso:dict[str,int])->int:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El valor mayor, que en este caso es el año más reciente.
    :rtype: int
    '''
    return max(dicc_bso.values())

def obtener_nombre_mas_largo(dicc_bso:dict[str,int])->str:
    '''
    Recibe:
    :param dicc_bso: Un diccionario que tiene como clave los títulos y como valores los años
    :type: {str:int}
    Devuelve:
    :return: El nombre de la canción con más caracteres
    :rtype: str
    '''
    return max(dicc_bso.keys(), key=len)