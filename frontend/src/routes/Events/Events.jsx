import styles from "./Event.module.css";
import ListEvents from "../../components/ListCard";
import { useEffect, useState } from "react";
import { Checkbox, FormControlLabel, Pagination } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import axios from "axios";
import { useSearch } from "../../components/Header/SearchContext";

const theme = createTheme();
const API_URL = "http://localhost:5001"; // URL của Flask server

const Events = () => {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);
  const [categories, setCategories] = useState([]);
  const { searchQuery } = useSearch();

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await axios.get(`${API_URL}/get_events`, {
          params: {
            name: searchQuery,
            categories: categories.join(','),
          },
        });
        console.log("events: ", response.data.events);
        setEvents(response.data.events);
      } catch (error) {
        setError(error);
        console.log(error);
      }
    };

    fetchEvents();
  }, [categories, searchQuery]);

  const handleCategoryChange = (category) => {
    // Check if the category is already in the list
    if (categories.includes(category)) {
      // Remove the category if it's already selected
      setCategories(categories.filter((cat) => cat !== category));
    } else {
      // Add the category if it's not selected
      setCategories([...categories, category]);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <div></div>
      <div className={`${styles.meinho} pt-16`}>
        <p>
          <span className={styles.destaque}>Events Result</span>
        </p>
        <div className="w-2/3">
          <div className="mb-8">
            <FormControlLabel
              control={
                <Checkbox
                  checked={categories.includes("Music")}
                  onChange={() => handleCategoryChange("Music")}
                />
              }
              label="Music"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={categories.includes("Art")}
                  onChange={() => handleCategoryChange("Art")}
                />
              }
              label="Art"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={categories.includes("Sport")}
                  onChange={() => handleCategoryChange("Sport")}
                />
              }
              label="Sport"
            />
            <FormControlLabel
              control={
                <Checkbox
                  checked={categories.includes("Other")}
                  onChange={() => handleCategoryChange("Other")}
                />
              }
              label="Others"
            />
          </div>
          <ListEvents events={events} />
        </div>
      </div>
      <div className="m-auto flex justify-center my-12">
        <Pagination count={Math.floor(events.length / 10) + 1} shape="rounded" sx={{ borderRadius: "0px" }} />
      </div>
    </ThemeProvider>
  );
};

export default Events;
