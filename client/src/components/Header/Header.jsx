import React, {useState, useEffect} from "react";
import {useNavigate} from "react-router-dom"
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faCircleXmark} from '@fortawesome/free-regular-svg-icons'
import {faBars} from '@fortawesome/free-solid-svg-icons'
import Modal from "../Modal/Modal";
import Logo from '../Logo/Logo'
import useModal from "../../hooks/useModal";
import CreatePortfolio from "../CreatePortfolio/CreatePortfolio";
import apiService from "../../services/apiService";
import useSubmitForm from "../../hooks/useSubmitForm";
import './Header.css'

const navItems = [
    {name:"Home"},
    {name:"New Portfolio"},
    {name:"Portfolios"},
    {name:"LogOut"}
]
const Header = ()=>{
    const [isOpen, setOpenMenu] = useState(false)
    const [openModal, modalHandler] = useModal()
    const [onSubmit, data, isSubmitting, error] = useSubmitForm(apiService.createPortfolio)
    const navigate = useNavigate()
    
    useEffect(()=>{
        if (!isSubmitting && data){
            modalHandler()
            navigate(`/portfolio/${data.id}`)
            
        }

        if (error){
            console.log(error)
        }
    }, [data, error, isSubmitting])
    const handleClick = ()=>{
        setOpenMenu(!isOpen)  
    }


    return (
        <>
            <Modal handleClick={modalHandler} open={openModal}>
                <CreatePortfolio onSubmit={onSubmit}/>
            </Modal>
            <div className="header">
                <div className="header-wrapper"> 
                    <div className="logo pd-left"><Logo/></div>
                    <div className="mobile-menu" onClick={handleClick}><FontAwesomeIcon icon={faBars}/></div>
                    <div className={`nav pd-left pd-right ${isOpen ? 'show-menu' : ''}`}>
                        <ul className="nav-list">
                            <div className="close-btn" onClick={handleClick}>
                                <FontAwesomeIcon icon={faCircleXmark}/>
                            </div>
                            {navItems.map((item) => (
                                <li className="nav-links" onClick={modalHandler}>{item.name}</li>
                            ))}
                        </ul>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Header