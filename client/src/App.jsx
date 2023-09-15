import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import AuthContextProvider from './context/AuthContext'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import Layout from './components/Layout/Layout'
import Home from './pages/HomePage/Home'
import Portfolios from './pages/Portfolios/Portfolios'
import Portfolio from './pages/Portfolio/Portfolio'
import Buy from './pages/BuyPage/Buy'
import Transaction from './pages/Transaction/Transaction'
import apiService from './services/apiService'
import useFetch from './hooks/useFetch'
import './App.css'

function App() {
  
  return (
    <>
      <Router>
        <AuthContextProvider>
          <Routes>
            <Route element={<Layout/>}> 
              <Route path="/home" element={<Home/>}/>
              <Route path="/portfolios" element={<Portfolios/>}/>
              <Route path="/portfolio/:id" element={<Portfolio/>}/>
              <Route path="/portfolio/:id/buy" element={<Buy/>}/>
              <Route path="/transactions" element={<Transaction/>}/>
            </Route>
              <Route path="/login" element={<Login/>}/>
              <Route path="/sign-up" element={<SignUp/>}/>
          </Routes>      
        </AuthContextProvider>
      </Router>
    </>
  )
}

export default App
