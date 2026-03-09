# 🖼️ WallStash

Социальная платформа для систематизации и обмена обоями для рабочего стола с функционалом персональных коллекций и социальных взаимодействий.

## ✨ Возможности

- 🔐 Аутентификация с поддержкой входа по username/email
- 👥 Система подписок на пользователей
- 🖼️ Автоматическая генерация превью с кешированием (django-imagekit)
- 🏷️ Система тегов для категоризации и поиска
- ❤️ Лайки и комментарии
- 📚 Персональные коллекции
- 📥 Отслеживание скачиваний
- 🔍 Поиск и фильтрация
- 🤖 Асинхронный парсинг Telegram-каналов с обоями (Celery + RabbitMQ)
## ⚙️ Стек
Проект использует:  
- Django + Django REST Framework
- PostgreSQL
- Celery
- RabbitMQ
- Docker + Docker Compose

Celery используется для фонового парсинга Telegram каналов.
## 🚀 Установка

### Быстрый старт с Docker

1. Клонировать репозиторий
```
git clone https://github.com/Danila1354/wallstash-app.git
cd wallstash-app
```

2. **Создать .env из примера**
```
cd backend-django/wallstash
cp .env.example .env
```  
Отредактируйте .env, указав свои значения.

3. **Запустить Docker Compose**
```
docker compose up -d --build
```
После этого:  
	•	PostgreSQL создаст базу и пользователя автоматически  
	•	Django применит миграции и запустится на http://localhost:8000

4. **Создать суперпользователя**
```env
docker compose exec backend python manage.py createsuperuser
```

5. **Остановка проекта**
```
docker compose down
```

API доступен по адресу `http://localhost:8000/api/v1/`


## 📚 API Endpoints

### Аутентификация
- `POST /api/v1/auth/users/` - Регистрация
- `POST /api/v1/auth/jwt/create` - Создание JWT-токена

### Пользователи
- `GET /api/v1/auth/users/` - Список пользователей
- `GET /api/v1/profile/{id}/` - Профиль пользователя
- `POST /api/v1/profile/{id}/follow/` - Подписаться
- `POST /api/v1/profile/{id}/unfollow/` - Отписаться
- `GET /api/v1/profile/{id}/wallpapers/` - Обои пользователя
- `GET /api/v1/auth/users/me/` - Текущий пользователь

### Обои
- `GET /api/v1/wallpapers/` - Список обоев
- `POST /api/v1/wallpapers/` - Загрузить обои
- `GET /api/v1/wallpapers/{slug}/` - Детали обоев
- `POST /api/v1/wallpapers/{slug}/like/` - Поставить лайк
- `POST /api/v1/wallpapers/{slug}/unlike/` - Убрать лайк
- `GET /api/v1/wallpapers/{slug}/download/` - Скачать обои

### Коллекции
- `GET /api/v1/profile/{user_id}/collections/` - Коллекции пользователя
- `POST /api/v1/profile/{user_id}/collections/` - Создать коллекцию
- `POST /api/v1/profile/{user_id}/collections/add_wallpaper` - Добавить обои в коллекцию
- `POST /api/v1/profile/{user_id}/collections/remove_wallpaper` - УДалить обои из коллекции
### Парсинг обоев с Telegram каналов
- `POST /api/v1/parse-channel/` - Выполнить парсинг
