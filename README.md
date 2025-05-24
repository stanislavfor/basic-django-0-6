![](assets/_logo_django_.jpg)
# Фреймворк Django (семинары)
# Урок 6. Развёртывание проекта
## Описание
На этом семинаре мы:
- поработаем с профилированием Django;
- научимся развёртывать проект на сервере.

<br><hr>
## Домашнее задание
Уважаемые студенты! Обращаем ваше внимание, что сдавать домашнее задание необходимо через Git. <br>
Задание: <br>
Настроить работу проекта на сервере.
<br><hr>
## Решение задания

<br><br>
### 1. Подготовка

- Создать аккаунт на PythonAnywhere:
   - Перейти на [pythonanywhere.com](https://www.pythonanywhere.com)
   - Нажать "Pricing & signup" -> выбрать бесплатный аккаунт "Beginner"
   - Зарегистрироваться, можно через email или используя аккаунт GitHub/Google

- Подготовить свой Django-проект:
   - Убедиться, что проект работает и открывается на локальном сервере (на локальном компьютере)
   - В settings.py добавить 'pythonanywhere.com' в ALLOWED_HOSTS как, например, `ALLOWED_HOSTS = ['your_login.pythonanywhere.com']`.
   - Создать файл requirements.txt с зависимостями (pip freeze > requirements.txt) 
     или выполнить команду для [библиотеки pigar](#pigar) 

### 2. Загрузка проекта на PythonAnywhere

- Загрузить файлы проекта:
   - В панели PythonAnywhere выбрать вкладку "Files"
   - Нажать "Upload a file" и загрузить:
      - Django-проект (всю папку проекта)
      - Файл requirements.txt
или 
     
- Клонировать репозиторий с GitHub.
    - Введите команду для клонирования репозитория:
      ```bash
      git clone https://github.com/stanislavfor/basic-django-0-6.git
      ```
    - Это создаст папку `basic-django-0-6` в домашнем каталоге на PythonAnywhere.


- Создать виртуальное окружение (рекомендуется):
   - Открыть вкладку "Consoles" -> "Bash console"
   - Перейти в папку проекта:
   ```bash
      cd basic-django-0-6
   ```
   - Выполнить:
    ```bash
        mkvirtualenv myenv --python=/usr/bin/python3.10
        workon myenv
    ```

- Проверить, установлен ли Django в виртуальном окружении, с помощью команды:

```bash
  pip list
```

- Установить Django, если Django не установлен, установить его с помощью pip:

```bash
  pip install django
```

- Проверить установку Django. Эта команда должна вывести версию Django, если он установлен правильно:

```bash
  python -m django --version
```
- Проверить список установленных пакетов:
```
  pip list
```

- Установить библиотеку Pillow:
 ```
    python -m pip install Pillow
 ```

- Создать файл requirements.txt
```bash
  touch requirements.txt
```

- Установить зависимости:
   - В той же консоли выполнить:
```bash
     pip install -r requirements.txt
```

### 3. Настройка веб-приложения

- Создать веб-приложение:
   - Перейти на вкладку "Web"
   - Нажать "Add a new web app"
   - Выбрать "Manual configuration" (не Django)
   - Выбрать Python версию, совместимую с проектом (например, 3.10)

- Настроить WSGI-файл:
   - В разделе "Code" нажать на ссылку WSGI configuration file
   - Удалить всё содержимое и заменить на:
```  
    import os
    import sys
    
    # Add the project directory to the sys.path
    path = '/home/stass/basic-django-0-6'
    if path not in sys.path:
        sys.path.append(path)
    
    # Set the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
    
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

```
   - Сохранить файл, нажав комбинацию **Ctrl+S** или кнопку Save.

- Настроить статические файлы:
   - В разделе "Static files" добавить:
      - URL: /static/
      - Путь: например, `shop_project/shop/static`

### 4. Настройка базы данных

- Инициализировать БД:
   - На вкладке "Databases" создать новую SQLite базу данных
   - Запомнить имя (название) базы данных, имя пользователя и пароль

- Обновить настройки Django:
   - В settings.py изменить DATABASES на:
```    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'shop_project', 'databases', 'db.sqlite3'),
        }
    }
```

- Применить миграции:
   - В консоли Bash выполнить:
```bash
     workon myenv  # если используется virtualenv     
```

- Перейдите в папку `shop_project`.
    - В консоли Bash на PythonAnywhere перейти в папку `shop_project`:
      ```bash
        cd /home/ваш_логин/basic-django-0-6/shop_project
      ```

    - Примените миграции.
        - Выполнить команду для применения миграций:
          ```bash
            python manage.py migrate
          ```
        - Это создаст все необходимые таблицы в базе данных `db.sqlite3`.
        - Проверить, что файл `db.sqlite3` существует в папке `shop_project/databases/`.
      

### 5. Завершение настройки

- Создать суперпользователя, если нужно:
```bash
   python manage.py createsuperuser
```

- Настроить файл `settings.py`.
    - Проверить, что настройки статических файлов выглядят следующим образом:
      ```
          STATIC_URL = '/static/'
          STATIC_ROOT = os.path.join(BASE_DIR, 'static')
      ```
    - Заменить строку определения `BASE_DIR` на следующую:
     ```
        BASE_DIR = Path(__file__).resolve().parent.parent
     ```

- Собрать статические файлы:
```bash
   python manage.py collectstatic
```

- Перезагрузить приложение:
   - На вкладке "Web" нажать кнопку "Reload"

- Проверить сайт:
   - На вкладке "Web" найти ссылку вида your_username.pythonanywhere.com
   - Перейти по возможной ссылке, где сайт должен быть доступен


### 6. Запуск проекта на сервере

Перейти по адресу интернета: https://stass.pythonanywhere.com/

<br><br>
### 7. Дополнительные настройки (при необходимости)

- Настройка домена (но, для бесплатного аккаунта только поддомен pythonanywhere):
   - В разделе "Web" → "Domains" можно добавить свой домен для платных аккаунтов

- Планировщик задач (cron):
   - На вкладке "Tasks" можно настроить регулярные задачи

- Доступ по SSH:
   - На вкладке "Consoles" можно открыть SSH-консоль для управления сервером

<br><br>
### Запуск проекта на localhost:8000

- Скачать архив с проектом;
- Перейти в директорию проекта 'shop_project';
- Запустить команду ```python manage.py runserver```;
- Открыть в браузере страницу с адресом http://127.0.0.1:8000/;
- По окончанию работы с проектом, отключить комбинацией клавиш 'Ctrl+C'.

<br><br>
### Маршрутизация в браузере на localhost:8000

- Страница admin-панели http://localhost:8000/admin/
  <br><br>
- Главная страница проекта http://127.0.0.1:8000/
- Список всех клиентов http://127.0.0.1:8000/clients/
- Список всех продуктов http://127.0.0.1:8000/products/
- Список всех заказов http://127.0.0.1:8000/orders/
  <br><br>
- Информация о конкретном клиенте http://127.0.0.1:8000/clients/1/, где ```http://127.0.0.1:8000/clients/{ID_клиента}/```
- Информация о конкретном товаре http://127.0.0.1:8000/products/1/, где ```http://127.0.0.1:8000/products/{ID_товара}/```
- Информация о конкретном заказе http://127.0.0.1:8000/orders/1/, где ```http://127.0.0.1:8000/orders/{ID_заказа}/```
  <br><br>
- Страница редактирования конкретного заказа http://127.0.0.1:8000/edit-order/1/, где ```http://127.0.0.1:8000/edit-order/{ID_заказа}/```
- Страница добавления нового клиента http://127.0.0.1:8000/add-client/
- Страница добавления нового товара http://localhost:8000/add-product/
- Страница добавления нового заказа http://localhost:8000/add-order/
- Страница редактирования профиля http://localhost:8000/update-profile/
  <br><br>
- Список всех заказов клиента http://127.0.0.1:8000/clients-orders/
- Список всех личных заказов http://127.0.0.1:8000/client-orders/


<br><hr>
## Инструкция

<br><br>
### Бесплатный аккаунт на PythonAnywhere

<br><br>
Бесплатный аккаунт на [PythonAnywhere](https://www.pythonanywhere.com/) идеально подходит для обучения, <br>
но не годится для постоянного хостинга production-проектов.
Бесплатный аккаунт имеет ограничения: <br>
- Доступ по HTTP (без HTTPS).
- Ограниченное время работы веб-приложения.
- Ограниченные ресурсы CPU и трафика.
- PythonAnywhere блокирует SMTP по умолчанию. Для работы с почтой нужно запросить разблокировку или использовать внешние SMTP-серверы.

##### Ограничения бесплатного аккаунта на PythonAnywhere

1. Время работы веб-приложения:
    - Бесплатный аккаунт *активен 3 месяца* с момента регистрации
    - После этого срок действия аккаунта истекает, и сайт перестает быть доступен
    - Чтобы продлить, нужно зайти в аккаунт и нажать "Extend" (можно продлевать бесплатно)

2. Ежемесячное обновление:
    - Даже в течение этих 3 месяцев нужно *раз в месяц* заходить в аккаунт и явно продлевать его (кнопка "Extend")
    - Если не продлить в течение месяца - сайт временно отключается до следующего продления

3. Ограничения CPU и трафика:
    - *100 секунд CPU времени в день* для веб-приложения
    - При превышении лимита сайт временно блокируется до следующего дня
    - *512 МБ дискового пространства*

4. Другие важные ограничения:
    - Максимум *1 веб-приложение*
    - Доступ только по HTTP (без HTTPS)
    - Невозможно принимать входящие HTTP-запросы (только исходящие)
    - SMTP-порт заблокирован (нельзя отправлять email через стандартные порты)

5. При исчерпании CPU-лимита:
    - Сайт возвращает *502 ошибку* до сброса счетчика (в 00:00 UTC)
    - Аккаунт не блокируется, только временно недоступен веб-интерфейс

6. При неактивности аккаунта:
    - Если не заходить в аккаунт *90 дней* - он может быть удален
    - Все файлы и данные будут потеряны

7. При нарушении правил сервиса:
    - PythonAnywhere может полностью заблокировать аккаунт за:
        - Попытки обхода ограничений
        - Рассылку спама
        - Хостинг запрещенного контента

<br><br>
### Рекомендации для учебного проекта на PythonAnywhere

1. Регулярно продлевать аккаунт:
    - Заходить хотя бы раз в месяц и нажимать "Extend"

2. Сохранять резервные копии:
    - Регулярно скачивать свой проект через "Files" → "Download"

3. Для долгосрочных проектов:
    - Рассмотреть переход на платный аккаунт ($5/месяц), что снимает большинство ограничений
    - Или перенести проект на другой хостинг после обучения

4. Мониторить использование CPU:
    - На вкладке "Web" есть график использования CPU
    - Оптимизировать код, если есть исчерпание лимита

<br><hr>
## Дополнительная информация

<br><br>
### Профилирование Django

Профилирование - это процесс анализа скорости выполнения операций и определения узких мест в коде. <br> 
**Основные методы и инструменты для профилирования приложений Django**:

##### 1.Использование команды `runserver` с параметром `--nothread` 
Запуск сервера разработчика с отключением многопоточности помогает выявить проблемы с производительностью:

```bash
python manage.py runserver --nothreads
```

##### 2.Средства мониторинга запросов SQL
Django автоматически выводит запросы SQL в консоль при включённом режиме DEBUG. <br> 
Нужно включить режим отладки и проверить выполнение SQL-запросов. <br>  
После этого запускайте проект, и все выполняемые SQL-запросы будут выводиться в терминал:

```
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}
```

##### 3. Использование библиотеки django-debug-toolbar
Установить библиотеку `django-debug-toolbar` и добавить её в middleware, чтобы видеть детальную статистику выполнения запросов:

```bash
pip install django-debug-toolbar
```

В `settings.py`:

```
INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ['127.0.0.1']  # Список IP адресов, которым разрешен доступ к debug toolbar
```

Эта библиотека покажет подробную информацию о каждом HTTP-запросе, включая используемые шаблоны, запросы к БД и временные затраты.

##### 4. Анализ потребления памяти
Использовать инструмент `memory_profiler` для отслеживания расхода оперативной памяти приложением:

```bash
pip install memory-profiler
```

и запустить сервер с профилировщиком:

```bash
python -m memory_profiler manage.py runserver
```


<br><br>
### Развёртывание Django-проекта на сервере

Процесс разворачивания Django-проекта включает ряд шагов подготовки окружения и деплоя на удалённый сервер. <br>
**Ключевые этапы**: <br>
- Подготовка среды для производства;
- Подготовка конфигурации веб-сервера (Apache/Nginx + WSGI-сервер);
- Сборка статики и работа с медиафайлами;
- Обеспечение безопасности приложения.

##### 1. Подготовка среды для производства
- Создать виртуальное окружение и установить необходимые зависимости:

```bash
python -m venv myvenv
source myvenv/Scripts/activate
pip install -r requirements.txt
```

- Подключиться к своему удалённому серверу (например, через SSH), создать каталог для проекта и скопировать туда исходники:

```bash
scp -r /path/to/your/project user@remote_host:/home/user/django_project
```

##### 2. Конфигурация веб-сервера (Apache/Nginx + WSGI-сервер)

Наиболее распространённым решением для продакшена является использование Nginx в качестве обратного прокси перед WSGI-сервером типа Gunicorn или uWSGI.

- Установка и настройка Nginx:

```bash
sudo apt-get update && sudo apt-get install nginx
```

- Отредактировать конфигурационный файл для домена:

```bash
sudo nano /etc/nginx/sites-enabled/myproject.conf
```

- Добавить следующее содержимое:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location /static/ {
        alias /path/to/static/files/;
    }

    location /media/ {
        alias /path/to/media/files/;
    }

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

- Перезагрузить Nginx:

```bash
sudo systemctl restart nginx
```

##### Запуск Django с использованием Gunicorn:

- Установить Gunicorn и запустить его в терминале:

```bash
pip install gunicorn
gunicorn --bind localhost:8000 project.wsgi:application
```

или добавить скрипт запуска в службу Linux:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

- Добавить содержание:

```ini
[Unit]
Description=Gunicorn service
After=network.target

[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/django_project
ExecStart=/home/user/myvenv/bin/gunicorn --workers 3 --bind unix:/home/user/django_project/myproject.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```

- Активировать и запустить сервис:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

##### 3. Сборка статики и работа с медиафайлами
Перед развёртыванием следует проверить, что сборка статичных ресурсов выполнена правильно:

```bash
python manage.py collectstatic
```

Возможно хранение медиа-ресурсов пользователей через создание отдельного каталога для медийных файлов и настройки их пути в конфигурации:

```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```

##### 4. Безопасность
Проверить безопасность проекта, что отключены ненужные модули и установлен секретный ключ (`SECRET_KEY`):

```
DEBUG = False
ALLOWED_HOSTS = ['example.com', 'www.example.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

<br><br><hr>
<div id="pigar"><h3>Использование для Python библиотеки pigar</h3></div>

*pigar* - это инструмент для анализа зависимостей в Python-проектах, <br>
который помогает находить используемые модули и генерировать файл `requirements.txt`.


##### Установка pigar
```bash
  pip install pigar
```

##### Основные команды для pigar:

1. Анализ зависимостей и генерация requirements.txt (аналог pigar generate), создаст или обновит файл requirements.txt в текущей директории.  
```bash
   pigar
```
   или
```bash
   pigar generate  # Явное указание генерации зависимостей
```
   - pigar generate и pigar без аргументов делают одно и то же - анализируют зависимости и создают requirements.txt.

2. Проверка зависимостей (pigar check), все ли зависимости из кода указаны в requirements.txt:
```bash
   pigar check /путь/к/проекту
```
   - pigar check полезен для проверки расхождений между используемыми и установленными пакетами. 

3. Анализ зависимостей в указанной директории:
```bash
   pigar -p /путь/к/проекту
```
   - Для динамических зависимостей (importlib, pkg_resources) pigar может не обнаружить импорты, что требует проверять requirements.txt вручную.

4. Проверка обновлений для зависимостей, покажет доступные обновления для пакетов из requirements.txt:
```bash
   pigar -u
```
   - После выполнения команд следует проверять сгенерированный файл и при необходимости редактировать его.

5. Генерация requirements.txt с указанием версий, добавит точные версии пакетов:
```bash
   pigar -P
```
  
6. Игнорирование системных пакетов:
```bash
   pigar --ignore /путь/к/виртуальному/окружению
```


##### Дополнительные опции:
- `pigar -s`  анализ зависимостей в одном файле, например, `pigar -s script.py`
- `pigar -v`  вывод версии pigar
- `pigar -h`  справка по командам pigar


<br><br>
### Ключевые различия REST API в Spring (Java) и Django (Python)



| **Критерий**       | **Spring (Java)**                        | **Django (Python)**                 |
|--------------------|------------------------------------------|-------------------------------------|
|                    |                                          |                                     |
| **Фреймворк**      | Spring Boot (+ Spring MVC)               | Django REST Framework (DRF)         |
| **Синтаксис**      | Аннотации (@RestController, @GetMapping) | Декораторы (@api_view, @action)     |
| **Сериализация**   | Jackson (автоматически в JSON)           | Django Serializers (явное описание) |
| **ORM**            | Spring Data JPA (Hibernate)              | Django ORM (встроенная)             |
| **Роутинг**        | Через аннотации (@RequestMapping)        | Через urls.py + ViewSet             |
| **Запуск сервера** | Встроенный Tomcat/Jetty                  | Разработческий сервер (runserver)   |
| **Пример кода**    | java @GetMapping("/books")               | python @api_view(['GET'])           |
|                    |                                          |                                     |

<br><br>
##### Главные отличия:
1. Spring - строгая типизация в Java, Django - динамическая типизация в Python.
2. Spring Boot - присутствует автоконфигурация, Django - требуется настройка, например, настройка сериализаторов.
3. Django ORM проще для быстрого старта, но JPA (Spring) - мощнее для сложных запросов.
4. Spring - лучше для масштабируемых enterprise-решений (в производстве), но Django - быстрее для создания MVP.

##### Выбор фреймворка в зависимости от задачи:
- Java/Spring, если нужна производительность и строгая архитектура.
- Python/Django, если важна скорость разработки и простота.

<br><br><br><br>
<hr><hr><hr><hr>