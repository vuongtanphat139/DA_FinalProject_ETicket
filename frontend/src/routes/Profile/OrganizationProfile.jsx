import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

import { useEffect, useState } from "react";
import axios from "axios";

import styles from "./Profile.module.css";

export default function UserProfile() {
  const [organizationID, setUserid] = useState("");
  const [organizationusername, setOrganizationUsername] = useState("");
  const [organizationfullname, setOrganizationFullname] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");

  const [userlogininfo, setUserlogininfo] = useState(null);

  const getUserInfor = () => {
    const storedUser = localStorage.getItem("Organizationuser");
    let userloginusername = "";
    console.log("123:", storedUser);
    if (storedUser) {
      const parsedUser = JSON.parse(storedUser);
      //setUserlogin(parsedUser);
      console.log("temp:", parsedUser);
      userloginusername = parsedUser.OrganizationUserName;
      console.log("temp2:", userloginusername);
    }
    if (!userloginusername) {
      console.error("User login information is not available .");
      return;
    }

    const url = `http://localhost:5000/organizationusername/${userloginusername}`;
    axios
      .get(url)
      .then((response) => {
        console.log("Data:", response.data);
        console.log("Status:", response.status);
        setUserlogininfo(response.data);

        setUserid(response.data.OrganizationID);
        setOrganizationUsername(response.data.OrganizationUserName);
        setOrganizationFullname(response.data.OrganizationFullName);
        setPhone(response.data.Phone);
        setEmail(response.data.Email);
        setAddress(response.data.Address);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("signin");

    const User = {
      organization_fullname: organizationfullname,
      username: organizationusername,
      email: email,
      phone: phone,
      address: address,
    };

    console.log("User", User);
    console.log("Userid", organizationID);
    const url = `http://localhost:5000/profile/userOrganization/${organizationID}`;
    axios
      .put(url, User)
      .then((response) => {
        console.log("Data:", response.data);
        console.log("Status:", response.status);
        window.location.href = "/";
      })
      .catch((error) => {
        // handle error
        console.error("Error:", error);
      });
  };

  useEffect(() => {
    getUserInfor();
    console.log("check userinfo", userlogininfo);
  }, []);

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      noValidate
      sx={{ mt: 1, width: "50%", margin: "auto" }}
    >
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
        id="username"
        name="username"
        autoFocus
        value={organizationusername}
        onChange={(e) => setOrganizationUsername(e.target.value)}
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
        Full Name*
      </Typography>
      <TextField
        margin="normal"
        required
        fullWidth
        id="fullname"
        name="fullname"
        value={organizationfullname}
        onChange={(e) => setOrganizationFullname(e.target.value)}
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
        Phone*
      </Typography>
      <TextField
        margin="normal"
        required
        fullWidth
        id="phone"
        name="phone"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
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
        Email*
      </Typography>
      <TextField
        margin="normal"
        required
        fullWidth
        id="email"
        name="email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
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
        Address*
      </Typography>
      <TextField
        margin="normal"
        required
        fullWidth
        id="address"
        name="address"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
      />

      {/* ---button--- */}
      <Grid container spacing={2} sx={{ mt: 3, mb: 2 }}>
        <Button
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
          onClick={handleSubmit}
        >
          Save Changes
        </Button>
      </Grid>
    </Box>
  );
}
