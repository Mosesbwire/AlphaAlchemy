import React from "react";
import classNames from 'classnames'
import './Button.css'

const Button = ({children, primary, secondary, rounded, outline, neutral})=>{
    const classes = classNames("btn", {
        "primary": primary,
        "secondary": secondary,
        "neutral": neutral,
        "rounded": rounded && primary,
        "outline-primary": outline && primary,
        "outline-secondary": outline && secondary,
    })
    return (
        <button className={classes}>{children}</button>
    )
}

export default Button