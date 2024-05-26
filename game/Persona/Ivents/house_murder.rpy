label repeat_animation(n, mother = False):
    $ i = 0
    while i < n:
        show effi_kitchen_behind with dissolve
        $ renpy.pause(0.3)
        hide effi_kitchen_behind
        show effi_kitchen_behind_knife with dissolve
        $ renpy.pause(0.3)
        hide effi_kitchen_behind_knife
        if mother:
            show mother_kitchen_behind_knife with dissolve
            $ renpy.pause(0.3)
            hide mother_kitchen_behind_knife
            show effi_kitchen_behind_knife with dissolve
            $ renpy.pause(0.22)
            hide effi_kitchen_behind_knife
        $ i += 1
    return 

# label repeat_animation(n, mother=False):
#     camera at parallax_on
#     $ i = 0
#     while i < n:
#         scene bg effi_kitchen_behind
#         show effi_kitchen_behind with dissolve
#         $ renpy.pause(0.3)
#         hide effi_kitchen_behind
#         scene bg effi_kitchen_behind_knife
#         show effi_kitchen_behind_knife with dissolve
#         $ renpy.pause(0.3)   
#         hide effi_kitchen_behind_knife
#         scene bg effi_kitchen_behind
#         show effi_kitchen_behind with dissolve
#         if mother:
#             hide effi_kitchen_behind_knife
#             scene bg mother_kitchen_behind
#             show mother_kitchen_behind_knife with dissolve
#             $ renpy.pause(0.3)       
#             hide mother_kitchen_behind_knife
#             scene bg mother_kitchen_behind_knife
#             show effi_kitchen_behind_knife with dissolve
#             $ renpy.pause(0.22)  
#             hide effi_kitchen_behind_knife
#             scene bg effi_kitchen_behind
#             show effi_kitchen_behind with dissolve
#         $ i += 1
#     return

label kill_effi:
    camera at parallax_on
    show bg effi_kitchen_coock_bg 
    show bg effi_kitchen_coock_bg at walk(step="step.ogg")
    $ renpy.pause(1.7)

    scene bg kitchen_top

    show mother_kitchen_cook
    $ renpy.pause(0.12)
    hide mother_kitchen_cook
    show effi_kitchen_coock
    $ renpy.pause(0.38)
    hide effi_kitchen_coock
    
    call repeat_animation(1)
    call repeat_animation(2, mother=True)    
    call repeat_animation(1)
    call repeat_animation(1, mother=True)

    hide bg kitchen_top
    scene bg kitchen_bottom
    # show glitch_mother_kitchen_floor
    # $ renpy.pause(0.12)
    # hide glitch_mother_kitchen_floor
    with eopen
    show bg kitchen_bottom at blur(32)
    show mother_kitchen_floor at blur(32)
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
