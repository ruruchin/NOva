label кафе_внутри:
    scene bg in_cafe with dissolve
    "Мы заходим в здание. Мы занимаем столик у окна, и что ж происходит?"
    "Да пришли не только мы, к нам присоединилась Ное. Кажется, это было запланировано."
    "С ней я не виделся в школе, потому что мы учимся в разных корпусах."

    noe "Этот дурак наконец-то вышел из дома?"
    "Повалив сумку, она с недовольным выражением лица села с нами за один стол."
    kidzuki "Да, он тоже рад тебя видеть. Выглядишь потрепано."
    noe "А как иначе? Лучше бы кто-то спросил, как у меня дела."
    noe "Почему люди всегда заходят так издалека? Я очень волновалась в последнее время!"
    noe "[gg]никогда так далеко не заходил."

    menu:
        "И ты действительно так обо мне беспокоилась?":
            call забота

        "Как будто твоя жизнь бы в момент развалилась":
            call сарказм

        "Что произошло пока меня не было?":
            call интерес


label кафе_разговор:
    kidzuki "Недавно прошла волна смертей учеников."
    kidzuki "Это было явно из-за того что..."
    noe "Из-за того что в наши школы теперь прикреплены к новым районам."
    noe "В который входит р-н Камагасаки."
    kidzuki "Я понимаю, к чему ведет Ное, но кажется, это не из-за того, что какие-то «детишки гангстеров» теперь прессуют молодёжь."
    kidzuki "Им не до этого никакого дела."
    gg "Да, но недавно по пути со школы я прошел через Камагасаки..."

    noe "Дурак."
    kidzuki "Прекрати, Ное, человек впервые видит свет за такой долгий перерыв."

    menu:
        "Рассказать про труп":
            call рассказ_про_труп

        "Я просто проходил мимо":
            call просто_мимо

label кафе_продолжение:
    kidzuki "Да, там и вправду теперь целая нарко-империя."
    kidzuki "Я по новостям слышал о людях, валяющихся в экстазе, и людях, находящихся в реальном бешенстве."
    kidzuki "Не ты не понял."
    kidzuki "Чувак, я говорю о бешенстве! Кажется, мы все понимаем, о чём идет речь."
    kidzuki "Это же реально страшно. Походу и до нашей школы добралось."
    noe "Не то чтобы это было удивительно."
    noe "У нас, конечно, и так были те, кто способны на «новые» ощущения."
    noe "И проблема с веществами была всегда."
    noe "Но теперь, если сопоставить смерти и Камагасаки, то становится понятно."
    noe "Здесь замешаны новые препараты."
    noe "А папины мамины придурки так и спускают кучу денег, спонсируя производство."
    gg "Они похоже нашли себе «Промоутеров» в большом количестве."
    

scene black with dissolve