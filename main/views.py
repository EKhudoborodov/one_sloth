from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
    achievements = [

        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553293099479081010/test2463.png?ex=6aba09ed&is=6ab8b86d&hm=e1eb2024d038ae482417c24be39b4e9fdb4a1f14a58f686111829a15615acbf5&',
            'title': 'Достижение получено!',
            'name': 'Холодильник бы проведать',
            'desc': 'Хорята отправили Юлю покушать 5 раз. (Если она реально уйдёт покушать, засчитаю даже за 1 раз)',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1278295011045412988/1445099213359939787/c98305a21c45127e9a099f80d98b2bcb.png?ex=6ab9f645&is=6ab8a4c5&hm=4ba6785c928110843c38ced2163550e0918aef86164cfe335773df1f66492290&',
            'title': 'Достижение получено!',
            'name': 'Да, помню этот прЕкол',
            'desc': 'Хорёнок вспомнил клип, опубликованный больше года назад',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553297290662383656/1_5.jpg?ex=6aba0dd4&is=6ab8bc54&hm=5b821892e8af2b0f1be3fc9a34f3f1b4763498b7784e231d96037a12b4bc7b2d&',
            'title': 'Достижение получено!',
            'name': 'Странно, а раньше работало',
            'desc': 'Использованны 3 команды бота, которых нет на этом канале',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_5b0bd816faf840b3acec6c2009952628/default/dark/3.0',
            'title': 'Достижение получено!',
            'name': 'Ага... так... угу... записываю...',
            'desc': 'Юля поведела какую-то историю из жизни, после чего не менее 7 хорят продемонстрировали свою вовлечённость в рассказ',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553298893834559539/22646b8125c131d5.jpg?ex=6aba0f53&is=6ab8bdd3&hm=cb6f53664121e7b1f64869567a74c1e90eac44ca4e011814f674338afeb75899&',
            'title': 'Достижение получено!',
            'name': 'Это же ты! Да... как же там тебя...',
            'desc': 'Юлю назвали 7 разными способами',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_a4c2c8de3c854b64bd9263f6fa5c9a5c/default/light/3.0',
            'title': 'Достижение получено!',
            'name': 'Вот это ты меня, конечно, рассмешнил',
            'desc': 'Зритель написал в чат шутку или прикол, после которого Вакрос посмеялся на 4-ю стадию смеха',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://avatars.mds.yandex.net/i?id=983fb48b6a0c79149ea4d867012fdc46_l-4033040-images-thumbs&n=13',
            'title': 'Достижение получено!',
            'name': 'Переводчик',
            'desc': 'Сообщение написанное одним хорёнком на \"эльфийском\" языке было переведено другим на русский',
            'progress': 100,
        },
        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553304436330467379/123.jpg?ex=6aba147c&is=6ab8c2fc&hm=51d11b934d3f4837b64f4e3f88b34ff6f56358e733303c61ca9105ab90224016&',
            'title': 'Достижение получено!',
            'name': 'Моя игра — твои правила',
            'desc': 'Хорёнок сделал предположение задания, которого нет ни в одной категории. Оно было выполнено совместными усилиями с другими хорятами.',
            'progress': 100,
        },

        {
            'category': 1,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_208cd91a7492496abf6f81197fcd19b8/default/dark/3.0',
            'title': 'Задание №1',
            'name': 'Да не забыла я!',
            'desc': 'Юля захочет что-то сделать, но в итоге забудет без напоминания',
            'progress': 0,
        },
        {
            'category': 1,
            'link_href': 'https://cdn.discordapp.com/attachments/1192877614717747381/1459632919575265335/horiPOP.gif?ex=6aba19d6&is=6ab8c856&hm=e547e96267f263f126b5a085b31cb05cfa79cd4680d067fcc1655e5a57ba9290&   ',
            'title': 'Задание №4',
            'name': 'Хрюшка-повторюшка',
            'desc': ' Не менее 5 разных хорят повторят в чате сказанную Юлей смешную фразу',
            'progress': 100 * 4 / 5,
        },

        # ВОТ ТУТ ВТОРЫЕ

        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553306142392975371/cf1f63bfe81287cf.jpg?ex=6aba1613&is=6ab8c493&hm=e5a134e062c7881196ee9d1ec6eea172b8398bbf2272819061b795d184e2e811&',
            'title': 'Достижение получено!',
            'name': 'Я тоже хочу поучаствовать',
            'desc': 'Юля скинула в чат любой из своих смайликов',
            'progress': 100,
        },
        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553385615729360968/image.png?ex=6aba6017&is=6ab90e97&hm=f5a5cab4a45228ba76a2bcd05fe4b5fe135e79082a6b154545a25cedc32648a4&',
            'title': 'Достижение получено!',
            'name': 'Фирменный бренд',
            'desc': 'Упоминание в чате не менее 5 старых или придуманных oihori смайликов',
            'progress': 100,
        },
        {
            'category': 2,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_1b44ad989b4448d9ae63b617f5ce7183/default/light/3.0',
            'title': 'Достижение получено!',
            'name': 'Ты топ',
            'desc': 'Используя награду "Прослушать моё сообщение", хорята отправили не менее 5 сообщений, содержащих oihoriYES',
            'progress': 100,
        },
        {
            'category': 2,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_968b575a3c4d46de9e770039e3f4af8a/default/light/3.0',
            'title': 'Достижение получено!',
            'name': 'Самое время устроить ВеЧеРиНкУ',
            'desc': 'Используя награду "Трек", хорёнок устроил дискотеку, в ходе которой не менее 10 разных хорят отправили любой танцующий смайлик. (Счётчик сбрасывается по окончании трека)',
            'progress': 100,
        },

        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553307040498192404/2_2.jpg?ex=6aba16e9&is=6ab8c569&hm=459daf58e4dace8eeef4bfb1147ee10f088326b0b43c6fb069f87b41058af55c&',
            'title': 'Задание №2',
            'name': 'Кто такая эта ваша пунктуация?',
            'desc': 'Написано сообщение не менее 12 слов, в котором каждое слово обособленно любым одинаковым смайликом',
            'progress': 0,
        },
        {
            'category': 2,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/81249/default/light/3.0',
            'title': 'Задание №5',
            'name': 'Лень SeriousSloth',
            'desc': 'Собранно "Ленивое комбо" (с помощью смайлика SeriousSloth ) длиной не менее 25 сообщений',
            'progress': 100 * 11 / 25,
        },
        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553309234723295242/b60ee958d0a6615d.jpg?ex=6aba18f4&is=6ab8c774&hm=baf68c46379cc542a4fb3d67d62235ffc6bdb7327abaa4e1ab7c2cafdba9e3e9&',
            'title': 'Задние №6',
            'name': 'СОЛНЫШКО, ДАВАЙ!',
            'desc': 'Отправлена подбадривающая паста в поддержку хорёнка, который зашёл поиграть',
            'progress': 0,
        },
        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553309855085887518/2_7.jpg?ex=6aba1988&is=6ab8c808&hm=d5af376f5548b4d29c33317954d1e248be2298a90de41ed2ce2780ae040edead&',
            'title': 'Задание №7',
            'name': 'Восьмое чудо света',
            'desc': 'Построена пирамида из любого смайлика шириной не менее 7 с участием не менее 7 разных зрителей',
            'progress': 0,
        },
        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553310716478496848/2_8.jpg?ex=6aba1a55&is=6ab8c8d5&hm=4d836a4b9e7eccabd039aff8d1e96098953a5bc250355114c9ce0679e5ff02b1&',
            'title': 'Задание №8',
            'name': 'Два барана на мосту',
            'desc': 'Собрана цепочка не менее 8 ответных сообщений между 2 хорятами, каждый из которых использовал свой одинаковый смайлик, противоположный по смыслу смайлику собеседника, в каждом из своих сообщений',
            'progress': 100 * 3 / 8,
        },
        {
            'category': 2,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553398940005564496/image.png?ex=6aba6c80&is=6ab91b00&hm=c9e8fb910ed28df5bc7d7aac396c847cc060ebac427ec0bfb51ae2a6deb05bc1&',
            'title': 'Задание №10',
            'name': 'Я художник, я так вижу',
            'desc': 'Написано сообщение, содержащее описание любой произошедшей на стриме ситуации с помощью смайликов',
            'progress': 0,
        },

        # ВОТ ТУТ ТРЕТИЕ

        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553312518305349703/3_1.jpg?ex=6aba1c03&is=6ab8ca83&hm=ed54e50541afa46fc724e580db379c461c6999103a50a54848aa8b03f79aaa40&',
            'title': 'Достижение получено!',
            'name': 'Каноничная обложка',
            'desc': 'Юля поставит поставит попу Вескера в меню',
            'progress': 100,
        },
        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553313407313248306/3_3.jpg?ex=6aba1cd7&is=6ab8cb57&hm=8e54af3bc45be73b07f14e31fc7b4b51fa12a2397546fa7b43b28fe76d23c938&',
            'title': 'Достижение получено!',
            'name': 'Не отставай от моды',
            'desc': 'Сыграть игру, где каждый хорёнок выберет одинакового выжившего',
            'progress': 100,
        },
        {
            'category': 3,
            'link_href': 'https://avatars.yandex.net/get-music-content/18132539/8ab81e57.a.42267337-1/m1000x1000',
            'title': 'Достижение получено!',
            'name': 'И тебя вылечат',
            'desc': '2 хорёнка с классом Медика прибежали на помощь и вылечили Юлю во время погони',
            'progress': 100,
        },
        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553346209412947968/image.png?ex=6aba3b64&is=6ab8e9e4&hm=a4b2b1eb8c666721c395c9fd0c3185bfa7baefecf7024f9d5a0408b898e3a260&',
            'title': 'Достижение получено!',
            'name': 'Твой хозяин для меня важен',
            'desc': 'Бот Вакроса был спасён фонариком/флешкой/палетой',
            'progress': 100,
        },


        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553397949663551498/image.png?ex=6aba6b93&is=6ab91a13&hm=f06d971b27d0da9e1da750dd1de0b3a35b0a9af361fb5a1b5c04603f0167260d&',
            'title': 'Задание №2',
            'name': 'Больше никогда руки не буду мыть',
            'desc': 'За матч каждый хорёнкок потрогал Юлю с помощью махающего эмоута',
            'progress': 100 * 5 / 7,
        },
        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553314196458971166/3_4.jpg?ex=6aba1d93&is=6ab8cc13&hm=c5d163a2aab82b268d62e2779d2bd8b225b3cb26fecb018a09c5f754ee9b21a4&',
            'title': 'Задание №4',
            'name': 'Семейное фото',
            'desc': 'В матче 2 на 8 все 7 хорят собрались вокруг Юли так, что каждый находится в поле зрения',
            'progress': 100 * 5 / 7,
        },
        {
            'category': 3,
            'link_href': 'https://torrent-mars.ru/_ld/75/39993118.jpg',
            'title': 'Задание №5',
            'name': 'Мой любимый трюк',
            'desc': 'Юля предложила сделать Сиджей тек хорёнку 5 раз за стрим',
            'progress': 100 * 3 / 5,
        },
        {
            'category': 3,
            'link_href': 'https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_2c57572e71084ce0b2d6c66eb08d3c91/default/light/3.0',
            'title': 'Задание №6',
            'name': 'О! Спасибо! Я выбрал!',
            'desc': 'Используя награду "выбор сурва + скин", хорёнок написал числа, по которым Юля выбрала себе скин',
            'progress': 0,
        },
        {
            'category': 3,
            'link_href': 'https://cdn.discordapp.com/attachments/1552748839092617309/1553401365777358899/image.png?ex=6aba6ec2&is=6ab91d42&hm=0c6e63a4ba2a495e249a1b1d8c01baa27efadcfb4a0ccdcbc67d46958bf3e14e&',
            'title': 'Задание №7',
            'name': 'Вас много, я одна',
            'desc': 'Не менее 17 разных хорят зашли вместе поиграть',
            'progress': 100 * 11 / 17,
        },
        {
            'category': 3,
            'link_href': 'https://static.wikia.nocookie.net/dead-by-daylight/images/b/b6/IconPerks_ResidualManifest.png/revision/latest?cb=20220609174641&path-prefix=ru',
            'title': 'Задание №9',
            'name': 'Я знаю, ты их любишь',
            'desc': '3 хорёнка отдали свой фонарик Юле, и она попользовалась каждым из фонариков',
            'progress': 100 * 2 / 3,
        },
    ]

    # Группируем по категориям
    columns = {1: [], 2: [], 3: []}
    for item in achievements:
        cat = item.get('category', 1)  # если категории нет — попадёт в 1
        if cat in columns:
            columns[cat].append(item)

    return render(request, 'main/index.html', {'columns': columns})

def index(request):
    """Главная страница — просто пустая заглушка."""
    return render(request, 'main/index.html')

def alert(request):
    """Страница, на которой показывается ачивка (другое устройство)."""
    return render(request, 'main/alert.html')

def remote(request):
    """Пульт: при нажатии кнопки отправляет сообщение в WebSocket-группу."""
    if request.method == 'POST':
        achievement_name = request.POST.get('a1', 'default')
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "alert_group",
            {
                "type": "alert_message",   # должно совпадать с методом в consumers.py
                "achievement": achievement_name,
            }
        )
        # После отправки возвращаемся на ту же страницу (или можно вернуть JSON)
        return render(request, 'main/remote.html', {'sent': True})
    return render(request, 'main/remote.html')