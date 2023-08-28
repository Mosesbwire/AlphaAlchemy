import React from "react"
import Form from '../../components/AuthForm/LoginForm'
import Logo from "../../components/Logo/Logo"
import "./Login.css"

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
                <Form/>
                <div>
                    <p className="tag-line">Don't have an account? <span className="signup-link">Sign Up</span></p>
                </div>
            </div>
            <div className="section-white"></div>
        </div>
    )
}

export default Login