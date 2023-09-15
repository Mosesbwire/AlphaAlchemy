import React from "react";
import DoughnutChart from "../Chart/Doughnut/Doughnut";
import './PortfolioSummary.css'

const PortfolioSummary = ({name, marketValue})=>{
    
    const delta = 2
    let isProfit = delta > 0
    return (
        <div className={`portfolio__ ${isProfit ? 'portfolio__border_profit' : 'portfolio__border_loss'}`}>
            <div className="chart-wrapper">
                <DoughnutChart/>
            </div>
            <div className="portfolio-overview">
                <div className="port_overview_row">
                    <p className="f1">Name:</p>
                    <p>{name}</p>
                </div>
                <div className="port_overview_row">
                    <p className="f1">Market Value:</p>
                    <p>{marketValue}</p>
                </div>
            </div>
        </div>
    )
}

export default PortfolioSummary