label scene_room:
    camera at parallax_off
    scene bg room
    gg "Да, я бы не отказался от ключа или чего-то такого. Я бы ещё не отказался выйти с этой комнаты, да."
    gg "И мое сердце начало биться чаще. Мне совсем не хотелось находиться здесь. Мысли о том, что мое тело может сгнить в этой комнате, посещали и посещали меня."
    gg "Я также не хотел бы, чтобы мое тело досталось той жалкой реинкарнированной душе, надеюсь, происходит не так."
    gg "А может, Ное и Кидзуки поменялись точно так же, как меня сменяет Эффи. Ну, во-первых, я надеюсь, что это не так, а во-вторых, мне кажется, что я сегодня довольно хорошо потравился едой из кафе, хотя это вполне могла быть та странная вода, которую я купил по дороге домой (Алое вера типо → не пиши)."
    gg "В любом случае мне нужно выйти отсюда!"
    gg "Я достал первую попавшуюся палку у себя в комнате, а также какой-то железный язычок. По-моему, в детстве у меня был конструктор, точно не помню."
    gg "Но, кажется, сейчас у меня нет выхода, кроме как попытаться ломануть свою же дверь! Какой я идиот."
    call lock_init from _call_lock_init
    call lock_start from _call_lock_start
    gg "Получилось!"
    gg "Надо быстрее добраться до кухни и взять..."
    jump scene_kitchen
    return
label scene_kitchen:
    camera at parallax_off
    scene kitchen at zoom_1
    gg "Таблетки..."
    gg "Я понял, так это все реально не шутки."
    effi "Угу, я думала, ты не выйдешь со своей комнаты, что за таблетки ты теперь ищешь?"
    gg "Дерьмо, теперь ты мне ещё и видишься, да? Сука сука сука сука"
    effi "Ну садись, садись за стол, я уже положила тебе! Как столько спать! Хэх"
    gg "Яя–я-Я не мо-о"
    gg "Не могу"
    gg "Я не хочу ххачы"
    gg "Нет"
    gg "Неенетнетне"
    effi "Ты весь дрожишь!? Ну ничего, сейчас мы отдохнем и все станет как раньше, да? Ты сильный мальчик."
    gg "Ч"
    gg "Ч-то мне делать ..."
    gg "Она"
    gg "Она уже в моей голове, и я не"
    gg "Так легко войти в мой дом и так нагло со мной обращаться ещё никто не смел. Я"
    gg "Я не могу"
    gg "Я тру глаза"
    gg "У меня льется пот, я весь мокрый. Сдавив вилку так сильно, я думал, что погнул ее на несколько оборотов. Мне хотелось вырвать, но и вырвать себе глаза, вынуть каждый орган, пропитанный ей. И еда. Она тоже? Я не хочу есть. Я хочу"

menu:
    "Убить Эффи":
        call kill_effi from _call_kill_effi
    "Ничего не предпринимать":
        call do_nothing from _call_do_nothing
        