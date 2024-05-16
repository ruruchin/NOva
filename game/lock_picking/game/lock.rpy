init python:
    # время на перемещение отмычки
    lock_key_t = .25

    # диапазон для рандомного выбора времени на сокращение пружины
    lock_min_t, lock_max_t = .35, .65

    # расстояние между левыми краями соседних штифтов
    lock_pin_xstep = 144

    # высота хода штифта
    lock_pin_ystep = 80

    # размеры штифта
    lock_pin_width, lock_pin_height = 100, 140

    # высота пружины
    lock_spr_height = 210

    # координаты первой пружины
    lock_spr_x0, lock_spr_y0 = 405, 185

    # максимальное количество штифтов
    lock_max_i = 5

    # флаг необходимости проверки коллизий
    lock_check = False

    # флаг свершившейся коллизии
    lock_error = False

    # автоматическое объявление спрайтов с учётом префиксов, включая webp
    images_auto()

    # штифты
    lock_pin = []

    # класс для штифтов
    class LockPin():
        def __init__(self, i):
            # номер пружины
            self.i = i
            # положение по х (зависит от номера)
            self.x = lock_spr_x0 + lock_pin_xstep * i
            # чтобы не путаться
            self.spr_x = self.x
            # положение по y (для всех одинаковое)
            self.spr_y = lock_spr_y0
            # рандомное стартовое положение штифта
            self.y = lock_spr_height + lock_spr_y0 + rnd(lock_pin_ystep)
            # рандомное направление движения - вверх или вниз
            self.dir = rnds(-1, 1)
            # скорость пкс/сек
            self.speed = lock_pin_ystep / rndf(lock_min_t, lock_max_t)
            # для анимации
            self.st = None

    # функция для определения текущего состояния пружины
    def lock_spr_at_f(i, trans, st, at):
        if i < len(lock_pin):
            trans.anchor = (0, 0)
            trans.pos = (lock_pin[i].spr_x, lock_pin[i].spr_y)
            trans.yzoom = (lock_pin[i].y - lock_pin[i].spr_y) / lock_spr_height
        return 1/60.

    # функция для определения текущего состояния штифта
    def lock_pin_at_f(i, trans, st, at):
        global lock_pin

        if i < len(lock_pin):
            # текущий штифт движется
            if lock_game_mode and i == lock_i:
                if lock_pin[i].st is None:
                    lock_pin[i].st = st
                lag = st - lock_pin[i].st
                lock_pin[i].y += lag * lock_pin[i].speed * lock_pin[i].dir

                if lock_pin[i].y < lock_spr_y0 + lock_spr_height:
                    lock_pin[i].y = lock_spr_y0 + lock_spr_height
                    lock_pin[i].dir = - lock_pin[i].dir
                if lock_pin[i].y > lock_spr_y0 + lock_spr_height + lock_pin_ystep:
                    lock_pin[i].y = lock_spr_y0 + lock_spr_height + lock_pin_ystep
                    lock_pin[i].dir = - lock_pin[i].dir

            lock_pin[i].st = st
            trans.anchor = (0, 0)
            trans.pos = (lock_pin[i].x, int(lock_pin[i].y))

            # при необходимости проверяем коллизии
            if lock_game_mode and lock_check and not lock_error:
                col = lock_collision()

        return 1/60.

    # проверка коллизий
    def lock_collision():
        global lock_check, lock_error, lock_i

        # спрайт отмычки
        x, y, w, h = get_sprite_bounds("key")

        # координаты спрайтов штифтов
        for i in range(lock_pin_count):
            xx, yy = lock_pin[i].x + 20, lock_pin[i].y + lock_pin_height

            # некоторые точки на дне штифтов
            for iy in range(1):  # уменьшено до одной точки по вертикали
                for ix in range(3):  # уменьшено до трех точек по горизонтали
                    # если они столкнулись с рисунком отмычки
                    if is_opaque("key", xx + ix * 20 - x, yy - y - iy * 8):
                        lock_check, lock_error = False, True

                        # откатываем игру до задетого штифта
                        lock_i = i

                        # вспышка
                        splay("wrong")
                        renpy.transition(Flash("#f88", .2))

                        # сбрасываем паузу
                        renpy.end_interaction(1)
                        return True
        return False

init -1:
    # растягивание пружины зависит от положения штифта под ней
    transform lock_spr_at(i):
        function renpy.curry(lock_spr_at_f)(i)

    # положение штифта
    transform lock_pin_at(i):
        function renpy.curry(lock_pin_at_f)(i)

# инициализация игры
label lock_init(pins=5, bg="lock bg"):
    python:
        lock_game_mode = False

        # текущий штифт
        lock_i = 0

        # задаём количество штифтов
        lock_pin_count = pins

        # список с заданным количеством новых штифтов
        lock_pin = [ LockPin(i) for i in range(lock_pin_count) ]

        # флаг необходимости проверки коллизий
        lock_check = False

        # флаг свершившейся коллизии
        lock_error = False

    # отобразить игру в режиме фона

    # сам фон
    scene expression bg as bg

    # отмычка
    show lock key as key:
        xoffset -lock_pin_xstep * lock_max_i

    # все штифты
    python:
        for i in range(lock_pin_count):
            renpy.show("spring" + str(i), what="lock spring", at_list=[ lock_spr_at(i) ])
            renpy.show("pin" + str(i), what="lock pin", at_list=[ lock_pin_at(i) ])

        # для сохранений
        renpy.retain_after_load()

    return

# начало игры
label lock_start:
    $ lock_game_mode = True

    # повторяем, пока не пройдём игру
    while lock_i < lock_pin_count:
        # сброс флагов
        $ lock_check = False
        $ lock_error = False

        # ждём клика
        pause

        # начинаем проверки на коллизии
        $ lock_check = True

        # старт движения отмычки
        show lock key as key:
            linear lock_key_t xoffset -lock_pin_xstep * (lock_max_i - lock_i - 1)

        # время движения отмычки
        pause lock_key_t

        # обработка результатов
        if lock_error:
            # если зацепили штифт, то откат
            show lock key as key:
                linear lock_key_t xoffset -lock_pin_xstep * (lock_max_i - lock_i)
        else:
            # иначе продолжаем
            $ lock_i += 1
            $ splay("right")

    # конец игры
    $ lock_game_mode = False

    return
