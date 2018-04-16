from Grid import *


def main():
    while True:
        print('First player: Player p or Bot b')
        out = input()
        if out == 'p' or out == 'b':
            first = out
            break
    while True:
        print('Second player: Player p or Bot b')
        out = input()
        if out == 'p' or out == 'b':
            second = out
            break
    grid = Grid(first, second)
    grid.start_game()


if __name__ == "__main__":
    main()

