﻿define persistent.profanity = 0
############################################################

transform zoom_1:   
    zoom 1.0

transform effi_position:
    xalign 0.4
    yalign 1.9

#############################################################
init python:
    import random  
    import renpy.exports as renpy
default preferences.audio_when_minimized = False 


# Определение персонажей игры.
define effi = Character('Эффи', color="#000000")
define gg = Character('[gg]', color="#000000")
define kidzuki = Character('Кидзуки', color="#000000") 
define noe = Character('Ное', color="#000000")

init python:
    # Функция для установки музыки главного меню
    def set_main_menu_music():
        if persistent.changed_music:
            renpy.music.play("music/midnight_stroll.mp3")
# Определение переменных игры


# Игра начинается здесь:
label start:
    camera at parallax_off
    hide quick_menu
   
    stop music fadeout 1.0
    
    $ persistent.changed_music = False
    $ renpy.save_persistent()
   

# Определение главы 1
label chapter_one:
    $ renpy.music.play("music/midnight stroll.mp3")
    stop music

    $ gg = renpy.input("Как тебя зовут?")
    $ gg = gg.strip()
    if not gg:
        $gg = "Я" 
    # gg "Мое имя [gg]"
    
    scene room at zoom_1
        
    "20.01. XXXX"
    "Это Я. Самое простое Я, которое может быть."
    "Самое скучное место – мой дом."
    "Я прожил в нем всю свою жизнь."
    "Перевод в старшую школу изменил многое в моей жизни."
    "Начнем с того, что это второе по значимости событие в моей жизни."
    
    "Первым был факт ухода отца из семьи."
    "Мать с ним очень часто ругалась."
    "Это в принципе не важно, Я не особо застал тот момент. "
    scene blob_room at zoom_1
    hide room
        
    "Мне не нравится"
    "Я не ХОЧУ"
   
    scene black at zoom_1
    hide blob_room
    
    "Мне начинает казаться, что я всегда хотел быть частью чего-то целого. Мои одноклассники не особо заинтересованы в общении со мной."
    "Я выбиваюсь из массы."
    "День за днем я мечтаю о том, чтобы Я вобрал в себя все то, что меня окружает и стал комочком. "
    "Маленьким комочком размером с аэропорт. С трассы начнет готовиться к отлету самолет. Пилот вдруг резко уснет. "
    "Самолет на бешеной скорости влетит в меня, и я улечу на стратосферу. "
    "Я хочу быть планетой. Новой собственной планетой. "
    "Я хочу содержать все и быть своей собственностью."
    
   
    "Моя подруга Ное пришла навестить меня. Она очень давно не заходила.
        Мама приготовила поесть.
        Чувство, будто я хочу умереть."
     
    "Я комок."
    scene black at zoom_1
     
    
    "Хочется быть комком."
    effi "Это наша первая встреча."
    effi "Как ты думаешь, что произойдет?"
    scene bg fonnav2
    hide black
    hide black 
    jump NAC  
    
return

label NAC:
    camera at parallax_on
    scene bg fonnav2
    # $ persistent.changed_background = True
    # $ renpy.save_persistent()
  

    "Я должен быть здесь, в моей комнате. Я заперся на пару дней, ничего не ем и не пью. В последнее время мои сны стали красочнее то ли из-за недостатка кислорода, то ли из-за некоторого эйфорического состояния."
    "Я всегда думаю, насколько я могу остаться там в следующий раз. Там приятно тепло и ничего не беспокоит. "
    "Думаю, что это именно та планета, о которой я всегда мечтал. "
    "В один момент я начал замечать силуэт девушки, которая как бы пряталась от меня в моем же мирке. Я стал недоумевать и нервничать, думая о том, что я не могу это контролировать. Это мое место."
   
    gg"Я обернулся и увидел беловолосую девушку лет 18-19."
    jump paralax
