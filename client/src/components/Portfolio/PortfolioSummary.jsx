import React, {useState} from "react";
import DoughnutChart from "../Chart/Doughnut/Doughnut";
import './PortfolioSummary.css'

const PortfolioSummary = ({capital, marketValue})=>{
    
    const delta = marketValue - capital
    let isProfit = delta > 0
    return (
        <div className={`portfolio__ ${isProfit ? 'portfolio__border_profit' : 'portfolio__border_loss'}`}>
            <div className="chart-wrapper">
                <DoughnutChart/>
            </div>
            <div className="portfolio-overview">
                <div className="port_overview_row">
                    <p className="f1">Capital:</p>
                    <p>{capital}</p>
                </div>
                <div className="port_overview_row">
                    <p className="f1">Market Value:</p>
                    <p>{marketValue}</p>
                </div>
                <div className="port_overview_row">
                    {isProfit ? <p className="f1">Profit</p> : <p className="f1">Loss</p>}
                    <p className={`${isProfit ? 'profit': 'loss'}`}>{delta}</p>    
                </div>
            </div>
        </div>
    )
}

export default PortfolioSummary