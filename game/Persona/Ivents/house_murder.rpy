label kill_effi:
    camera at parallax_on 
    scene bg effi_kitchen_coock with dissolve
    show bg effi_kitchen_coock at walk(0.5, 3, step="step.ogg")
    $ renpy.pause(1)


    scene bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind with dissolve 
    $ renpy.pause(0.1)
    # show bg mother_kitchen_behind with dissolve
    # $ renpy.pause(0.1)
    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    scene bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.1)
    # show bg mother_kitchen_behind_knife with dissolve
    # $ renpy.pause(0.1)
    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)


    scene bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.1)
    # show bg mother_kitchen_behind with dissolve
    # $ renpy.pause(0.1)
    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    scene bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.1)
    show bg mother_kitchen_behind_knife with dissolve
    $ renpy.pause(0.1)
    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)


    scene bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.1)
    show bg mother_kitchen_behind with dissolve
    $ renpy.pause(0.1)
    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    scene bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.1)
    show bg mother_kitchen_behind_knife with dissolve
    $ renpy.pause(0.1)
    show bg effi_kitchen_behind_knife with dissolve
    $ renpy.pause(0.3)


    scene bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)

    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.1)
    show bg mother_kitchen_behind with dissolve
    $ renpy.pause(0.1)
    show bg effi_kitchen_behind with dissolve
    $ renpy.pause(0.3)


    # scene bg mother_kitchen_floor with dissolve
    # $ renpy.pause(3.5)
    show bg mother_kitchen_floor at blur(32)
    with eopen
    show bg mother_kitchen_floor at blur(0)
    with dissolve
    show bg mother_kitchen_floor at drunk()
    pause 8
    with eclose
    pause 2

    $ renpy.full_restart()
    return

label do_nothing:
    $ renpy.full_restart()
    return 
