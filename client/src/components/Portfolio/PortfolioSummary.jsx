import React from "react";
import DoughnutChart from "../Chart/Doughnut/Doughnut";
import './PortfolioSummary.css'

const PortfolioSummary = ({ marketValue }) => {


    return (
        <div className={`portfolio__ portfolio__border_profit`}>
            <div className="chart-wrapper">
                <DoughnutChart />
            </div>
        </div>
    )
}

export default PortfolioSummary