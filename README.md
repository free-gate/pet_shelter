# pet_shelter
Веб-приложение для управления базой данных животных приюта


* API приложение на основе Django REST Framework предназначено для получения списка всех животных приюта, редактрирования, мягкого удаления, данные возвращает в json-формате

* Совместима с ОС windows,  и версией python 3.7.0. (на остальных системах не проверялась)
Приложение работает с базой данных PostgreSQL (по умолчанию используется SQLite)
Для безопасной работы необходимо создать переменные окружения:
    ```
    DJANGO_SECRET_KEY (ключ используемый для криптографической подписи)
    DJANGO_DEBUG (на робочем сервере нужно устанавливать значение False)
    POSTGRES_NAME (при использовании PostgreSQL название базы данных)
    POSTGRES_USER (при использовании PostgreSQL имя пользователя базы)
    POSTGRES_PASS (при использовании PostgreSQL пароль пользователя базы)
    ```
* Шаги по установке, сборке, запуску:  
  1. Необходимо установить Postgres на ваш рабочий компьютер
  2. создать базу данных со следующими параметрами:
  ```
  NAME: pet_shelter
  USER: pet_shelter
  PASSWORD: 123qweQWE
  HOST: 127.0.0.1
  PORT: 5432
  ```
   или ввести свои параметры, но тогда необходимо или создать переменные окружения, которые относятся к базе данных (указанные выше) или менять настройки pet_shelter/pet_shelter/setting.py 
  ```
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser # Create a superuser
  python manage.py runserver
  ```
  