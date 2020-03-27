#!/usr/bin/python3
# Equipo: Mustafar
# Fecha: 27 de marzo de 2020
# Integrantes:
#
#   Félix López Juan Pablo
#   López Velásquez Octavio
#   Serna Navarro Ángel Emilio
''' Juego de Baraja Francesa con Clases '''
import argparse
import tarjetas


def genera_lista_cartas():
    ''' 
        genera una lista de todas las cartas de la baraja (52 cartas)
        y regresa una lista de estas
    '''
    lista_cartas = list()
    for i in range(0, 4):
        if i == 0:
            figura = "♥"  # Corazones
        elif i == 1:
            figura = "♠"  # Picas
        elif i == 2:
            figura = "♣"  # Trébol
        elif i == 3:
            figura = "♦"  # Diamante
        for valor in range(2, 15):  # los valores de las cartas empiezan en 2
            if valor == 14:
                valor = 20  # As vale 20
            carta_nueva = tarjetas.Carta(valor, figura)
            lista_cartas.append(carta_nueva)

    return lista_cartas


def genera_jugadores(lista_jugadores, baraja):
    '''
        genera los jugadores en un objeto baraja
        recibe: una lista de jugadores (string)
        recibe: un objeto baraja
    '''
    for nombre in lista_jugadores:
        nombre = tarjetas.Jugador(nombre, baraja)


def desplegar_cartas(lista_cartas):
    '''
        imprime cada carta de una lista de cartas
        POSIBLEMENTE QUEDE EN DESHUSO
    '''
    for carta in lista_cartas:
        print(carta)


def despliega_lista_manos(baraja, mano):
    '''
        imprime las cartas de todos los jugadores
        recibe: objeto baraja
    '''
    lista_puntajes = []
    i = 0
    dic = {}
    lista_diccionarios = []
    lista_jugadores = []
    for jugador in baraja.lista_jugadores:
        lista_valores = []
        cartas_mano = jugador.despliega_mano(baraja)
        nombre_jugador = (baraja.lista_jugadores[i].nombre)
        lista_jugadores.append(nombre_jugador)
        for index in range(0, mano):
            valores = (baraja.lista_jugadores[i].mano[index].valor)

            lista_valores.append(valores)

        i += 1
        dic = {i:lista_valores.count(i) for i in lista_valores}

        lista_puntaje = []
        for key, value in dic.items():
            temp = [key, value]
            lista_puntaje.append(temp)

        lista_diccionarios.append(lista_puntaje)

        puntuacion = (puntaje(lista_puntaje)[0])
        pares = (puntaje(lista_puntaje)[1])
        trios = (puntaje(lista_puntaje)[2])

        print("Cantidad de pares: " + str(pares))
        print("Cantidad de trios: " + str(trios))
        lista_puntajes.append(puntuacion)
        print("\nPuntuación: " + str(puntuacion))
    print(lista_puntajes)
    zipp = list(zip(lista_jugadores, lista_puntajes))
    print(zipp)
    return lista_diccionarios

#OctavioLovesLists

def puntaje(lista_diccionarios):

    lista_puntaje = []
    puntaje = 0
    i = 0
    cantidad_pares = 0
    cantidad_trios = 0

    for elemento in lista_diccionarios:
        if elemento[1] >= 2:
            lista_puntaje.append(elemento)
            if elemento[1] == 2:
                cantidad_pares += 1
            if elemento[1] == 3:
                cantidad_trios += 1

            for carta in lista_puntaje:
                carta = lista_puntaje[i]
                puntaje += carta[0]*carta[1]
                i += 1

    return puntaje, cantidad_pares, cantidad_trios

def main(jugadores, mano):
    lista_cartas = genera_lista_cartas()

    if (len(jugadores) >= 2 and (
    len(jugadores)) * mano <= 52):  # Tienen que ser solo dos jugadores y la mano menor a 52
        print("\n== JUEGO DE BARAJA FRANCESA ==\n")
        baraja = tarjetas.Baraja(lista_cartas)
        genera_jugadores(jugadores, baraja)
        baraja.genera_mano(mano)
        despliega_lista_manos(baraja, mano)

        #puntuacion(jugadores, baraja)
    else:
        print(
            "\nLa cantidad de cartas repartidas por jugador debe de ser acorde al número de cartas disponible en la baraja.\n")
        print("Cantidad solicitada: " + str(mano * len(jugadores)))
        print("Total de cartas disponibles: " + str(len(lista_cartas)) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jugadores', dest='jugadores',
                        help="Nombre del jugador.", required=True, action="append")
    parser.add_argument('-m', '--mano', dest='mano',
                        help="Tamaño de mano", type=int, required=False, default=5)
    args = parser.parse_args()
    jugadores = args.jugadores
    mano = args.mano

    main(jugadores, mano)
