import styles from "./Home.module.css";
import aviao from "../../assets/aviao.png";
import Button from "@mui/material/Button";
import { Icon, ImageList, ImageListItem } from "@mui/material";
import { AttachMoney, Deck, Sailing } from "@mui/icons-material";
import listras from "../../assets/fundolistra.png";
import Categories from "../../components/Categories/Categories";
import Card from "../../components/Card";

const Home = () => {
  // const checkIfUserIsLoggedIn = () => {
  //   const user = localStorage.getItem("user");
  //   if (user) {
  //     return true;
  //   }
  //   return false;
  // };

  // useEffect(() => {
  //   if (!checkIfUserIsLoggedIn()) {
  //     window.location.href = `/SignIn`;
  //   }
  // }, []);
  return (
    <>
      <div>
        <div className={styles.banner}>
          <img src={aviao} alt="imagem de avião" />
          {/* <div className="relative flex-none"> */}
          <div className="absolute inset-0 flex items-center justify-center mt-80">
            <p>
              <span className={`${styles.destaque} max-w-xl`}>
                The masked singer vietnam concert
              </span>
            </p>
            <div className={`${styles.enjoy} max-w-7xl`}>
              <h3>
                The Masked Singer Vietnam All-Star Concert 2023 left a strong
                impression on many attendees. With a grand investment in modern
                sound and lighting systems, along with a distinctive touch
                through its state-of-the-art stage design that meets
                international standards, it is undeniable that the organizers
                made great efforts to deliver a high-quality event, meticulous
                in every detail. Additionally, the lineup of talented artists
                contributed to creating a memorable experience for this
                all-star concert night.
              </h3>
            </div>
            <Button
              className={styles.register}
              href="SignUp"
              variant="contained"
              sx={{
                background: "#EC194C",
                fontFamily: "Roboto Condensed",
                fontSize: "20px",
                fontWeight: 700,
                lineHeight: "28px",
                textTransform: "uppercase",
                textDecoration: "none",
                width: "200px",
                padding: "15px 67px 17px 67px",
                borderRadius: "0",
                display: "flex",
                alignItems: "center",
                "&:hover": {
                  backgroundColor: "#C71B45",
                },
              }}
            >
              Book<span className="ml-1">now</span>
            </Button>
          </div>
        </div>
      </div>

      <div className={styles.info}>
        <img src={listras} alt="" />

        <div className={styles.sbm}>
          <div className={styles.sunshade}>
            <Icon
              sx={{
                width: "100%",
                height: "55px",
              }}
            >
              <Deck
                sx={{
                  width: "50px",
                  height: "50px",
                }}
              />
            </Icon>
            <h1>The best luxury hotels</h1>
            <h2>
              From the latest trendy boutique hotel to the iconic palace with
              XXL pool, go for a mini-vacation just a few subway stops away from
              your home.
            </h2>
          </div>
          <div className={styles.boat}>
            <Icon
              sx={{
                width: "100%",
                height: "55px",
              }}
            >
              <Sailing
                sx={{
                  width: "50px",
                  height: "50px",
                }}
              />
            </Icon>
            <h1>New experiences</h1>
            <h2>
              Privatize a pool, take a Japanese bath or wake up in 900m2 of
              garden... your Sundays will not be alike.
            </h2>
          </div>
          <div className={styles.money}>
            <Icon
              sx={{
                width: "100%",
                height: "55px",
                // display: "flex",
                // justifyContent: "flex-end",
                // marginTop: -7,
              }}
            >
              <AttachMoney
                sx={{
                  width: "50px",
                  height: "50px",
                }}
              />
            </Icon>
            <h1>Exclusive rates</h1>
            <h2>
              By registering, you will access specially negotiated rates that
              you will not find anywhere else.
            </h2>
          </div>
        </div>
      </div>

      <div className={styles.meinho}>
        <p>
          <span className={styles.destaque}>
            Explore the categories
          </span>
        </p>
        <Categories />
      </div>

      {/* Trending */}
      <div>
        <div className={styles.meinho}>
          <p>
            <span className={styles.destaque}>Trending</span>
          </p>
        </div>

        <div className="flex max-w-7xl m-auto pb-24 ">
          <Card></Card>
          <Card></Card>
          <div className="flex items-center justify-center">
            <Button
              className={styles.register}
              href="/events"
              variant="contained"
              sx={{
                background: "#EC194C",
                fontFamily: "Roboto Condensed",
                fontSize: "14px",
                fontWeight: 700,
                lineHeight: "28px",
                width: "100px",
                height: "30px",
                padding: "15px 67px 15px 67px",
                borderRadius: "0",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                boxShadow: 0,
                "&:hover": {
                  backgroundColor: "#C71B45", // your desired hover color
                },
              }}
            >
              Explore <span className="ml-1">→</span>
            </Button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
