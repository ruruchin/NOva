# ЕСЛИ СКОПИРОВАТЬ СЕБЕ В ПРОЕКТ ЭТОТ МОДУЛЬ, ТО ПРИ НАЖАТИИ ЛКМ ИЛИ ESC
# ВМЕСТО СОХРАНЕНИЙ БУДЕТ ОКРЫВАТЬСЯ ИГРОВОЕ МЕНЮ (ГРАФИКА НЕ ОБЯЗАТЕЛЬНА)

# назначить своё игровое меню
define _game_menu_screen = "gamemenu"

# разворачивание-сворачивание при появлении-исчезании
transform openclose(z0=.01, z1=1, a0=0, a1=1, xy0=(1., 1.), xy1=(.5, .5), t=.0):
    on show:
        alpha a0 zoom z0 align xy0
        ease t zoom z1 alpha a1 align xy1

    on hide:
        ease t zoom z0 alpha a0 align xy0

# силуэт цвета color
transform paint(color="#fff"):
    matrixcolor TintMatrix(color) * InvertMatrix(1.) * TintMatrix("#ff0000")

# растягивающийся кружок для фона
define round = Frame(Text( "⚫", font="DejaVuSans.ttf", size=48), 24, 24)

# стиль для кнопок
style gamemenu_button is button:
    # постоянная ширина
    xsize 400
    # цвет фона кнопки
    background At(round, paint(gui.hover_color))
    # цвет фона кнопки при наведении
    hover_background At(round, paint(gui.hover_muted_color))
    # цвет фона кнопки при выборе
    selected_background At(round, paint(gui.hover_muted_color))
    # цвет фона кнопки неактивной
    insensitive_background At(round, paint("#00000055"))

# стиль для кнопок
style gamemenu_button_text is button_text:
    size gui.name_text_size
    xalign .5
    layout "subtitle"
    color gui.hover_muted_color
    hover_color gui.hover_color
    selected_color gui.hover_color
    insensitive_color gui.insensitive_color

style gamemenu_vbox is vbox:
    align(.5, .5)
    # отступы между кнопками
    spacing 8

style gamemenu_frame is frame:
    align(.5, .5)
    # отступы от краёв рамки до кнопок
    padding(100, 75)

    # можно раскомментировать, если нет нужной рамки
    # будет просто белый скруглённый прямоугольник
    # background At(round, paint("#fff"))

# своё игровое меню
screen gamemenu:
    tag menu

    # затемнение с плавным появлением-исчезанием без зума
    #add "gui/overlay/confirm.png" at openclose(1)

    # оформление для меню
    style_prefix "gamemenu"

    # рамка с кнопками
    frame:
        # с заданным выше разворачиванием-сворачиванием
        at openclose

        # стопка кнопок
        vbox:
            label _("МЕНЮ") xalign .5

            null height 8

            textbutton _("Вернуться") action Return()
            textbutton _("Сохранить") action ShowMenu("save")
            textbutton _("Загрузить") action ShowMenu("load")
            textbutton _("В меню") action MainMenu()
            textbutton _("Настройки") action ShowMenu("preferences")

# перепишем quick_menu, чтобы убрать лишние кнопки
screen quick_menu():
    zorder 100

    if quick_menu:

        hbox:
            align(.975, 1.)

            spacing 4

            textbutton _("←") action Rollback() yalign 1. text_size gui.text_size
            textbutton _("▤") action ShowMenu('gamemenu') text_yoffset -2 text_size gui.text_size
