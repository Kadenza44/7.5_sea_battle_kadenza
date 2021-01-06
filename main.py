import random


# Класс для создания кораблей
class Ship:
    def __init__(self, position):
        self.position = position

    @property
    def get_position(self):
        try:
            position = []
            for i in range(len(self.position)):
                x = ord(self.position[i][0]) - 97
                y = int(self.position[i][1]) - 1
                position.append([y, x])
            return position
        except:
            return 'error_input'

    @property
    def check_position(self):
        s_consistency_x = ''
        s_consistency_y = ''
        ship_consistency = ''
        for i in range(size_game_field):
            for j in range(size_game_field):
                s_consistency_x += str(i) + str(j)
                s_consistency_y += str(j) + str(i)
            s_consistency_x += ' '
            s_consistency_y += ' '

        for i in range(len(self.get_position)):
            for j in range(len(self.get_position[i])):
                ship_consistency += str(self.get_position[i][j])

        if (ship_consistency in s_consistency_x) or (ship_consistency in s_consistency_y):
            return True
        else:
            return False

    @property
    def around_point(self):
        around_point_ship = []
        around_p = [[-1, -1], [-1, 0], [-1, 1],
                    [0, -1], [0, 1],
                    [1, -1], [1, 0], [1, 1]]
        for i in self.get_position:
            for j in around_p:
                p = [x + y for x, y in zip(i, j)]
                if (0 <= p[0] < size_game_field and 0 <= p[1] < size_game_field) and (p not in around_point_ship) and (
                        p not in self.get_position):
                    around_point_ship.append(p)

        return around_point_ship


class GameField:
    def __init__(self, all_ship_position, around_ship, all_shot, visibility):
        self.all_ship_position = all_ship_position
        self.around_ship = around_ship
        self.all_shot = all_shot
        self.visibility = visibility

    def new_game_field(self):
        game_field = [["\u2B1C"] * size_game_field for i in range(size_game_field)]
        for e in self.all_shot:
            game_field[e[0]][e[1]] = '*'
        for x in self.all_ship_position:
            for y in x:
                if self.visibility:
                    game_field[y[0]][y[1]] = '\u2B1B'

                if len(y) == 3:
                    game_field[y[0]][y[1]] = 'x'
        for s in self.around_ship:
            for t in s:
                game_field[t[0]][t[1]] = '.'

        return game_field


def show_game_field():
    g_field_user = GameField(all_ship_position_user, around_ship_user, all_shot_pc, visibility_user)
    g_field_pc = GameField(all_ship_position_pc, around_ship_pc, all_shot_user, visibility_pc)
    game_field_user = g_field_user.new_game_field()
    game_field_pc = g_field_pc.new_game_field()

    tab = 10
    print(f'===Игрок==={count_user}', ' ' * tab, f'===Компьютер==={count_pc}')
    row_num = []
    for i in range(97, 97 + size_game_field, 1):
        row_num.append(chr(i))
    print(' ', *row_num, ' ' * tab, ' ', *row_num)
    for i in range(size_game_field):
        print(i + 1, *game_field_user[i], ' ' * tab, i + 1, *game_field_pc[i])


def input_position(n_deck):
    if n_deck == 3:
        message = 'Координаты 3-палубного корабля через пробел. (Пример: a1 b1 c1): '
    elif n_deck == 2:
        message = 'Координаты 2-палубного корабля через пробел. (Пример: a1 b1): '
    else:
        message = 'Координаты 1-палубного корабля. (Пример: a1): '
    ship = Ship(input(message).split())
    while not (ship.check_position) or (ship == 'error_input'):
        print('Координаты введены некорректно, попробуйте еще раз')
        ship = Ship(input(message).split())

    return ship


def random_ship_pc(n):
    x = str(random.randint(1, size_game_field))
    y = random.randint(97, size_game_field + 97)
    ship_random_pc = chr(y) + x
    direction = random.randint(0, 1)
    for i in range(1, n):
        if direction == 0:
            ship_random_pc += ' ' + chr(y) + str(int(x) + i)
        if direction == 1:
            ship_random_pc += ' ' + chr(y + i) + str(x)
    return ship_random_pc


def shot_point(point):
    try:
        if not len(point) == 2:
            print('Введено неверное значение, попробуйте еще раз')
            return 'error_input'
        x = ord(point[0]) - 97
        y = int(point[1]) - 1
        if not (0 <= x < size_game_field) or not (0 <= y < size_game_field):
            print('Вы стрелляете мимо игрового поля, попобуйте еще раз')
            return 'error_input'
        else:
            return [y, x]
    except:
        print('Коодината введена неверно, попробуйте еще раз')
        return 'error_input'


def victory(s):
    g = []
    for h in range(len(s)):
        f2 = 1
        for z in s[h]:
            if not len(z) == 3:
                f2 = 0
        if f2 == 1:
            g.append(h)
    return g


#  Процесс игры:
size_game_field = 0
all_ship_position_user = []
all_around_position_user = []
around_ship_user = []
all_shot_user = []
count_user = 0
aut = 'r'
step = 1
all_ship_position_pc = []
all_around_position_pc = []
around_ship_pc = []
all_shot_pc = []
count_pc = 0
visibility_user = True
visibility_pc = False

level = 6

