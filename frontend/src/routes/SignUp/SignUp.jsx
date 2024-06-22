import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";

import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";

import { Link } from "react-router-dom";
import { useEffect,useState } from 'react'
import { useSelector } from 'react-redux';
import axios from 'axios'


import styles from "./SignUp.module.css";

export default function SignUp() {
      
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');



  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('signup')
    const newUser = {
      username: username,
      password: password,
      fullname: fullName,
      email: email
    }
    console.log('new User', newUser)
    const url = 'http://localhost:5000/register';
    axios.post(url, newUser)
    .then(response => {
      console.log('Data:', response.data);
      console.log('Status:', response.status);
      window.location.href = '/SignIn';
    })
    .catch(error => {
      // handle error
      console.error('Error:', error);
    })
  };


  return (   
      <Container component="main" className={styles.signup} maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 9,
            padding: "3.5em",
            justifyContent: "center",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            background: "#F5F6FF",
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
              borderBottom: "5px solid #6867ac",
              textWrap: "nowrap",
              width: "50px",
              display: "flex",
              justifyContent: "center",
            }}
          >
            Sign up
          </Typography>
          <Link className={styles.si} to={"/SignIn"}>
            <Button href="SignIn" color="inherit" sx={{}}>
              <Typography className={styles.si}>
              Already have an account?
              </Typography>
            </Button>
          </Link>
          <Box
            component="form"
            noValidate
            onSubmit={handleSubmit}
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
                Full Name*
                <TextField
                  autoComplete="given-name"
                  name="FullName"
                  required
                  fullWidth
                  id="FullName"
                  autoFocus
                  onChange={(e)=>setFullName(e.target.value)}
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
                UserName*
                <TextField
                  autoComplete="given-name"
                  name="FullName"
                  required
                  fullWidth
                  id="FullName"
                  autoFocus
                  onChange={(e)=>setUsername(e.target.value)}
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
                Email Address*
                <TextField
                  required
                  fullWidth
                  id="email"
                  name="email"
                  autoComplete="email"
                  onChange={(e)=>setEmail(e.target.value)}
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
                Password*
                <TextField
                  required
                  fullWidth
                  name="password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                  onChange={(e)=>setPassword(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}></Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{
                mt: 3,
                mb: 2,
                background: "#6867AC",
                color: "#FFF",
                fontFamily: "Roboto Condensed",
                fontSize: "14px",
                fontStyle: "normal",
                fontWeight: 700,
                lineHeight: "24.5px",
                textTransform: "uppercase",
                height: "3.5em",
              }}
              
            >
              Sign Up
            </Button>
          </Box>
        </Box>
      </Container>
    
  );
}
