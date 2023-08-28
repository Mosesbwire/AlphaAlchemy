import React from "react"
import Form from '../../components/AuthForm/Form'
import Logo from "../../components/Logo/Logo"
import "./Login.css"

let formInputs = [
    {name: 'email', type: 'email', placeholder: 'Email Address'},
    {name: 'password', type: 'password', placeholder: 'Password'},

]
const Login = ()=>{
    return (
        <div className="login-page">
            <div className="container section-dark">
                <div>
                    <Logo/>
                </div>
            </div>
            <div className="form-section-login">
                <p className="welcome-text">Hello Again</p>
                <p className="access-text">Login to Access your Account</p>
                
                <Form inputs={formInputs} btnText={"Login"}/>
                
                <div>
                    <p className="tag-line">Don't have an account? <span className="signup-link">Sign Up</span></p>
                </div>
            </div>
            <div className="section-white"></div>
        </div>
    )
}

export default Login