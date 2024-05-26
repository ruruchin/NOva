init python:
    # открыть глаза
    eopen = ImageDissolve("eye", 1, ramplen=64)

    # закрыть глаза
    eclose = ImageDissolve("eye", 1, ramplen=64, reverse=True)

    # автообъявление спрайтов
    images_auto()

    # полный экран при первом запуске
    _preferences.fullscreen = True

init:
    # пьяный трансформ
    transform drunk():
        parallel:
            ease 1.5 zoom 1.1 align(.2, 1.)
            ease 1.15 zoom 1.05 align(.0, 1.)
            ease 1.5 zoom 1.1 align(1., 1.)
            ease 1.5 zoom 1 align(.0, .2)
            ease 1.15 zoom 1.1 align(1., .0)
            ease 1.25 zoom 1.15 align(.2, .2)
            repeat
        parallel:
            ease 1 blur 24
            ease .5 blur 4
            ease 1.5 blur 16
            ease 1.25 blur 0
            repeat
