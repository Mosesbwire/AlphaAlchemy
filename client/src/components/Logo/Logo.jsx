import { Link } from "react-router-dom"
import './Logo.css'

function Logo() {
    return (
        <div className='logo'>
            <Link to={'/home'}>
                <p>ALPHAALCHEMY.</p>
            </Link>
        </div>
    )
}

export default Logo