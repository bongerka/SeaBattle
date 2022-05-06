from modules.Game import Game, clear
import random


def main():
    clear()
    size = int(input("Square length: "))

    first_player = ['me', 'bot']
    game = Game(size, random.choice(first_player))

    game.get_coords()

    while game.is_continue():
        game.print_tables()
        print("в доработке, но у бота генерируются корабли сами")
        break
        new_hit = input("Your step: ")
        game.move(new_hit)


if __name__ == "__main__":
    main()