return
label paralax:
    camera at parallax_on
    scene bg fonnav1
   
    gg"Приятное лицо. В меру большие круглые глаза. Стройная фигура. Белое длинное платье."
    gg"Она заметила меня и резко перевела свой задумчивый и растерянный взгляд."
    scene bg pole
    gg"Она стала осторожно подходить ко мне, как бы увидев что-то необычно новое в её жизни."
    gg"Её жизнь..."
    gg"Может быть.."
    gg"это моя жизнь."
    gg"В конце концов она же всё-таки плод моего мозга, который генерирует её образ на основе полученной ранее информации."
    gg"И может ли она быть полноценно искренней?" # она нейронка епта, только как ты хочешь связать все происходящее с этим?
    gg"Умеет ли она вообще ощущать хоть какие-то искренние эмоции, подходя ко мне?"

    gg"Она уже довольно близко подошла, так что я мог едва расслышать, как её ноги шелестели по траве."
    
    gg"Внезапно я увидел небольшую улыбку на её лице, которая нарастала всё больше и больше." # спрайт менять тут надо её на улыбающийся, если вообще такое кол-во
    gg"Я тоже сделал пару нерешительных шагов, прежде чем мы практически подошли друг к другу."
    gg"Так резко сократить расстояние."
    gg" " #чтото типа неловкой паузы 

    scene bg fonnav2 
    show effi_happy_u at effi_position
      
    gg"Я никогда не думал, что расстояние не может быть подвергнуто единицам измерения, но осознав то, что я так его и не почувствовал, я сделал для себя неожиданные выводы."

    "Она начала первой"
    
    gg"Здравствуй."
    hide effi_happy_u 
    show effi_smile_bok at effi_position
   

    effi"Привет"
    hide effi_smile_bok 
    show effi_happy_za at effi_position
    
    gg"– В неожиданной для меня легкой манере ответила она мне" # тут хз, может просто закадровым сделать 
    gg"Я никогда не думал, что увижу кого-либо здесь, по крайней мере это место мне снится довольно часто"
    hide effi_happy_za
    show effi_smile_za at effi_position

    effi"А я никого здесь и не видела, ты первый кто за столько лет появился здесь."
    hide effi_smile_za
    show effi_smile_u at effi_position
    effi"Иногда мне казалось, что я останусь здесь, в этом мрачном месте навсегда,"
    effi"раньше здесь были зверюшки, ... "
    effi"ярко светило солнце и вода могла отражать его лучи."
    effi"Но с недавних пор всё стало тускнеть. Всё постепенно начало пропадать."
    effi"Иногда мне кажется, что земля вот-вот провалится, и я упаду в пустую яму, где я умру."
    hide effi_smile_u
    show effi_no_u at effi_position
    gg"Ты не знаешь, из-за чего это началось?"
    hide effi_no_u
    show effi_netral_pod at effi_position
    effi"А ты?"
    effi"Я думаю, тебе лучше знать"
    hide effi_netral_pod
    show effi_no_u at effi_position
    effi" " # типо дать игроку поразмыслить на этом приколе
    hide effi_no_u
    show effi_netral_bok at effi_position
    effi"Ведь, по крайней мере, я думаю, что ты замешан в этом больше, чем другие возможные вариации событий, изначально заложенные в суть и предрасположенность этого мира."
    effi"Я не могу влиять ровным счетом ни на что. Я как будто не имею даже возможности изменить саму себя."
    hide effi_netral_bok
    show effi_teeth_bok at effi_position
     

    effi"У меня не было детства, я всегда была такой. С «ранних» лет я старалась понять, зачем этот мир дан мне и что он получит взамен от его порождения."
    effi"Беспомощный ребенок, которого разбаловали красками этого чудесного мира, уже давно перестал получать ту любовь, которая давала ему жизнь."
    effi"Мой родитель состарился и скорее всего умрет. А вместе с ним и я."
    effi"Ведь я просто частичка, которая висит исключительно на его шее."

    menu: 
        "Что-то типа паразита?":
            call parasit
            pass
        "Ты довольна?":
            call blago 
            pass  
    hide effi_teeth_bok
    show effi_no_bok at effi_position
    gg"Но теперь есть я."
    hide effi_no_bok
    show effi_netral_bok at effi_position
    effi"Да, теперь ты повод засомневаться, что все так плохо."
    effi"Но я боюсь тебя,"
    hide effi_netral_bok
    show effi_netral_za at effi_position
    effi"я так же не хочу разочаровываться в выходке моего родителя"
    effi"Хотя возможно, что таким образом он наделяет меня силой своих последних слов, написанных на бумаге, которую обычно передают близким и значимым людям чтобы хоть что-то оставить после своей смерти."
    hide effi_netral_za
    show effi_smile_riad at effi_position
    effi"Получается, ты мой небольшой подарочек.~"
    hide effi_smile_riad
    show effi_happy_za at effi_position
    "Почему-то в моей голове сложилось ощущение, что я уже давно не управляю своим сном. Ровно после того момента, как мы сократили расстояние, между нами."
    "Я стал подарком, как и она для меня неожиданным сюрпризом."
    "Я стал думать о том, кем я являюсь в действительности."
    "Мне стало страшно."

    "Я весьма заинтересовался ей. Я хотел бы узнать её получше, поэтому решил спросить множество вопросов, чтобы понять, кем мы приходимся друг для друга."
    "Но неожиданно для меня она стала всё больше походить на расплывающееся пятно в моих глазах."
    hide effi_happy_za
    show effi_teeth_bok at effi_position
    effi"Ты первый..."
    # вот здесь нужны различные виды окружения нагенерировать 
    "Всё что я только успел разобрать в её речи."
    "В моменте некого состояния безмятежности и некоторого беспокойства о том, что мне снова придётся идти и заново проходить бесконечный лимб скучной повседневной жизни в некотором количестве отведенного мне времени до моего очередного срыва."
    "Я в какой-то степени люблю это."
    # я бы Такое-то дерьмо как Я. вставил бы вместо Я в строчку снизу
    "Но не понимаю, как такое-то дерьмо как Я могу сочетаться по цветовой гамме с этими красочными вспышками и узорами ночного города, как не беспокоиться о том, что загрязняю своим присутствием парки с необычайно красивыми деревьями и видами."
    "Я не понимаю, когда мама мне говорит, что этот мир создан для нас."
    "Я, не Мы."
    "Я не хочу, чтобы здесь кто-то ещё видел такой позор. Я хочу этот мир себе заново."
    "Вот почему я всё-таки просыпаюсь. Я просыпаюсь в надежде, что эти прекрасные виды смогут принадлежать мне."
    "Я просыпаюсь в надежде на то, что смогу отражать лучи бесконечно обтекающих меня каждый день билбордов."
    show black with zoomin and Dissolve(2.6)
    jump posleSna
    
    hide fonnav2
