
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";


import styles from "../../SignIn/SignIn.module.css";


export default function ForgotPasswordNoti() {
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
        <Box component="form" noValidate sx={{ mt: 1 }}>
          <Typography
            sx={{
              color: "rgba(0, 0, 0, 0.60)",
              fontFamily: "Work Sans",
              fontSize: "20px",
              fontStyle: "normal",
              fontWeight: 600,
              lineHeight: "25.875px",
            }}
          >
            *Check your email*
          </Typography>

          <Grid container>
            <Grid item>
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Container>

  );
}

