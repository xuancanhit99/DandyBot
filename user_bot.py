import random
import random_bot


def script(check, x, y):
    if check("gold", x, y):
        return "take"
    if check('level') == 1:
        if check('player', x+2, y) != check('wall', x, y):
            return 'right'
        return 'down'
    elif check('level') == 2:
        print(str(x) + " " + str(y) + "\n")

        if (check('player', x+2, y) != check('wall', x, y)) and (check('player', x, y + 1) == check('wall', x, y)):
            return 'right'
        if check('player', x, y-1) == check('wall', x + 2, y):
            return 'right'
        if (check('player', x, y-1) != check('wall', x, y)) and check('player', x - 2, y + 1) == check('wall', x, y):
            return 'up'
        elif check('player', x, y + 1) != check('wall', x, y) and check('player', x + 2, y - 1) == check('wall', x, y):
            return 'down'












