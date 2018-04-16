from Player import *


class Grid(object):

    COLUMNS = 7
    ROWS = 6

    def __init__(self):
        self.grid = [[0 for x in range(self.COLUMNS)] for y in range(self.ROWS)]
        self.player = []
        self.player.append(Player(1))
        self.player.append(Player(2))

    def __str__(self):
        out = ''
        for y in range(self.ROWS):
            for x in range(self.COLUMNS):
                # Change here
                out = out + str(self.grid[y][x]).ljust(4)
            if y != self.ROWS - 1:
                out = out + '\n'
        return out

    def check_horizontal_vertical(self, player_number, column, row, type):
        a = 0
        b = 0
        if type == 'horizontal':
            a = 1
        else:
            b = 1
        count = 0
        for x in range(1, 4):
            if row - b * x < 0 or column - a * x < 0:
                pass
            elif self.grid[row - b * x][column - a * x] != player_number:
                break
            else:
                count += 1
        for x in range(1, 4):
            if row + b * x > self.ROWS - 1 or column + a * x > self.COLUMNS - 1:
                pass
            elif self.grid[row + b * x][column + a * x] != player_number:
                break
            else:
                count += 1
        if count == 3:
            return True
        else:
            return False

    def check_diagonal(self, player_number, column, row, type):
        a = 1
        if type == 1:
            b = 1
        else:
            b = -1
        count = 0
        for x in range(1, 4):
            if row - a * x < 0 or column - b * x < 0 or \
                    row - a * x > self.ROWS - 1 or column - b * x > self.COLUMNS - 1:
                pass
            elif self.grid[row - a * x][column - b * x] != player_number:
                break
            else:
                count += 1
        for x in range(1, 4):
            if row + a * x < 0 or column + b * x < 0 or \
                    row + a * x > self.ROWS - 1 or column + b * x > self.COLUMNS - 1:
                pass
            elif self.grid[row + a * x][column + b * x] != player_number:
                break
            else:
                count += 1
        if count == 3:
            return True
        else:
            return False

    def check_connect_four(self, player_number, column, row):
        # Use position check vert, horz, diag x 2
        # Vert
        if self.check_horizontal_vertical(player_number, column, row, 'vertical') is True:
            return True
        # Horizontal
        if self.check_horizontal_vertical(player_number, column, row, 'horizontal') is True:
            return True
        # Diagonals
        if self.check_diagonal(player_number, column, row, 1) is True:
            return True
        if self.check_diagonal(player_number, column, row, 0) is True:
            return True
        return False

    def invalid_move(self):
        print('Invalid move')

    def player_turn(self, player_number):
        val = self.player[player_number - 1].input_column() - 1
        for x in range(self.ROWS):
            if self.grid[x][val] != 0:
                x -= 1
                break
        if x == -1:
            self.invalid_move()
            return -1
        self.grid[x][val] = player_number
        if self.check_connect_four(player_number, val, x) is True:
            return player_number
        else:
            return 0

    def play_round(self, player_number):
        print('Player' + str(player_number) + '\'s turn:')
        # Change here
        print('1   2   3   4   5   6   7')
        print('-------------------------')
        print(str(self))
        val = self.player_turn(player_number)
        if val == -1:
            return -1
        elif val != 0:
            return val
        return 0

    def start_game(self):
        """
        Starts the game
        :return:
        """
        x = 2
        while True:
            if x == 1:
                x = 2
            else:
                x = 1
            winner = self.play_round(x)
            if winner == -1:
                if x == 1:
                    x = 2
                else:
                    x = 1
            elif winner != 0:
                self.declare_winner(winner)
                return

    def declare_winner(self, player_number):
        print('Player' + str(player_number) + ' wins!')
        print(str(self))
