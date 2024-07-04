import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import SignIn from './routes/SignIn/SignIn.jsx'
import OrganizationSignIn from './routes/SignIn/OrganizationSignIn.jsx'
import ForgotPassword from './routes/SignIn/ForgotPassword/ForgotPassword.jsx'
import ForgotPasswordNoti from './routes/SignIn/ForgotPassword/ForgotPasswordNoti.jsx'
import ResetPassword from './routes/SignIn/ForgotPassword/ResetPassword.jsx'
import SignUp from './routes/SignUp/SignUp.jsx'
import OrganizationSignup from './routes/SignUp/OrganizationSignUp.jsx'
import OrganizationProfile from './routes/Profile/OrganizationProfile.jsx'
import UserProfile from './routes/Profile/UserProfile.jsx'
import Home from './routes/Home/Home.jsx'
import Test from './routes/Test/Test.jsx'
import BuyTicket from './routes/BuyTicket/BuyTicket.jsx'
import Payment from './routes/Payment/Payment.jsx'
import Events from './routes/Events/Events.jsx'
import EventDetail from './routes/EventDetail/index.jsx'
import SuccessPage from './routes/SuccessPage/SuccessPage.jsx'
import { SearchProvider } from './components/Header/SearchContext.jsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    // errorElement: <Error />,
    children: [
      {path:"/", element:<Home />},
      {path:"signIn", element: <SignIn />},
      {path:"organizationsignIn", element: <OrganizationSignIn />},
      {path:"signUp", element: <SignUp />},
      {path:"organizationSignup", element: <OrganizationSignup />},
      {path:"forgotPassword", element: <ForgotPassword />},
      {path:"forgotPasswordNoti", element: <ForgotPasswordNoti />},
      {path:"resetPassword", element: <ResetPassword/>},
      {path:"userprofile", element: <UserProfile/>},
      {path:"organizationprofile", element: <OrganizationProfile/>},
      {path:"test", element: <Test />},
      {path:"buyticket", element: <BuyTicket />},
      {path:"payment", element: <Payment />},
      {path:"events", element: <Events />},
      {path:"events/:id", element: <EventDetail />},
      {path:"successpage", element: <SuccessPage />},
    ]
  }
  ])
  
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <SearchProvider>
      <RouterProvider router={router} />
    </SearchProvider>
  </React.StrictMode>,
)
