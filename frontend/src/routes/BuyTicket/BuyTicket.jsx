
import React from 'react'
import { InputNumber } from 'antd';
import styles from "./BuyTicket.module.css";
import { useEffect, useState } from 'react';
import {useSelector} from 'react-redux'


///////////////////////////////// Đang bug ở chỗ file jsx không dùng được script giống index.html
const BuyTicket = () => {
    const [tickets, setTickets] = useState([]);
    const [selectedQuantities, setSelectedQuantities] = useState({});
    const [totalPrice, setTotalPrice] = useState(0);
    const [events, setEvents] = useState([]);
 
    const [customerName, setCustomerName] = useState('');
    const [items, setItems] = useState([]);

    const [ticketData, setTicketData] = useState({
        event_id: '',
        ticket_type: '',
        ticket_price: 0,
        total_quantity: 0,
        available_quantity: 0
    });    


    const onChange = (value) => {
        console.log('changed', value);
        // Hàm tính tiền ở đây
      };
    
    const fetchTickets = () => {
        fetch('http://127.0.0.1:5001/tickets')
            .then(response => response.json())
            .then(data => {
                if (Array.isArray(data.tickets)) {
                    setTickets(data.tickets);
                } else {
                    console.error('Invalid data format: expected "tickets" array.');
                }
            })
            .catch(error => {
                console.error('Error fetching tickets:', error);
            });
    };

    const fetchEvents = (event) => {
        fetch('http://127.0.0.1:5000/get_events')
            .then(response => response.json())
            .then(data => {
                if (Array.isArray(data.events)) {
                    setEvents(data.events);
                } else {
                    console.error('Invalid data format: expected "events" array.');
                }
            })
            .catch(error => {
                console.error('Error fetching events:', error);
            });
    };

    const handleAddTicket = (event) => {
        event.preventDefault();
        fetch('http://127.0.0.1:5002/add_ticket', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ticketData)
        })
        .then(response => {
            if (response.ok) {
                fetchTickets();
                setTicketData({
                    event_id: 0,
                    ticket_type: '',
                    ticket_price: 0,
                    total_quantity: 0,
                    available_quantity: 0
                });
            } else {
                console.error('Failed to add ticket');
            }
        })
        .catch(error => {
            console.error('Error adding ticket:', error);
        });
    };

    const updateTicket = (ticketId) => {
        console.log(`Updating ticket with ID: ${ticketId}`);
    };

    const deleteTicket = (ticketId) => {
        fetch(`http://127.0.0.1:5002/delete_ticket/${ticketId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                fetchTickets();
            } else {
                console.error('Failed to delete ticket');
            }
        })
        .catch(error => {
            console.error('Error deleting ticket:', error);
        });
    };

    
    useEffect(() => {
        fetchEvents();
    }, []);


    useEffect(() => {
        fetchTickets();
    }, []);

 

    const onQuantityChange = (ticketId, value, tickets) => {
        setSelectedQuantities(prevState => {
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
        tickets.forEach(ticket => {
            const quantity = selectedQuantities[ticket.ticket_id] || 0;
            totalPrice += quantity * ticket.ticket_price;
        });
        return totalPrice;
    };


    const renderTickets = (tickets) => {
        return tickets.map((ticket) => (
            <tr key={ticket.ticket_id}>
                <td className="text-center px-6 py-4 whitespace-nowrap">{ticket.ticket_type}</td>
                <td className="text-center px-6 py-4 whitespace-nowrap">{ticket.ticket_price}</td>
                <td className="text-center px-6 py-4 whitespace-nowrap">{ticket.available_quantity}</td>
                <td className="text-center px-6 py-4 whitespace-nowrap">
                    <InputNumber className='text-center' size="large" min={0} max={100} defaultValue={0} 
                                onChange={(value) => onQuantityChange(ticket.ticket_id, value, tickets)}/>
                </td>
            </tr>
        ));
    };

    const renderInfo = (tickets) => {
        return tickets.map((ticket) => (
            <tr key={ticket.ticket_id}>
                <td className="text-center px-6 py-4 whitespace-nowrap">{ticket.ticket_type}</td>
                <td className="text-center px-6 py-4 whitespace-nowrap">{ticket.ticket_price}</td>
            </tr>
        ));
    };



    // const handleContinueClick = () => {
    //     // Validate if there are tickets selected
    //     const selectedTickets = Object.keys(selectedQuantities).filter(ticketId => selectedQuantities[ticketId] > 0);
    //     if (selectedTickets.length === 0) {
    //         console.error('Please select at least one ticket.');
    //         return;
    //     }

    //     // Proceed to add order
    //     const orderItems = selectedTickets.map(ticketId => ({
    //         ticket_id: parseInt(ticketId),
    //         quantity: selectedQuantities[ticketId],
    //         price: tickets.find(ticket => ticket.ticket_id === parseInt(ticketId)).ticket_price
    //     }));

    //     const orderData = {
    //         customer_name: customerName, // Set customer name here
    //         items: orderItems
    //     };

    //     fetch('http://127.0.0.1:5001/orders', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify(orderData)
    //     })
    //     .then(response => {
    //         if (!response.ok) {
    //             throw new Error('Failed to add order');
    //         }
    //         return response.json();
    //     })
    //     .then(data => {
    //         console.log('Order created:', data.order);
    //         // Optionally, you can redirect or show a success message
    //         // After successful order creation, you may want to reset selectedQuantities and totalPrice
    //         setSelectedQuantities({});
    //         setTotalPrice(0);
    //         // Redirect to payment page or another page
    //         window.location.href = "/Payment";
    //     })
    //     .catch(error => {
    //         console.error('Error creating order:', error);
    //         // Handle error (e.g., show error message to user)
    //     });
    //     console.log(orderData)
    // };


    // console.log("events: ", events);
    // console.log("tickets", tickets);


    // const AddOrderComponent = () => {
    //     const [customerName, setCustomerName] = useState('');
    //     const [totalPrice, setTotalPrice] = useState(0);
    //     const [items, setItems] = useState([]);
    //     const [currentItem, setCurrentItem] = useState({ ticket_id: '', quantity: '', price: '' });
    
    //     const handleAddOrder = (event) => {
    //         event.preventDefault();
    
    //         const orderData = {
    //             customer_name: customerName,
    //             total_price: totalPrice,
    //             items: items.map(item => ({
    //                 ticket_id: item.ticket_id,
    //                 quantity: item.quantity,
    //                 price: item.price
    //             }))
    //         };
    
    //         fetch('http://127.0.0.1:5002/orders', {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             },
    //             body: JSON.stringify(orderData)
    //         })
    //         .then(response => {
    //             if (response.ok) {
    //                 fetchOrders();  // Gọi hàm để load lại danh sách đơn hàng sau khi thêm thành công
    //                 setCustomerName('');   // Reset các trường dữ liệu của đơn hàng
    //                 setTotalPrice(0);
    //                 setItems([]);
    //             } else {
    //                 console.error('Failed to add order');
    //             }
    //         })
    //         .catch(error => {
    //             console.error('Error adding order:', error);
    //         });
    //     };
    
    //     const handleAddItem = () => {
    //         setItems([...items, currentItem]);
    //         setCurrentItem({ ticket_id: '', quantity: '', price: '' });
    //     };
    // }


    const handleContinueClick = () => {
        const selectedTickets = Object.keys(selectedQuantities).filter(ticketId => selectedQuantities[ticketId] > 0);
        if (selectedTickets.length === 0) {
            console.error('Please select at least one ticket.');
            return;
        }

        const orderItems = selectedTickets.map(ticketId => ({
            ticket_id: parseInt(ticketId),
            quantity: selectedQuantities[ticketId],
            price: tickets.find(ticket => ticket.ticket_id === parseInt(ticketId)).ticket_price
        }));

        const orderData = {
            customer_name: customerName,
            items: orderItems
        };

        fetch('http://127.0.0.1:5001/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(orderData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to add order');
            }
            return response.json();
        })
        .then(data => {
            console.log('Order created:', data.order);
            setSelectedQuantities({});
            setTotalPrice(0);
            //window.location.href = "/Payment";
        })
        .catch(error => {
            console.error('Error creating order:', error);
        });
    };
  return (
    <>
    <div class = {styles.main} >
        
        <div class = {styles.insidebox}>
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
                <tbody id="ticketList" className="bg-white divide-y divide-gray-200">
                {renderTickets(tickets)}
                </tbody>
                
            </table>
        </div>
        <div class = {styles.insidebox}>
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
                    <tbody>
                        {renderInfo(tickets)}
                    </tbody>
                    
                </table>
            </div>
            <br />
            <div>
                {/* <a href="/Payment"> */}
                    <button class = {styles.buy_btn} 
                    className='flex w-full items-center justify-center rounded-lg bg-[#00A198] px-5 py-2.5 text-sm font-medium text-white hover:bg-[#009289] focus:outline-none focus:ring-4  focus:ring-primary-300'
                    onClick={handleContinueClick}> 
                        Continue - {totalPrice} VND 
                    </button>
                {/* </a> */}
            </div>

        </div>

    </div>
    </>
  );
};

export default BuyTicket;
