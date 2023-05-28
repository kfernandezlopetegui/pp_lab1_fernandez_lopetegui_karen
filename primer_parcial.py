import re
import json

ruta_archivo = "primer_parcial\pp_lab1_fernandez_lopetegui_karen\dt.json"


def imprimir_dato(dato: any) -> None:
    '''
    Imprime el dato recibido
    Recibe un string o numero
    No tiene retorno

    '''
    if type(dato) == float:

        print("{0:.2f}".format(dato))
    else:
        print(dato)


def imprimir_menu(lista_menu: list) -> None:
    '''
    Imprime un menú
    Recibe una lista de strings, que hace referencia a las opciones del menu
    No tiene retorno
    '''
    imprimir_dato("----- MENÚ -----")
    for indice in range(len(lista_menu)):
        dato = "{0}-{1}".format(indice+1, lista_menu[indice])
        imprimir_dato(dato)


def validar_numero_ingresado_indices(numero: str):
    ''' 
    Verifica que el numero ingresado sea valido y lo convierte a entero.
    Recibe el numero ingresado por el usuario en str
    Si el str no se puede convertir a un número entero,
    la función imprime un mensaje de error y devuelve `None,
    caso contrario devuelve el numero.

    '''
    if numero.isdigit():
        retorno = int(numero)
    else:
        print("Lo que ha ingresado no es un número válido.")
        retorno = None
    return retorno


def validar_respuesta(lista_opciones: list, respuesta: int) -> bool:
    '''
    Valida que la respuesta ingresada este dentro del rango de la lista de opciones del menu

    Recibe una lista de opciones y un entero que hace referencia a la respuesta del usuario

    Retorna True si la respuesta del usuario esta dentro del rango de la lista de opciones,
    en caso contrario retorna False
    '''
    retorno = False
    for indice in range(1, len(lista_opciones)+1):
        if respuesta == indice:
            retorno = True
            break
    return retorno


def pedir_opcion_menu() -> str:
    '''
    Solicita al usuario que ingrese la opcion elegida
    No recibe parametros
    Retorna un string con la respuesta del usuario
    '''
    respuesta = input("Ingrese una opcion del menú: ")

    return respuesta


def pedir_respuesta_validada() -> (int | None):
    '''
    Le solicita al usuario una respuesta y  valida que el numero ingresado sea entero
    No recibe parametros
    Retorna la respuesta del usuario
    '''
    respuesta = pedir_opcion_menu()
    respuesta = validar_numero_ingresado_indices(respuesta)
    return respuesta


def pedir_respuesta_menu_validada(lista_opciones: list) -> int:
    '''
    Le pide al usuario una respuesta hasta que está sea valida
    Recibe la lista de opciones del menu
    Retorna la respuesta del usuario validada.
    '''
    while True:
        respuesta = pedir_respuesta_validada()
        if respuesta != None and validar_respuesta(lista_opciones, respuesta):
            return respuesta


def dream_team_menu_principal() -> int:
    '''
    Imprime el menu de Dream Team y le pide al usuario que ingrese su respuesta
    No recibe parametros
    Retorna la respuesta del usuario validada 

    '''

    lista_menu = ["Mostrar lista de jugadores del Dream Team",
                  "Seleccionar índice del jugador y mostrar estadísticas",
                  "Guardar estadisticas del jugador seleccionado anteriormente",
                  "Buscar jugador por nombre y mostrar logros",
                  "Mostrar promedio de puntos por partido del equipo Dream Team",
                  "Buscar jugador y mostrar si está en el Salón de la Fama",
                  "Mostrar el jugador con la mayor cantidad de rebotes totales",
                  "Mostrar el jugador con el mayor porcentaje de tiros de campo",
                  "Mostrar el jugador con la mayor cantidad de asistencias totales",
                  "Mostrar jugadores con puntos superiores al promedio ingresado",
                  "Mostrar jugadores con rebotes superiores al promedio ingresado",
                  "Mostrar jugadores con asistencias superiores al promedio ingresado",
                  "Mostrar jugador con mayor cantidad de robos totales",
                  "Mostrar jugador con mayor cantidad de bloqueos totales",
                  "Mostrar jugadores con porcentajes de tiros libres superiores al ingresado",
                  "Mostrar promedio de puntos por partido del equipo sin el jugador de menor puntuación",
                  "Mostrar jugador con mayor cantidad de logros obtenidos",
                  "Mostrar jugadores con porcentaje de tiros triples mayor al ingresado",
                  "Mostrar jugador con mayor cantidad de temporadas jugadas",
                  "Mostrar jugadores con porcentaje de tiros de campo superior al valor ingresado, ordenados por posición.",
                  "Salir"]
    imprimir_menu(lista_menu)
    respuesta = pedir_respuesta_menu_validada(lista_menu)
    return respuesta


