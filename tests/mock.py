# coding=utf-8
from six import u
import json


account_auth = u('{"passkey": "of3k4oasd9498dfvjh5hthhgfgdfy"}')
account_profile = u('{"username": "UserName", "reputation": 125, "review_count": 11, "gold_badges": 2, "silver_badges": 14, "bronze_badges": 21, "unread_pm_count": 3, "unread_forum_count": 7, "unread_updatelist_count": 2, "subscription_count": 96}')
account_updatelist = u('{"item": [{"date": "2011-04-09T15:38:30", "description": "Новая раздача", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400813/", "new": 1, "for_object": {"movie": {"id": 115866, "title": "Элизиум: Рай не на Земле (2013)"}}}, {"date": "2011-04-09T15:28:35", "description": "2 новых комментария", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400812:400811/", "new": 0, "for_object": {"comment": {"id": 1810, "title": "Отзыв admin на фильм «Красное на белом (2009)»"}}}, {"date": "2011-04-09T15:27:24", "description": "Новый фильм", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400742:400743/", "new": 0, "for_object": {"person": {"id": 830, "title": "Райан Гослинг"}}}, {"date": "2011-04-09T15:17:14", "description": "3 новых раздачи", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400601:400599:400598/", "new": 0, "for_object": {"movie": {"id": 115866, "title": "Элизиум: Рай не на Земле (2013)"}}}]}')
account_watchlist = u('{"comment": [{"date": "2011-04-09T15:38:30", "name": "Отзыв UserName на фильм «Назад в будущее (1985)»", "description": "Новые комментарии", "url": "http://cinemate.cc/comment/123/"}, {"date": "2011-04-09T15:28:35", "name": "Отзыв UserName на фильм «Пипец (2010)»", "description": "Новые комментарии", "url": "http://cinemate.cc/comment/456/"}], "person": [{"date": "2011-04-02T02:08:23", "name": "Лив Тайлер", "description": "Новые фильмы с участием", "url": "http://cinemate.cc/person/18104/"}, {"date": "2011-04-03T02:08:31", "name": "Кристен Стюарт", "description": "Новые фильмы с участием", "url": "http://cinemate.cc/person/8151/"}], "movie": [{"date": "2011-04-04T16:37:24", "name": "Кунг-фу Панда 2 (2011)", "description": "Новые раздачи", "url": "http://cinemate.cc/movie/68725/"}, {"date": "2011-04-07T16:37:27", "name": "Супер 8 (2011)", "description": "Новые раздачи", "url": "http://cinemate.cc/movie/68709/"}]}')
movie = u('{"movie": {"kinopoisk": {"rating": "6.2", "votes": "11673"}, "director": {"person": {"attrib": {"id": "163239"}, "value": "Малькольм Венвилль"}}, "description": "Встречайте Генри – самого унылого парня в Америке. Он сидит в своей будке у дороги, взимая пошлину с проезжающих. Казалось, в его жизни ничто не может измениться. Но однажды сомнительный приятель попросил Генри подождать его у крыльца главного банка в Буффало... В результате – четыре года тюрьмы по ложному обвинению в ограблении. Но пройдет время, и Генри вернется к тому самому банку, чтобы взять свое…", "url": "http://cinemate.cc/movie/68675/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.medium.jpg"}}, "release_date_russia": "2011-04-07", "title_original": "Henry\'s Crime", "country": {"name": "США"}, "cast": {"person": [{"attrib": {"id": "2624"}, "value": "Киану Ривз"}, {"attrib": {"id": "1219"}, "value": "Вера Фармига"}, {"attrib": {"id": "2856"}, "value": "Петер Стормаре"}, {"attrib": {"id": "112"}, "value": "Джеймс Каан"}, {"attrib": {"id": "2243"}, "value": "Джуди Грир"}, {"attrib": {"id": "9803"}, "value": "Билл Дьюк"}, {"attrib": {"id": "13257"}, "value": "Фишер Стивенс"}, {"attrib": {"id": "39646"}, "value": "Карри Грэм"}, {"attrib": {"id": "9040"}, "value": "Дэвид Костабайл"}, {"attrib": {"id": "5933"}, "value": "Дэнни Хоч"}, {"attrib": {"id": "67860"}, "value": "Хэзер МакРэй"}, {"attrib": {"id": "108757"}, "value": "Джордан Гелбер"}, {"attrib": {"id": "190286"}, "value": "Елена Беука"}, {"attrib": {"id": "148348"}, "value": "Сара Гленденинг"}, {"attrib": {"id": "190285"}, "value": "Жули Ордон"}]}, "imdb": {"rating": "5.9", "votes": "12147"}, "title_russian": "Криминальная фишка от Генри", "year": 2010, "genre": {"name": "комедия"}, "runtime": 108, "type": "movie", "id": 68675, "trailer": "http://www.youtube.com/watch?v=6IcqfNeql68", "release_date_world": "2011-04-07"}}')
movie_one_person = u('{"movie": {"kinopoisk": {"rating": "8.1", "votes": "254"}, "director": {"person": [{"attrib": {"id": "82691"}, "value": "Джозеф Барбера"}, {"attrib": {"id": "82697"}, "value": "Уильям Ханна"}]}, "release_date_world": "1944-04-14", "description": "Том и Джерри вызывают смех и покоряют сердца детей и взрослых всего мира на протяжении десятилетий. Эти герои поражают зрителей своим мастерством перевоплощения, изобретательными трюками и розыгрышами, изощренными ловушками и уморительными проделками.", "url": "http://cinemate.cc/movie/147668/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.medium.jpg"}}, "title_english": "Tom and Jerry", "country": {"name": "США"}, "cast": {"person": {"attrib": {"id": "82697"}, "value": "Уильям Ханна"}}, "imdb": {"rating": "7.3", "votes": "384"}, "title_original": "The Million Dollar Cat", "year": 1944, "genre": {"name": ["комедия", "короткометражка", "мультфильм", "семейный"]}, "runtime": 7, "type": "short", "id": 147668, "title_russian": "Кот на миллион долларов"}}')
movie_list = u('{"movie": [{"url": "http://cinemate.cc/movie/131001/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.medium.jpg"}}, "title_original": "Mike & Molly", "title_russian": "Майк и Молли", "year": 2010, "runtime": 30, "type": "serial", "id": 131001}, {"url": "http://cinemate.cc/movie/131657/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.medium.jpg"}}, "title_original": "Astonishing X-Men: Gifted", "title_russian": "Удивительные Люди Икс: Одаренные", "year": 2010, "runtime": 60, "type": "video", "id": 131657}, {"url": "http://cinemate.cc/movie/109767/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.medium.jpg"}}, "title_original": "Iron Man: Extremis", "title_russian": "Железный человек: Экстремис", "year": 2010, "runtime": 0, "type": "serial", "id": 109767}, {"url": "http://cinemate.cc/movie/83460/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.medium.jpg"}}, "title_original": "America", "title_russian": "Америка", "year": 2010, "runtime": 111, "type": "movie", "id": 83460}, {"url": "http://cinemate.cc/movie/66450/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.medium.jpg"}}, "title_original": "Autoreiji", "title_russian": "Беспредел", "year": 2010, "runtime": 110, "type": "movie", "id": 66450}, {"url": "http://cinemate.cc/movie/135826/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.medium.jpg"}}, "title_original": "Making History", "title_russian": "Воссоздавая историю", "year": 2010, "runtime": 50, "type": "serial", "id": 135826}, {"url": "http://cinemate.cc/movie/105524/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.medium.jpg"}}, "title_original": "High School", "title_russian": "Крутые кексы", "year": 2010, "runtime": 99, "type": "movie", "id": 105524}, {"url": "http://cinemate.cc/movie/122874/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.medium.jpg"}}, "title_original": "The Big C", "title_russian": "Большая буква «Р»", "year": 2010, "runtime": 28, "type": "serial", "id": 122874}, {"url": "http://cinemate.cc/movie/133159/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.medium.jpg"}}, "title_original": "Killing Time", "title_russian": "Час Икс", "year": 2010, "runtime": 60, "type": "serial", "id": 133159}, {"url": "http://cinemate.cc/movie/52036/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.medium.jpg"}}, "title_original": "Legend of the Boneknapper Dragon", "title_russian": "Легенда о Костоломе", "year": 2010, "runtime": 16, "type": "short", "id": 52036}]}')
movie_search = u('{"movie": [{"url": "http://cinemate.cc/movie/120787/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.medium.jpg"}}, "title_original": "Pirates of the Caribbean: Dead Men Tell No Tales", "title_russian": "Пираты Карибского моря: Мертвецы не рассказывают сказки", "year": 2016, "runtime": 0, "type": "movie", "id": 120787}, {"url": "http://cinemate.cc/movie/68669/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.medium.jpg"}}, "title_original": "Pirates of the Caribbean: On Stranger Tides", "title_russian": "Пираты Карибского моря: На странных берегах", "year": 2011, "runtime": 141, "type": "movie", "id": 68669}, {"url": "http://cinemate.cc/movie/1787/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: At World\'s End", "title_russian": "Пираты Карибского моря 3: На краю Света", "year": 2007, "runtime": 169, "type": "movie", "id": 1787}, {"url": "http://cinemate.cc/movie/2194/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: Dead Man\'s Chest", "title_russian": "Пираты Карибского моря 2: Сундук мертвеца", "year": 2006, "runtime": 151, "type": "movie", "id": 2194}, {"url": "http://cinemate.cc/movie/15869/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.medium.jpg"}}, "title_original": "Blackbeard: Terror at Sea", "title_russian": "Пираты карибского моря: Черная борода", "year": 2006, "runtime": 120, "type": "movie", "id": 15869}, {"url": "http://cinemate.cc/movie/7412/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: The Curse of the Black Pearl", "title_russian": "Пираты Карибского моря: Проклятие черной жемчужины", "year": 2003, "runtime": 143, "type": "movie", "id": 7412}]}')
person = u('{"person": {"url": "http://cinemate.cc/person/3971/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg"}}, "name_original": "Jake Gyllenhaal", "id": 3971, "name": "Джейк Джилленхол"}}')
person_movies = u('{"person": {"name": "Ян Шванкмайер", "url": "http://cinemate.cc/person/43083/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.medium.jpg"}}, "name_original": "Jan Svankmajer", "movies": {"director": {"movie": [{"kinopoisk": {"rating": "7.8", "votes": "378"}, "url": "http://cinemate.cc/movie/79144/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.medium.jpg"}}, "title_original": "Prezít svuj zivot (teorie a praxe)", "imdb": {"rating": "7.3", "votes": "575"}, "title_russian": "Пережить свою жизнь", "year": 2010, "runtime": 105, "type": "movie", "id": 79144}, {"kinopoisk": {"rating": "7.4", "votes": "1361"}, "url": "http://cinemate.cc/movie/4974/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.medium.jpg"}}, "title_original": "Lunacy", "imdb": {"rating": "7.3", "votes": "2140"}, "title_russian": "Безумие", "year": 2005, "runtime": 123, "type": "movie", "id": 4974}, {"kinopoisk": {"rating": "7.5", "votes": "2248"}, "url": "http://cinemate.cc/movie/31965/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.medium.jpg"}}, "title_original": "Otesánek", "imdb": {"rating": "7.3", "votes": "3988"}, "title_russian": "Полено", "year": 2000, "runtime": 132, "type": "movie", "id": 31965}, {"kinopoisk": {"rating": "7.7", "votes": "904"}, "url": "http://cinemate.cc/movie/4703/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.medium.jpg"}}, "title_original": "Conspirators of Pleasure", "imdb": {"rating": "7.6", "votes": "1856"}, "title_russian": "Конспираторы наслаждений", "year": 1996, "runtime": 75, "type": "movie", "id": 4703}, {"kinopoisk": {"rating": "7.4", "votes": "471"}, "url": "http://cinemate.cc/movie/5509/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.medium.jpg"}}, "title_original": "Faust", "imdb": {"rating": "7.5", "votes": "2298"}, "title_russian": "Урок Фауста", "year": 1994, "runtime": 97, "type": "movie", "id": 5509}]}, "actor": {"movie": [{"kinopoisk": {"rating": "7.8", "votes": "378"}, "url": "http://cinemate.cc/movie/79144/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.medium.jpg"}}, "title_original": "Prezít svuj zivot (teorie a praxe)", "imdb": {"rating": "7.3", "votes": "575"}, "title_russian": "Пережить свою жизнь", "year": 2010, "runtime": 105, "type": "movie", "id": 79144}, {"kinopoisk": {"rating": "7.4", "votes": "1361"}, "url": "http://cinemate.cc/movie/4974/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.medium.jpg"}}, "title_original": "Lunacy", "imdb": {"rating": "7.3", "votes": "2140"}, "title_russian": "Безумие", "year": 2005, "runtime": 123, "type": "movie", "id": 4974}]}}, "id": 43083}}')
person_search = u('{"person": [{"url": "http://cinemate.cc/person/3971/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg"}}, "name_original": "Jake Gyllenhaal", "id": 3971, "name": "Джейк Джилленхол"}, {"url": "http://cinemate.cc/person/1685/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.medium.jpg"}}, "name_original": "Maggie Gyllenhaal", "id": 1685, "name": "Мэгги Джилленхол"}, {"url": "http://cinemate.cc/person/79826/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.medium.jpg"}}, "name_original": "Stephen Gyllenhaal", "id": 79826, "name": "Стивен Джилленхол"}, {"url": "http://cinemate.cc/person/76362/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.medium.jpg"}}, "name_original": "Eric Mendenhall", "id": 76362, "name": "Эрик Менденхол"}, {"url": "http://cinemate.cc/person/361603/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Мэгги Джилленхол", "id": 361603, "name": "Мэгги Джилленхол"}, {"url": "http://cinemate.cc/person/303647/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Stephen Gyllenhaal", "id": 303647, "name": "Стивен Джилленхол"}, {"url": "http://cinemate.cc/person/333519/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Стивен Джилленхол", "id": 333519, "name": "Стивен Джилленхол"}]}')
stats_new = u('{"users_count": 4, "reviews_count": 0, "comments_count": 2, "movies_count": 7}')
stats_wtf = u('{"error": "Unknown error"}')
response404 = u('response irrelevant 404')


