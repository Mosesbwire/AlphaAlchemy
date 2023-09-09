import React, {useEffect} from "react"
import {Navigate} from 'react-router-dom'
import Form from '../../components/AuthForm/LoginForm'
import Logo from "../../components/Logo/Logo"
import useSubmitForm from "../../hooks/useSubmitForm"
import apiService from "../../services/apiService"
import { useAuthContext } from "../../context/AuthContext"
import "./Login.css"

const Login = ()=>{
    const [onSubmit, data, isSubmitting, error] = useSubmitForm(apiService.login)
    const authContext = useAuthContext();
    const {isAuthenticated, setIsAuthenticated} = authContext
    useEffect(()=>{
        if(data){
            setIsAuthenticated(true)
        }
    }, [data])
   

    if (isSubmitting){
        return <div>Loading...</div>
    }

    if (error){
        console.log(error)
    }

    if (isAuthenticated){
        return <Navigate to={"/home"} replace={true}/>
    }
    
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
                <Form onSubmit={onSubmit}/>
                <div>
                    <p className="tag-line">Don't have an account? <span className="signup-link">Sign Up</span></p>
                </div>
            </div>
            <div className="section-white"></div>
        </div>
    )
}

export default Login