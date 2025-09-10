from sqlmodel import Session, select
from .models import Offer, OfferCreate

def create_offer(session: Session, data: OfferCreate) -> Offer:
    offer = Offer.from_orm(data)
    session.add(offer)
    session.commit()
    session.refresh(offer)
    return offer

def get_offer(session: Session, offer_id: int):
    return session.get(Offer, offer_id)

def list_offers(session: Session):
    return session.exec(select(Offer)).all()
