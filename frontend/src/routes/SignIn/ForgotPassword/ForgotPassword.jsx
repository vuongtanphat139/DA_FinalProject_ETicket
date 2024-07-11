import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

import { useEffect, useState } from "react";
import axios from "axios";

import styles from "../../SignIn/SignIn.module.css";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");

  //console.log("email:",email)
  const handleSubmit = (e) => {
    e.preventDefault();
    const url = "http://localhost:5000/reset-password/request";
    axios
      .post(
        url,
        { email },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((response) => {
        console.log("result:", response.data);
        window.location.href = "/forgotPasswordNoti";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <Container className={styles.signin} component="main" maxWidth="xs">
      <Box
        sx={{
          padding: "3.5em",
          justifyContent: "center",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          background: "#f8f8f8",
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
          Forgot Password
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <Typography
            sx={{
              color: "rgba(0, 0, 0, 0.60)",
              fontFamily: "Work Sans",
              fontSize: "15px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "25.875px",
            }}
          >
            Email to recover*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            name="email"
            autoComplete="email"
            autoFocus
            onChange={(e) => setEmail(e.target.value)}
          />

          <Button
            type="submit"
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
            // href="/forgotPasswordNoti"
          >
            Send
          </Button>
          <Grid container>
            <Grid item></Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}
