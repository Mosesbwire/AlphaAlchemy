import React from "react";
import MarketStat from "./MarketStat";
import './TotalMarketStat.css'
const MarketStatistics = ({data})=>{
    return (
        <div className="market-stats-container container">
            <div  className="market-stats-wrapper">
                {data.map((dt)=> (
                    <div>
                        <MarketStat data={dt} key={dt.title}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MarketStatistics