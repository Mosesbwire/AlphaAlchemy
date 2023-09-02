import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import Layout from './components/Layout/Layout'
import Home from './pages/HomePage/Home'
import Portfolios from './pages/Portfolios/Portfolios'
import './App.css'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route element={<Layout/>}> 
            <Route path="/home" element={<Home/>}/>
            <Route path="/portfolios" element={<Portfolios/>}/>
          </Route>
            <Route path="/login" element={<Login/>}/>
            <Route path="/sign-up" element={<SignUp/>}/>
        </Routes>
        
      </Router>
    </>
  )
}

export default App
