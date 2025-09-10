from sqlmodel import SQLModel, Session, create_engine, select
from .models import Offer
from datetime import date

DATABASE_URL = "sqlite:///./offers.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Создает таблицы и добавляет тестовые данные, если их нет"""
    # Создаём таблицы
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # Проверяем, есть ли данные в таблице Offer
        offer_exists = session.exec(select(Offer)).first()
        if not offer_exists:
            # Тестовые данные
            sample_offers = [
                Offer(
                    title="Скидка на кофе",
                    category="Еда",
                    city="Москва",
                    price=150,
                    discount=20,
                    popularity=5,
                    start_date=date.today(),
                    end_date=date.today()
                ),
                Offer(
                    title="Йога для начинающих",
                    category="Спорт",
                    city="Санкт-Петербург",
                    price=1000,
                    discount=50,
                    popularity=10,
                    start_date=date.today(),
                    end_date=date.today()
                )
            ]
            session.add_all(sample_offers)
            session.commit()
            print("Тестовые данные добавлены!")

def get_session():
    """Генератор сессии для Depends() в FastAPI"""
    with Session(engine) as session:
        yield session
