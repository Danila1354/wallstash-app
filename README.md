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

## 🚀 Установка

### Требования

- Python 3.11+
- PostgreSQL 15+

### Быстрый старт

1. **Клонировать репозиторий**
```bash
git clone https://github.com/yourusername/wallstash.git
cd wallstash-app/backend-django/wallstash
```

2. **Создать виртуальное окружение и установить зависимости**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Создать базу данных PostgreSQL**
```sql
CREATE DATABASE wallstash;
CREATE USER wallstash_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE wallstash TO wallstash_user;
```

4. **Настроить переменные окружения**

Создайте файл `.env` в папке backend-django/wallstash:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=wallstash
DB_USER=wallstash_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. **Применить миграции и создать суперпользователя**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Запустить сервер**
```bash
python manage.py runserver
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
