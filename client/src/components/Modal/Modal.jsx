
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import { faClose } from '@fortawesome/free-solid-svg-icons'
import './Modal.css'

const Modal = ({children, handleClick, open})=> {
    
    return (
        open ?
        <div className="modal" id="modal" onClick={handleClick}>
            <div className="modal-item">
                <div className='close-modal-btn close-modal' onClick={handleClick}>
                    <FontAwesomeIcon icon={faClose} className='close-modal' onClick={handleClick}/>
                </div>
                <div onClick={e => e.stopPropagation()}>
                    {children}
                </div>
            </div>
        </div> : null
    )
}

export default Modal