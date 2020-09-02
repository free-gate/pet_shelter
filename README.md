# pet_shelter
Веб-приложение для управления базой данных животных приюта


* API приложение на основе Django REST Framework предназначено для получения списка всех животных приюта, редактрирования, мягкого удаления, данные возвращает в json-формате

* Совместима с ОС windows,  и версией python 3.7.0. (на остальных системах не проверялась)
Приложение работает с базой данных PostgreSQL.
Для безопасной работы необходимо создать переменные окружения:

```
DJANGO_SECRET_KEY
DJANGO_DEBUG
POSTGRES_NAME
POSTGRES_USER
POSTGRES_PASS
```
* Шаги по установке, сборке, запуску:
   ```
   pip install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```