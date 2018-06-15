# June 15, 2018
# prints the game borad on the screen
def game(gamesize):
    for x in range(0, gamesize):
        for i in range(0, gamesize):
            print(' ---', end='')

        print('')

        for i in range(0, gamesize + 1):
            print('|', end='\t')
        print('')


game(4)
