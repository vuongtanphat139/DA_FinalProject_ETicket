import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useSearch } from "./SearchContext";
import {
  Box,
  Button,
  Grid,
  Link,
  Modal,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";

const API_URL = "http://localhost:5001"; // URL của Flask server

const Search = () => {
  const [searchTerm, setSearchTerm] = useState(""); // State to manage search term
  const { setSearchQuery } = useSearch(); // If using context to manage search globally

  const navigate = useNavigate();

  const handleSubmit = () => {
    event.preventDefault(); // Prevent the default form submission
    setSearchQuery(searchTerm); // Example if using context
    navigate("/events");
  };

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value); // Update search term as user types
  };

  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const [eventName, setEventName] = useState("");
  const [eventDate, setEventDate] = useState("");
  const [eventLocation, setEventLocation] = useState("");
  const [eventMinPrice, setEventMinPrice] = useState("");

  const handleCreateEvent = async () => {
    console.log(eventName);
    console.log(eventDate);
    console.log(eventLocation);
    console.log(eventMinPrice);
    try {
      const response = await axios.post(`${API_URL}/create_event`, {
        name: eventName,
        bannerURL:
          "https://media.viez.vn/prod/2022/9/25/1664080399555_07f9bfb367.jpeg",
        datetime: eventDate,
        minTicketPrice: eventMinPrice,
        location: eventLocation,
      });

      console.log("Response from server:", response);
    } catch (error) {
      console.error("Error creating event:", error);
    }
  };

  return (
    <div>
      <form
        className="flex justify-start max-w-3xl mx-auto"
        onSubmit={handleSubmit}
      >
        <label htmlFor="simple-search" className="sr-only">
          Search
        </label>
        <div className="relative w-full">
          <input
            type="text"
            id="simple-search"
            className="bg-[#100000] border border-gray-300 text-white text-sm focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 "
            placeholder="Search events, concerts, workshops..."
            onChange={handleInputChange} // Handle input change
          />
        </div>
        <button
          type="submit"
          className="p-2.5 ms-2 text-sm font-medium text-white bg-primary-500 border border-primary-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300"
        >
          <svg
            className="w-4 h-4"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 20"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
            />
          </svg>
          {/* <span className="sr-only">Search</span> */}
        </button>
      </form>
      <button
        onClick={handleOpen}
        className="p-2.5 ms-2 text-sm font-medium text-white bg-primary-500 border border-primary-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300"
      >
        Create Event
      </button>
      <Modal
        open={open}
        onClose={handleClose}
        className="flex justify-center h-5/6"
      >
        <Box
          sx={{
            marginTop: 9,
            padding: "3.5em",
            justifyContent: "center",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            background: "#F8f8f8",
            width: "800px",
          }}
        >
          <Typography
            component="h1"
            variant="h5"
            sx={{
              color: "rgba(0, 0, 0, 0.87)",
              fontFamily: "Roboto Condensed",
              fontSize: "42px",
              fontStyle: "normal",
              fontWeight: 700,
              lineHeight: "49.014px",
              textTransform: "uppercase",
              borderBottom: "5px solid #EC194C",
              textWrap: "nowrap",
              width: "50px",
              display: "flex",
              justifyContent: "center",
            }}
          >
            Create New Event
          </Typography>

          <Box
            component="form"
            noValidate
            onSubmit={handleCreateEvent}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid
                item
                xs={12}
                sx={{
                  color: "rgba(0, 0, 0, 0.60)",
                  fontFamily: "Work Sans",
                  fontSize: "15px",
                  fontStyle: "normal",
                  fontWeight: 400,
                  lineHeight: "25.875px",
                }}
              >
                Event Name:
                <TextField
                  autoComplete="given-name"
                  name="FullName"
                  required
                  fullWidth
                  id="FullName"
                  autoFocus
                  onChange={(e) => setEventName(e.target.value)}
                />
              </Grid>
              <Grid
                item
                xs={12}
                sx={{
                  color: "rgba(0, 0, 0, 0.60)",
                  fontFamily: "Work Sans",
                  fontSize: "15px",
                  fontStyle: "normal",
                  fontWeight: 400,
                  lineHeight: "25.875px",
                }}
              >
                Date:
                <TextField
                  autoComplete="given-name"
                  name="FullName"
                  required
                  fullWidth
                  id="FullName"
                  autoFocus
                  onChange={(e) => setEventDate(e.target.value)}
                />
              </Grid>
              <Grid
                item
                xs={12}
                sx={{
                  color: "rgba(0, 0, 0, 0.60)",
                  fontFamily: "Work Sans",
                  fontSize: "15px",
                  fontStyle: "normal",
                  fontWeight: 400,
                  lineHeight: "25.875px",
                }}
              >
                Min price:
                <TextField
                  required
                  fullWidth
                  id="email"
                  name="email"
                  autoComplete="email"
                  onChange={(e) => setEventMinPrice(e.target.value)}
                />
              </Grid>
              <Grid
                item
                xs={12}
                sx={{
                  color: "rgba(0, 0, 0, 0.60)",
                  fontFamily: "Work Sans",
                  fontSize: "15px",
                  fontStyle: "normal",
                  fontWeight: 400,
                  lineHeight: "25.875px",
                }}
              >
                Location:
                <TextField
                  required
                  fullWidth
                  name="password"
                  id="password"
                  autoComplete="new-password"
                  onChange={(e) => setEventLocation(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}></Grid>
            </Grid>
            <Button
              onClick={handleCreateEvent}
              fullWidth
              variant="contained"
              sx={{
                mt: 3,
                mb: 2,
                background: "#EC194C",
                color: "#FFF",
                fontFamily: "Roboto Condensed",
                fontSize: "14px",
                fontStyle: "normal",
                fontWeight: 700,
                lineHeight: "24.5px",
                textTransform: "uppercase",
                height: "3.5em",
                "&:hover": {
                  background: "#C71B45",
                },
              }}
            >
              Sign Up
            </Button>
          </Box>
        </Box>
      </Modal>
    </div>
  );
};

export default Search;
