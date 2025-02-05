# Космический Телеграм

Данная программа позволяет скачивать, а затем отправлять в Телеграмм канал фотографии из космоса от NASA и SpaceX.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы с программой необходимо получить индивидуальный ключь от NASA (по ссылке: https://api.nasa.gov/), И добавить его в `.env` файл, 
так же для отправки файлов нужен токен для работы с телеграмм ботом, chat_id , и время задержки отправления файлов.
Так должен выглядеть файл `.env`:
```
API_KEY="Ключ NASA"
TOKEN="Токен для работы с ботом"
CHAT_ID="@cosmicpicture1"
TIME=Время задержки в секундах
```
Фотографии отправляються в телеграмм канал: https://t.me/cosmicpicture1

### Как использовать 
Для скачивания фотографий от "SpeseX" запустите файл `fetch_spacex_images.py` через консоль:
```
pytnon fetch_spacex_images.py
```
Для скачивания фотографий: "фото дня" или "EPIC" от NASA прроделайте тоже самое с файлами `fetch_nasa_images.py` и `fetch_nasa_epic.py`:
```
pytnon fetch_nasa_images.py
```
```
python fetch_nasa_epic.py
```

Для Запуска скрипта Телеграмм бота используйте файл `tg_bot.py`:
```
pytnon tg_bot.py
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
