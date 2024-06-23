import React from 'react'
import styles from "./Promotion.module.css";

import { useEffect, useState } from 'react';
import axios from "axios";

// Mock data sự kiện
// const events = [
//     {
//       id: 1,
//       title: "Hội chợ du lịch 2024",
//       date: "2024-07-15",
//       location: "Hà Nội",
//       description: "Hội chợ du lịch quốc tế tại Hà Nội, diễn ra từ ngày 15/07 đến 18/07."
//     },
//     {
//       id: 2,
//       title: "Triển lãm công nghệ mới",
//       date: "2024-08-20",
//       location: "TP.HCM",
//       description: "Triển lãm giới thiệu công nghệ mới nhất tại TP.HCM, diễn ra vào tháng 8."
//     },
//     // Thêm các sự kiện khác nếu cần
//   ];
  
  
//   // Promotion Component
//   const Promotion = ({ event }) => {
//     const { title, date, location, description } = event;
  
//     return (
//       <div className={styles.event}>
//         <h2 className={styles.title}>{title}</h2>
//         <p className={styles.date}>{date}</p>
//         <p className={styles.location}>{location}</p>
//         <p className={styles.description}>{description}</p>
//       </div>
//     );
//   };
  
//   // EventListPage Component
//   const EventListPage = () => {
//     return (
//       <div className={styles.eventList}>
//         <h1>Danh sách các sự kiện hiện có</h1>
//         {events.map(event => (
//           <Promotion key={event.id} event={event} />
//         ))}
//       </div>
//     );
//   };
  
//   export default EventListPage;

const Promotion = () => {
  const [promotions, setPromotions] = useState([]);

  useEffect(() => {
      const fetchPromotions = async () => {
          try {
              const response = await axios.get('http://127.0.0.1:5000/promotions');
              setPromotions(response.data);
          } catch (error) {
              console.error('Error fetching promotions:', error);
          }
      };

      fetchPromotions();
  }, []);

  return (
      <div className={styles.promotionList}>
          {promotions.map(promo => (
              <div key={promo.promotion_id} className={styles.promotionItem}>
                  <div className={styles.promotionDescription}>{promo.description}</div>
                  <div className={styles.promotionDiscount}>Discount: {promo.discount.toLocaleString()} VND</div>
                  <div className={styles.promotionEvent}>Event: {promo.event_id} </div>
              </div>
          ))}
      </div>
  );
};

export default Promotion;