def crear_lista_desde_json(nombre_archivo: str) -> list:
    '''
    Convierte y copia el archivo Json a una lista
    Recibe un String con el nombre del archivo Json
    Retorna la lista convertida
    '''
    lista = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]

    return lista


def capitalizar_palabras(cadena: str) -> str:
    '''
    Capitaliza todas las palabras de la cadena ingresada quedando asi -> Cadena Ingresada
    Recibe un String con la cadena a capitalizar
    Retorna la cadena capitalizada
    '''
    cadena = re.split(" ", cadena)
    cadena_auxiliar = ""
    for palabra in cadena:

        cadena_auxiliar = cadena_auxiliar+palabra.capitalize()+" "

    return cadena_auxiliar.strip()


def obtener_nombre_capitalizado(diccionario: dict) -> str:
    '''
    Obtiene la clave 'nombre' del diccionario ingresado y lo capitaliza
    Recibe un diccionario
    Retorna un String con el nombre capitalizado
    '''
    nombre_obtenido = capitalizar_palabras(diccionario["nombre"])

    return nombre_obtenido


def obtener_nombre_y_dato(diccionario: dict, key: str) -> str:
    '''
    Obtiene un nombre y datos solicitado
    Recibe una diccionario y  string con la clave
    Retorna un String en formato: Nombre - Dato Solicitado
    '''

    nombre_obtenido = obtener_nombre_capitalizado(diccionario).strip()
    dato_obtenido = capitalizar_palabras(diccionario[key]).strip()
    if (type(dato_obtenido) == float):
        texto_formateado = "{0} - {1:.2f}".format(
            nombre_obtenido, dato_obtenido)
    else:
        texto_formateado = "{0} - {1}".format(
            nombre_obtenido, dato_obtenido)

    return texto_formateado


def imprimir_nombres(lista: list):
    '''
    Imprime una lista de nombres ingresados si la lista no esta vacia
    Recibe una lista de diccionarios
    Retorna -1 si la lista esta vacia

    '''
    if len(lista) > 0:

        for elemento in lista:
            nombre_y_posicion = obtener_nombre_capitalizado(elemento)
            imprimir_dato(nombre_y_posicion)
    else:
        return -1


def imprimir_nombres_y_posicion(lista: list):
    '''
    Imprime los nombres de la lista y su posicion 
    Recibe una lista de diccionarios
    Retorna -1 si la lista esta vacia

    '''
    if len(lista) > 0:

        for elemento in lista:
            nombre_y_posicion = obtener_nombre_y_dato(elemento, "posicion")
            imprimir_dato(nombre_y_posicion)
    else:
        return -1


def dar_mensaje_error() -> None:
    '''
    Imprime un mensaje de error
    No recibe parametros
    No tiene retorno
    '''
    imprimir_dato("Error.No se pudo realizar la accion.")


def dt_imprimir_nombre_y_posicion(nombre_archivo: str) -> None:
    '''
    Abre el archivo imprime el nombre y la posicion de los jugadores y lo cierra
    Recibe un string con el nombre del archivo
    No tiene retorno
    '''
    lista = []
    imprimir_dato("Lista jugadores Dream Team:")
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        if len(lista) > 0:
            imprimir_nombres_y_posicion(lista)
        else:
            dar_mensaje_error()


def imprimir_indice_y_nombre(lista: list):
    '''
    Imprime una lista de nombres con sus indices
    Recibe una lista de diccionarios
    Retorna -1 si la lista esta vacia

    '''
    if len(lista) > 0:

        for indice in range(len(lista)):
            nombre = obtener_nombre_capitalizado(lista[indice])
            imprimir_dato("{0}-{1}".format(indice+1, nombre))
    else:
        return -1


def dt_imprimir_indice_y_nombre(nombre_archivo: str) -> None:
    '''
    Abre el archivo imprime el indice y nombre de los jugadores y lo cierra
    Recibe un string con el nombre del archivo
    No tiene retorno
    '''
    lista = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        if len(lista) > 0:
            imprimir_indice_y_nombre(lista)
        else:
            dar_mensaje_error()


def pedir_respuesta_indice_jugador(nombre_archivo: str):
    '''
    Le pide al usuario que ingrese una respuesta y la valida,
    para esto abre el archivo y se lo pasa a la funcion que retorna la respuesta validada
    segun la lista que le pasen por parametro,cuando obtiene la respuesta solicitada la retorna
    Si la lista de jugadores esta vacia imprime un mensaje de error
    Recibe un string con el nombre del archivo.
    '''
    lista = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        if len(lista) > 0:
            return pedir_respuesta_menu_validada(lista)-1
        else:
            dar_mensaje_error()


