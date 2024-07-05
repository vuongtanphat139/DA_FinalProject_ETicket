
import React from 'react'
import { InputNumber } from 'antd';
import { Button, Popconfirm } from 'antd';

import styles from "./HandleTicket.module.css";
import { useEffect, useState } from 'react';
import {useSelector} from 'react-redux'


const HandleTicket = () => {
    const [tickets, setTickets] = useState([]);
    const [selectedQuantities, setSelectedQuantities] = useState({});
    const [totalPrice, setTotalPrice] = useState(0);
    const [events, setEvents] = useState([]);
 
    const [customerName, setCustomerName] = useState('');
    const [items, setItems] = useState([]);

    const [ticketData, setTicketData] = useState({
        event_id: 0,
        ticket_type: '',
        ticket_price: 0,
        total_quantity: 0,
        available_quantity: 0
    });    


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
                console.log();
            });
    };

    const fetchTicketsByEvent = () => {
        // fetch(`http://127.0.0.1:5001/tickets_by_event/${event_id}`)
        fetch(`http://127.0.0.1:5001/tickets_by_event/1`) //Check: sửa lại thành biến khi ghép coide
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
                console.log();
            });
    };

    const fetchTicketById = async (ticketId) => {
        try {
            const response = await fetch(`http://127.0.0.1:5001/tickets/${ticketId}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
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
            console.error('Error fetching ticket:', error);
        }
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

    const handleAddTicket = async (event) => {
        event.preventDefault();
        
        try {
            // Check: Khi ghép & có event ID thì cần sửa eventId trong ticketData
            const updatedTicketData = {
                ...ticketData,
                event_id: 1, //Sửa chỗ này
            };
            setTicketData(updatedTicketData);

            const response = await fetch('http://127.0.0.1:5001/tickets', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedTicketData)
            });
    
            if (response.ok) {
                await fetchTicketsByEvent();
                console.log("ADD TICKET SUCCESS!")
                setTicketData({
                    event_id: 0,
                    ticket_type: '',
                    ticket_price: 0.0,
                    total_quantity: 0,
                    available_quantity: 0
                });
            } else {
                console.error('Failed to add ticket');
            }
        } catch (error) {
            console.error('Error adding ticket:', error);
        }
    };
    
    // const handleAddTicket = (event) => {
    //     event.preventDefault();
    //     fetch('http://127.0.0.1:5001/add_ticket', {
    //         method: 'POST',
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
    //             console.error('Failed to add ticket');
    //         }
    //     })
    //     .catch(error => {
    //         console.error('Error adding ticket:', error);
    //     });
    // };

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

    const updateTicket = async (ticketId, updatedTicketData) => {
        try {
            console.log("Update ticket: ", ticketId);
    
            const response = await fetch(`http://127.0.0.1:5001/tickets/${ticketId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedTicketData)
            });
    
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
            console.error('Error updating ticket:', error);
        }
    };
    
    const deleteTicket = async (ticketId) => {
        try {
            const response = await fetch(`http://127.0.0.1:5001/tickets/${ticketId}`, {
                method: 'DELETE',
            });
    
            if (response.ok) {
                await fetchTicketsByEvent();
                console.log("DELETE TICKET SUCCESS!");
            } else {
                console.error('Failed to delete ticket');
            }
        } catch (error) {
            console.error('Error deleting ticket:', error);
        }
    };
    

    useEffect(() => {
        fetchEvents();
    }, []);


    useEffect(() => {
        fetchTicketsByEvent();
    }, []);

 

    

    const renderTickets = (tickets) => {
        return tickets.map((ticket, index) => (
            <tr key={ticket.ticket_id}>
                <td className="text-center whitespace-nowrap border border-black">
                    <input type="text" name="ticket_type" className='text-center whitespace-nowrap' 
                    value={ticket.ticket_type}
                    onChange={(e) => handleInputChangeWithIndex(index, 'ticket_type', e.target.value)}
                    />
                        
                </td>
                <td className="text-center whitespace-nowrap border border-black">
                    <input type="text" name="ticket_price" className='text-center whitespace-nowrap' 
                    value={ticket.ticket_price}
                    onChange={(e) => handleInputChangeWithIndex(index, 'ticket_price', e.target.value)}
                    />                        
                </td>
                <td className=" text-center whitespace-nowrap border border-black">
                    <input type="text" name="available_quantity" className='text-center whitespace-nowrap w-1/2' 
                    value={ticket.available_quantity}
                    onChange={(e) => handleInputChangeWithIndex(index, 'available_quantity', e.target.value)}
                    />
                </td>
                <td className="text-center whitespace-nowraptext-center whitespace-nowrap border border-black">
                    <input type="text" name="total_quantity" className='text-center whitespace-nowrap w-1/2' 
                    value={ticket.total_quantity}
                    onChange={(e) => handleInputChangeWithIndex(index, 'total_quantity', e.target.value)}
                    />
                </td>
                <td className='bg-[#F7F8FA] '></td>
                <td className="text-center  whitespace-nowrap">
                    <button 
                    onClick={() => updateTicket(ticket.ticket_id, ticket)}
                    className='text-center px-6 py-4 bg-[#FAAF4380] hover:bg-[#FAAF43] hover:text-white'>
                        Update
                    </button>
                    </td>
                <td className="text-center whitespace-nowrap ">
                    <button 
                    onClick={() => deleteTicket(ticket.ticket_id)}
                    className='text-center px-6 py-4 bg-[#EE4136B3] hover:bg-[#EE4136] hover:text-white'>
                        Delete
                    </button>
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

    const handleInputChange = (name, value) => {
        //Lấy ra name và value của input được thay đổi.
        setTicketData(prevTicketData => ({
            ...prevTicketData,
            [name]: value
        }));
    };
    
    const handleInputChangeWithIndex = (index, name, value) => {
        // Tạo một bản sao của tickets để thay đổi chỉ mục index
        const updatedTickets = [...tickets];
        updatedTickets[index] = {
            ...updatedTickets[index],
            [name]: value
        };
        // Cập nhật lại state của tickets
        setTickets(updatedTickets);
    };

  return (
    <>
    <div class = {styles.main}>
        
        <div class = {styles.insidebox}>
            <h1>Handle ticket</h1>
            <br />
            <table >
                <thead>
                    <tr>
                        <th className='border border-black'>Ticket Type</th>
                        <th className='border border-black'>Price</th>
                        <th className='border border-black'>Available</th>
                        <th className='border border-black'>Quantity</th>
                    </tr>
                </thead>
                <tbody id="ticketList" className="bg-white divide-y divide-gray-200">
                {renderTickets(tickets)}
                </tbody>
                <br />
                <tr >
                <td className="text-center px-0 py-0  border border-black">
                    <input 
                    type="text" name="ticket_type" className='p-1 w-full text-center' 
                    value={ticketData.ticket_type}
                    onChange={(e) => handleInputChange('ticket_type', e.target.value)}
                    />
                </td>
                <td className="text-center px-0 py-0 border border-black">
                     <input 
                     type="text" name="ticket_price" className='p-1 w-full text-center' 
                     value={ticketData.ticket_price}
                     onChange={(e) => handleInputChange('ticket_price', e.target.value)}
                     />
                </td>
                <td className="text-center px-0 py-0 border border-black">
                    <input
                    type="text" name="available_quantity" className='p-1 w-full text-center'
                    value={ticketData.available_quantity}
                    onChange={(e) => handleInputChange('available_quantity', e.target.value)}/>
                </td>
                <td className="text-center px-0 py-0 border border-black">
                    <input 
                    type="text" name="total_quantity" className='p-1 w-full text-center' 
                    value={ticketData.total_quantity}
                    onChange={(e) => handleInputChange('total_quantity', e.target.value)}
                    />
                </td>
                <td className="text-center whitespace-nowrap border-r-black"></td>
                <td className="text-center px-0 py-0 whitespace-nowrap border border-black bg-[#00A19880] hover:bg-[#00A198] hover:text-white">
                    <button onClick={handleAddTicket}>
                        Add
                    </button>
                </td>

                </tr>

                
            </table>

        </div>

    </div>
    </>
  );
};

export default HandleTicket;
