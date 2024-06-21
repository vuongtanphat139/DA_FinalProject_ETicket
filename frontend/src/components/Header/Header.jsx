import { Link } from "react-router-dom";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import { useState, useEffect } from 'react';
import axios from 'axios'
import styles from "./Header.module.css";

const navigation = [
  { component: "/", name: "Home" },
  { component: "signIn", name: "SignIn" },
  { component: "signUp", name: "SignUp" },
];

export default function Header() {

  const [userlogin, setUserlogin] = useState([]);

  useEffect(() => {
    const user = localStorage.getItem("user");
    if (user) {
      setUserlogin(user);
    }
  }, []);

  const handleLogout = () => {
    const url = 'http://localhost:5000/logout';
    axios.get(url)
    .then(response => {
      localStorage.removeItem('user');
      setUserlogin(null);
      console.log('Data:', response.data);
      console.log('Status:', response.status);
      console.log('Token:', userlogin);
    })
    .catch(error => {
      // handle error
      console.error('Error:', error);
    })   
  };

  return (
    <Box sx={{ flexGrow: 1, position: "fixed", width: "100%", zIndex:"10"}}>
      <AppBar sx={{ background: "#28282A" }} position="static">
        <Toolbar>
          <Typography
            align="center"
            variant="h6"
            component="div"
            sx={{
              flexGrow: 1,
              textTransform: "uppercase",
              color: "#FFF",
              fontFamily: "Roboto Condensed",
              fontSize: "24px",
              fontStyle: "normal",
              fontWeight: 700,
              lineHeight: "38.4px" /* 160% */,
              textTransform: "uppercase",
            }}
          >
            <Link className={styles.link} to={"/"}>
              Onepirate
            </Link>
          </Typography>
          {userlogin ? (
            <>
              {/* Display logout button when logged in */}
              <Button
                color="inherit"
                onClick={handleLogout}
                sx={{
                  fontFamily: "Roboto Condensed",
                  fontSize: "16px",
                  fontWeight: 700,
                  textTransform: "uppercase",
                }}
              >
                Log out
              </Button>
            </>
          ) : (
            <>
              {/* Display sign in and sign up buttons when not logged in */}
              <Link className={styles.signIn} to={"/SignIn"}>
                <Button
                  color="inherit"
                  sx={{
                    fontFamily: "Roboto Condensed",
                    fontSize: "16px",
                    fontWeight: 700,
                    textTransform: "uppercase",
                  }}
                >
                  Sign in
                </Button>
              </Link>
              <Link to={"/SignUp"}>
                <Button
                  color="inherit"
                  sx={{
                    color: "#6867AC",
                    fontFamily: "Roboto Condensed",
                    fontSize: "16px",
                    fontWeight: 700,
                    textTransform: "uppercase",
                  }}
                >
                  Sign up
                </Button>
              </Link>
            </>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
}
