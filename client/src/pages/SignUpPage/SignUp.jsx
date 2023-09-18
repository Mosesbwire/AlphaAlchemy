import React from "react";
import {Navigate} from 'react-router-dom'
import Form from "../../components/AuthForm/SignUpForm";
import Logo from "../../components/Logo/Logo";
import apiService from "../../services/apiService";
import useSubmitForm from "../../hooks/useSubmitForm";
import Loading from "../../components/Loader/Loading";
import './SignUp.css'

const SignUp = () => {
    const [onSubmit, data, isSubmitting, error] = useSubmitForm(apiService.createUser)

    if (isSubmitting){
        return <Loading/>
    }

    if(error){
        console.log(error)
    }

    if (data){
        return <Navigate to="/home" replace={true}/>
    }
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
                    <Form onSubmit={onSubmit}/>
                </div>
                <div >
                    <p className="tag-line">Already have an account? <span className="login-link">Login</span></p>
                </div>
            </div>
        </div>
    )
}

export default SignUp