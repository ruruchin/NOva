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

label pian:
    pause 1

    $ mplay("Acid Trip Gone Wrong")

    scene bg class
    show eric at xalign(.5)
    # размываем всё, что есть на экране - и фон, и персонажей
    show layer master at blur(32)
    # поднимаем веки
    with eopen

    # фокусируем взгляд
    show layer master at blur(0)
    with dissolve

    # и тут нас начинает колбасить, плющить и таращить
    show layer master at drunk()

    pause 8

    "Эрик? Зачем он меня разбудил?.. А почему я спал?.. Ну, капец! Я пьян, как фортепьян... Нет, это другое. Ах да, я же с авиамоделистами самолётики клеил. Кажется, я упоролся клеем. Глаза слипаются... Ладно, я только моргну разочек..."

    $ mstop()
    scene black
    with eclose
    pause 1

    return
