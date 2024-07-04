import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

import { useEffect, useState } from 'react';
import axios from 'axios';

import styles from "./Profile.module.css";

export default function UserProfile() {
  
  const [Userid, setUserid] = useState('');
  const [username, setUsername] = useState('');
  const [fullname, setFullname] = useState('');
  const [gender, setGender] = useState('');
  const [dob, setDob] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');
  const [citizenid, setCitizenid] = useState('');

  const [userlogin, setUserlogin] = useState(null);
  const [userlogininfo, setUserlogininfo] = useState(null);
  
const getUserInfor = () => {
  const storedUser = localStorage.getItem("user");
  let userloginusername = "";
  console.log('123:', storedUser);
  if (storedUser) {
    const parsedUser = JSON.parse(storedUser);
    setUserlogin(parsedUser);
    console.log('temp:', parsedUser);
    userloginusername=parsedUser.username;
    console.log('temp2:', userloginusername);
  }
  if (!userloginusername) {
    console.error('User login information is not available .');
    return;
  }

  const url = `http://localhost:5000/username/${userloginusername}`;
  axios.get(url)
    .then(response => {
      console.log('Data:', response.data);
      console.log('Status:', response.status);
      setUserlogininfo(response.data)


      setUserid(response.data.UserID)
      setUsername(response.data.UserName)
      setFullname(response.data.FullName)
      setGender(response.data.Gender)
      setDob(response.data.DOB)
      setPhone(response.data.Phone)
      setEmail(response.data.Email)
      setAddress(response.data.Address)
      setCitizenid(response.data.CitizenID)
    })
    .catch(error => {
      console.error('Error:', error);
    });
};

useEffect(() => {
  const loggedIn = checkIfUserIsLoggedIn(); 
  const user = localStorage.getItem("user");
  setUserlogin(loggedIn);

  console.log('user',userlogin)
  console.log('usertemp',user)
}, []);

const checkIfUserIsLoggedIn = () => {
  const user = localStorage.getItem("user");
  if (user) {
    setUserlogin(user);
    return true;
  }
  return false
};

const handleLogout1 = () => {
  const url = 'http://localhost:5000/logout';
  axios.get(url)
  .then(response => {
    localStorage.removeItem('user');
    setUserlogin(null);
    console.log('Data:', response.data);
    console.log('Status:', response.status);
    console.log('user:', userlogin);
    window.location.href = '/organizationSignup';
  })
  .catch(error => {
    // handle error
    console.error('Error:', error);
  })   
};

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('signin');
    const User = {
      username: username,
      fullname: fullname,
      gender: gender,
      dob: dob,
      phone: phone,
      email: email,
      address: address,
      citizenID: citizenid
  }
  

    console.log('User', User);
    console.log('Userid', Userid);
    const url = `http://localhost:5000/profile/user/${Userid}`;
    axios.put(url, User)
    .then(response => {
      console.log('Data:', response.data);
      console.log('Status:', response.status);
      window.location.href = '/';
    })
    .catch(error => {
      // handle error
      console.error('Error:', error);
    });
  };

  useEffect(() => {
    getUserInfor() 
    console.log("check userinfo",userlogininfo)
  }, []);
  
  return (
    
    <Container className={styles.signin} component="main" maxWidth="xs">
      <Box
        sx={{
          padding: '3.5em',
          justifyContent: 'center',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          background: '#F5F6FF',
          width: '800px',
        }}
      >
        <Typography
          component="h1"
          variant="h5"
          sx={{
            color: 'rgba(0, 0, 0, 0.87)',
            fontFamily: 'Roboto Condensed',
            fontSize: '42px',
            fontStyle: 'normal',
            fontWeight: 700,
            lineHeight: '49.014px',
            textTransform: 'uppercase',
            borderBottom: '5px solid #6867ac',
            textWrap: 'nowrap',
            width: '50px',
            display: 'flex',
            justifyContent: 'center',
          }}
        >
          Profile
        </Typography>
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
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
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
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
            value={fullname}
            onChange={(e) => setFullname(e.target.value)}
          />
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
            }}
          >
            Gender*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            id="gender"
            name="gender"
            value={gender}
            onChange={(e) => setGender(e.target.value)}
          />
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
            }}
          >
            Date of Birth*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            id="dob"
            name="dob"
            type="date"
            value={dob}
            onChange={(e) => setDob(e.target.value)}
          />
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
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
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
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
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
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
          <Typography
            sx={{
              color: 'rgba(0, 0, 0, 0.60)',
              fontFamily: 'Work Sans',
              fontSize: '15px',
              fontStyle: 'normal',
              fontWeight: 400,
              lineHeight: '25.875px',
            }}
          >
            Citizen ID*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            id="citizenid"
            name="citizenid"
            value={citizenid}
            onChange={(e) => setCitizenid(e.target.value)}
          />

          {/* ---button--- */}
          <Grid container spacing={2} sx={{ mt: 3, mb: 2 }}>
            <Grid item xs={6}>
              <Button
                fullWidth
                variant="contained"
                sx={{
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
                onClick={handleSubmit}
              >
                Save Changes
              </Button>
            </Grid>
            <Grid item xs={6}>
              <Button
                fullWidth
                variant="contained"
                onClick={handleLogout1}
                sx={{
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
                // href="/companySignup"
              >
                UPDATE TO COMPANY
              </Button>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>
  );
}
