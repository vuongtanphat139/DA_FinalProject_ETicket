import Footer from "../../components/footer/Footer";
import Header from "../../components/Header/Header";

function DefaultLayout({ children }) {
  return (
    <div className="relative">
      <Header />
      <div>{children}</div>
      <Footer />
    </div>
  );
}

export default DefaultLayout;
