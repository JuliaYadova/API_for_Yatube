# Api_for_Yatube
Проект родолжение проекта yatube. В данной части рассмотрена настройка API в отрыве от Web.
## Описание
API позволяет: просматривать список постов, создавать новые посты, оставлять комментарии к постам, удалять и редактировать посты и комментарии, добавлять авторов в избранное.
Для аутентификации используются JWT-токены.
## Технологии:
* Python 3.8
* Django 2.2.16
* Djoser
*  *В dev-режиме используется SQLite3*
## Запуск проекта в dev-режиме:
- Cоздать и активировать виртуальное окружение:
*В зависимости от типа системы запрос может быть изменен - python3/python/py, используйте соответсвующее наименование далее по тексту по умолчанию стоит python команды для системы Windows.*

```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```
### Документация
Полная документация после запуска сервера доступна по адресу:
```
   /redoc/
```
### Авторы:
Юлия Ядова
