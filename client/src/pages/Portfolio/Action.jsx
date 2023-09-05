import React from "react";
import Button from "../../components/Button/Button";
import './portfolio.css'

const Actions = ()=>{
    return (
        <div className="stock-action">
            <Button primary outline>Buy</Button>
            <Button secondary outline>Sell</Button>
        </div>
    )
}

export default Actions