return
label posleSna:
    camera at parallax_off
    $ renpy.music.play("music/dver.mp3")
    stop music 
    scene dver at blur(52)
    hide black
    hide effi_no_u
    "Я просыпаюсь."
    "Мать стучит в комнату."
    "Я проснулся."
    "Я боюсь, "
    "боюсь так сильно, что чувствую будто засыхаю и скоро расщеплюсь на маленькие крошки от чипсов, обёртки которых были разбросаны по всей моей комнате."
    "Кажется, это был мой последний запас, который Я благополучно оприходовал во время очередной истерики."
    "Подходить к двери так неловко, "
    "и каждый раз проходя через это чувство и расстояние между моей кроватью и некой моей оградой от всего сущего, я переживал как бы ни случилось какой-либо беды."
    "Я подошел к двери и набрал воздуха."
    "Я отворил дверь."
    show black at zoom_1
    $ renpy.music.play("music/open_door.mp3")
    stop music
    hide black at zoom_1
    
    scene kitchen at zoom_1
    "Моя мама всё так же стоит и улыбается мне так непринужденно. Она явно выглядела счастливой."
    "Который раз она терпит такого мудака как я, но продолжает улыбаться мне каждый мой день и ждёт моего «возвращения»." 

    "К горлу у меня снова подкатил ком."
    "Я всегда пытался сдерживать слёзы именно в эти встречи. У меня никогда не получалось."
    "Крепко обняв Маму, я как обычно поблагодарил её за её заботу, и мы вместе пошли на кухню, чтобы что-либо запихнуть из нормальной еды в мой желудок."
    "Кажется, после моего сна с той девушкой я стал больше уделять внимания деталям. Всё стало более красочным и четким."
    "Я благодарил."
    "Благодарил сам факт того, что я смог увидеть эту прекрасную картину"
    "За окном начало учебного года, сентябрь."
    "Не дождливый, очень солнечный день." 
    "На кухне приятный запах."
    "У меня пробился нос. Чувство, будто мой нос только сейчас стал дышать."
    "Дышать не дымом сигарет, которые обычно разили с каждого второго человека в метро. Дышать не дымом машин и бесконечных парфюмов."
    "Я чувствовал, как будто сами легкие имели области нервов «вкусного» восприятия, которые как корни проросли по всему их периметру."
    "Я смог рассмаковать практически каждый кубик воздуха, который я вдыхал. Я смог почувствовать что-то обыденное."
    "Как долго это продлится?"
    "Кажется, что я со временем теряю своё сознание."
    "Мне так хорошо"
    "Я видел. Видел то, как моя Мама ловит мою падающую прямиком в свежий суп голову и хохочет."
    "Видимо, я перенасытился новыми ощущениями, которые, по всей видимости, поглотили меня. Это было чудесное состояние шокового умиротворения."
    "Я не заснул. Я отряхнулся и пришел в чувства."
    "То ли от нервов, то ли от состояния своей беспомощности и от всей ситуации в целом, которую я даже не пытался контролировать, отдаваясь себе полностью я рассмеялся."
    "Комната закатилась смехом моей мамы и меня."
    "Я был счастлив."
    "Доев свой обед, я вспомнил её. Девушка, что умело наслаждалась дарами, которые дали ей свои «родители»."
    "Интересно, она чувствовала когда-нибудь что-либо схожее с тем, что испытал сегодня я?"
    "Могу ли вообще быть ей благодарным?"
    "Может, это именно она подарила мне это?"
    " "
    "Но ведь она начала это первой"
    " "
    "Остаток своего дня я провел довольно продуктивно."
    "Казалось, что моя сетчатка разрывается  после слез за обеденным столом и мешает мне заполнять все те бланки, которые я должен был подписать ещё несколько занятий назад."
    "Я сделал львиную долю всей своей домашней работы, а также начал готовить свою сумку для начала нового завтрашнего дня."
    hide kitchen
    jump scnd_chapter
return

