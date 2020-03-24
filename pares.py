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
import itertools
import random


def genera_lista_cartas():
    ''' genera una lista de todas las cartas de la baraja (52 cartas)
        y regresa una lista de estas
    '''
    lista_cartas = list()
    i = 0
    for i in range(0,3):
        if i == 0:
            figura = "C"
        elif i == 1:
            figura = "P"
        elif i == 2:
            figura = "T"
        elif i == 3:
            figura = "D"
        for j in range(2,14):
            if j == 11:
                valor = "J"
            elif j == 12:
                valor = "Q"
            elif j == 13:
                valor = "K"
            elif j == 14:
                valor = "A"
            carta_nueva = Carta(figura, valor)
            lista_cartas.append(carta_nueva)
        return lista_cartas

def main(lista_jugadores, mano):
    if len(lista_jugadores) == 2:  # Tienen que ser solo dos jugadores


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--lista_jugadores', dest='lista_jugadores',
                        help="Nombre del jugador.", required=True, action="append")
    parser.add_argument('-m', '--mano', dest='mano',
                        help="Tamaño de mano", required=True)
    args = parser.parse_args()
    lista_jugadores = args.lista_jugadores
    mano = args.mano

    main(lista_jugadores, mano)
