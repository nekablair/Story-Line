import React from 'react'
import { createBrowserRouter } from 'react-router-dom'
import App from './App'
import Homepage from './pages/Homepage'
import Signup from './pages/Signup'
import Login from './pages/Login'
import ErrorPage from './pages/ErrorPage'
import Notfoundpage from './pages/Notfoundpage'


const router = createBrowserRouter([{
    path:'/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
        {
            index: true,
            element: <Homepage />
        },
        {
            path:"signup/",
            element: <Signup />
        },
        {
            path: "login/",
            element: <Login />
        },
        {
            path: "Notfoundpage",
            element: <Notfoundpage />
        },
    ]
}])

export default router
