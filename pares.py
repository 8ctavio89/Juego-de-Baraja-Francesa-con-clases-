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
            figura = "C" # Corazones
        elif i == 1:
            figura = "P" # Picas
        elif i == 2:
            figura = "T" # Trébol
        elif i == 3:
            figura = "D" # Diamante
        for valor in range(2, 15): # los valores de las cartas empiezan en 2
            if valor == 14:
                valor = 20 # As vale 20
            carta_nueva = tarjetas.Carta(valor, figura)
            lista_cartas.append(carta_nueva)

    return lista_cartas

def desplegar_cartas(lista_cartas):
    '''
        imprime cada carta de una lista de cartas
    '''
    for carta in lista_cartas:
        print(carta)


def main(jugadores, mano):
    if (len(jugadores) == 2 and mano <= 26):  # Tienen que ser solo dos jugadores y la mano menor a 52
        nombre_jugador1 = jugadores[0]
        nombre_jugador2 = jugadores[1]
        lista_cartas = genera_lista_cartas()
        baraja = tarjetas.Baraja(lista_cartas)
        #print(baraja)
        jugador1 = tarjetas.Jugador(nombre_jugador1, baraja)
        jugador2 = tarjetas.Jugador(nombre_jugador2, baraja)
        jugador1.mano = baraja.genera_mano(mano)
        jugador2.mano = baraja.genera_mano(mano)
        jugador1.despliega_mano(baraja)
        jugador2.despliega_mano(baraja)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jugadores', dest='jugadores',
                        help="Nombre del jugador.", required=True, action="append")
    parser.add_argument('-m', '--mano', dest='mano',
                        help="Tamaño de mano", type = int, required=True)
    args = parser.parse_args()
    jugadores = args.jugadores
    mano = args.mano

    main(jugadores, mano)
