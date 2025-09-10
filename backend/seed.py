from datetime import datetime, timedelta
from sqlmodel import Session
from app.database import engine, init_db
from app.models import Offer

# Создаем таблицы, если их нет
init_db()

# Тестовые акции
test_offers = [
    Offer(
        title="Скидка 20% на пиццу",
        city="Москва",
        category="еда",
        price=500,
        discount=20,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=5),
        popularity=50
    ),
    Offer(
        title="Маникюр за полцены",
        city="Санкт-Петербург",
        category="красота",
        price=1000,
        discount=50,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=2),
        popularity=120
    ),
    Offer(
        title="Бесплатный билет в кино",
        city="Москва",
        category="развлечения",
        price=0,
        discount=100,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=7),
        popularity=80
    )
]

# Заполняем базу
with Session(engine) as session:
    for offer in test_offers:
        session.add(offer)
    session.commit()

print("База заполнена тестовыми акциями!")
