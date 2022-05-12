from modules.Game import Game
from modules.Interface import Interface
from random import choice


def main():
    
    interface = Interface()

    size = int(interface.my_input("Square length: "))

    first_player = ['me', 'bot']

    game = Game(size, choice(first_player))

    game.get_coords()

    game.set_shots()

    game.winner()

 

if __name__ == "__main__":
    main()
