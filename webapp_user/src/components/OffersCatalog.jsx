import { useEffect, useState } from "react";
import axios from "axios";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

function OffersCatalog() {
  const [offers, setOffers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOffers = async () => {
      try {
        const response = await axios.get(`${BACKEND_URL}/offers/`);
        setOffers(response.data);
      } catch (err) {
        setError("Ошибка при загрузке акций");
      } finally {
        setLoading(false);
      }
    };

    fetchOffers();
  }, []);

  if (loading) return <p>Загрузка...</p>;
  if (error) return <p>{error}</p>;
  if (offers.length === 0) return <p>Акций пока нет.</p>;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
      {offers.map((offer) => (
        <div key={offer.id} style={{ border: "1px solid #ccc", padding: "12px", borderRadius: "8px" }}>
          <h3>{offer.title}</h3>
          <p>Категория: {offer.category}</p>
          <p>Город: {offer.city}</p>
          <p>Цена: {offer.price} ₽</p>
          <p>Скидка: {offer.discount}%</p>
          <p>Популярность: {offer.popularity}</p>
          <p>
            {new Date(offer.start_date).toLocaleDateString()} — {new Date(offer.end_date).toLocaleDateString()}
          </p>
        </div>
      ))}
    </div>
  );
}

export default OffersCatalog;
