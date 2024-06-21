
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { useLocation } from 'react-router-dom';
import { useEffect,useState } from 'react'
import axios from 'axios'


import styles from "../../SignIn/SignIn.module.css";


export default function ResetPassword() {
  
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const location = useLocation();
  const token = new URLSearchParams(location.search).get('token');
 //console.log("email:",email)
 const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(`http://localhost:5000/reset-password/${token}`, {
        new_password: newPassword,
      });

      if (response.status === 200) {
        setMessage('Password reset successfully.');
        setError('');
      }
    } catch (error) {
      setMessage('');
      setError('Error resetting password: ' + error.response.data.error);
    }
  };

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
          Reset Password
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
            New Password*
          </Typography>
          <TextField
            margin="normal"
            required
            fullWidth
            type="password"
            id="newPassword"
            name="newPassword"
            autoComplete="new-password"
            autoFocus
            onChange={(e) => setNewPassword(e.target.value)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{
              mt: 3,
              mb: 2,
              background: '#6867AC',
              color: '#FFF',
              fontFamily: 'Roboto Condensed',
              fontSize: '14px',
              fontStyle: 'normal',
              fontWeight: 700,
              lineHeight: '24.5px',
              textTransform: 'uppercase',
              height: '3.5em',
            }}
          >
            Done
          </Button>
          {message && <Typography color="success.main">{message}</Typography>}
          {error && <Typography color="error.main">{error}</Typography>}
        </Box>
      </Box>
    </Container>
  );
}

