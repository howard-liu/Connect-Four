

class Player(object):

    def __init__(self, number):
        self.player_number = number

    @staticmethod
    def input_column():
        """
        Returns the column the player wants to drop a piece in
        :return: Column inputted
        """

        while True:
            try:
                column = int(input())
            except ValueError:
                print('That\'s not an integer')
                continue
            if 0 < column < 8:
                return column
            else:
                print('Please enter a valid column')










