import React from "react";
import Header from "../../components/Header/Header";
import MarketStatistics from "../../components/MarketStat/TotalMarketStat";
import PerfomanceSummary from "../../components/StockDataSummary/PerfomanceSummary";
import DropDown from "../../components/DropDown/DropDown";
import Table from "../../components/Table/Table";

import './Home.css'

let data = [
    {title: "Equity Turnover", stat: "475.75M"},
    {title: "Shares Traded", stat: "24.75M"},
    {title: "Deals", stat: "1120"},
]


const Home = ()=>{
    
    return(
        <div>
            <div className="header">
                <Header/>
            </div>
            <div className="market-data">
                <MarketStatistics data={data}/>
            </div>
            <div className="daily-market-summary">
                <PerfomanceSummary/>
            </div>
            <div className="current-stock-data">
                <Table/>
            </div>
            
        </div>
    )
}

export default Home