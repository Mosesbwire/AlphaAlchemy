import React from 'react'
import './Button.css'

function Button({text}) {
    return (
        <button type='submit' className='auth-btn'>
            {text}
        </button>
    )
}

export default Button