label кафе_внутри:
    
    "Мы заходим в здание. Мы занимаем столик у окна, и что ж происходит?"
    "Да пришли не только мы, к нам присоединилась Ное. Кажется, это было запланировано."
    "С ней я не виделся в школе, потому что мы учимся в разных корпусах."
    show noe_smile1 at effi_position
    noe "Этот дурак наконец-то вышел из дома?"
    "Повалив сумку, она с недовольным выражением лица села с нами за один стол."
    hide noe_smile1
    show kidz_smile at effi_position
    kidzuki "Да, он тоже рад тебя видеть. Выглядишь потрепано."
    hide kidz_smile
    show noe_smile2 at effi_position
    noe "А как иначе? Лучше бы кто-то спросил, как у меня дела."
    hide noe_smile2
    show noe_smile3 at effi_position
    noe "Почему люди всегда заходят так издалека? Я очень волновалась в последнее время!"
    hide noe_smile3
    show noe_smile2 at effi_position
    noe "[gg]никогда так далеко не заходил."

    menu:
        "И ты действительно так обо мне беспокоилась?":
            call забота
            

        "Как будто твоя жизнь бы в момент развалилась":
            call сарказм
         

        "Что произошло пока меня не было?":
            call интерес
           


label кафе_разговор:
    show kidz_smile at effi_position
    kidzuki "Недавно прошла волна смертей учеников."
    kidzuki "Это было явно из-за того что..."
    hide kidz_smile
    show noe_smile3 at effi_position
    noe "Из-за того что в наши школы теперь прикреплены к новым районам."
    noe "В который входит р-н Камагасаки."
    hide noe_smile3 
    show kidz_smile at effi_position
    kidzuki "Я понимаю, к чему ведет Ное, но кажется, это не из-за того, что какие-то «детишки гангстеров» теперь прессуют молодёжь."
    kidzuki "Им не до этого никакого дела."
    gg "Да, но недавно по пути со школы я прошел через Камагасаки..."
    hide kidz_smile
    show noe_smile2 at effi_position
    noe "Дурак."
    hide noe_smile2 
    show kidz_smile at effi_position
    kidzuki "Прекрати, Ное, человек впервые видит свет за такой долгий перерыв."

    menu:
        "Рассказать про труп":
            call рассказ_про_труп

        "Я просто проходил мимо":
            call просто_мимо


label кафе_продолжение:
    kidzuki "Чувааааак, не слушай её,"
    "Ное бьет кулаком по затылку Кидзуки, от чего его выражение лица довольно быстро меняется."
    kidzuki "ДА и ВООБЩЕ блять нинадо"
    "Ное довольно смотрит, приподняв свою голову вверх."
    kidzuki "Ребят, по-моему, нам надо как бы расслабиться типа."
    kidzuki "Мне недавно приснилась довольно жуткая вещь."
    
    noe "Что говорит сонник?"
    
    kidzuki "У меня нет книг в доме, кроме учебных. Я хотел начать что-то, но, по-моему, я не хочу."
    
    gg "В соннике такой глубокий сюжет!"
    
    kidzuki "Короче, ладно, стою я в полной пустоте, вот прям кромешная светлень, я и два человека."
    kidzuki "Я так и не понял, кто это, но мне было крайне важно выбрать."
    kidzuki "В руках у меня оказался пистолет и интуитивно я понял, что должен делать, но я всё также сомневался."
    kidzuki "С одной стороны мой близкий, а с другой ни в чем не повинный человек."
    kidzuki "Ну и естественно я хотел спасти своего, но в моменте, когда я выстреливаю в одного, на меня бежит силуэт девушки, ну той, которую я спас."
    kidzuki "Она бежит ко мне, расставив руки, готовая обнять."
    kidzuki "Но в другой руке у меня появляется второй пистолет."
    kidzuki "Я не знаю, что мне следовало делать, но меня охватил страх."
    kidzuki "Я так и не выстрелил. Зачем я её спасал? Чтобы потом убить?"

    noe "Ну так и что там?"

    kidzuki "Она убила меня, ну так видимо по приколу."

    noe "Ой."

    gg "По приколу?"

    kidzuki "Ну да, потому что она сначала обняла меня, а потом достала нож и тихонько вводила его в меня несколько раз."
    kidzuki "Я не чувствовал боли, но понимал, что умираю."
    kidzuki "В этот момент я нажимаю на курок, но обойма пистолета пуста."
    kidzuki "На самом деле стрёмное и непонятное дерьмо…"

    noe "Да, довольно мрачно."

    "Мы еще немного посидели, а потом, собираясь расходиться и попрощавшись с Кидзуки, мы с Ное пошли по домам."
    "Казалось, что я на секунду переместился в детство, когда прогулки были точно такими же."
    "Довольно приятное ощущение спокойствия и необычной суеты, которые так приятно давили на меня, что я не мог нарадоваться изменениям."
    "Мы с Ное также идем по улице, проходим мимо небольших прилавков, а потом хочется пить, и мы идем в магазин."
    "Магазин был недалеко от места, где мы уже идём своей дорогой."
    "Мы пришли и уже по старой традиции зашли взять что-нибудь. Это может быть какая-то булочка или просто разного рода сок."
    "Ное всегда ещё покупала жвачку."
    "Расплатившись на кассе, мы выходим из магазина."
    "Но она не купила жевачку. Простой бутылки воды ей было достаточно, я хотел удивится, но скорее огорчился ведь я пропустил момент когда она поменялась. "
    "Да, Ное действительно сильно изменилась с последнего раза когда мы с ней встретились"
    "Она совершенно новый человек и теперь я даже незнаю что от нее ожидать."
return
