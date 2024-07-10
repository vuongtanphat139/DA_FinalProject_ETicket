import { Box, Button, Grid, TextField } from "@mui/material";
import React from "react";

const profile = () => {
  return (
    <div className="w-1/2 m-auto mb-8">
      <Box
        component="form"
        noValidate
        // onSubmit={handleCreateEvent}
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
              // onChange={(e) => setEventName(e.target.value)}
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
              // onChange={(e) => setEventDate(e.target.value)}
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
              // onChange={(e) => setEventMinPrice(e.target.value)}
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
              // onChange={(e) => setEventLocation(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}></Grid>
        </Grid>
        <Button
          // onClick={handleCreateEvent}
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
          Create Event
        </Button>
      </Box>
    </div>
  );
};

export default profile;
