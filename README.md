### Веб-сервис без использования БД
#### 1. Установка зависимостей
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
#### 2. Миграции
```bash
python3 manage.py makemigrations
python3 manage.py migrate                 
```
#### 3. Запуск проекта
```bash
python3 manage.py runserver                         
```
#### 4. Работа с проектом
```bash
open Postman
```
```text
GET: http://127.0.0.1:8000/ ===> просмотр всех созданных объектов

GET: http://127.0.0.1:8000/version/<ID созданного объекта>/ ===> просмотр одного созданного объекта

POST: http://127.0.0.1:8000/ ===> создание объекта
    BODY:
        form-data:
                 KEY:       | VALUE: 
                 software   | <Введите Ваше зачение>
                 version    | <Введите Ваше зачение>
                 

POST: http://127.0.0.1:8000/correct/<ID созданного объекта>/ ===> изменение созданного объекта по ID
    BODY:
        form-data:
                 KEY:       | VALUE: 
                 software   | <Введите Ваше зачение>
                 version    | <Введите Ваше зачение>
                 
POST: http://127.0.0.1:8000/delete/<ID созданного объекта>/ ===> удаление созданного объекта по ID
```