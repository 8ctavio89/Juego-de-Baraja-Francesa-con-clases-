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

def genera_jugadores(lista_jugadores,baraja):
    for nombre in lista_jugadores:
        nombre = tarjetas.Jugador(nombre,baraja)

def desplegar_cartas(lista_cartas):
    '''
        imprime cada carta de una lista de cartas
    '''
    for carta in lista_cartas:
        print(carta)

def despliega_lista_manos(baraja):
    for jugador in baraja.lista_jugadores:
        jugador.despliega_mano(baraja)


def main(jugadores, mano):
    if (len(jugadores) >= 2 and (len(jugadores))*mano <= 52):  # Tienen que ser solo dos jugadores y la mano menor a 52
        lista_cartas = genera_lista_cartas()
        baraja = tarjetas.Baraja(lista_cartas)
        #print(baraja)
        genera_jugadores(jugadores,baraja)
        baraja.genera_mano(mano)
        despliega_lista_manos(baraja)



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
