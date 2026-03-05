from TVPoke.BaseClasses.PokeTypes import Water, Dark
from TVPoke.BaseClasses.Move import Move

class Golduck(Water):
    def __init__(self):
        moves = [
            Move("Hydro Pump", "WATER", 110),
            Move("Water Gun", "WATER", 40),
            Move("Surf", "WATER", 80),
            Move("Dark Pulse", "Dark", 80)
        ]
        super().__init__("Golduck", 80, moves, "./TVPoke/Pokemon/imgs/Greninja.png")