/* eslint-disable react/prop-types */
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardActionArea from "@mui/material/CardActionArea";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import august from "../assets/august.png";

const ListEvents = ({ events }) => {
  return (
    <Grid item xs={6} md={8} className="grid grid-cols-2 gap-8">
      {events.map((item) => (
        <CardActionArea
          key={item.id}
          component="a"
          href="#"
          sx={{ borderWidth: 5 }}
        >
          <Card sx={{ display: "flex", borderWidth: 2, boxShadow: 0 }}>
            <CardContent sx={{ flex: 1 }}>
              <Typography variant="h5" sx={{fontWeight: 500}}>
                {item.name}
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                {item.datetime}
              </Typography>
              <Typography variant="subtitle1" paragraph>
                
              </Typography>
              <Typography variant="subtitle2" color="grey">
                {item.address}
              </Typography>
              {/* <Typography variant="h5" paragraph color={"#EC194C"}>
                From {item.minTicketPrice}
              </Typography> */}
            </CardContent>
            <CardMedia
              component="img"
              sx={{ width: "30%", display: { xs: "none", sm: "block" } }}
              image={item?.bannerUrl}
              alt={"august"}
            />
          </Card>
        </CardActionArea>
      ))};
      {/* <CardActionArea component="a" href="#" sx={{ borderWidth: 5 }}>
        <Card sx={{ display: "flex", borderWidth: 2, boxShadow: 0 }}>
          <CardContent sx={{ flex: 1 }}>
            <Typography component="h2" variant="h5">
              Title
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              Date
            </Typography>
            <Typography variant="subtitle1" paragraph>
              Description
            </Typography>
            <Typography variant="subtitle1" color="primary">
              Continue reading...
            </Typography>
          </CardContent>
          <CardMedia
            component="img"
            sx={{ width: "50%", display: { xs: "none", sm: "block" } }}
            image={august}
            alt={"august"}
          />
        </Card>
      </CardActionArea>
      <CardActionArea component="a" href="#" sx={{ borderWidth: 5 }}>
        <Card sx={{ display: "flex", borderWidth: 2, boxShadow: 0 }}>
          <CardContent sx={{ flex: 1 }}>
            <Typography component="h2" variant="h5">
              Title
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              Date
            </Typography>
            <Typography variant="subtitle1" paragraph>
              Description
            </Typography>
            <Typography variant="subtitle1" color="primary">
              Continue reading...
            </Typography>
          </CardContent>
          <CardMedia
            component="img"
            sx={{ width: "50%", display: { xs: "none", sm: "block" } }}
            image={august}
            alt={"august"}
          />
        </Card>
      </CardActionArea>
      <CardActionArea component="a" href="#" sx={{ borderWidth: 5 }}>
        <Card sx={{ display: "flex", borderWidth: 2, boxShadow: 0 }}>
          <CardContent sx={{ flex: 1 }}>
            <Typography component="h2" variant="h5">
              Title
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              Date
            </Typography>
            <Typography variant="subtitle1" paragraph>
              Description
            </Typography>
            <Typography variant="subtitle1" color="primary">
              Continue reading...
            </Typography>
          </CardContent>
          <CardMedia
            component="img"
            sx={{ width: "50%", display: { xs: "none", sm: "block" } }}
            image={august}
            alt={"august"}
          />
        </Card>
      </CardActionArea>
      <CardActionArea component="a" href="#" sx={{ borderWidth: 5 }}>
        <Card sx={{ display: "flex", borderWidth: 2, boxShadow: 0 }}>
          <CardContent sx={{ flex: 1 }}>
            <Typography component="h2" variant="h5">
              Title
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
              Date
            </Typography>
            <Typography variant="subtitle1" paragraph>
              Description
            </Typography>
            <Typography variant="subtitle1" color="primary">
              Continue reading...
            </Typography>
          </CardContent>
          <CardMedia
            component="img"
            sx={{ width: "50%", display: { xs: "none", sm: "block" } }}
            image={august}
            alt={"august"}
          />
        </Card>
      </CardActionArea> */}
    </Grid>
  );
};

export default ListEvents;