def mostrar_estadisticas(diccionario_jugador: dict) -> None:
    '''
    Imprime las estadisticas del jugador ingresado
    Recibe un diccionario con la informacion del jugador a imprimir
    No tiene retorno
    '''
    nombre_jugador = obtener_nombre_capitalizado(diccionario_jugador)
    diccionario_estadisticas = diccionario_jugador["estadisticas"]

    imprimir_dato("+" + "-" * 38 + "+" + "-" * 11 + "+")
    imprimir_dato("Estadisticas del jugador {}".format(nombre_jugador))

    for clave, valor in diccionario_estadisticas.items():
        clave = clave.capitalize().replace("_", " ")

        imprimir_dato("+" + "-" * 38 + "+" + "-" * 11 + "+")
        imprimir_dato("| {:<36} | {:>9} |".format(clave, valor))
    imprimir_dato("+" + "-" * 38 + "+" + "-" * 11 + "+")


def dt_mostrar_estadisticas_jugador(nombre_archivo: str, indice_jugador: int) -> None:
    '''
    Abre el archivo imprime las estadisticas del jugador solicitado y lo cierra
    Recibe un string con el nombre del archivo y un entero con el indice del jugador que se desea imprimir
    No tiene retorno
    '''
    lista = []

    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        diccionario_jugador = lista[indice_jugador]
        mostrar_estadisticas(diccionario_jugador)


def dt_seleccionar_y_mostrar_estadisticas_jugador(nombre_archivo: str) -> int:
    '''
    Muestra el indice y nombre de los jugadores para que el usuario ingrese el indice del jugador
    que desea ver sus estadisticas y luego imprime las estadisticas del seleccionado.

    Recibe el nombre del archivo donde se encuentra la lista de jugadores

    Retorna el indice ingresado por el usuario

    '''

    dt_imprimir_indice_y_nombre(nombre_archivo)
    respuesta_usuario = pedir_respuesta_indice_jugador(nombre_archivo)
    dt_mostrar_estadisticas_jugador(nombre_archivo, respuesta_usuario)
    return respuesta_usuario


def guardar_archivo_csv(nombre_archivo: str, lista: list) -> bool:
    '''
    Guarda la lista recibida en formato csv
    Recibe un string que contiene el nombre que va a tener el archivo y/o direccion
    y la lista a guardar en formato csv
    Retorna True si se pudo guardar,  en caso contrario False
    '''
    if len(lista) > 0:
        lista_claves = list(lista[0].keys())
        cabecera = ",".join(lista_claves)
        with open(nombre_archivo, "w") as archivo:
            archivo.write(cabecera + "\n")
            for elemento in lista:
                lista_valor = list(elemento.values())
                lista_valor_str = []
                for valor in lista_valor:
                    lista_valor_str.append(str(valor))
                dato = ",".join(lista_valor_str)
                archivo.write(dato + "\n")
        retorno = True
    else:
        retorno = False

    return retorno


def crear_lista_estadisticas(diccionario: dict) -> list:
    '''
    Crea la lista de diccionarios de las estadisticas del jugador ingresado
    Recibe un diccionario con los datos del jugador
    Retorna la lista de estadisticas creada
    '''
    lista_estadisticas = []
    diccionario_auxiliar = {}
    estadisticas_jugador = diccionario["estadisticas"]
    diccionario_auxiliar["nombre"] = diccionario["nombre"]
    diccionario_auxiliar["posicion"] = diccionario["posicion"]
    for clave, valor in estadisticas_jugador.items():
        diccionario_auxiliar[clave] = valor

    lista_estadisticas.append(diccionario_auxiliar)
    return lista_estadisticas


