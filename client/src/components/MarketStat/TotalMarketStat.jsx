import React from "react";
import { v4 as uuid } from "uuid"
import MarketStat from "./MarketStat";
import './TotalMarketStat.css'
const MarketStatistics = ({ data }) => {
    return (
        <div className="market-stats-container container">
            <div className="market-stats-wrapper">
                {data.map((dt) => (
                    <div key={uuid()}>
                        <MarketStat data={dt} key={dt.title} />
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MarketStatistics