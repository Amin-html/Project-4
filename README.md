# 🎮 GameShop

Магазин игр — Проект 4 из 10.

## Стек
- Python 3.13 + Django 5.2
- **PostgreSQL** (первый проект на реальной БД!)
- Docker + Docker Compose

## Функционал
- 🎮 Каталог игр с фото
- 🏷️ Фильтр по жанрам — Action, RPG, Strategy, Sports
- 💻 Фильтр по платформам — PC, PS5, Xbox
- 🔍 Поиск по названию
- 🛒 Корзина
- ✅ Оформление заказа
- 📦 История заказов
- 🔐 Регистрация и вход

## Запуск

```bash
git clone https://github.com/Amin-html/Project-4.git
cd Project-4
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Открой: `http://127.0.0.1:8000`