def guardar_archivo_estadisticas_csv(in_nombre_archivo: str, indice_jugador: int) -> None:
    '''
    Guarda la lista de estadisticas del jugador seleccionado en formato csv
    Recibe el nombre del archivo de donde va a sacar la informacion y el indice del jugador que
    se desea guardar.
    No tiene retorno
    '''
    lista = []
    with open(in_nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        diccionario_jugador = lista[indice_jugador]
        nombre_archivo = "estadisticas_{0}.csv".format(indice_jugador)
        lista_guardar = crear_lista_estadisticas(diccionario_jugador)

    guardar_archivo_csv(nombre_archivo, lista_guardar)
    imprimir_dato("Se ha creado exitosamente el archivo.")


def preguntar_si_desea_continuar() -> bool:
    '''
    Le pregunta al usuario si desea continuar
    No recibe ningun parametro
    Retorna True en caso de la respuesta ser S o s, en caso contrario False
    '''
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == "s":
        retorno = True
    else:
        retorno = False
    return retorno


def dar_mensaje_error_estadisticas() -> None:
    '''
    Imprime un mensaje de error para el usuario si este intenta guardar un jugador sin ser
    previamente seleccionado
    No recibe parametros
    No tiene retorno
    '''
    imprimir_dato(
        "No se ha ingresado previamente al jugador que quiere guardar")
    imprimir_dato("Ingrese a la opcion 2 para poder realizar la accion")


def validar_entrada_nombre(palabra_ingresada: str) -> bool:
    '''
    Valida que el nombre ingresado no contenga numeros ni caracteres especiales
    Recibe un string, con el nombre ingresado por el usuario
    Retorna true si el patron no contiene numeros ni caracteres especiales,
    False en caso contrario
    '''
    patron = r'[^a-zA-Z ]$'

    if re.search(patron, palabra_ingresada):
        imprimir_dato("Nombre ingresado invalido")
        retorno = False
    else:
        retorno = True
    return retorno


def pedir_nombre_validado() -> str:
    '''
    Le pide al usuario que ingrese un nombre hasta obtener uno valido
    No recibe parametros
    Retorna el nombre obtenido
    '''
    nombre_valido = False
    while nombre_valido == False:
        nombre = input("Ingrese el nombre a buscar: ")
        nombre_valido = validar_entrada_nombre(nombre)
    return nombre


def buscar_nombre(nombre_buscado: str, lista_diccionarios: list) -> list:
    '''
    Busca el indice que hace referencia al nombre buscado
    Recibe un string con el nombre buscado y una lista de diccionarios con los jugadores
    Retorna una lista con los indices de los jugadores que coinciden con la info ingresada
    '''
    nombre_buscado = capitalizar_palabras(nombre_buscado)

    lista_indices = []
    verificacion = r"{0}+".format(nombre_buscado)
    for indice in range(len(lista_diccionarios)):
        if re.search(verificacion, lista_diccionarios[indice]["nombre"]):
            lista_indices.append(indice)

    return lista_indices


def buscar_por_nombre(nombre_archivo: str) -> list:
    '''
    Le pide al usuario que ingrese el nombre del jugador que quiere buscar,
    abre el archivo para buscar los indices de los jugadores que coinciden con el 
    nombre ingresado y lo cierra

    Recibe un string que contiene el nombre del archivo donde se encuentran los jugadores

    Retorna una lista con los indices que coincidieron.
    '''
    nombre_buscar = pedir_nombre_validado()
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        indices_nombres = buscar_nombre(nombre_buscar, lista)

    return indices_nombres


def mostrar_logros(diccionario_jugador: dict) -> None:
    '''
    Muestra los logros del jugador ingresado
    Recibe un diccionario con la informacion del jugador
    No tiene retorno
    '''
    nombre_jugador = obtener_nombre_capitalizado(diccionario_jugador)
    lista_logros = diccionario_jugador["logros"]

    imprimir_dato("Logros del jugador {}".format(nombre_jugador))
    imprimir_dato("+" + "-" * 40 + "+")

    for logro in lista_logros:
        imprimir_dato("{0}".format(logro))

    imprimir_dato("+" + "-" * 40 + "+")


def mostrar_sus_logros_por_indice(nombre_archivo: str, indice_jugador: int) -> None:
    '''
    Abre el archivo donde se encuentran todos los jugadores y muestra
    los logros del indice del jugador ingresado(puede ser mas de un indice)
    y luego cierra el archivo

    Recibe un String con el nombre del archivo que contiene la informacion de los 
    jugadores y un entero con el indice del jugador

    No tiene retorno
    '''
    lista = []

    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        if (len(indice_jugador) > 0):
            for indice in indice_jugador:

                diccionario_jugador = lista[indice]
                mostrar_logros(diccionario_jugador)
        else:
            imprimir_dato("No se ha encontrado el nombre ingresado.")


def dt_mostrar_logros_jugador_por_nombre(nombre_archivo: str) -> None:
    '''
    Le pide al usuario que ingrese el nombre del jugador y muestra sus logros
    Recibe un string con el nombre del archivo
    No tiene retorno
    '''
    indice_jugadores = buscar_por_nombre(nombre_archivo)
    mostrar_sus_logros_por_indice(nombre_archivo, indice_jugadores)


def sumar_dato_jugador(lista: list, clave: str):
    '''
    Suma los datos de las estadisticas de los jugadores requeridos
    Recibe una lista de diccionarios y una clave 
    Retorna el resultado final de la suma
    '''

    suma = 0
    for jugador in lista:
        if (type(jugador) == dict and len(jugador) > 0):
            parametro = jugador["estadisticas"][clave]
            suma = suma+parametro

    return suma


def dividir(dividendo: float, divisor: float):
    '''
    Realiza la division de los numeros ingresados
    Recibe dos numeros, dividendo y divisor
    Retorna 0 si el divisor es 0, retorna el resultado en caso contrario

    '''
    if divisor == 0:
        retorno = 0
        print("No se puede dividir por 0")
    else:
        retorno = dividendo/divisor
    return retorno


def obtener_promedio_general(nombre_archivo: str, clave: str):
    '''
    Abre el archivo obtiene el promedio general de la clave ingresada y lo cierra
    Recibe dos strings uno con el nombre de archivo y el otro con la clave
    Retorna el promedio
    '''
    lista = []

    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        promedio = dividir(sumar_dato_jugador(lista, clave), len(lista))
    return promedio


def mostrar_resultados_general(resultado: float, clave: str) -> None:
    '''
    Muestra el resultado ingresado
    Recibe un float con el resultado y un string con la clave
    a la que hace referencia el resultado
    No tiene retorno

    '''
    texto_mostrar = "El resultado de {} de todo el equipo Dream Team es:".format(
        clave.capitalize().replace("_", " "))
    imprimir_dato(texto_mostrar)

    imprimir_dato(resultado)


def ordenar_por_sortquick_asc_des(lista_original: list, clave: str, orden: bool) -> list:
    '''
    Ordena de forma ascendente o descendente la lista ingresada en funcion de la clave y
    dependiendo el valor de 'orden' ingresado
    Recibe una lista de diccionarios, un string como la clave por la que van a ordenar 
    y un booleano que controla el orden ascendente('orden'=True) o descendente ('orden'=False)
    Retorna la lista ordenada
    '''

    lista_derecha = []
    lista_izquierda = []
    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:

            if orden == True and elemento[clave] > pivot[clave] or orden == False and elemento[clave] < pivot[clave]:
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento)

    lista_izquierda = ordenar_por_sortquick_asc_des(
        lista_izquierda, clave, orden)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_por_sortquick_asc_des(lista_derecha, clave, orden)
    lista_izquierda.extend(lista_derecha)

    return lista_izquierda


