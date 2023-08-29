import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import Home from './pages/HomePage/Home'
import './App.css'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={<Login/>}/>
          <Route path="/sign-up" element={<SignUp/>}/>
          <Route path="/home" element={<Home/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
