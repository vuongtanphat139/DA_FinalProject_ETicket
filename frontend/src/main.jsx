import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import SignIn from './routes/SignIn/SignIn.jsx'
import ForgotPassword from './routes/SignIn/ForgotPassword/ForgotPassword.jsx'
import ForgotPasswordNoti from './routes/SignIn/ForgotPassword/ForgotPasswordNoti.jsx'
import ResetPassword from './routes/SignIn/ForgotPassword/ResetPassword.jsx'
import SignUp from './routes/SignUp/SignUp.jsx'
import Home from './routes/Home/Home.jsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    // errorElement: <Error />,
    children: [
      {path:"/", element:<Home />},
      {path:"signIn", element: <SignIn />},
      {path:"forgotPassword", element: <ForgotPassword />},
      {path:"forgotPasswordNoti", element: <ForgotPasswordNoti />},
      {path:"resetPassword", element: <ResetPassword/>},
      {path:"signUp", element: <SignUp />}
    ]
  }
  ])
  
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