def mostrar_nombres_ordenados_asc_des(nombre_archivo: str, orden=True) -> None:
    '''
    Abre el archivo y muestra los nombres ordenados de forma ascendente predeterminado
    y luego lo cierra
    Recibe un string con el nombre del archivo y un booleano con el valor por defecto True
    No tiene retorno
    '''

    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        lista_ordenada = ordenar_por_sortquick_asc_des(lista, "nombre", orden)
    imprimir_nombres(lista_ordenada)


def mostrar_nombres_ordenados_con_promedio(nombre_archivo: str) -> None:
    '''
    Muestra los nombres ordenados ascendentes y el promedio general de puntos por partido
    Recibe un string con el nombre del archivo de jugadores
    No tiene retorno
    '''
    imprimir_dato("Los jugadores del Dream Team son: ")
    mostrar_nombres_ordenados_asc_des(nombre_archivo)
    promedio_gral = (obtener_promedio_general(
        nombre_archivo, "promedio_puntos_por_partido"))
    mostrar_resultados_general(
        promedio_gral, "promedio_puntos_por_partido")


def pertenece_salon_de_la_fama(lista: list, indice_jugador: int) -> str:
    '''
    Verifica si el indice de jugador ingresado pertenece o no al Salon de la fama
    Recibe la lista de jugadores y el indice del jugador que se consulto
    Retorna el logro que detalla si es miembro o "No es Miembro del salon de la fama"
    '''
    busqueda = "Miembro del Salon de la Fama del Baloncesto"
    jugador = lista[indice_jugador]

    verificacion = r"{0}+".format(busqueda)

    for indice in jugador["logros"]:
        if re.search(verificacion, indice):
            pertenece = indice
        else:
            pertenece = "No es Miembro del salon de la fama"

    return pertenece


