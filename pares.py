#!/usr/bin/python3
# Equipo: Mustafar
# Fecha: 27 de marzo de 2020
# Integrantes:
#
#   Félix López Juan Pablo
#   López Velásquez Octavio
#   Serna Navarro Ángel Emilio

import argparse
import tarjetas
import itertools
import random


def genera_lista_cargas():
   

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
