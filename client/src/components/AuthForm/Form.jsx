import React from 'react'
import Button from '../AuthBtn/Button'
import './Form.css'

function Form({inputs, btnText,}){
    return(
        <form className='form'>
            {inputs.map((input)=>(
                <div key={input.name} className='input' id={input.name}>
                    <input type={input.type} name={input.name} placeholder={input.placeholder}/>
                </div>
            ))}

            <div className='btn'>
                <Button text = {btnText} />
            </div>
        </form>
    )
}

export default Form