def mostrar_pertenecia(pertenencia: str, lista: list, indice_jugador: int) -> None:
    '''
    Muestra la pertenencia del jugador
    Recibe un string con la pertenencia, la lista de jugadores y un entero con el indice
    del jugador a mostrar
    No tiene retorno
    '''
    nombre_jugador = obtener_nombre_capitalizado(lista[indice_jugador])
    if re.search(r"^[No]+", pertenencia):
        imprimir_dato("El jugador {0} {1}".format(nombre_jugador, pertenencia))

    else:
        imprimir_dato("El jugador {0} es {1}".format(
            nombre_jugador, pertenencia))


def mostrar_si_pertenece_salon_de_la_fama(nombre_archivo: str) -> None:
    '''
    Muestra la pertenencia del jugador ingresado al salon de la fama
    Abre el archivo de los jugadores y lo cierra al terminar de mostrar su pertenencia
    Recibe un string con el nombre del archivo de los jugadores
    '''
    nombre_ingresado = buscar_por_nombre(nombre_archivo)
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        if len(nombre_ingresado) > 0:

            for indice in nombre_ingresado:
                pertenece = pertenece_salon_de_la_fama(lista, indice)
                mostrar_pertenecia(pertenece, lista, indice)


def calcular_max(lista: list, key: str, clave_sec: str):
    '''
    Calcula el maximo de la lista en funcion de las claves ingresadas
    Recibe una lista, dos strings con las claves para buscar el maximo
    retorna el maximo encontrado
    '''
    bandera_del_primero = True
    for elemento in lista:
        if (bandera_del_primero == True or elemento[key][clave_sec] > max):
            bandera_del_primero = False
            max = elemento[key][clave_sec]
    return max


def calcular_min(lista: list, key: str, clave_sec: str):
    '''
    Calcula el minimo de la lista en funcion de las claves ingresadas
    Recibe una lista, dos strings con las claves para buscar el minimo
    Retorna el minimo encontrado
    '''
    bandera_del_primero = True
    for elemento in lista:
        if (bandera_del_primero == True or elemento[key][clave_sec] < min):
            bandera_del_primero = False
            min = elemento[key][clave_sec]
    return min


def calcular_mayores(lista: list, clave: str, clave_sec: str) -> list:
    '''
    Calcula si hay mas de un maximo en una busqueda
    Recibe una lista, dos strings con las claves para buscar el maximo
    Retorna una lista con los mayores encontrados
    '''
    lista_mayor = []
    maximo = calcular_max(lista, clave, clave_sec)
    for elemento in lista:
        if float(elemento[clave][clave_sec]) == maximo:
            lista_mayor.append(elemento)

    return lista_mayor


def calcular_estadisticas_max(nombre_archivo: str, clave: str) -> list:
    '''
    Calcula el maximo en 'estadisticas' en funcion de la clave ingresada
    Abre el archivo de jugadores para realizar la busqueda y lo cierra al obtener el resultado
    Recibe dos strings uno con el nombre del archivo y el otro con la clave
    Retorna la lista con los mayores en funcion de la clave ingresada
    '''
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        mayores = calcular_mayores(lista, "estadisticas", clave)
    return mayores


def mostrar_y_calcular_mayor_por_clave_estadisticas(nombre_archivo: str, clave: str) -> None:
    '''
    Muestra y calcula al mayor o mayores en funcion de la clave ingresada
    Recibe dos strings, uno con el nombre de archivo de los jugados y el segundo la clave
    No tiene retorno
    '''
    mayor = calcular_estadisticas_max(nombre_archivo, clave)
    if len(mayor) > 0:
        for elemento in mayor:
            nombre_jugador = obtener_nombre_capitalizado(elemento)
            valor = elemento["estadisticas"][clave]
            imprimir_dato("El jugador con mayor {0} es {1} con {2}".format(
                clave.replace("_", " "), nombre_jugador, valor))


def calcular_max_logros(lista: list) -> int:
    '''
    Calcula el maximo de la lista en la clave 'logros'
    Recibe una lista y una clave para buscar el maximo
    retorna el maximo encontrado
    '''
    bandera_del_primero = True
    for elemento in lista:
        if (bandera_del_primero == True or len(elemento["logros"]) > max):
            bandera_del_primero = False
            max = len(elemento["logros"])
    return max


def calcular_mayores_logros(lista: list) -> list:
    '''
    Calcula si hay uno o mas mayores en la lista y la clave 'logros'
    Recibe la lista de jugadores
    Retorna la lista con los mayores
    '''
    lista_mayor = []
    maximo = calcular_max_logros(lista)
    for elemento in lista:
        if len(elemento["logros"]) == maximo:
            lista_mayor.append(elemento)

    return lista_mayor


