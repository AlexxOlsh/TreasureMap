import logging

class Game:
    def __init__(self, player, treasure_map):
        self.player = player
        self.letters = 'ABCDEFGHIJ'
        self.treasure_map = treasure_map
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")

    def game_start(self):
        message = 'Добро пожаловать в игру «Поиск сокровища»! \n'
        message += 'Ваша задача — найти его за минимальное количество попыток. Координаты вводятся в формате «x, y», где x — горизонтальная координата, y — вертикальная координата. \n'
        message += 'У вас ' + str(self.player.limit) +' попыток. \n'
        message += 'Удачи! \n'
        print(message)
        submenu = 'Выберите действие: \n 1 - Ввести координату \n 2 - Посмотреть карту \n 0 - Завершить игру \n'
        self.visual_map()
        choise = None
        logging.info("Начало игры")

        while self.player.attempt < self.player.limit:
            try:
                choise = int(input(submenu))
                if choise == 1:
                    print('Введите координаты, чтобы проверить, содержится ли сокровище в этой клетке.\n')
                    coord = input("Целое число, буква от A до J: ")
                    points = coord.split(',')
                    if len(points) != 2:
                        logging.error("Ошибка! Введите через запятую целое число и букву от A до J")
                        print("Ошибка! Введите через запятую целое число и букву от A до J")
                    else:
                        try:
                            x = int(points[0])

                            if x < 1 or x > 10:
                                logging.error("Ошибка! Число должно быть от 1 до 10")
                                print("Ошибка! Число должно быть от 1 до 10")
                            else:
                                if self.letters.find(points[1].upper()) < 0:
                                    logging.error("Ошибка! Буква должна быть в диапазоне от A до J")
                                    print("Ошибка! Буква должна быть в диапазоне от A до J")
                                else:
                                    y = points[1].upper()
                                    self.player.new_point(x, y)
                                    logging.info(f"User: Введены координаты ({x}, {y})")
                                    point_res = self.treasure_map.check_position(x, y)
                                    logging.info(f"System: {point_res}")
                                    print(point_res)
                                    if self.player.attempt == self.player.limit:
                                        logging.info("System: Игра завершена")
                                        print('Количество попыток исчерпано. Сокровище не найдено.')

                        except ValueError:
                            print("Ошибка! Первым должно идти целое число")
                elif choise == 2:
                    self.visual_map()
                elif choise == 0:
                    break
            except ValueError:
                print('Ошибка! Введите число')



    def visual_map(self):
        visual = ''
        for i in range(0, 10):
            for j in range(ord('A'), ord('K')):
                if [i+1, chr(j)] in self.player.position_history:
                    visual += f'[V]'
                else:
                    visual += f'[ ]'
            visual += f' {i+1} \n'

        for i in range(ord('A'), ord('K')):
            visual += f' {chr(i)} '
        visual += '\n\n'
        print(visual)


