init python:
    lock_key_t = 0.25  # V перемещания отмычки 
    lock_min_t, lock_max_t = 0.35, 0.65  # V сокращение пружины  
    lock_pin_xstep = 149  # между штифтами
    lock_pin_ystep = 80  # ход пружины 
    lock_pin_width, lock_pin_height = 100, 140
    lock_spr_height = 210
    lock_spr_x0, lock_spr_y0 = 388, 170
    lock_max_i = 5

    lock_check = False
    lock_error = False

    images_auto()

    lock_pin = []


    class LockPin():
        def __init__(self, i):
            self.i = i
            self.spr_x = lock_spr_x0 + lock_pin_xstep * i
            self.spr_y = lock_spr_y0
            self.y = lock_spr_height + lock_spr_y0 + rnd(lock_pin_ystep)
            self.direction = rnds(-1, 1)
            self.speed = lock_pin_ystep / rndf(lock_min_t, lock_max_t)
            self.curr_time = None

    def lock_spr_at_f(i: int, trans: 'Transformation', curr_time: float, at: float) -> float:
        """
        определяет текущее состояние пружины, растягивая её в зависимости от положения штифта
        """
        if i < len(lock_pin):
            trans.anchor = (0, 0)
            trans.pos = (lock_pin[i].spr_x, lock_pin[i].spr_y)
            trans.yzoom = (lock_pin[i].y - lock_pin[i].spr_y) / lock_spr_height
        return 1/60.

    def lock_pin_at_f(i: int , trans, curr_time: float, at: float) -> float:
        """ 
        определение текущего состояния штифта
        """
        global lock_pin

        if i < len(lock_pin):
            if lock_game_mode and i == lock_i:
                if lock_pin[i].curr_time is None:
                    lock_pin[i].curr_time = curr_time
                lag = curr_time - lock_pin[i].curr_time
                lock_pin[i].y += lag * lock_pin[i].speed * lock_pin[i].direction

                if lock_pin[i].y < lock_spr_y0 + lock_spr_height:
                    lock_pin[i].y = lock_spr_y0 + lock_spr_height
                    lock_pin[i].direction = - lock_pin[i].direction
                if lock_pin[i].y > lock_spr_y0 + lock_spr_height + lock_pin_ystep:
                    lock_pin[i].y = lock_spr_y0 + lock_spr_height + lock_pin_ystep
                    lock_pin[i].direction = - lock_pin[i].direction

            lock_pin[i].curr_time = curr_time
            trans.anchor = (0, 0)
            trans.pos = (lock_pin[i].spr_x, int(lock_pin[i].y))

            if lock_game_mode and lock_check and not lock_error:
                col = lock_collision()

        return 1/60.

    def lock_collision():
        global lock_check, lock_error, lock_i

        x, y, w, h = get_sprite_bounds("key")

        for i in range(lock_pin_count):
            xx, yy = lock_pin[i].spr_x + 20, lock_pin[i].y + lock_pin_height

            for iy in range(3):
                for ix in range(1):
                    if is_opaque("key", xx + ix * 20 - x, yy - y - iy * 8):
                        lock_check, lock_error = False, True

                        lock_i = i

                        splay("wrong")
                        renpy.transition(Flash("#f88", .2))

                        renpy.end_interaction(1)
                        return True
        return False


init -1:
    transform lock_spr_at(i):
        function renpy.curry(lock_spr_at_f)(i)

    transform lock_pin_at(i):
        function renpy.curry(lock_pin_at_f)(i)

label lock_init(pins=5, bg="lock bg"):
    python:
        lock_game_mode = False
        lock_i = 0
        lock_pin_count = pins
        lock_pin = [ LockPin(i) for i in range(lock_pin_count) ]
        lock_check = False
        lock_error = False

    scene expression bg as bg

    show lock key as key:
        xoffset -lock_pin_xstep * lock_max_i

    python:
        for i in range(lock_pin_count):
            renpy.show("spring" + str(i), what="lock spring", at_list=[ lock_spr_at(i) ])
            renpy.show("pin" + str(i), what="lock pin", at_list=[ lock_pin_at(i) ])

        renpy.retain_after_load()

    return

label lock_start:
    $ lock_game_mode = True

    while lock_i < lock_pin_count:
        $ lock_check = False
        $ lock_error = False

        pause

        $ lock_check = True

        show lock key as key:
            linear lock_key_t xoffset -lock_pin_xstep * (lock_max_i - lock_i - 1)

        pause lock_key_t

        if lock_error:
            show lock key as key:
                linear lock_key_t xoffset -lock_pin_xstep * (lock_max_i - lock_i)
        else:
            $ lock_i += 1
            $ splay("right")

    $ lock_game_mode = False

    return
