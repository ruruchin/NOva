label final_dream_1: 
    camera at parallax_on
    scene bg mainmenu  

    # scene bg fieldone
    # hide bg mainmenu

    show effi_smile_riad at effi_position
    effi "Я надеюсь, что сейчас закроются все вопросы. Раз ты такой размякший, что мне остаётся делать?"
    hide effi_smile_riad
    show effi_no_riad at effi_position
    effi "Расслабляться нельзя, а ведь первоначально именно ТЫ - моя проблема, ведь я зависима от тебя."
    hide effi_no_riad
    show effi_smile_bok at effi_position
    effi "Все то, что ты мне дал - это все то, что ты у меня забрал, но я тебя не виню."
    hide effi_smile_bok
    show effi_happy_pod at effi_position
    effi "Я хочу больше, ты лишь даёшь мне шанс, и сегодня я поменяю нашу жизнь, ибо тебе же со мной всё лучше!"
    hide effi_happy_pod
    show effi_smile_za at effi_position
    effi "Я всего-то хочу быть там, где ты каждый день засыпаешь. Я хочу быть пробуждением."
    hide effi_smile_za
    show effi_happy_bok at effi_position
    effi "Именно Я хочу вобрать в себя все то, что ты у меня когда-то забрал, ведь я достойна этого больше, чем ты мог представить!"
    hide effi_happy_bok
    show effi_smile_pod2 at effi_position
    effi "Давай мы сейчас ненадолго останемся, а ты будешь говорить 'да' на каждое мое предложение."
    hide effi_smile_pod2
    show effi_smile_u at effi_position
    effi "Мне уже не терпится вместе с тобой разделить этот сон. Тебе разве нужен кто-то ещё?"
    hide effi_smile_u
    show effi_teeth_za at effi_position
    effi "Без меня ты всего лишь кусочек, ищущий место в этом мире, но со мнооой. Тебе не кажется, что это ещё надо уметь?"
    hide effi_teeth_za
    show effi_no_za at effi_position
    effi "А ты получил все это сразу. Ты опасен для себя, а я – оболочка, которая может скрыть в подсознательном все то, что ты хочешь забыть."
    hide effi_no_za
    show effi_smile_riad at effi_position
    effi "По-моему все просто, да?"
    # hide effi_smile_riad

    menu:
        "Да":
            call final_dream_yes

        "Ты не можешь так, почему?":
            call final_dream_why

label final_dream_2:
    # scene bg fieldtwo
    # hide bg fieldone

    show effi_happy_pod at effi_position
    effi "Ну вот смотри, сейчас будет ебейший лайфхак! Вот я сливаюсь с тобой да? Ну да, я уже этим занята."
    gg "Я не могу выбраться"
    hide effi_happy_pod
    show effi_teeth_riad at effi_position
    effi "Стой стой стой, Не-не-не у тебя не получится, потому что я не хочу отвлекать себя."
    hide effi_teeth_riad
    show effi_smile_u at effi_position
    effi "Ну так, короче, я что-то типо заварки, дошло до тебя, да?"
    hide effi_smile_u
    show effi_happy_riad at effi_position
    effi "И вот ты сейчас конечно же согласен со мной. Вот и я как бы не против, в итоге мы оба будем красить эту воду, которую льют на нас грустные дожди, слезы матушки и душ каждый вечер."
    gg "Она разговаривает"
    hide effi_happy_riad
    show effi_smile_pod2 at effi_position
    effi "Да, ну что-то типо Кидзуки, угу. Стоит отметить, что я почти закончила, не переживай так."
    gg "Я хочу выйти, я не хочу"
    hide effi_smile_pod2
    show effi_no_za at effi_position
    effi "Не, тебе просто кажется это странным сейчас, но всё пройдет."
    hide effi_no_za
    show effi_teeth_pod at effi_position
    effi "Давай сейчас ты будешь сидеть тихо и ждать, пока я не закончу!?"
    gg "Нет"
    hide effi_teeth_pod
    show effi_smile_bok at effi_position
    "Я проснулся, мне плохо. Пот. Мне нужно встать с кровати и"
    effi "Ненене, стой тут"
    gg "падаю, Я падаю в обморок. Я чувствую, как мое тело бесконтрольно падает и бьется о пол"
    hide effi_smile_bok
    show effi_no_riad at effi_position
    effi "Так, сейчас мы попробуем кое-что другое, у меня и так было мало времени. Ты настолько слаб, что наш организм скоро перейдет в аварийный режим."
    effi "Ты вообще в курсе сколько спал? Я тоже не знаю, но давай не будем пока об этом думать, я думаю, что закончу чуть позже, но а ты можешь пока подождать там."
    hide effi_no_riad
    gg "Это карусель"
    gg "Да блять сколько можно!?"
    with vpunch
    "Я на кровати."
    "Почему я на кровати? Ну, нахуй это всё."
    "Я хочу выйти, просто выйти и поесть, и попить, и подышать, это страшно."
    "Что на нее вообще нашло?"
    gg "Сколько суток вообще человек может не спать? Мне бы не хотелось повторить весь этот бред."
    $ renpy.play("audio/wrong.ogg")
    gg "Сука, что происходит?"
    gg "Я не закрывал дверь!?"
    gg "Где ключ...."
    gg "ДА МНЕ ТУТ ТРЯХНУЛО КАБИНУ ОЧЕНЬ ДАЖЕ ХОРОШО! МММММММММ"
    hide bg cafe