def calcular_max_mayores_logros(nombre_archivo: str) -> list:
    '''
    Abre el archivo para realizar el calculo del que tiene mayores logros y luego 
    cierra el archivo
    Recibe un string con el nombre del archivo
    Retorna una lista con los que tienen el mayor logro
    '''
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        mayores = calcular_mayores_logros(lista)
    return mayores


def mostrar_y_calcular_mayor_logros(nombre_archivo: str) -> None:
    '''
    Muestra y calcula a el/los que tienen mayores logros
    Recibe un string con el nombre del archivo de los jugadores
    No tiene retorno
    '''
    mayor = calcular_max_mayores_logros(nombre_archivo)
    if len(mayor) > 0:
        for elemento in mayor:
            nombre_jugador = obtener_nombre_capitalizado(elemento)
            imprimir_dato(
                "El jugador con mayores logros es {0}\n".format(nombre_jugador))
            mostrar_logros(elemento)


def validar_numero_ingresado(numero: str):
    '''
    Valida el numero ingreso y si es valido lo convierte a float
    Recibe un string con el numero ingresado
    Retorna el numero si es valido, caso contrario None
    '''
    if numero.isdigit():
        retorno = float(numero)
    else:
        print("Lo que ha ingresado no es un número válido.")
        retorno = None
    return retorno


def pedir_numero():
    '''
    Pide al usuario que ingrese un numero
    No recibe ningun parametro
    Retorna el numero ingresado  si es valido, None en caso contrario
    '''
    numero_ingresado = input("Ingrese un numero: ")
    numero_ingresado = validar_numero_ingresado(numero_ingresado)
    return numero_ingresado


def calcular_mayores_a_parametro(lista: list, clave: str, clave_sec: str, maximo: float) -> list:
    '''
    Calcula los que son mayores al numero ingresado y los guarda en una lista
    Recibe una lista, dos strings con las claves en las que se buscaran los mayores,
    y un float que sera el numero por el que se van a comparar los valores
    Retorna la lista con los mayores al numero ingresado
    '''
    lista_mayor = []
    for elemento in lista:
        if float(elemento[clave][clave_sec]) > maximo:
            lista_mayor.append(elemento)

    return lista_mayor


def calcular_estadisticas_por_parametro_ingresado(
        nombre_archivo: str, clave: str, parametro_ingresado: float) -> list:
    '''
    Abre el archivo para calcular los mayores al parametro ingresado en funcion de la 
    clave ingresada y lo cierra.
    Recibe dos strings, uno con el nombre del archivo de los jugadores, la segunda con la clave
    y un float con el valor a ser comparado.
    Retorna la lista de los mayores 
    '''
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        lista_mayores = calcular_mayores_a_parametro(
            lista, "estadisticas", clave, parametro_ingresado)
    return lista_mayores


def mostrar_mayor_por_parametro(nombre_archivo: str, clave: str) -> None:
    '''
    Muestra a todos los jugadores que tienen valores superiores al numero ingresado
    en la clave solicitada
    Recibe dos strings, uno con el nombre del archivo de jugadores y la segunda con la clave
    No tiene retorno
    '''
    numero_ingresado = pedir_numero()
    if numero_ingresado != None:
        mayores = calcular_estadisticas_por_parametro_ingresado(
            nombre_archivo, clave, numero_ingresado)

        if len(mayores) > 0:
            imprimir_dato("Los jugadores que superan el numero ingresado en {0} son: ".format(
                clave.replace("_", " ")))
            for elemento in mayores:
                nombre_jugador = obtener_nombre_capitalizado(elemento)
                valor = elemento["estadisticas"][clave]

                imprimir_dato("{0} con {1}".format(nombre_jugador, valor))
        else:
            imprimir_dato(
                "No hay nadie que supere el valor del numero ingresado")

    else:
        imprimir_dato(
            "No se puede mostrar informacion con el numero ingresado.")


def mostrar_mayor_por_parametro_ordenado(nombre_archivo: str, clave: str) -> None:
    '''
    Muestra a todos los jugadores que tienen valores superiores al numero ingresado
    en la clave solicitada y ordenados por su posicion
    Recibe dos strings, uno con el nombre del archivo de jugadores y la segunda con la clave
    No tiene retorno
    '''
    numero_ingresado = pedir_numero()
    if numero_ingresado != None:
        mayores = calcular_estadisticas_por_parametro_ingresado(
            nombre_archivo, clave, numero_ingresado)

        if len(mayores) > 0:
            imprimir_dato("Los jugadores que superan el numero ingresado en {0} son: ".format(
                clave.replace("_", " ")))
            mayores_ordenados = ordenar_por_sortquick_asc_des(
                mayores, "posicion", True)

            imprimir_nombres_y_posicion(mayores_ordenados)

        else:
            imprimir_dato(
                "No hay nadie que supere el valor del numero ingresado")

    else:
        imprimir_dato(
            "No se puede mostrar informacion con el numero ingresado.")


