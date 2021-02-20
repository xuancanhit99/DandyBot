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
        # Debug
        # print(str(x) + " " + str(y) + "\n")

        # Re phai ngay buoc dau tien(1 buoc cach tuong 1 o)
        if (check('player', x+2, y) != check('wall', x, y)) and (check('player', x, y + 1) == check('wall', x, y)):
            return 'right'
        # Dieu kien Re phai:
        # Neu buoc tiep theo ben phai khong phai tuong(cach tuong 1 o trong)
        # Hoac buoc tiep theo khong co gold => tiep tuc di phai(Re phai o doan cuoi)
        if (check('player', x, y-1) == check('wall', x + 2, y)) or (check("gold", x + 1, y) != 0):
            return 'right'
        # Len neu buoc tiep theo len tren khong co tuong(sat tuong) va so lan len cach deu 8 o bat dau tu vi tri 1
        if check('player', x, y-1) != check('wall', x, y) and ((x - 1) % 8 == 0):
            return 'up'
        # Xuong neu buoc tiep theo di xuong khong co tuong(sat tuong) va so lan xuong cach deu 8 o bat dau tu vi tri 5
        if check('player', x, y + 1) != check('wall', x, y) and ((y + 3) % 8 == 0):
            return 'down'
        # Xuong de khong bi dung yen(Tac dong nhan vat)
        return 'down'
    elif check('level') == 3:
        if not (check("wall", x, y - 1)) and check("wall", x - 1, y):
            return "up"
        if not (check("wall", x + 1, y)) and check("wall", x, y - 1):
            return "right"
        if not (check("wall", x, y + 1)) and check("wall", x + 1, y):
            return "down"
        if not (check("wall", x - 1, y)) and check("wall", x, y + 1):
            return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x - 1, y + 1):
            return "left"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
    elif check('level') == 4:
        if check("gold", x, y):
            return "take"
        if (x == 23 and y == 8):
            return "left"
        if (x == 22 and y == 9):
            return "right"
        if (x == 4 and y == 14):
            return "right"
        if not (check("wall", x, y - 1)) and check("wall", x - 1, y):
            return "up"
        if not (check("wall", x + 1, y)) and check("wall", x, y - 1):
            return "right"
        if not (check("wall", x, y + 1)) and check("wall", x + 1, y):
            return "down"
        if not (check("wall", x - 1, y)) and check("wall", x, y + 1):
            return "left"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x - 1, y + 1):
            return "left"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
    return "pass"



