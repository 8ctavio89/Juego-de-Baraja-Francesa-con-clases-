class Jugador:
    nombre = None
    mano = None
    puntuacion = None

    def __init__(self,nombre):
        self.nombre = nombre
        self.mano = []
        self.puntuacion = 0

    def despliega_mano(self):
        print(self.nombre)
        print("----------")
        for carta in self.mano:
            print(f"{carta.__str__()}\n")
        print(f"Puntuacion: {self.puntuacion}")

class Carta:
    valor = None
    figura = None

    def __init__(self,valor,figura):
        self.valor = valor
        self.figura = figura

    def __str__(self):
        return (f"{self.valor}-{self.figura}")

class Baraja:
    diccionario_cartas = None
    figuras = None
    lista_cartas = None
    lista_jugadores = None

    def __init__(self,lista_cartas): #El método Genera_litsa_cartas() debe de hacer la lista de 52 cartas
        self.diccionario_cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":20}
        self.figuras = ["C","P","T","D"]
        self.lista_cartas = lista_cartas
        self.lista_jugadores = []

    #def genera_mano (self):
        #debe llamar a guarda_jugador al terminar o crear otra funcion que lo haga

    def guarda_jugador(self,jugador):
        self.lista_jugadores.append(jugador)

