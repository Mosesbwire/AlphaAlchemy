import React from "react";
import Form from "../../components/AuthForm/Form";
import Logo from "../../components/Logo/Logo";
import './SignUp.css'

let formInputs = [
    {name: 'first_name', type: 'text', placeholder: 'First Name'},
    {name: 'last_name', type: 'text', placeholder: 'Last Name'},
    {name: 'email', type: 'email', placeholder: 'Email Address'},
    {name: 'password', type: 'password', placeholder: 'Password'},
    {name: 'confirm_password', type: 'password', placeholder: 'Confirm Password'},
]

const SignUp = () => {
    return (
        <div className="sign-up-page">
            <div className="sign-up-hero-container container">
                <Logo/>
                <div className="sign-up-hero">
                    <h1>Trade Without Limits</h1>
                    <h1>Learn Without Loss</h1>
                    <h1>AlphaAlchemy</h1>
                    <h1>Your Virtual Advantage!</h1>
                </div>                  
            </div>
            <div className="form-section">
                <div className="tag-line top-tag-line">
                    <p>Virtual Investing, Real Learning. Sign Up Now</p>
                </div>
                <div>
                    <Form inputs={formInputs} btnText={'Sign Up'}/>
                </div>
                <div >
                    <p className="tag-line">Already have an account? <span className="login-link">Login</span></p>
                </div>
            </div>
        </div>
    )
}

export default SignUp