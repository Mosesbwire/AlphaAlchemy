import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import SignUp from './pages/SignUpPage/SignUp'
import Login from './pages/LoginPage/Login'
import './App.css'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={<Login/>}/>
          <Route path="/sign-up" element={<SignUp/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
