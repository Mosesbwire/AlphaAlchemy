import React, { useState } from 'react'
import Button from '../Button/Button'
import useForm from '../../hooks/useForm'
import './Form.css'

const inputs = [
    { name: 'first_name', type: 'text', placeholder: 'First Name' },
    { name: 'last_name', type: 'text', placeholder: 'Last Name' },
    { name: 'email', type: 'email', placeholder: 'Email Address' },
    { name: 'password', type: 'password', placeholder: 'Password' },
    { name: 'confirm_password', type: 'password', placeholder: 'Confirm Password' },

]

function SignUpForm({ onSubmit, error }) {
    const initialValues = sessionStorage.getItem("formData") ? JSON.parse(sessionStorage.getItem("formData")) :
        { first_name: "", last_name: "", email: "", password: "", confirm_password: "" }
    const [values, handleChange, resetForm] = useForm(initialValues)


    const [err, handleErrors] = useState(error ? error : null)


    const submitForm = async e => {
        e.preventDefault()
        sessionStorage.setItem("formData", JSON.stringify(values))
        onSubmit(values)
    }

    const inputChange = (e) => {
        handleChange(e)

        if (err) {
            const updatedErr = err.filter(er => er.hasOwnProperty(e.target.name))

            handleErrors(updatedErr)
        }

    }
    return (
        <form className='form' onSubmit={submitForm}>
            {inputs.map((input) => (
                <div key={input.name} className='input input-normal' id={input.name}>
                    <input
                        type={input.type}
                        name={input.name}
                        placeholder={input.placeholder}
                        value={values[input.name]}
                        onChange={e => inputChange(e)}

                    />
                    {err ? <>
                        {err.map((e, idx) => (
                            <small key={idx}>{e[input.name]}</small>
                        ))}
                    </> : null}
                </div>
            ))}

            <div className='btn-wrapper'>
                <Button primary rounded>Sign In</Button>
            </div>
        </form>
    )
}

export default SignUpForm