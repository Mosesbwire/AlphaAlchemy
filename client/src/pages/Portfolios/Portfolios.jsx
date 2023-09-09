import React from "react";
import PortfolioSummary from "../../components/Portfolio/PortfolioSummary";
import Modal from "../../components/Modal/Modal";
import './Portfolio.css'

const Portfolios = ()=>{
    return(
    
            <div className="portfolios-wrapper container">
                <PortfolioSummary capital={30000} marketValue={10000}/>
                <PortfolioSummary capital={30000} marketValue={50000}/>
                <PortfolioSummary capital={50000} marketValue={50000}/>
                <PortfolioSummary capital={50000} marketValue={50000}/>
                <PortfolioSummary capital={50000} marketValue={70000}/>
            </div>
        
    )
}

export default Portfolios