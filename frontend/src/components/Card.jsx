import { Box, Grid, Typography } from "@mui/material"; // Import các component từ thư viện MUI
import august from "../assets/august.png";

const Card = () => {
  return (
    <Box
      sx={{
        width: "fit-content",
        margin: "auto",
        overflow: "hidden",
        // '&:hover': {
        //   "& .MuiTypography-root": {
        //     color: "#EC194C",
        //   }
        // }
      }}
    >
      <Grid container className="border-2 hover:border-primary-500 w-fit">
        {/* Cột trái */}
        <Grid item sx={{ backgroundColor: "#C3CAD9" }}>
          <Box className="bg-white h-32">
            <Typography
              variant="h3"
              pt={2}
              fontWeight={700}
              className="text-center mt-4"
            >
              17
            </Typography>
            <Typography variant="h4" fontWeight={700} className="text-center hover:text-primary-500">
              MAY
            </Typography>
          </Box>
          <Box sx={{ mx:1 }}>
            <Typography variant="body1">
              <svg
                className="h-8 mt-2"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
              >
                <title>map-marker</title>
                <path d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z" />
              </svg>
            </Typography>
            <Typography
              variant="body1"
              style={{ width:"100px", fontWeight: 500, marginTop: "45%" }}
            >
              The Little Bean Coffee
            </Typography>
            <Typography variant="body2" style={{ fontSize: 12, marginTop: 8 }} >District 3, TP HCM</Typography>
          </Box>
        </Grid>

        {/* Cột phải */}
        <Grid item sx={{ position: "relative", overflow: "hidden" }}>
          <img
            src={august}
            alt="Placeholder"
            style={{ width: "100%", height: 300, objectFit: "cover" }}
          />
          <Typography
            variant="h5"
            sx={{
              width: "100%",
              position: "absolute",
              top: "85%",
              left: "7%",
              color: "#fff",
              textAlign: "left",
              fontWeight: 700,
            }}
          >
            August Đỗ Hải Đăng - 1S1M
          </Typography>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Card;
