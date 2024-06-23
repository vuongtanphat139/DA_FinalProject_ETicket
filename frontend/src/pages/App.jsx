import { Outlet } from "react-router-dom";
import Header from "../components/Header/Header";
import Footer from "../components/footer/Footer";

const App = () => {
  const currentUrl = window.location.href;
  console.log(currentUrl);

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
