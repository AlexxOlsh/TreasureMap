class Player:
    def __init__(self, limit):
        self.position_history = []  # история передвижений
        self.limit = limit  # количество попыток
        self.attempt = 0  # попытка

    def new_point(self, x, y):
        position = [x, y]
        self.position_history.append(position)
        self.attempt += 1
