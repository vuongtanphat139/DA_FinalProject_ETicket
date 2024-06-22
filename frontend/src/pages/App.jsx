import { Outlet } from "react-router-dom";
import Header from "../components/Header/Header";
import Footer from "../components/footer/Footer";
import { useEffect, useState } from "react";
import { getEvents } from "../api/api";

const App = () => {
  const currentUrl = window.location.href;
  console.log(currentUrl);
  // const [events, setEvents] = useState([]);
  // const [loading, setLoading] = useState(true);
  // const [error, setError] = useState(null);

  // useEffect(() => {
  //   const fetchEvents = async () => {
  //     try {
  //       const eventsData = await getEvents();
  //       setEvents(eventsData);
  //       setLoading(false);
  //     } catch (error) {
  //       setError(error);
  //       setLoading(false);
  //     }
  //   };

  //   fetchEvents();
  // }, []);

  // if (loading) return <div>Loading...</div>;
  // if (error) return <div>Error fetching events: {error.message}</div>;

  return (
    <div>
      {currentUrl === "http://localhost:5173/SignUp" ||
      currentUrl === "http://localhost:5173/SignIn" ||
      currentUrl === "http://localhost:5173/forgotPassword" ? (
        <Outlet />
      ) : (
        <div>
          <Header />
          <Outlet />
          <Footer />
        </div>
      )}
    </div>
  );
};

export default App;
