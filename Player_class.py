class Player:
    letters = 'ABCDEFGHIJ'

    def __init__(self, limit):
        self.position_history = []  # история передвижений
        self.limit = limit  # количество попыток
        self.attempt = 0  # попытка

    def new_point(self, points):
        try:
            x = int(points[0])

            if x < 1 or x > 10:
                return [0, "Ошибка! Число должно быть от 1 до 10"]
                # logging.error("Ошибка! Число должно быть от 1 до 10")
            else:
                if self.letters.find(points[1].upper()) < 0:
                    return [0, "Ошибка! Буква должна быть в диапазоне от A до J"]
                else:
                    y = points[1].upper()
                    self.position_history.append([x, y])
                    self.attempt += 1
                    return [1, f"Введены координаты ({x}, {y})"]
                    # logging.info(f"User: Введены координаты ({x}, {y})")
                    # point_res = self.treasure_map.check_position(x, y)
                    # logging.info(f"System: {point_res}")
                    # print(point_res)
                    # if self.player.attempt == self.player.limit:
                    #     logging.info("System: Игра завершена")
                    #     print('Количество попыток исчерпано. Сокровище не найдено.')

        except ValueError:
            print("Ошибка! Первым должно идти целое число")

        # position = [x, y]
        # self.position_history.append(position)
        # self.attempt += 1
