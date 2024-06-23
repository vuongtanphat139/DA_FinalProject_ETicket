/* eslint-disable react/prop-types */
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import CardActionArea from "@mui/material/CardActionArea";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";

const ListEvents = ({ events, image = null }) => {
  return (
    <Grid item xs={6} md={8} className="grid grid-cols-2 gap-8">
      {events.map((item) => (
        <CardActionArea
          key={item.id}
          component="a"
          href="events/1"
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
              image={image || "https://scontent.fhan14-5.fna.fbcdn.net/v/t39.30808-6/430858252_952662943088200_3508925116975497269_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGK2S-T1s4sCpMi6CHMybn7253QTyUWbuvbndBPJRZu627tuMaQbrZ8TtH2t-3-P_9ymZK8Ld8lDSa6OtFHPlVz&_nc_ohc=xDuh50S4YVMQ7kNvgG_dCgq&_nc_ht=scontent.fhan14-5.fna&oh=00_AYD9JoVs2N5RjosabvxguFKj93pxsJc0uY5o7renkDaBEQ&oe=667DBC88"}
              alt={"august"}
            />
          </Card>
        </CardActionArea>
      ))}
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