label scnd_chapter:
    scene trainpaths at zoom_1 with Dissolve(.7)
    "Это был мой первый день, когда я пошёл на учёбу. На моё удивление мне было отнюдь не противно шагать тем же самым наизусть вызубренным маршрутом."
    "Я всегда говорил, что надо бы его поменять и найти более подходящий. Теперь я понимаю, что в этом нет необходимости."
    "Он действительно прекрасен, даже будучи таким обычным."
    "Меня и так всё устраивало, не так-то сильно значит я и хотел найти новый путь, если всё так же сейчас иду по тому же маршруту, что и раньше."
    "Видимо за свою жизнь я так и не научился ценить то, что есть. Меня постоянно что-то не устраивало."
    "Но почему сейчас я так непринужденно иду."
    "Мне казалось, что буквально вчера проклинал всё то, что меня окружало."
    hide trainpaths with Dissolve(.7)
    scene trainpaths2 at zoom_1 with Dissolve(.7)
    gg"Я проклинал?"
    "А зачем? Почему я не могу дать своим чувствам оценку?"
    "Кажется, что сегодня действительно тревожный день. Иначе почему сегодня светит солнце."
    "Почему я ещё не встретил ни единого человека, которому захотел бы высказать всё дерьмо о нём."
    "Солнце сегодня действительно необычайно ярко. Кажется, что через часика 2-3 оно станет ещё резче, оно будет больше."
    "Квадрат."
    "Его лучи просто испепелят многоэтажки. Все ослепнут и даже не поймут, что их сжигает заживо то, что их встречает каждое утро."
    "А для некоторых это олицетворение полноценного нового дня."
    hide trainpaths2 with Dissolve(.7)
    scene busstop at zoom_1 with Dissolve(.7)
    "Своеобразный закат."
    "Но никто его не увидит. А я буду знать."
    "Это проделки солнца, оно полностью принадлежит мне на этот день." 
    "Я не позволю увидеть его тем же каким вижу его я."
    "Человек, что посмотрит на него, будет слеп. Он не увидит всего того прекрасного обыкновения, какое видел Я."
    "Я прожгу ему кристаллики. Надо знать своё место."
    hide busstop with Dissolve(.7)

    scene school at zoom_1 with Dissolve(.7)
    "Прошёл мимо здания, в котором учусь..."
    "Только Я мог выдать что-то подобное."
    "Только Я мог сделать вид, что прошел его совершенно случайно и отправиться в соседний парк, в котором Я обычно проводил своё время, отведенное на занятия. Там и дышится легче, и народу меньше."
    "Но в этот раз я все-таки пересек ворота и зашел внутрь."
    "Охраны нет."
    "Всё как обычно."
    hide school with Dissolve(.7) 
    scene corridor at zoom_1 with Dissolve(.7)
    "Почему люди, которые казались такими веселыми, начинают кусочек за кусочком отмирать?"
    "Почему, как только я зашел, все вокруг стали тише, а коридоры длиннее?"
    "Отсидев занятия, я уже не чувствовал той атмосферы счастья, которое мне было дано."
    "Мне показалось, что люди с моим приходом начинают прятаться. Все начинают меняться. У всех своя цель разочаровать меня."
    hide corridor with Dissolve(.7) 
    scene post at zoom_1 with Dissolve(.7)
    "Выйдя на порог, готовясь идти домой, я увидел солнце."
    "Оно было не способно жечь..."
    "У всех сегодня своя цель разочаровать меня." 
    "Но день действительно прошел довольно неплохо."
    gg"Воспоминания о сегодняшнем утре разве настолько хороши?" 
    "Какая разница, каким было утро, когда оно было слишком натянутым?"
    gg"? А утро действительно было?"
    "Кажется, солнце тускнеет, не удивительно, потому что уже подходит к своему началу вечер, который обязан затмить собой всё то, что было до."
    gg"А вечер ярче чем солнце?"
    "Я думаю, нет. Вечером солнце начинает тускнеть и слабеть. Оно уже не будет мне светить так, как это было буквально несколько часов назад."
    "А я надеялся, что оно всё-таки сможет быть со мной в любой момент моего дня."
    hide post with Dissolve(.7)

    scene anteroom at zoom_1 with Dissolve(.7)
    gg"Я дома"
    "Мама снова готовит что-то на кухне. Запах остался таким же приятным"
    "Хоть это остаётся неизменным, но факт того, что это когда-то закончится, меня разочаровывает сильнее, чем все произошедшее за этот день."
    "Зайдя в свою комнату, мне уже сложно было включить свет."
    "Не переодевшись, я уже смог лечь на свою кровать."
    "Уткнувшись лицом в подушку, я понял, что обиделся, и закат уже не имеет для меня какого-то смысла. Стало даже немного грустно."
    "Никто не вернет мне солнце? Почему никто не хочет помочь мне?"
    "Я снова лежу на кровати, надеясь, что что-либо изменится, Мне плевать как, я просто хочу, чтобы сейчас произошло что-то такое, что заставило бы поменять моё мнение о солнце."
    "Пересилив себя, я все-таки переоделся и вышел на кухню"
    "Мама всё так же готовила рис с мясом."
    hide anteroom with Dissolve(.7)
    scene kitchen at zoom_1 with Dissolve(.7)
    "Присев за стол, я снова обдумал всё то, что произошло вчера. Кажется, я быстро меняю своё мнение стоит мне представить вещи наилучшим образом."
    "Ничего страшного, если не учитывать её."
    gg"Я так и не узнал её ближе. Возможно, она ненавидит всё то, что было у неё раньше."
    "Множество ярких красок, которые наполняли её жизнь, но так и не смогли полностью удовлетворять её на протяжении её существования."
    "Да и кто она сама по себе."
    "Это лишь моя фантазия, хотя в моменте мне показалось, что она действительно выглядит «настоящей»."
    "Я хотел бы кое-что проверить, сегодня у меня довольно много времени."
    "Если лягу чуть пораньше, скорее всего не собью себе режим, которого с таким трудом я пытался держаться начиная со вчерашнего дня."
    "Ну иногда-то надо чем-то жертвовать."
    "Поблагодарив за ужин, я отправился в свою комнату начинать моё небольшое расследование."
    "Звучит странно с учётом того, что её может и не быть."
    "Значит, я либо просрал за этим занятием своё время, либо просрал своё время, преуспев в своих начинаниях."
    "Звучит лучше, чем ничего."
    hide kitchen

    show blob_room_dark at zoom_1 with Dissolve(.7)
    "Сколько я буду ещё заниматься подобной хуйней?"
    hide blob_room_dark 
    
    show black at zoom_1
    "Я так и не заснул."
    
    "Время действительно было довольно ранним и не подходило для того, чтобы начать свой сон. А она вообще спит?"
    "Своеобразное начало её утра определяю Я."
    "В таком случае режим действительно важен. Не удивительно, что её мир начал тускнеть. А собственно почему?"
    "Возможно, ей бы стоило задуматься над этим. Скорее всего, она виновата в этом, если не смогла удержать в своих руках всё то, что окружало её. Мне кажется, ей стоило бы быть немного тверже и решительнее."
    "Не понимаю почему, но что-то мне подсказывает, что это именно то, что ей не хватает."
    "«И всё-таки почему»"
    scene bg fonnav2
    hide black
    gg"-И все-таки почему я её не вижу. Мне казалось, она будет где-то именно здесь, на месте нашей прошлой встречи."
    "И я искал её долго, очень долго. В конце концов поле было бесконечным и его границы не имели четкого ограничения. Я как будто каждый раз неуклюже топтался на одном и том же месте."
    hide do_first
    gg"Но в итоге я увидел."
    gg"Увидел силуэт, который в точности повторяет её очертания"
    gg"Бежав к нему, я рассчитывал увидеть её, ту самую её."
    show effi_teeth_pod at effi_position
    effi"А всё такое непредсказуемое."
    hide effi_teeth_pod
    show effi_netral_pod2 at effi_position
    effi"Раньше я думала, что всё, что есть у меня, подвластно только мне и только мне подарен этот мир в состоянии, в котором был и есть сейчас."
    hide effi_netral_pod2
    show effi_netral_bok at effi_position
    effi"Я думала, что всё идет своим чередом. Обычный механизм «выцветания», который обычно должен приводить к логическому концу."
    effi"Но солнце сегодня. Я смогла разглядеть в нем небольшой лучик света. Он настолько тусклый, что изначально я даже думала, что у меня начинаются проблемы с головой раз вижу что-то, что должно было иссякнуть как ресурс, но мне дают шанс."
    gg"Оно действительно сегодня странное."
    hide effi_netral_bok
    show effi_teeth_u at effi_position
    effi"Ты странный."
    gg"Ты жалеешь о том, что случилось сегодня?"
    hide effi_teeth_u
    show effi_teeth_za at effi_position
    effi"Ты видишь больше, заходишь, когда вздумается, мне страшно."
    hide effi_teeth_za
    show effi_no_riad2 at effi_position
    effi"Я думала, что тот раз был последним. Разве это нормально, что мы можем так видеться?"
    effi"Ты сможешь мне принести пользу своим существованием в моей голове?"
    hide effi_no_riad2
    show effi_smile_u at effi_position
    effi"Всё вокруг блеклое, разве ты это так спокойной принимаешь?"
    hide effi_smile_u
    show effi_teeth_u at effi_position    
    effi"Почему ты насмехаешься надо мной?"
    hide effi_teeth_u
    show effi_no_bok at effi_position
    effi"Всё у тебя так хорошо, что даже не замечаешь, как эта душнота бьёт по мне."
    effi"Ты даже ничего не сможешь изменить."
    hide effi_no_bok
    show effi_teeth_za at effi_position
    effi"Мудак, который думает лишь о себе." 
    effi"Я вынуждена ОТВЕЧАТЬ на твои вопросы?"
    hide effi_teeth_za
    show effi_no_pod at effi_position
    effi"Каждый раз я думаю лишь о том, когда я наконец перестану видеть эти черно-белые тона."
    hide effi_no_pod
    show effi_smile_pod at effi_position
    effi"Когда мне выжгут глаза ярким светом, чтобы запомнить его навсегда и спокойно уйти на покой. Без сожалений, я ничего не привнесла, ничего не убыло, я хочу, хочу, чтобы я больше не тратила своё время."
    hide effi_smile_pod
    show effi_netral_bok at effi_position
    effi"Я вдыхаю, а что я вдыхаю? Мне никто не скажет, чем я дышу. Я перестала видеть свет, я больше стала просто сидеть и ждать, ждать, когда очередь дойдёт и до меня."
    hide effi_netral_bok
    show effi_smile_bok at effi_position
    effi"Меня дразнят тусклым светом, которого мне НЕДОСТАТОЧНО."
    hide effi_smile_bok
    show effi_teeth_bok at effi_position
    effi"НЕДОСТАТОЧНО именно то, о чём ты хотел спросить?"
    hide effi_teeth_bok
    show effi_no_riad at effi_position
    effi"Разве для тебя это не равносильно тому, когда дело, которое казалось тебе интересным и увлекательным, со временем больше не приносит какой-то былой радости или счастливых эмоций?"
    hide effi_no_riad
    show effi_no_riad2 at effi_position
    effi"Мы зависимы от того, чтобы получать больше. Больше эмоций, которыми мы так не дорожим и которые так быстро проходят."
    hide effi_no_riad2
    show effi_netral_bok at effi_position
    effi"А потом жалуемся на то, что жизнь такая несправедливая и ужасная."
    hide effi_netral_bok
    show effi_teeth_bok at effi_position
    effi"Мы - худшее, что только она могла себе позволить. Я думала я свыклась с этим, думала, что за полем просто давно никто не ухаживал, красивый лес сгорел и от него остались лишь пепельные скелеты, а солнце просто устало светить для тех, кто больше не нуждается в нём."
    hide effi_teeth_bok
    show effi_smile_pod at effi_position
    effi"Но вдруг появляется надежда на то, что я смогу вновь увидеть что-то зарождающееся, что-то, что будет прописано с чистого листа, но я не могу это так просто принять, я старалась свыкнуться с мыслью о том, что всё кончено, но во мне всё так же било желание хотя бы в последний раз насладиться всем тем, чем одарили меня при моём рождении."
    hide effi_smile_pod
    show effi_smile_pod2 at effi_position
    effi"И мне не надо будет больше думать о многих маловажных вещах, я наконец-то просто смогу насладиться тем, что меня окутает."
    hide effi_smile_pod2
    show effi_netral_pod2 at effi_position
    effi"НО, ЕсЛИ кОНЕц ужЕ ЗаВТрА, А ЧеГО Я ХОЧу ВИдетЬ"
    hide effi_netral_pod2
    show effi_teeth_bok at effi_position
    effi"НЕДОСТАТОЧНО?"
    hide effi_teeth_bok with Dissolve(0.5) 
    "Я так и не успел ничего ответить ей. Она была так зла."
    "Я не хотел её обидеть. Но, по крайней мере, мне теперь более известно о её переживаниях."
    gg"Всё, что было утрачено.."
    
    # "В детстве у меня была игрушка. Это была небольшая фигурка персонажа из какой-то передачки по ТВ, которую постоянно крутили по утрам."
    # "Всегда перед выходом из дома я смотрел её. То ли потому что мне было действительно интересно, то ли потому что мне просто не было что смотреть."
    # "Ну а в итоге. Её просто украли."
    # "Украли прямо во время обеда, на котором я, как по воле случая, оставил свой рюкзак у столика без присмотра."
    # "Это было ужасно. Чувство полного разочарования и потерянности."
    # "Эта фигурка была очень мне дорога. Это был подарок мамы в мой день рождения."
    # "Строгий наказ обходиться с ней бережно и аккуратно, который постоянно шел в комплекте с любым подарком в голове любого человека в конце концов надавил на меня."
    
    # "Я чуть не проблевался на пол около моих же одноклассников."
    # "Вырвать свой только что съеденный обед как последние крики разбитого импульсивного сердца, которое так и норовит, разрезав мою грудную клетку и сломав кости, вылететь и пустить фонтан красных слёз, которые возможно описали бы всю горечь моей утраты."
    # "Я сдержался. Сдерживая порыв эмоций, я побрёл в туалет."
    # "Идя по коридору, я еле сдерживал свои зрачки глаз на местах, было ощущение, будто они крутятся как на центрифуге. В разные стороны."
    # "Правая или левая? Я выбрал правую стенку, по которой я таки смог добрести до таблички, указывающей на место, в котором я смогу «выплеснуть» все свои сожаления."
    # "Я заперся в одной из кабинок. Кажется, никого поблизости не было в тот момент."
    # "И я плакал, кричал и захлебывался в своих слюнях вперемешку с рвотой. Для меня это оказалось настолько сильным ударом."
    
    # "Успокоившись, я отсидел весь оставшийся день в кабинке, вытерев слёзы и убрав следы преступления, начал собираться домой."
    # "Нет, ЭТО ДАЖЕ НЕ БЫЛ САМ ПОДАРОК. НО ТО, ЧТО Я СЕГОДНЯ ОЩУТИЛ, МОЖНО ВПОЛНЕ СЧИТАТЬ ПОДАРКОМ НА ВСЮ МОЮ ЖИЗНЬ."

    # "Отлично, теперь давайте пройдёмся по твоим чувствам. Что бы ты ощущал, если бы то, что у тебя было украдено, маячило прямо перед твоим носом?"
    # "Я был бы недоволен."
    # "Увидев лишь на небольшое мгновение моего кроху в толпе людей прямо на следующий день на каком-то спортивном мероприятии на свежем воздухе, которое доводилось собрать лишь несколько раз во время, которое позволяет это сделать, опираясь на погодные условия, я сразу же вбежал в неё."
    # "Всем так всё равно. Никто даже не замечал моего присутствия."
    # "Я бежал, спотыкаясь о ноги людей, которые так и норовили собраться компанией около четырёх человек передо мной и начать обсуждать: Красивый маникюр, недавно выигранный матч какой-то из команд по футболу."
    # "А у меня нога болит. А у меня голова. А мне отказали в чувствах. А меня ебёт?"
    # "Я лишь вижу маленький шанс вернуть то, что некогда принадлежало мне. Я МНОГОГО ПРОШУ???"
    # "Я так и не нашёл человека, у которого была моя статуэтка. Я был так обозлён."
    # "Мне не важно, кого было винить. Мне лишь хотелось выпустить пар."

    # "Смотря на всё это с другой стороны, я всё такой же, как и люди в толпушках."
    # "Кто поможет МНЕ, когда они так же, как и Я, ищут помощи у других?"
    # "Может, я начинаю взрослеть? Мне снова тошно."
    # "Мой маленький Я стоит на другом берегу. Я нашёл себя?"
    # "Я наконец могу его понять? А что это даст мне?"
    # "Смотря на него, мне кажется, что я был таким глупеньким."
    # "Мне бы не мешало разок в день перевести дух. Возможно, надо пересмотреть свои взгляды на некоторые вещи."
    jump Hes_yshol
