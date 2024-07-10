import React, { useEffect, useState } from "react";
import axios from "axios";
import ListEvents from "../../components/ListCard";

const API_URL = "http://localhost:5001";

const UserEvent = () => {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);

  const fetchEvents = async () => {
    try {
      const response = await axios.get(`${API_URL}/get_event_by_organization_id/1`);
      console.log("events: ", response.data.events);
      setEvents(response.data.events);
    } catch (error) {
      setError(error);
      console.log(error);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <div className="mt-4 mb-8">
      <ListEvents events={events} />
    </div>
  );
};

export default UserEvent;
