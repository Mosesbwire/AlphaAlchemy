import React from 'react'
import Button from '../Button/Button'
import useForm from '../../hooks/useForm'
import './Form.css'

const inputs = [
    {name: 'email', type: 'email', placeholder: 'Email Address'},
    {name: 'password', type: 'password', placeholder: 'Password'},
]

function LoginForm({onSubmit}){
    const initialValues = {email: "", password:""}
    const [values, handleChange, resetForm] = useForm(initialValues)

    const onSubmitForm = async(event) =>{
        event.preventDefault()
        await onSubmit(values)
        resetForm()
    }
    return(
        <form className='form' onSubmit={onSubmitForm}>
            {inputs.map((input)=>(
                <div key={input.name} className='input input-normal' id={input.name}>
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
                <Button primary rounded >Login</Button>
            </div>
        </form>
    )
}

export default LoginForm