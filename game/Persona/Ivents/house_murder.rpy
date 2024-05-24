label kill_effi:
    gg "Я хочу лишь убить ее"
    $ renpy.full_restart()
    return

label do_nothing:
    $ renpy.full_restart()
    return 
