from sqlmodel import SQLModel, Field
from datetime import date

class Offer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    category: str
    city: str
    price: float
    discount: float
    popularity: int
    start_date: date
    end_date: date