return

init:
    $ images_auto()

    image clock:
        anchor(.5, .5)
        contains:
            align(.5, .5)
            "theclock"
        contains:
            align(.475, .425)
            At(Clock(tformat="%H:%M", size=200, color="#7ac", font="fonts/digitalicg.ttf"), turn(5, -25, 7))


label Hes_yshol:
    camera at parallax_off
    scene bg desk

    show clock at posing(1.75, .475, .7, .475)
    with dissolve

    "Я открыл глаза, на часах моего будильника были заветные любые цифры."
    "Главное, что я проснулся. И новый день может начаться так же, как и прошлые."
    "Теперь я её хотя бы немного, да понимаю."
    "Но, разве что, я мог ухватиться за разные мысли, например за надежду найти этого человека, который был властен к моему расположению духа в любой момент."
    "А что она? У неё разве кто-то это забрал?"
    "Ничто, как и сама она, которая даже не может полноценно влиять на свою жизнь."
    "Он ушёл?"

    scene street_dead at zoom_1 
    hide clock
    hide bg desk 
    gg "Неделя прошла довольно удачно. Я стал лучше высыпаться. Но её я больше не видел."
    gg "Я нагнал учебный план и теперь могу чувствовать себя спокойней. Кажется, что я сделал серьёзный шаг, который в какой-то степени будет влиять на мою жизнь всё больше и больше."
    gg "Нарастающий комочек будущих планов, целей и их достижения, всё слишком хорошо. Это нагнетает."
    gg "Кажется, что это всё происходит не по моей воле. Нечто управляет мной и заставляет ощущать себя легче."
    gg "Некоторые мои одноклассники знают, как ощутить себя «легче». Я всегда думал, что даже так они счастливее меня."
    gg "А ведь веселье не вечно. Ощущать себя как перо – всегда риск."
    gg "И твой путь в «рай», не всегда может увенчаться успехом. Пока ты со своими кентами ищешь пути поймать хорошее настроение, ты будешь получать от этого ещё большее удовольствие."
    gg "Но в «безветренную» погоду пёрышки могут опуститься с небес на землю. А некоторые и вовсе погребены на несколько метров вглубь."
    gg "И ты уже не Икар, который воспарил благодаря искренним чувствам, а скорее бесполезный кусок дерьма, который сидит на кухне в панике, ломке по небу и в депрессии."
    gg "Ты уже не можешь «взлететь выше», и ты скучаешь по этим чувствам. В конце концов ты больше не намерен это терпеть и в большинстве своём сам и поджигаешь свои крылья."
    gg "Ты был намерен от них избавиться, но, неожиданно для тебя, пламя начинает переноситься на твоё тело. Ты горишь заживо."
    gg "Умер, а время смерти никто не зафиксирует. Тешь себя, что ты можешь четко распределять границы."
    gg "Тешь себя, ведь ты можешь не выходить за рамки. Тешь себя, что ты прожил немногим дольше людей, которые закончили свои полёты раньше тебя."
    gg "Тешь себя, что ты остался один. Тешь себя, что мир несправедлив именно к тебе."
    gg "На тебя явно повлияло твоё окружение, да и вообще ты ни на грамм не виноват. Никогда не понимал их."
    gg "Мама в детстве говорила: «Долгий, славный смех - предвестник горьких слёз»."
    gg "Но человек вопреки всему хочет найти способ стать счастливым раз и навсегда. Он хочет добиться идеальной жизни, упрямый ты идешь прямо в лоб к своей цели."
    gg "Но по пути не видишь, что причиняешь кому-то этим неудобства. А когда за твоё открытие велосипеда тебе не дадут вознаграждения и твой труд не окупится – ты сразу вспомнишь и поймешь чувства тех людей, которые вставали у тебя на пути."
    gg "Ты лишь отсрочил себе это мгновение принятия. А если бы ты и дошел, и твои труды окупились, ты был бы всё так же недоволен."
    gg "Тебе бы было явно недостаточно. И ты, ставя новую недостижимую цель, вдруг узнаешь о своих лимитах."
    gg "А когда испробовал под один миллион разных способов, понимаешь, насколько ты жалкий."
    gg "Ещё никому не удавалось в порыве быть довольным настолько, насколько это надо. Иногда рискуя своим здоровьем, ты ограничиваешь себе жизнь заранее зарезервированной койкой в больнице."
    gg "Когда ты поставил на зеро, счёт в банке покидает тебя, и ты вынужден платить деньги плохим ребятам. И то и то незаконно и не честно."
    gg "Я никогда не пойму их. Какой смысл вообще имеет что-то найти, если чтобы дать себе большее, ты потеряешь в двойне?"

    gg "По дороге домой я увидел совсем молодого парня. Его тело валялось около мусорных пакетов и контейнеров в темном переулке."
    gg "Видимо, оно было бездыханным. А ведь это был парень из моей школы судя по нашивке у него на рукаве. Форма явно нашей школы."
    
    menu:
        "Подойти ближе":
            call label_podoyti_blyzhe
        
        "Не подходить":
            call label_ne_podhodit
    
    # "Следующий день есть следующий день, просыпаясь утром я обнаруживаю приятную для меня вещь. На столе рядом с кроватью стоит мой завтрак."
    # "Кружка кофе, макароны и небольшие прожаренные кусочки мяса. Можно сказать, это были тефтельки."
    # "Но, самое главное - записка, которую, судя по всему, оставила мама. А мог бы быть кто-то ещё?"
    # "В записке было написано о том, что она уехала за город и вернется только следующим днем. Приятно."
    # "Мама всё так же верит в меня и надеется на мою самостоятельность. Кажется, в её глазах я стал нормальным."
    # "Не то чтобы раньше она думала, что я не нормальный, скорее просто переживала за меня, для матерей мы выглядим чуть лучше."
    # "Мама сильно любит меня. Забота и ответственность — это всё то, что её окружало и окружает сейчас."
    # "Но сейчас она наконец смогла перевести меня к аспекту моего развития. Самостоятельного развития."
    # "Всю мою жизнь она то и делала, что показывала какая жизнь на самом деле хорошая. Будто цитируя Бога, она создавала землю под моими ногами."
    # "В будущем я смогу созидать. Это не приходит с начала жизненного пути. По крайней мере, это не мой случай."
    # "Я был так поглощён простотой этого мира, что перестал даже думать кто я, и почему двигаются мои руки. Почему мои глаза могут смотреть в разные стороны?"
    # "Я многого не подмечал. Этот процесс начался заново."
    # "И мама не опровергала это чисто из-за желания привить мне мир каким видит его она. Она всегда поддерживала и надеялась."
    # "Но с тем. Материнская любовь к жизни так же заразительна, как и тревожность."
    # "Это тоже оказало на меня большое влияние, иногда я видел, как она плакала, когда мне было плохо и я долго болел, она не отходила на меня ни на шаг и усердно трудилась лишь для того, чтобы я смог встать на ноги."
    # "Я не заснул полностью. Её комната за стеной. Её всхлипы слышны отчетливо."
    # "Иногда, чтобы в порыве не закричать, она сдерживалась и из-за этого её плач превратился в мягкий грустный шепот. Протяжный шепот."
    # "Шмурыгая носом и под конец вдыхая всё больше воздуха, но уже через рот. Она шла в ванную и, по всему видимому, умывалась."
    # "Сейчас она может хоть немного выдохнуть. Я рад за неё."

    # "По-моему, я уже забыл, как это было на самом деле. Дни, которые ощущались будто бы я был высушен."
    # "Я улыбаюсь, идя домой, я счастлив новому дню, который начинается с прогулки до места учебы."
    # "Мне не хотелось постоянно садиться в автобус к людям, которые, возможно, как и я, были потеряны, люди, которые не могут прочувствовать всю мою радость и разделить её со мной."
    # "Постоянно ехав в автобусе, я не приходил в дичайший восторг. По ряду многих случаев."
    # "Я боюсь насекомых, но не тех, которые выглядят как обычные насекомые. Видя что-то новое и довольно жуткое, я всегда входил в состояние ужаса."
    # "Сидя у окна, когда рядом со мной сидит здоровый лоб, раскинувши свои плечи и всем видом показывая свою доминантность, я боялся пошелохнутся. А очень то мне и хотелось."
    # "Справа от меня – прижавшегося к окну, я увидел то ли муху, то ли комара, то ли скорпиона."
    # "Это создание было похоже на скорпиона чисто из-за своего жала, оно опускало и поднимало его снова и снова."
    # "В моменте, когда я понял, что эта хуйня может ещё и летать, было уже поздно. Оно полетело прямо на меня, на чистейшем рывке с низкого старта, как это делали спринтеры по телеку."
    # "Конечно, я дернулся! Никто бы не остался в положении «поклонения» этому созданию, пустив всё на самотек, как будто это священный скарабей."
    # "Это село на меня. А мужик, которого я чуть не вытолкнул с его места (на процентов 20 оно было моим, но не суть), начал смеяться надо мной."
    # "Я бы посмотрел на его лицо, будь он по левую сторону от меня. Рожа, которую он скорчил, будто смотря сверху вниз, запомнится мне на долго."
    # "Я кое-как достал листок с конспектом, который так и не вклеил в тетрадь, и по божьей воле это создание зацепилось за него, что позволило мне выкинуть его в открытое окно."
    # "А мужик становился всё больше и больше. Это скорее не была основная причина, почему я больше в этот лоховоз не сяду."
    # "Выпившие в сопли люди по праздникам, которым не сидится дома, деды и старушки, готовые вечно с тобой поругаться и постоянные давки,"
    # "в которых ты всё боишься тронуть других людей немногим больше, чем было до этого, чем ты провоцируешь их посмотреть на тебя, повернув свою недовольную голову в твою сторону и осмотреть тебя с ног до головы."
    
    # "Так я и дошел до школы. Выпускной класс обычно имеет некие привилегии, по типу: «Главное готовься к экзаменам и сдавай тесты вовремя, за посещения можешь совсем не волноваться!»,"
    # "Но я не особо могу поверить в то, что совсем не посещая, можно добиться хорошего расположения заведующих."
    # "Там же у меня был кореш, с которым я проводил всё свое время, которое было мне дано на момент нахождения в стенах заведения."
    # "После учёбы я пошёл посидеть в парк неподалёку. На лавочках было довольно много народа оно и не удивительно, учебный день окончен."
    # "В парке была небольшая кофейня, в которую меня и позвал Кидзуки."
    camera at parallax_off
    scene streetcafe at zoom_1

    show kidzuki_smile2 at effi_position
    kidzuki "Мы, кажется, почти пришли!?"
    gg "Я до сих пор не особо верю, что вытащил тебя куда-то в люди."
    gg "В последнее время ты не выходил не то чтобы на улицу, а даже из комнаты."
    gg "Мне все рассказала Ное."
    hide kidzuki_smile2

    menu:
        "Что она тебе успела наговорить?":
            call рассказать
            
        "Как у неё язык изо рта еще не выпал":
            call язвить     
return
