
import React from 'react'
import { InputNumber } from 'antd';
import styles from "./BuyTicket.module.css";

const onChange = (value) => {
    console.log('changed', value);
    // Hàm tính tiền ở đây
  };
///////////////////////////////// Đang bug ở chỗ file jsx không dùng được script giống index.html
const BuyTicket = () => {
  return (
    <>
    <div class = {styles.main} >
        
        <div class = {styles.insidebox}>
        Choose ticket
            <table>
                <thead>
                    <tr>
                        <th>Ticket Type</th>
                        <th>Price</th>
                        <th>Available</th>
                        <th>Quantity</th>
                    </tr>
                </thead>
                <tbody id="ticketList">
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>
                       <InputNumber size="large" min={1} max={100} defaultValue={3} onChange={onChange} />
                    </td>
                </tbody>
                <tbody id="ticketList">
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>
                        <input type="text" />
                    </td>

                </tbody>
                <tbody id="ticketList">
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>
                        <input type="text" />
                    </td>

                </tbody>
                <tbody id="ticketList">
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>aaaaaaaaaa</td>
                    <td>
                        <input type="text" />
                    </td>

                </tbody>
            </table>
        </div>
        <div class = {styles.insidebox}>
        Infomation
            <div>[HCM] Hà Trần: Thiên Hà Tinh Khôi</div>
            <div>19:00, 10 tháng 8, 2024</div>
            <div>Nhà thi đấu Quân Khu 7</div>
            <div>Giá vé
                <table>
                    <thead>
                        <tr>
                            <th>Ticket Type</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody id="ticketList">
                        <td>aaaaaaaaaa</td>
                        <td>aaaaaaaaaa</td>
                    </tbody>
                    <tbody id="ticketList">
                        <td>aaaaaaaaaa</td>
                        <td>aaaaaaaaaa</td>
                    </tbody>
                    <tbody id="ticketList">
                        <td>aaaaaaaaaa</td>
                        <td>aaaaaaaaaa</td>
                    </tbody>
                </table>
            </div>
            <div>
                <button class = {styles.buy_btn}>Continue - 9.600.000 VND </button>
            </div>

        </div>

    </div>

    
    </>
  );
};

export default BuyTicket;
