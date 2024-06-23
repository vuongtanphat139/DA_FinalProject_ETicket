import styles from "./Event.module.css";
import ListEvents from "../../components/ListCard";
import { useEffect, useState } from "react";
import { getEvents } from "../../api/api";
import { Card, CardActionArea, CardContent, CardMedia, Checkbox, FormControlLabel, Pagination, Typography } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import august from "../../assets/august.png";

const theme = createTheme();
const label = { inputProps: { "aria-label": "Checkbox demo" } };

const Events = () => {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const eventsData = await getEvents();
        setEvents(eventsData);
        console.log("log: ", eventsData);
      } catch (error) {
        setError(error);
      }
    };

    fetchEvents();
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <div></div>
      <div className={`${styles.meinho} pt-16`}>
        <p>
          <span className={styles.destaque}>Event Result</span>
        </p>
        <div className="w-2/3">
          <div className="mb-8">
            <FormControlLabel control={<Checkbox />} label="Music" />
            <FormControlLabel control={<Checkbox />} label="Art" />
            <FormControlLabel control={<Checkbox />} label="Sport" />
            <FormControlLabel control={<Checkbox />} label="Others" />
          </div>
          <ListEvents events={events} />
        </div>
      </div>
      <div className="m-auto flex justify-center my-12">
        <Pagination count={10} shape="rounded" sx={{ borderRadius: "0px" }} />
      </div>
    </ThemeProvider>
  );
};

export default Events;
