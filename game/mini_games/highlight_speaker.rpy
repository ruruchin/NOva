# Объединенный файл с автоматическим выделением говорящего зумом и цветом

# Параметры пузыря по умолчанию
init -1 python:
    mark_t = .25
    sprite_brightness = .1
    sprite_zoom = 1.025
    sprite_yalign = 1.
    sprite_yanchor = 1.

# Объявление персонажей
# init python:
#     narrator = CH()
#     lika = CH(_("ЛИКА"), color="#e85")
#     likab = CHBM(_("ЛИКА"), tag="lika", b_ypos=.65, color="#e85")
#     tabita = CH(_("ТАБИТА"), color="#a6b")
#     tabitab = CHBM(_("ТАБИТА"), tag="tabita", b_ypos=.55, color="#a6b", b_paint = "#25d", b_foreground="bubblew", b_color="#fff", b_outlines=gui.text_outlines)

# Позиция спрайта на экране
init:
    transform xpos(x=.5):
        anchor(.5, 1.)
        pos(x, 1.)

    # Плавно отключаем выделение персонажа
    transform mark_off_z(t=mark_t):
        ease_quad t matrixcolor BrightnessMatrix(0) zoom 1

    # Плавно включаем выделение персонажа
    transform mark_on_z(t=mark_t, z=sprite_zoom):
        parallel:
            matrixcolor BrightnessMatrix(0)
            ease_quad t*.25 matrixcolor BrightnessMatrix(sprite_brightness * 2)
            ease_quad t*.75 matrixcolor BrightnessMatrix(sprite_brightness)
        parallel:
            ease_back t zoom z

init -1 python:
    from functools import partial

    speaker = None
    last_spr = ""
    last_tag = ""

    def get_showing_images(layer='master'):
        images = []
        tags = renpy.get_showing_tags(layer)
        for i in tags:
            tag = i
            atrs = renpy.get_attributes(i, layer)
            for a in atrs:
                tag += ' ' + a
            images.append(tag)
        return images

    def get_showing_speaker(tag=False):
        if tag == False:
            tag = speaker
        if tag:
            images = get_showing_images()
            for i in images:
                if str(tag) in str(i):
                    return str(i)
        return None

    def sprite_on(tag=False):
        if tag == False:
            tag = speaker
        i = get_showing_speaker(tag)
        if i:
            atlist = [mark_on_z()]
            renpy.show(i, at_list=atlist)

    def sprite_off(t=True):
        if t == True:
            t = mark_t
        i = get_showing_speaker()
        if i:
            if i != True:
                atlist = [mark_off_z()]
                renpy.show(i, at_list=atlist)
        if t:
            renpy.pause(t)

    def mark_sprite(tag, mark, event, **kwarg):
        spr = get_showing_speaker(tag)

        if event == "begin" and (tag != store.speaker or tag != last_tag):
            store.last_spr = spr
            store.last_tag = tag

            if mark:
                sprite_off()

            store.speaker = tag

            if mark:
                sprite_on()

    def callback(tag, mark, **kwarg):
        return partial(mark_sprite, tag, mark, **kwarg)

    def CH(name=None, bubble=False, mark=False, **kwarg):
        tag = None
        if "tag" in kwarg.keys():
            tag = kwarg["tag"]
            del kwarg["tag"]
        return Character(name, callback=callback(tag, mark, **kwarg), **kwarg)

    def CHM(name=None, **kwarg):
        return CH(name, False, True, **kwarg)

    def CHBM(name=None, **kwarg):
        return CH(name, True, True, **kwarg)
