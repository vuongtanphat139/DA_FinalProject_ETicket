/* eslint-disable no-unused-vars */
import React from "react";
import { InputNumber } from "antd";
import { Button, Popconfirm } from "antd";

import styles from "./BuyTicket.module.css";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";

const BuyTicket = () => {
  const [tickets, setTickets] = useState([]);
  const [selectedQuantities, setSelectedQuantities] = useState({});
  const [totalPrice, setTotalPrice] = useState(0);
  const [events, setEvents] = useState([]);

  const [customerName, setCustomerName] = useState("");
  const [items, setItems] = useState([]);

  const [ticketData, setTicketData] = useState({
    event_id: "",
    ticket_type: "",
    ticket_price: 0,
    total_quantity: 0,
    available_quantity: 0,
  });

  const fetchTickets = () => {
    fetch("http://127.0.0.1:5001/tickets")
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data.tickets)) {
          setTickets(data.tickets);
        } else {
          console.error('Invalid data format: expected "tickets" array.');
        }
      })
      .catch((error) => {
        console.error("Error fetching tickets:", error);
        console.log();
      });
  };

  const fetchTicketsByEvent = () => {
    // fetch(`http://127.0.0.1:5001/tickets_by_event/${event_id}`)
    fetch(`http://127.0.0.1:5001/tickets_by_event/1`)
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data.tickets)) {
          setTickets(data.tickets);
        } else {
          console.error('Invalid data format: expected "tickets" array.');
        }
      })
      .catch((error) => {
        console.error("Error fetching tickets:", error);
        console.log();
      });
  };

  const fetchTicketById = async (ticketId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5001/tickets/${ticketId}`);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      if (data && data.ticket) {
        setTicketData(data.ticket);
        console.log("TICKET DATA NOW IS: ", data.ticket);
        return data.ticket;
      } else {
        console.error('Invalid data format: expected "ticket" object.');
      }
    } catch (error) {
      console.error("Error fetching ticket:", error);
    }
  };

  const fetchEvents = (event) => {
    fetch("http://127.0.0.1:5001/get_events")
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data.events)) {
          setEvents(data.events);
        } else {
          console.error('Invalid data format: expected "events" array.');
        }
      })
      .catch((error) => {
        console.error("Error fetching events:", error);
      });
  };

  const handleAddTicket = (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:5001/add_ticket", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(ticketData),
    })
      .then((response) => {
        if (response.ok) {
          fetchTickets();
          setTicketData({
            event_id: 0,
            ticket_type: "",
            ticket_price: 0,
            total_quantity: 0,
            available_quantity: 0,
          });
        } else {
          console.error("Failed to add ticket");
        }
      })
      .catch((error) => {
        console.error("Error adding ticket:", error);
      });
  };

  // const updateTicket = (ticketId) => {
  //     //event.preventDefault();
  //     console.log("Update ticket: ", ticketId)

  //     fetch(`http://127.0.0.1:5001/tickets/${ticketId}`, {
  //         method: 'PUT',
  //         headers: {
  //             'Content-Type': 'application/json'
  //         },
  //         body: JSON.stringify(ticketData)
  //     })
  //     .then(response => {
  //         if (response.ok) {
  //             fetchTickets();
  //             setTicketData({
  //                 event_id: 0,
  //                 ticket_type: '',
  //                 ticket_price: 0,
  //                 total_quantity: 0,
  //                 available_quantity: 0
  //             });
  //         } else {
  //             console.error('Failed to update ticket');
  //         }
  //     })
  //     .catch(error => {
  //         console.error('Error updating ticket:', error);
  //     });    };

  const updateTicket = async (ticketId, ticket) => {
    try {
      console.log("Update ticket: ", ticketId);

      const response = await fetch(
        `http://127.0.0.1:5001/tickets/${ticketId}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(ticket),
        }
      );

      // if (response.ok) {
      //     fetchTickets();
      //     setTicketData({
      //         event_id: 0,
      //         ticket_type: '',
      //         ticket_price: 0,
      //         total_quantity: 0,
      //         available_quantity: 0
      //     });
      // } else {
      //     console.error('Failed to update ticket');
      // }
    } catch (error) {
      console.error("Error updating ticket:", error);
    }
  };

  const deleteTicket = (ticketId) => {
    fetch(`http://127.0.0.1:5001/delete_ticket/${ticketId}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          fetchTickets();
        } else {
          console.error("Failed to delete ticket");
        }
      })
      .catch((error) => {
        console.error("Error deleting ticket:", error);
      });
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  useEffect(() => {
    fetchTicketsByEvent();
  }, []);

  const onQuantityChange = (ticketId, value, tickets) => {
    setSelectedQuantities((prevState) => {
      // Update the selected quantities
      const updatedState = {
        ...prevState,
        [ticketId]: value,
      };

      // Calculate total price using the updated selected quantities
      setTotalPrice(calculateTotalPrice(updatedState, tickets));

      // Return the updated state
      return updatedState;
    });
  };

  const calculateTotalPrice = (selectedQuantities, tickets) => {
    let totalPrice = 0;
    tickets.forEach((ticket) => {
      const quantity = selectedQuantities[ticket.ticket_id] || 0;
      totalPrice += quantity * ticket.ticket_price;
    });
    return totalPrice;
  };

  const renderTickets = (tickets) => {
    return tickets.map((ticket) => (
      <tr key={ticket.ticket_id}>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          {ticket.ticket_type}
        </td>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          {ticket.ticket_price}
        </td>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          {ticket.available_quantity}
        </td>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          <InputNumber
            className="text-center"
            size="large"
            min={0}
            max={100}
            defaultValue={0}
            onChange={(value) =>
              onQuantityChange(ticket.ticket_id, value, tickets)
            }
          />
        </td>
      </tr>
    ));
  };

  const renderInfo = (tickets) => {
    return tickets.map((ticket) => (
      <tr key={ticket.ticket_id}>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          {ticket.ticket_type}
        </td>
        <td className="text-center px-6 py-4 whitespace-nowrap">
          {ticket.ticket_price}
        </td>
      </tr>
    ));
  };

  const handleContinueClick = async () => {
    // Lọc các vé đã được chọn (số lượng lớn hơn 0)
    const selectedTickets = Object.keys(selectedQuantities).filter(
      (ticketId) => selectedQuantities[ticketId] > 0
    );

    // Nếu không có vé nào được chọn, hiển thị thông báo lỗi và dừng hàm
    if (selectedTickets.length === 0) {
      console.error("Please select at least one ticket.");
      return;
    }

    // Duyệt qua các vé đã chọn để cập nhật dữ liệu và gọi hàm updateTicket
    for (const ticketId of selectedTickets) {
      const ticket = tickets.find(
        (ticket) => ticket.ticket_id === parseInt(ticketId)
      );
      const quantity = selectedQuantities[ticketId];

      try {
        const response = await fetchTicketById(ticketId);
        console.log("TICKET DATA IN RESPONSE IS: ", response);
        console.log("QUANTITY IS: ", quantity);

        (response.available_quantity = response.available_quantity - quantity),
          // setTicketData({
          //     ...response,
          //     available_quantity: response.available_quantity - quantity,
          // });
          // Gọi hàm updateTicket với dữ liệu được cập nhật
          await updateTicket(ticketId, response);
        // renderTickets(tickets);
      } catch (error) {
        console.error("Error fetching ticket:", error);
      }
    }

    /////////////////////////////////////////////// BUG: xong phần update số lượng available & get ticket by event, xong phần logic chặn chuyển trang khi chưa chọn, và nút return ở trang payment, rồi đến hàm update trạng thái đơn hàng khi nhấn thanh toán, rồi đến chức năng tiếp theo. ////////////////////////////////////////////////////////
    ////////////// Chưa  xử lý flow return từ payment về BuyTicket, không có xoá order và tăng lại số lượng vé
    // Đã fix bug id của order thay đổi mỗi lần select???
    // DDax fix xong, Đang làm hàm update order, lỗi status rỗng, còn lại ỏke v:
    // Giờ gọi update ở fe
    // Đã viết hàm gọi update ở FE, giờ cần truyền orderId từ BuyTicket sang Payment và dùng hàm ở nút pay

    // Tạo danh sách các mục đơn hàng từ các vé đã chọn
    const orderItems = selectedTickets.map((ticketId) => ({
      ticket_id: parseInt(ticketId), // Chuyển đổi ticketId sang kiểu số nguyên
      quantity: selectedQuantities[ticketId], // Lấy số lượng vé đã chọn
      price: tickets.find((ticket) => ticket.ticket_id === parseInt(ticketId))
        .ticket_price, // Tìm và lấy giá vé tương ứng
    }));

    // Tạo dữ liệu đơn hàng bao gồm tên khách hàng, các mục đơn hàng, tổng giá và trạng thái
    const orderData = {
      customer_name: "temp customer", //customerName, // Tên khách hàng
      items: orderItems, // Danh sách các mục đơn hàng
      total_price: totalPrice,
      status: "", // mặc định trong csdl là pending
    };

    // Ghi log dữ liệu đơn hàng để kiểm tra
    console.log("Order Data:", JSON.stringify(orderData));

    // Gửi yêu cầu POST đến URL chỉ định với dữ liệu đơn hàng
    fetch("http://127.0.0.1:5001/orders", {
      method: "POST", // Phương thức HTTP
      headers: {
        "Content-Type": "application/json", // Định dạng dữ liệu là JSON
      },
      body: JSON.stringify(orderData), // Chuyển dữ liệu đơn hàng sang chuỗi JSON
    })
      .then((response) => {
        // Nếu phản hồi không thành công (status code không phải 2xx), ném lỗi
        if (!response.ok) {
          return response.json().then((errorInfo) => {
            throw new Error(`Failed to add order: ${errorInfo.message}`);
          });
        }
        // Chuyển đổi phản hồi thành JSON
        return response.json();
      })
      .then((data) => {
        // Ghi log đơn hàng đã được tạo thành công
        console.log("Order created:", data.order);
        // Đặt lại số lượng vé đã chọn
        setSelectedQuantities({});
        // Đặt lại tổng giá trị đơn hàng
        setTotalPrice(0);
        const order_id = data.order.order_id;
        // window.location.href = `/Payment/${event_id}`;
        window.location.href = `/Payment/${order_id}`;
      })
      .catch((error) => {
        // Ghi log lỗi nếu có lỗi xảy ra
        console.error("Error creating order:", error);
      });
  };

  return (
    <>
      <div class={styles.main}>
        <div class={styles.insidebox}>
          <h1>Choose ticket</h1>
          <br />
          <table>
            <thead>
              <tr>
                <th>Ticket Type</th>
                <th>Price</th>
                <th>Available</th>
                <th>Quantity</th>
              </tr>
            </thead>
            <tbody
              id="ticketList"
              className="bg-white divide-y divide-gray-200"
            >
              {renderTickets(tickets)}
            </tbody>
          </table>
        </div>
        <div class={styles.insidebox}>
          <h1>Infomation</h1>
          <br />
          <div>{events[0]?.name}</div>
          <div>{events[0]?.datetime}</div>
          <div>{events[0]?.venue}</div>
          <br />
          <div>
            <table>
              <thead>
                <tr>
                  <th>Ticket Type</th>
                  <th>Price</th>
                </tr>
              </thead>
              <tbody>{renderInfo(tickets)}</tbody>
            </table>
          </div>
          <br />
          <div>
            {totalPrice === 0 ? (
              <Popconfirm
                placement="bottom"
                title="Vui lòng chọn ít nhất 1 vé để mua!"
                okText="Oke"
                cancelText=""
              >
                <button
                  class={styles.buy_btn}
                  className="flex w-full items-center justify-center rounded-lg bg-[#00A198] px-5 py-2.5 text-sm font-medium text-white hover:bg-[#009289] focus:outline-none focus:ring-4 focus:ring-primary-300"
                  onClick={handleContinueClick}
                >
                  Continue - {totalPrice} VND
                </button>
              </Popconfirm>
            ) : (
              <button
                class={styles.buy_btn}
                className="flex w-full items-center justify-center rounded-lg bg-[#00A198] px-5 py-2.5 text-sm font-medium text-white hover:bg-[#009289] focus:outline-none focus:ring-4 focus:ring-primary-300"
                onClick={handleContinueClick}
              >
                Continue - {totalPrice} VND
              </button>
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default BuyTicket;
