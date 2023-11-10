import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import Layout from './components/Layout/Layout'
import Home from './pages/HomePage/Home'
import Portfolio from './pages/Portfolio/Portfolio'
import Order from './pages/Order/Order'
import Transaction from './pages/Transaction/Transaction'
import ToastContainer from './ToastContainer.jsx'
import RequireAuth from './components/RequireAuth.jsx'


import './App.css'

function App() {

  return (
    <>
      <ToastContainer />
      <Router>
        <Routes>
          <Route element={<Layout />}>
            <Route path="/home" element={<RequireAuth><Home /></RequireAuth>} />
            <Route path="/portfolio" element={<RequireAuth><Portfolio /></RequireAuth>} />
            <Route path="/portfolio/order" element={<RequireAuth><Order /></RequireAuth>} />
            <Route path="/portfolio/transactions" element={<RequireAuth><Transaction /></RequireAuth>} />
          </Route>
          <Route path="/login" element={<Login />} />
          <Route path="/sign-up" element={<SignUp />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
