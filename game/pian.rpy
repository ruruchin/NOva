init python:
    eopen = ImageDissolve("eye", 1, ramplen=64)

    eclose = ImageDissolve("eye", 1, ramplen=64, reverse=True)

    images_auto()

    _preferences.fullscreen = True

init:
    transform drunk():
        parallel:
            ease 1.5 zoom 1.05 align(.5, .8)
            ease 1.15 zoom 1.03 align(.5, .8)
            ease 1.5 zoom 1.05 align(.5, .8)
            ease 1.5 zoom 1.03 align(.5, .8)
            ease 1.15 zoom 1.05 align(.5, .8)
            ease 1.25 zoom 1.07 align(.5, .8)
            repeat
        parallel:
            ease 1 blur 24
            ease .5 blur 4
            ease 1.5 blur 16
            ease 1.25 blur 0
            repeat