def crear_lista_sin_el_menor(nombre_archivo: str, clave: str) -> list:
    '''
    Abre el archivo y crea una lista sin el jugador que tenga menores puntos en la clave
    ingresada y lo cierra
    Recibe dos strings, uno con el nombre del archivo de jugadores y la segunda con la clave
    Retorna la lista sin el menor
    '''
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
        menor_promedio = calcular_min(lista, "estadisticas", clave)
        lista_sin_el_menor = calcular_estadisticas_por_parametro_ingresado(
            nombre_archivo, clave, menor_promedio)
    return lista_sin_el_menor


def calcular_promedio_sin_el_menor(nombre_archivo: str, clave: str):
    '''
    Calcula el promedio general de la clave ingresada sin el jugador de menor puntaje
    Recibe dos strings, uno con el nombre del archivo de jugadores y la segunda con la clave
    retorna el resultado del promedio
    '''
    lista = crear_lista_sin_el_menor(nombre_archivo, clave)
    promedio = dividir(sumar_dato_jugador(lista, clave), len(lista))
    return promedio


def mostrar_y_calcular_promedio_sin_el_menor(nombre_archivo: str, clave: str) -> None:
    '''
    Calcula y muestra el promedio sin el del menor puntaje
    Recibe dos strings, uno con el nombre del archivo de jugadores y la segunda con la clave
    No tiene retorno
    '''
    promedio = calcular_promedio_sin_el_menor(nombre_archivo, clave)
    imprimir_dato("El {0} sin el que tiene menor puntaje es de: ".format(
        clave.replace("_", " ")))
    imprimir_dato(promedio)


def dream_team_app(nombre_archivo: str) -> None:
    '''
    Es la app que corre todo el programa con el menu de usuario y las opciones
    Recibe un string con el nombre del archivo de los jugadores
    No tiene retorno
    '''
    continuar_programa = True
    indice_estadisticas = None
    while continuar_programa:

        respuesta_menu = dream_team_menu_principal()

        match(respuesta_menu):
            case 1:
                dt_imprimir_nombre_y_posicion(nombre_archivo)

            case 2:

                indice_estadisticas = dt_seleccionar_y_mostrar_estadisticas_jugador(
                    nombre_archivo)
            case 3:
                if (indice_estadisticas != None):
                    guardar_archivo_estadisticas_csv(
                        nombre_archivo, indice_estadisticas)
                else:
                    dar_mensaje_error_estadisticas()

            case 4:
                dt_mostrar_logros_jugador_por_nombre(nombre_archivo)
            case 5:
                mostrar_nombres_ordenados_con_promedio(nombre_archivo)
            case 6:
                mostrar_si_pertenece_salon_de_la_fama(nombre_archivo)
            case 7:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "rebotes_totales")
            case 8:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "porcentaje_tiros_de_campo")
            case 9:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "asistencias_totales")
            case 10:
                mostrar_mayor_por_parametro(
                    nombre_archivo, "promedio_puntos_por_partido")
            case 11:
                mostrar_mayor_por_parametro(
                    nombre_archivo, "promedio_rebotes_por_partido")
            case 12:
                mostrar_mayor_por_parametro(
                    nombre_archivo, "promedio_asistencias_por_partido")
            case 13:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "robos_totales")
            case 14:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "bloqueos_totales")
            case 15:
               mostrar_mayor_por_parametro(
                    nombre_archivo, "porcentaje_tiros_libres")
            case 16:
                mostrar_y_calcular_promedio_sin_el_menor(
                    nombre_archivo, "promedio_puntos_por_partido")
            case 17:
                mostrar_y_calcular_mayor_logros(nombre_archivo)
            case 18:
                mostrar_mayor_por_parametro(
                    nombre_archivo, "porcentaje_tiros_triples")
            case 19:
                mostrar_y_calcular_mayor_por_clave_estadisticas(
                    nombre_archivo, "temporadas")
            case 20:
                mostrar_mayor_por_parametro_ordenado(
                    nombre_archivo, "porcentaje_tiros_de_campo")
            case 21:
                continuar_programa = False

        if continuar_programa:
            continuar_programa = preguntar_si_desea_continuar()

    print("Fin del programa.")


def main() -> None:
    '''
    Es la funcion en la que se llama a la aplicacion
    No recibe parametros
    No tiene retorno
    '''
    dream_team_app(ruta_archivo)


main()
