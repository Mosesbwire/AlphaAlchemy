import React from "react";
import { Link } from "react-router-dom";
import Button from "../../components/Button/Button";
import './portfolio.css'

const Actions = ({id, stock})=>{
    return (
        <div className="stock-action">
            <Link to={`/portfolio/${id}/order?action=buy&stock=${stock}`}>
                <Button primary outline>Buy</Button>
            </Link>
            <Link to={`/portfolio/${id}/order?action=sell&stock=${stock}`}>
                <Button secondary outline>Sell</Button>
            </Link>
        </div>
    )
}

export default Actions