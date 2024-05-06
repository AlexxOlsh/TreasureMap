import random


class TreasureMap:
    def __init__(self):
        self.x = random.randint(1, 10)
        self.y = chr(random.randint(ord('A'), ord('K')))
        print('')

    def check_position(self, pos_x, pos_y):
        if pos_x != self.x:
            if ord(pos_y) != ord(self.y):
                if abs(pos_x - self.x) <= 3 and abs(ord(pos_y) - ord(self.y)) <= 3:
                    return ('Вы близко к сокровищу!')
                else:
                    return ("Вы пока не нашли сокровище")
            else:
                return ('Вы близко к сокровищу!')
        else:
            if abs(ord(pos_y) - ord(self.y)) <= 3:
                return ('Вы близко к сокровищу!')
            elif ord(pos_y) == ord(self.y):
                return f'Поздравляем! Игра завершена. Сокровище найдено. Попыток: . \n Ваш промокод SUPER100'
            else:
                return("Вы пока не нашли сокровище")


