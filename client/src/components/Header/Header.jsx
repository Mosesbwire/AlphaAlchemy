import React, {useState} from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faCircleXmark} from '@fortawesome/free-regular-svg-icons'
import {faBars} from '@fortawesome/free-solid-svg-icons'
import Logo from '../Logo/Logo'
import './Header.css'

const navItems = [
    {name:"Home"},
    {name:"New Portfolio"},
    {name:"Portfolios"},
    {name:"LogOut"}
]
const Header = ()=>{
    const [isOpen, setOpenMenu] = useState(false)
    const handleClick = ()=>{
        setOpenMenu(!isOpen)
        
    }
    return (
        <div>
            <div className="header-wrapper"> 
                <div className="logo pd-left"><Logo/></div>
                <div className="mobile-menu" onClick={handleClick}><FontAwesomeIcon icon={faBars}/></div>
                <div className={`nav pd-left pd-right ${isOpen ? 'show-menu' : ''}`}>
                    <ul className="nav-list">
                        <div className="close-btn" onClick={handleClick}>
                            <FontAwesomeIcon icon={faCircleXmark}/>
                        </div>
                        {navItems.map((item) => (
                            <li className="nav-links">{item.name}</li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default Header