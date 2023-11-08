import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import AuthContextProvider from './context/AuthContext'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import Layout from './components/Layout/Layout'
import Home from './pages/HomePage/Home'
import Portfolio from './pages/Portfolio/Portfolio'
import Order from './pages/Order/Order'
import Transaction from './pages/Transaction/Transaction'
import ToastContainer from './ToastContainer.jsx'


import './App.css'

function App() {

  return (
    <>
      <ToastContainer />
      <Router>
        <AuthContextProvider>
          <Routes>
            <Route element={<Layout />}>
              <Route path="/home" element={<Home />} />
              <Route path="/portfolio" element={<Portfolio />} />
              <Route path="/portfolio/order" element={<Order />} />
              <Route path="/portfolio/:name/:id/transactions" element={<Transaction />} />
            </Route>
            <Route path="/login" element={<Login />} />
            <Route path="/sign-up" element={<SignUp />} />
          </Routes>
        </AuthContextProvider>
      </Router>
    </>
  )
}

export default App
