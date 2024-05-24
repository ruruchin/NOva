init -2 python:
    def_step = "step"

    def s_play(sound, trans, st, at):
        if sound:
            renpy.play("audio/" + sound, channel="audio")

init -2:
    transform turnf(t=.5):
        xzoom 1
        ease t xzoom -1

    transform turnb(t=.5):
        xzoom -1
        ease t xzoom 1

    transform walk(xa=.5, t=2, dy=25, ty=.5, a1=1, a2=1, wa=.0001, step=def_step):
        alpha a1

        yanchor 1.
        yalign 1.

        parallel:
            ease t xalign xa

        parallel:
            wa
            ease (t - wa) * .5 alpha a2

        parallel:
            yoffset 0
            ease ty*.5 yoffset dy
            function renpy.curry(s_play)(step)
            ease ty*.5 yoffset 0
            repeat int(t / ty + .5)