while True:

    while not 6 <= size_game_field <= 9:
        try:
            size_game_field = int(input('Введите размер игрового поля от 6 до 9 '))
        except:
            size_game_field = 0

    while not 0 <= level <= 5:
        try:
            level = int(input('Введите уровень сложности от 0 до 5 '))
        except:
            level = 6

    while step == 1:
        all_ship_position_pc = []
        all_around_position_pc = []
        if aut == 'y':
            step = 3
        else:
            step = 2
        count = 0
        for i in [3, 2, 2, 1, 1, 1, 1]:
            e = 0
            while e == 0:
                e = 1
                ship_pc = Ship(random_ship_pc(i).split())
                if not ship_pc.check_position:
                    e = 0

                for n in ship_pc.get_position:
                    for f in sum(all_ship_position_pc, []):
                        if n == f:
                            e = 0
                    for f in sum(all_around_position_pc, []):
                        if n == f:
                            e = 0

                count += 1
                if count >= 1000:
                    step = 1
                    e = 4

                if e == 1:
                    all_ship_position_pc.append(ship_pc.get_position)
                    all_around_position_pc.append(ship_pc.around_point)

    if step == 2 and not aut == 'y':
        while True:
            aut = input('Хотите расставить корабли автоматически? (y/n)')
            if aut == 'y' or aut == 'n':
                break
        if aut == 'y':
            all_ship_position_user = all_ship_position_pc
            all_around_position_user = all_around_position_pc
            step = 1
            # show_game_field()
        else:
            show_game_field()
            for i in [3, 2, 2, 1, 1, 1, 1]:
                er = 0
                while er == 0:
                    er = 1
                    ship_user = input_position(i)
                    for n in ship_user.get_position:
                        for f in sum(all_ship_position_user, []):
                            if n == f:
                                er = 0
                        for k in sum(all_around_position_user, []):
                            if n == k:
                                er = 0
                    if not (len(ship_user.get_position) == i):
                        er = 2

                    if er == 1:
                        all_ship_position_user.append(ship_user.get_position)
                        all_around_position_user.append(ship_user.around_point)
                        show_game_field()
                    elif er == 2:
                        print('Введено неверное количество координат')
                        er = 0
                    else:
                        print('Тут расположить корабль нельзя, попробуйте еще раз')
            step = 3

    if step == 3:
        show_game_field()
        user_shot = 1
        while user_shot == 1:
            step = 3
            user_shot = 0
            shot = shot_point(input('Введите координату выстрела (Например: a1) '))
            if shot == 'error_input':
                user_shot = 1
            if shot in all_shot_user:
                print('Сюда Вы уже стрелляли, попробуйте еще раз')
                user_shot = 1
            if shot in sum(around_ship_pc, []):
                print('Тут не может быть корабля, попробуйте еще раз')
                user_shot = 1
            if user_shot == 0:
                step = 4
                all_shot_user.append(shot)
            if shot in sum(all_ship_position_pc, []) and user_shot == 0:
                for r in range(len(all_ship_position_pc)):
                    for t in range(len(all_ship_position_pc[r])):
                        if all_ship_position_pc[r][t] == shot:
                            all_ship_position_pc[r][t] += 'x'
                step = 3
                v_user = victory(all_ship_position_pc)
                for d in v_user:
                    if len(v_user) >= 1 and not all_around_position_pc[d] in around_ship_pc:
                        around_ship_pc.append(all_around_position_pc[d])
                        count_user = len(v_user)
                        print(f'Вы потопили {len(all_ship_position_pc[d])}-палубный корабль')
                        step = 4
                        user_shot = 0

                if len(v_user) == 7:
                    print('ПОБЕДА ЗА ВАМИ!')
                    visibility_pc = True
                    show_game_field()
                    step = 5

    if step == 4:
        r = 1
        shot_pc = []
        while r == 1:
            r = 0
            if random.randint(0, 5 - level) > 0:
                x = random.randint(0, size_game_field - 1)
                y = random.randint(0, size_game_field - 1)
                shot_pc = [x, y]
            else:
                shot_pc = random.choice(sum(all_ship_position_user, []))
                while len(shot_pc) == 3:
                    shot_pc = random.choice(sum(all_ship_position_user, []))

            if shot_pc in all_shot_pc:
                r = 1
            if shot_pc in sum(around_ship_user, []):
                r = 1
            if shot_pc in sum(all_ship_position_user, []):
                r = 1

            if r == 0:
                all_shot_pc.append(shot_pc)
                step = 3

            if shot_pc in sum(all_ship_position_user, []):
                for e in range(len(all_ship_position_user)):
                    for t in range(len(all_ship_position_user[e])):
                        if all_ship_position_user[e][t] == shot_pc:
                            all_ship_position_user[e][t] += 'x'
                step = 4

                v_pc = victory(all_ship_position_user)

                for d in v_pc:
                    if len(v_pc) >= 1 and not all_around_position_user[d] in around_ship_user:
                        around_ship_user.append(all_around_position_user[d])
                        count_pc = len(v_pc)
                        print(f'У Вас потопили {len(all_ship_position_user[d])}-палубный корабль')
                        r = 0
                        step = 3
                if len(v_pc) == 7:
                    print('ПОБЕДА КОМПЬЮТЕРА!')
                    visibility_pc = True
                    show_game_field()
                    step = 5
                    r = 0
                else:
                    if not step == 3:
                        show_game_field()

    if step == 5:
        print('Игра окончена')
        while True:
            next = input('Хотите сыграть еще раз? y/n ')
            if next == 'y':
                size_game_field = 0
                all_ship_position_user = []
                all_around_position_user = []
                around_ship_user = []
                all_shot_user = []
                count_user = 0
                aut = 'r'
                step = 1
                all_ship_position_pc = []
                all_around_position_pc = []
                around_ship_pc = []
                all_shot_pc = []
                count_pc = 0
                visibility_user = True
                visibility_pc = False
                level = 6
                break
            elif next == 'n':
                print('Пока')
                while True:
                    pass
