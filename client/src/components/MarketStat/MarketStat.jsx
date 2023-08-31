import React from "react";
import './MarketStat.css'

const MarketStat = ({data})=>{
    return (
        <div className="stat-container">
            <p className="stat-title">{data.title}</p>
            <p className="market-statistic">{data.stat}</p>
        </div>
    )
}

export default MarketStat