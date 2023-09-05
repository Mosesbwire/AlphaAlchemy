import React from "react";
import MarketStatistics from "../../components/MarketStat/TotalMarketStat";
import PerfomanceSummary from "../../components/StockDataSummary/PerfomanceSummary";
import Table from "../../components/Table/Table";
import Button from "../../components/Button/Button";

import './Home.css'

let marketData = [
    {title: "Equity Turnover", stat: "475.75M"},
    {title: "Shares Traded", stat: "24.75M"},
    {title: "Deals", stat: "1120"},
]

const tableHeader = [
    "Ticker",
    "Prev",
    "Latest",
    "Change",
    "% Change",
    "High",
    "Low",
    "Volume",
    "Average"
]

const classes = ['d-block', 'd-block', 'd-block', 'd-block', 'd-sm-none d-md-block',
    'd-sm-none d-md-block','d-sm-none d-md-block','d-sm-none d-md-block',
    'd-sm-none d-md-none d-lg-block'
]

const data = [
    ["BRIT", "5.18", "5.64", "0.64", "8.88%", "5.68", "5.20", "6,000", "5.64"],
    ["TPSE", "11.55", "12.50", "0.95", "8.23%", "12.50", "12.50", "5,000", "12.50"],
    ["HFCK", "4.71", "5.00", "0.29", "6.16%", "5.10", "4.40", "107,500", "4.97"],
    ["KNRE", "1.80", "1.89", "0.09", "5.00%", "1.90", "1.82", "2,100", "1.89"],
    ["ABSA", "11.50","11.60", "0.10","0.87% ","12.00","11.60", "17,600", "11.80"],
    ["KEGN", "2.21", "2.35", "0.14", "6.33% ", "2.35", "2.30", "6,700",	"2.34"]	
]


const Home = ()=>{
    
    return(
        <div>
            <div className="market-data">
                <MarketStatistics data={marketData}/>
            </div>
            <div className="daily-market-summary">
                <PerfomanceSummary/>
            </div>
            <div className="current-stock-data">
                <Table header={tableHeader} data={data} classes={classes}/>
            </div>    
        </div>
    )
}

export default Home