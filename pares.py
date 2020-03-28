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

        for index in range(0, mano):
            valores = (baraja.lista_jugadores[i].mano[index].valor)

            lista_valores.append(valores)


        i += 1
        dic = {i:lista_valores.count(i) for i in lista_valores}
        dic1 = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse= True)}
        lista_puntaje = []
        for key, value in dic.items():
            temp = [key, value]
            lista_puntaje.append(temp)

        lista_diccionarios.append(lista_puntaje)

        puntuacion = (puntaje(lista_puntaje)[0])
        pares = (puntaje(lista_puntaje)[1])
        trios = (puntaje(lista_puntaje)[2])

        print("\nCantidad de pares: " + str(pares))
        print("Cantidad de trios: " + str(trios))

        tupla_jugadores = []
        tupla_jugadores.append(nombre_jugador)
        tupla_jugadores.append(puntuacion)
        tupla_jugadores.append(pares)
        tupla_jugadores.append(trios)

        lista_puntajes.append(tuple(tupla_jugadores))


        print(dic1)
        print("\nPuntuación: " + str(puntuacion) + " puntos")

    jugador_ganador = list((ganador(lista_puntajes)))
    if(len(jugador_ganador) != 0):
        ganante = "\nGanador: " + str(jugador_ganador[0]) + ", con " + str(jugador_ganador[1]) + " puntos, " + str(jugador_ganador[2]) + " pare(s) y " + str(jugador_ganador[3]) + " trio(s)."
        print(ganante)
    else:
        print("\nEmpate.")

    return lista_diccionarios, lista_puntajes

#OctavioLovesLists

def puntaje(lista_diccionarios):

    lista_puntaje = []
    puntaje = 0
    cantidad_pares = 0
    cantidad_trios = 0
    index = -1

    for elemento in lista_diccionarios:
        if elemento[1] >= 2:
            lista_puntaje.append(elemento)
            if elemento[1] % 2 == 0:
                cantidad_pares += 1
            if elemento[1] % 3 == 0:
                cantidad_trios += 1
            index += 1

            for carta in range(len(lista_puntaje)-index):
                cartas = lista_puntaje[index]
                puntaje += cartas[0]*cartas[1]


    return puntaje, cantidad_pares, cantidad_trios

def ganador(lista_puntajes):
    ganador = () #En teoria, aquí se hace un append del que, supuestamente, es el jugador con las mejores características para ganar.
    '''
        Los índices dentro de lista_puntajes son:
        [0] = Nombre del jugador.
        [1] = Puntaje del jugador.
        [2] = Número de pares del jugador.
        [3] = Número de tríos del jugador.
    '''
    for jugador in lista_puntajes: #Entra al ciclo, tupla por tupla (con la información de cada jugador). Ejemplo: (Octavio, 40, 2, 0)
        if (len(ganador) == 0): #Si la lista ganador está vacía entra a este if.
            if(jugador[1] != 0): #Omite los puntajes con cero. Si no tiene puntaje, no tiene ni pares ni trios. Se descarta.
                ganador = jugador#Si sí cumple se hace un append para que la lista ganador no esté vacía.

        elif(jugador[1] > 0): #Aquí, si el jugador en cuestión, dado por el ciclo, su puntaje es mayor a cero, entonces se empieza a comparar con el jugaddor que está en lista ganador (ahí siempre va a haber un solo jugador).

            if (jugador[2] == ganador[0][2] or jugador[3] == ganador[0][3]) and (jugador[1] > ganador[0][1] or ganador[0][1]>jugador[1]):
                '''
                    Si el número de pares del jugador y el ganador coincide o el número de trios de ambos sujetos es igual,  indica empate.  Solamente entrará al if si el puntaje del jugador
                    es mayor que el del ganador. 
                '''
                ganador = jugador


            elif(jugador[2] > ((ganador[3]))):

                '''
                    Si el número de pares del jugador es igual a dos y el número de trios del ganador es igual a uno, entonces jugador se convierte en el nuevo ganador.
                '''
                ganador = jugador

            elif(jugador[3] == 1) and (ganador[0][2] == 1):
                ganador = jugador

            elif(jugador[2] == 1) and (ganador[0][3] == 1):
                ganador = jugador

            elif(jugador[2] == 2) and (ganador[0][2] == 1):
                ganador = jugador


    return (ganador)

def main(jugadores, mano):
    lista_cartas = genera_lista_cartas()

    if (len(jugadores) >= 2 and (
    len(jugadores)) * mano <= 52):  # Tienen que ser solo dos jugadores y la mano menor a 52
        print("\n== JUEGO DE BARAJA FRANCESA ==\n")
        baraja = tarjetas.Baraja(lista_cartas)
        genera_jugadores(jugadores, baraja)
        baraja.genera_mano(mano)
        despliega_lista_manos(baraja, mano)


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
