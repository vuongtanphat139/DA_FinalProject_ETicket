// src/api/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5000'; // URL của Flask server

export const getEvents = async () => {
    try {
        const response = await axios.get(`${API_URL}/get_events`);
        console.log(response);
        return response.data.events; // Giả sử API trả về một object có key là events chứa danh sách các sự kiện
    } catch (error) {
        console.error("There was an error fetching the events!", error);
        throw error;
    }
};
