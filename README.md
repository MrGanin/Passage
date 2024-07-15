Было необходимо создать API к сайту с базой о перевалах, чтобы пользователь с мобильного телефон, мог отправлять необходимую
информацию, а именно: 
-координаты перевала и его высота;
-имя пользователя;
-почта и телефон пользователя;
-название перевала;
-несколько фотографий перевала.

Данная информация передается с помощью JSON файлов в формате:


{
    "beauty_title": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "user": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович",
        "phone": "+7 555 55 55"
    },
    "coords": {
        "latitude": 45.3842,
        "longitude": 7.1525,
        "height": 1200
    },
    "level": {
	"winter": ""
        "summer": "1А",
        "autumn": "1А",
        "spring": "",
        
    },
    
    "images": [{data:"<https://i.ytimg.com/vi/iPoRE9VRckM/hqdefault.jpg>", title:"Седловина"}, {data:"<https://fullpicture.ru/wp-content/uploads/2023/09/1623729976_60-pibig_info-p-vulkan-reinir-priroda-krasivo-foto-64-1024x640.jpg>", title:"Подъём"}]
}
}

В проекте реализованные необходимые модели, под требуемые данные. API приложение работает на основе сериализаторов, наследуемых от из коробки
ModelSerializer и WritableNestedModelSerializer, на каждую модель, и используемые в представлении PassageAPIView, которое наследуется от ModelViewSet
Полностью реальзовано создание, просмотр, полное редактирование, частичное редактирование, удаление.
