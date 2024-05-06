from TreasureMap_class import TreasureMap
from Player_class import Player
from Game_class import Game


if __name__ == '__main__':
    new_map = TreasureMap()
    new_player = Player(12)
    new_game = Game(new_player, new_map)


    new_game.game_start()