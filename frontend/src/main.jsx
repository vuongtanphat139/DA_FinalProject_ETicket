import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import SignIn from './routes/SignIn/SignIn.jsx'
import CompanySignIn from './routes/SignIn/CompanySignIn.jsx'
import ForgotPassword from './routes/SignIn/ForgotPassword/ForgotPassword.jsx'
import ForgotPasswordNoti from './routes/SignIn/ForgotPassword/ForgotPasswordNoti.jsx'
import ResetPassword from './routes/SignIn/ForgotPassword/ResetPassword.jsx'
import SignUp from './routes/SignUp/SignUp.jsx'
import CompanySignup from './routes/SignUp/CompanySignUp.jsx'
import CompanyProfile from './routes/Profile/CompanyProfile.jsx'
import UserProfile from './routes/Profile/UserProfile.jsx'
import Home from './routes/Home/Home.jsx'
import Test from './routes/Test/Test.jsx'
import BuyTicket from './routes/BuyTicket/BuyTicket.jsx'
import Payment from './routes/Payment/Payment.jsx'
import Events from './routes/Events/Events.jsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    // errorElement: <Error />,
    children: [
      {path:"/", element:<Home />},
      {path:"signIn", element: <SignIn />},
      {path:"companysignIn", element: <CompanySignIn />},
      {path:"signUp", element: <SignUp />},
      {path:"companySignup", element: <CompanySignup />},
      {path:"forgotPassword", element: <ForgotPassword />},
      {path:"forgotPasswordNoti", element: <ForgotPasswordNoti />},
      {path:"resetPassword", element: <ResetPassword/>},
      {path:"userprofile", element: <UserProfile/>},
      {path:"companyprofile", element: <CompanyProfile/>},
      {path:"test", element: <Test />},
      {path:"buyticket", element: <BuyTicket />},
      {path:"payment", element: <Payment />},
      {path:"events", element: <Events />},
    ]
  }
  ])
  
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
