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

let dropDownData = [
    "All Sectors",
    "Agricultural",
    "AutoMobiles and Accessories",
    "Banking",
    "Commercial and Services",
    "Construction and Allied",
    "Energy and Petroleum",
    "Insuarance",
    "Investment",
    "Investment Services",
    "Manufaturing and Allied",
    "Telecommunication and Technology",
    "Real Estate Investment Trust",
    "Exchange Traded Fund"
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
            <div>
                <DropDown title={"Sector"} content={dropDownData}/>
            </div>
            <div>
                <Table/>
            </div>
            
        </div>
    )
}

export default Home