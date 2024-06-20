import { Outlet } from "react-router-dom"
import Header from "../components/Header/Header"
import Footer from "../components/footer/Footer"

const App = () => {
  return (
    <div>
      <Header />
      <Outlet />
      <Footer />
      
    </div>
  )
}

export default App