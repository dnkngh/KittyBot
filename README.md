# Проект KittyBot

## Описание
Telegram-бот , отправляющий произвольные картинки котов/собак по запросу пользователю. Картинки запрашиваются ботом у API ```thecatapi.com``` и ```thedogapi.com```. Предусмотрено логирование ошибок.

![image](https://user-images.githubusercontent.com/72282178/179049396-fb1d76cd-0c66-4cd6-853b-9e87eca3d950.png)

## Установка
1. Клонируйте репозиторий

```
git clone https://github.com/dnkngh/KittyBot
```

2. Установите и активируйте виртуальное окружение

```
py -m venv venv
source venv/scripts/activate
```

3. Обновите pip

```
python -m pip install --upgrade pip
```

4. Установите python-telegram-bot

```
pip install python telegram-bot
```

5. В папке с файлом ```kittybot.py``` создайте файл ```.env```. Внутри укажите:

```
TOKEN = '<ваш телеграм-токен>'
```

6. Запустите бота

```
python kittybot.py
```

7. Для начала работы с ботом отправьте ему ```/start``` в telegram. 
