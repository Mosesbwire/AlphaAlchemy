import React, { useRef } from "react"
import { Navigate, Link } from 'react-router-dom'
import Form from '../../components/AuthForm/LoginForm'
import Logo from "../../components/Logo/Logo"
import Loading from "../../components/Loader/Loading"
import useSubmitForm from "../../hooks/useSubmitForm"
import apiService from "../../services/apiService"
import { useAuthContext } from "../../context/AuthContext"
import { toast } from "react-toastify"
import { v4 as uuid } from "uuid"
import "./Login.css"

const Login = () => {
    const [onSubmit, data, isSubmitting, error] = useSubmitForm(apiService.login)
    const { isAuthenticated, setIsAuthenticated } = useAuthContext()
    const toastId = useRef(null)
    if (isSubmitting) {
        return <Loading />
    }

    if (error) {
        const err_msg = error === "User not found" ? `No account associated with provided email. Sign up` : `Invalid password`
        if (!toast.isActive(toastId.current)) {
            toastId.current = toast.error(err_msg, {
                position: toast.POSITION.TOP_CENTER,
                autoClose: false,
                theme: "light"
            })
        }
    }

    if (data && !isSubmitting) {
        // setIsAuthenticated(true)
        return <Navigate to={"/home"} replace={true} />
    }

    return (
        <div className="login-page">
            <div className="container section-dark">
                <div>
                    <Logo />
                </div>
            </div>
            <div className="form-section-login">
                <p className="welcome-text">Hello Again</p>
                <p className="access-text">Login to Access your Account</p>
                <Form onSubmit={onSubmit} />
                <div>
                    <p className="tag-line">Don't have an account?
                        <Link to={'/sign-up'}>
                            <span className="signup-link">Sign Up</span>
                        </Link>
                    </p>
                </div>
            </div>
            <div className="section-white"></div>
        </div>
    )
}

export default Login
