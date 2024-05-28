label label_podoyti_blyzhe:
    camera at parallax_on
    scene black with dissolve
    scene bg dead with dissolve
    hide black

    gg "Мной овладело любопытство. Я позволил себе подойти немного ближе. Бездыханное тело все больше давило на меня."
    gg "На лбу стал выступать пот. Кажется, он упарывался не только обычными таблетками. Рядом лежали шприцы и разбитые стеклянные флакончики."
    gg "Вряд-ли от какого-то парфюма - от него явно пахло ужасно. И ничего ему не поможет."
    gg "По телу пробежала дрожь, мне казалось, что картина передо мной начала бурлить, будто я постоянно погружаюсь в воду с открытыми глазами, не успевая вдохнуть воздух."
    gg "На лбу начинает выступать пот, а кисти покрылись мурашками. Они как будто затекли. По телу бежит дрожь. А глаза начинают вытекать."
    gg "Что-то не так. Я успел выбежать с этого закутка, и, облокотившись на близлежащую стену, смог спокойно набрать воздуха."
    gg "Уже вечерело. Не стоит мне и дальше разгуливать в этих окрестностях. Район не безопасный."
    gg "Постоянные патрули. Даже сейчас я не чувствую себя в полной безопасности, хах. Даже не знаю почему."
    gg "А может, потому что наисвежайший труп парня моего возраста лежит практически за моей спиной. Он явно не выглядит нормально. А я пиздец замёрз."
    gg "Надо двигаться. Мало ли что может случиться, если меня увидят здесь кто-либо из мужчин в форме. Время сейчас не особо располагает, да и проблем явно не оберусь."

    camera at parallax_off
    scene black with dissolve
    hide bg dead with dissolve
    scene bg room with dissolve

    gg "Я дома, весь в поту, уставший и злой. Нахуй я вообще туда полез, был ли в этом какой-то резон?"
    gg "Иногда люди совершают ужасные вещи. Мама, кажется, спит, надо постараться быть немного да тише. Я всё ещё дрожу, думаю, надо лечь спать пораньше."

    hide bg room with dissolve
    scene black with dissolve

    jump posle
    return

label label_ne_podhodit:
    camera at parallax_on
    scene black with dissolve
    scene bg dead_dark with dissolve
    hide black

    gg "Такой мерзкий и вялый. Даже смотреть тошно. Разрушить свою жизнь так просто. А ведь его даже об этом никто не просил."
    gg "Ничтожество вроде него довольно популярно, он явно получал от этого определенный ~КаЙ~ф."
    gg "Стоит ли говорить то, что на его похоронах его будут оплакивать и сожалеть о его смерти? Я, конечно, не говорю, что это неправильно."
    gg "Но определенно на его ошибках стоит учиться. Похороны роскошны, у него явно были деньги на это дерьмо. Родители? Не хочу дальше думать об этом."
    gg "Все равно меня это не касается, я ничего не добьюсь, если продолжу. Лучше подумать о чем то, что позволило бы мне отвлечь себя."
    gg "Скажем. А что, если таких как ~он~ уносят все глубже во тьму люди, которые бы съели его. Ну что-то вроде вынужденного людоедства, когда надо цепляться за каждую возможность выжить."
    gg "Возможно ли такое? Верить в это весело, но жутко. Это хотя бы способно разбавить наши обыденные дни."
    gg "Это неблагополучный район. Патрули, которые устраивают проходки по окрестностям довольно резки, но люди все также способны пропадать."
    gg "Некоторых находят. Находят, как его нашел я. А некоторые просто пропадают без вести."
    gg "Не то что тела, ни единого намека на его существование найти не способны. А что, если все действительно так, как я это представил? Хах."
    gg "Мне кажется, что надо скорее вернуться домой, начинает темнеть."

    camera at parallax_off
    scene black with dissolve
    hide bg dead_dark with dissolve

    scene bg room with dissolve
    gg "Я дома, всё довольно спокойно. Мама в это время ложится спать, не хочу ее будить. Надо бы и мне отойти ко сну, день сегодня был довольно насыщенным. Думаю, лягу пораньше."

    hide bg room with dissolve
    scene black with dissolve
    camera at parallax_off

    jump posle
    return