reqresp = {
    'account.auth': {
        'req': 'http://api.cinemate.cc/account.auth?username=USERNAME&password=PASSWORD&format=json',
        'resp': account_auth,
    },
    'account.profile': {
        'req': 'http://api.cinemate.cc/account.profile?passkey=PASSKEY&format=json',
        'resp': account_profile,
    },
    'account.updatelist': {
        'req': 'http://api.cinemate.cc/account.updatelist?passkey=PASSKEY&newonly=1&format=json',
        'resp': account_updatelist,
    },
    'account.watchlist': {
        'req': 'http://api.cinemate.cc/account.watchlist?passkey=PASSKEY&format=json',
        'resp': account_watchlist,
    },
    'movie': {
        'req': 'http://api.cinemate.cc/movie?apikey=APIKEY&id=68675&format=json',
        'resp': movie,
    },
    'movie_one_person': {
        'req': 'http://api.cinemate.cc/movie?apikey=APIKEY&id=147668&format=json',
        'resp': movie_one_person,
    },
    'movie.list': {
        'req': 'http://api.cinemate.cc/movie.list?apikey=APIKEY&year=2010&format=json',
        'resp': movie_list,
    },
    'movie.search': {
        'req': u('http://api.cinemate.cc/movie.search?apikey=APIKEY&term=Пираты%20кариб&format=json'),
        'resp': movie_search,
    },
    'person': {
        'req': 'http://api.cinemate.cc/person?id=3971&apikey=APIKEY&format=json',
        'resp': person,
    },
    'person.movies': {
        'req': 'http://api.cinemate.cc/person.movies?id=43083&apikey=APIKEY&format=json',
        'resp': person_movies,
    },
    'person.search': {
        'req': u('http://api.cinemate.cc/person.search?apikey=APIKEY&term=гиленхол&format=json'),
        'resp': person_search,
    },
    'stats.new': {
        'req': 'http://api.cinemate.cc/stats.new?format=json',
        'resp': stats_new,
    },
    'stats.wtf': {  # raise RuntimeError('Unknown error')
        'req': 'http://api.cinemate.cc/stats.wtf?format=json',
        'resp': stats_wtf,
    },
    'account.wrong_status_code': {  # raise RuntimeError()
        'req': 'http://api.cinemate.cc/account.auth?username=USERNAME&password=PASSWORD&format=pewpewpew',
        'resp': response404,
        'status': 404,
    },
}

if __name__ == '__main__':
    for k, v in reqresp.items():
        try:
            json.loads(v['resp'])
        except ValueError as exc:
            print(k, exc)
