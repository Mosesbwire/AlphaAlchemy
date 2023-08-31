import React, {useState} from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faCaretDown} from '@fortawesome/free-solid-svg-icons'
import './DropDown.css'

const DropDown = ({title, content})=>{
    const [openDrop, setOpenDropDown] = useState(false)

    const openDropDown = ()=>{
        setOpenDropDown(true)
    }

    const closeDropDown = ()=>{
        setOpenDropDown(false)
    }
    return (
        <div className="drop-down">
            <div className="drop-down-header">
                <p className="drop-down-title">{title}</p>
            </div>
            <div onMouseEnter={openDropDown} onMouseLeave={closeDropDown}>
                <div className="content-upper-section" >
                    <p>All Sectors</p>
                    <div className="drop-down-caret"><FontAwesomeIcon icon={faCaretDown}/></div>
                </div>
                {openDrop ?
                    <div className="drop-down-content">
                        {content.map(cnt => (
                            <div className="drop-down-text">{cnt}</div>
                        ))}
                    </div> : null}
                
            </div>
        </div>
    )
}

export default DropDown