
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

import { useEffect,useState } from 'react'
import axios from 'axios'


import styles from "./SignIn.module.css";


export default function SignIn() {
  
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [userlogin, setUserlogin] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('signin')
    const User = {
      username: username,
      password: password
    }

    console.log('User', User)
    const url = 'http://localhost:5000/login';
    axios.post(url, User)
    .then(response => {
      console.log('Data:', response.data);
      console.log('Status:', response.status);
      // localStorage.setItem('authToken', response.data);
      localStorage.setItem('user', JSON.stringify(response.data));
      // console.log('Token:', localStorage.getItem("authToken"));
      setUserlogin(localStorage.getItem("user"))
      console.log('user:', userlogin);
      window.location.href = '/';
    })
    .catch(error => {
      // handle error
      console.error('Error:', error);
    })
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
          Sign in
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <Link className={styles.su} to={"/SignIn"}>
            <Button href="Signup" color="inherit">
              <Typography className={styles.su}>
            {"Not a member yet? Sign Up here"}
            </Typography>
            </Button>
          </Link>
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
            UserName*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            name="email"
            autoComplete="email"
            autoFocus
            onChange={(e)=>setUsername(e.target.value)}
          />
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
            Password*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={(e)=>setPassword(e.target.value)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2, 
              background: "#6867AC",
              color: "#FFF",
              fontFamily: "Roboto Condensed",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 700,
              lineHeight: "24.5px",
              textTransform: "uppercase",
              height: "3.5em",}}

          >
            Sign In
          </Button>
          <Grid container>
            <Grid item xs>
              <Link href="/forgotPassword" variant="body2">
                <Typography className={styles.fp}>
                Forgot password?
                </Typography>
              </Link>
            </Grid>
            <Grid item>
            </Grid>
          </Grid>
        </Box>
        {/* {userlogin} */}
      </Box>
    </Container>

  );
}

