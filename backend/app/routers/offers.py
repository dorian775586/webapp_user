from fastapi import APIRouter, Query, Depends
from typing import Optional, List
from sqlmodel import select, Session
from app.database import get_session
from app.models import Offer

router = APIRouter()

@router.get("/", response_model=List[Offer])
def get_offers(
    city: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    sort: Optional[str] = Query("new"),
    session: Session = Depends(get_session)
):
    query = select(Offer)
    if city:
        query = query.where(Offer.city.ilike(f"%{city}%"))
    if category:
        query = query.where(Offer.category.ilike(f"%{category}%"))

    offers = session.exec(query).all()

    if sort == "new":
        offers.sort(key=lambda x: x.start_date, reverse=True)
    elif sort == "popular":
        offers.sort(key=lambda x: x.popularity, reverse=True)
    elif sort == "ending":
        offers.sort(key=lambda x: x.end_date)

    return offers
