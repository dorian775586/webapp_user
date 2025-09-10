import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";
import axios from "axios";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;


function App() {
  const [offers, setOffers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${BACKEND_URL}/offers/`)
      .then(res => {
        setOffers(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Загрузка акций...</div>;

  if (offers.length === 0) return <div>Акций пока нет</div>;

  return (
    <div style={{ maxWidth: 600, margin: "20px auto", fontFamily: "Arial" }}>
      <h1>Каталог акций</h1>
      {offers.map(o => (
        <div key={o.id} style={{ border: "1px solid #ccc", padding: 10, marginBottom: 10 }}>
          <h2>{o.title}</h2>
          <p>Категория: {o.category}</p>
          <p>Город: {o.city}</p>
          <p>Скидка: {o.discount}%</p>
          <p>Цена: {o.price} ₽</p>
          <p>Популярность: {o.popularity}</p>
        </div>
      ))}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
