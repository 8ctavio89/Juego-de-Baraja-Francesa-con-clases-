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
    ''' genera una lista de todas las cartas de la baraja (52 cartas)
        y regresa una lista de estas
    '''
    lista_cartas = list()
    for i in range(0,4):
        if i == 0:
            figura = "C"
        elif i == 1:
            figura = "P"
        elif i == 2:
            figura = "T"
        elif i == 3:
            figura = "D"
        for valor in range(2,15):
            if valor == 14:
                valor = 20
            carta_nueva = tarjetas.Carta(valor, figura)
            lista_cartas.append(carta_nueva)
    return lista_cartas

def main(jugadores, mano):
    if len(jugadores) == 2:  # Tienen que ser solo dos jugadores
        lista_cartas = genera_lista_cartas()
        for i in lista_cartas:
            print(i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--jugadores', dest='jugadores',
                        help="Nombre del jugador.", required=True, action="append")
    parser.add_argument('-m', '--mano', dest='mano',
                        help="Tamaño de mano", required=True)
    args = parser.parse_args()
    jugadores = args.jugadores
    mano = args.mano

    main(jugadores, mano)
