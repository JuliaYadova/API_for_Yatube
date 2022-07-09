# Api_for_Yatube
Проект родолжение проекта yatube. В данной части рассмотрена настройка API в отрыве от Web.
## Описание

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
