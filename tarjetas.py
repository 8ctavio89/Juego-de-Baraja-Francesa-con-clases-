import random


class Jugador:
    nombre = None
    mano = None
    puntuacion = None

    def __init__(self, nombre, baraja):
        self.nombre = nombre
        self.mano = []
        self.puntuacion = 0
        baraja.guarda_jugador(self)

    def despliega_mano(self, baraja):
        print(self.nombre)
        print("----------")
        for carta in self.mano:
            print(f"{carta.display(baraja.diccionario_cartas)}")
        print(f"Puntuacion: {self.puntuacion}")


class Carta:
    valor = None
    figura = None

    def __init__(self, valor, figura):
        self.valor = valor
        self.figura = figura

    def __str__(self): # quité dict_cartas
        #carta_cara = dict_cartas[self.valor]
        #return f"{carta_cara}-{self.figura}"
        return f"{self.valor}-{self.figura}"

    def display(self, dict_cartas):
        carta_cara = dict_cartas[self.valor]
        return f"{carta_cara}-{self.figura}"


class Baraja:
    diccionario_cartas = None
    figuras = None
    lista_cartas = None
    lista_jugadores = None

    def __init__(self, lista_cartas):
        # El método Genera_lista_cartas() debe de hacer la lista de 52 cartas
        self.diccionario_cartas = {
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "J",
            12: "Q",
            13: "K",
            20: "A",
        }
        # Corazones, Picas, Trébol, Diamante
        self.figuras = ["C", "P", "T", "D"]
        self.lista_cartas = lista_cartas
        self.lista_jugadores = []

    def genera_mano(self, num_cartas):
        # debe asignar una mano aleatoriamente a cada uno de los jugadores de la lista
        # Se genera una nueva lista de cartas revueltas con la cantidad de la mano
        cartas_revueltas = random.sample(self.lista_cartas, num_cartas)
        for carta in cartas_revueltas:      # Se elimina las cartas usadas por el jugador en la lista vieja
            self.lista_cartas.remove(carta)
        return cartas_revueltas

    def guarda_jugador(self, jugador):
        self.lista_jugadores.append(jugador)
