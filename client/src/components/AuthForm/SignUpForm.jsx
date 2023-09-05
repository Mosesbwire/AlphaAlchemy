import React from 'react'
import Button from '../Button/Button'
import useForm from '../../hooks/useForm'
import apiService from '../../services/apiService'
import './Form.css'

const inputs = [
    {name: 'first_name', type: 'text', placeholder: 'First Name'},
    {name: 'last_name', type: 'text', placeholder: 'Last Name'},
    {name: 'email', type: 'email', placeholder: 'Email Address'},
    {name: 'password', type: 'password', placeholder: 'Password'},
    {name: 'confirm_password', type: 'password', placeholder: 'Confirm Password'},

]

function SignUpForm(){
    const initialValues = {first_name: "", last_name: "",email: "", password:"", confirm_password: ""}
    const [values, handleChange, resetForm] = useForm(initialValues)

    const onSubmit = async(event) =>{
        event.preventDefault()
        console.log(values)
        const data = await apiService.createUser(values)
        console.log(data)
        resetForm()
    }
    return(
        <form className='form' onSubmit={onSubmit}>
            {inputs.map((input)=>(
                <div key={input.name} className='input' id={input.name}>
                    <input
                        type={input.type} 
                        name={input.name} 
                        placeholder={input.placeholder}
                        value = {values[input.name]}
                        onChange={e => handleChange(e)}
                    />
                </div>
            ))}

            <div className='btn-wrapper'>
                <Button primary rounded>Sign In</Button>
            </div>
        </form>
    )
}

export default SignUpForm