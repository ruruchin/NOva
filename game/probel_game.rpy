
label probel_game:
    $ screen_blur = False
    $ blur_start_time = random.uniform(5, 10) # Случайное время от 5 до 10 секунд
    $ blur_duration = 3.0 # Длительность размытия экрана
    $ start_time = renpy.get_time()
    $ success = False

    show screen main_game_screen

    while game_running:
        $ current_time = renpy.get_time()
        if not screen_blur and (current_time - start_time >= blur_start_time):
            $ screen_blur = True
            $ blur_start_time = current_time # Обновляем время начала размытия

        if screen_blur:
            show screen blur_screen
            if (current_time - blur_start_time >= blur_duration):
                $ game_running = False

        if success:
            hide screen blur_screen
            hide screen main_game_screen
            $ game_running = False
            jump game_success

        $ renpy.pause(0.1) # Пауза для обновления экрана

screen blur_screen:
    add "blob_room.png" at center # Ваш эффект размытия, замените "blur_effect.png" на ваш файл
    key "K_SPACE" action SetVariable("success", True)