init:
    define dissolve = Dissolve(0.5)

label repeat_animation(n, mother = False):
    $ i = 0
    while i < n:
        show effi_kitchen_behind with dissolve
        $ renpy.pause(0.3)
        hide effi_kitchen_behind
        show effi_kitchen_behind_knife with dissolve
        $ renpy.pause(0.4)
        if mother:
            show mother_kitchen_behind_knife with dissolve
            $ renpy.pause(0.2)
            hide mother_kitchen_behind_knife
            show effi_kitchen_behind_knife with dissolve
            $ renpy.pause(0.3)
        $ i += 1
    return 

label kill_effi:
    camera at parallax_on
    show bg effi_kitchen_coock_bg 
    show bg effi_kitchen_coock_bg at walk(0.5, 3, step="step.ogg")
    $ renpy.pause(1.7)

    scene bg kitchen_top
    call repeat_animation(1)

    hide effi_kitchen_behind_knife
    call repeat_animation(2, mother=True)

    hide bg kitchen_top
    scene bg kitchen_bottom
    show bg kitchen_bottom at blur(32)
    show mother_kitchen_floor at blur(32)
    with eopen
    show bg kitchen_bottom at blur(0)
    show mother_kitchen_floor at blur(0)
    with dissolve
    show bg kitchen_bottom at drunk()
    show mother_kitchen_floor at drunk()
    pause 8
    with eclose
    pause 2

    $ renpy.full_restart()
    return

label do_nothing:
    $ renpy.full_restart()
    return
