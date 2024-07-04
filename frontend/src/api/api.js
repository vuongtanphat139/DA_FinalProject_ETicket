// src/api/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5000'; // URL của Flask server

export const getEvents = async () => {
    try {
        const response = await axios.get(`${API_URL}/get_events`, {
            params: {
                name: "",
                categories: ""
            }
        });
        console.log(response);
        return response.data.events;
    } catch (error) {
        console.error("There was an error fetching the events!", error);
        throw error;
    }
};
