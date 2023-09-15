import React from "react";
import MarketStatistics from "../../components/MarketStat/TotalMarketStat";
import PerfomanceSummary from "../../components/StockDataSummary/PerfomanceSummary";
import Table from "../../components/Table/Table";
import { useAuthContext } from "../../context/AuthContext";
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch";
import {prepMarketData, prepStockData} from "../../services/processData"
import './Home.css'

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

const Home = ()=>{
    const [data, error, isLoading] = useFetch(apiService.getMarketMetrics)
    useFetch(apiService.getLoggedInUser)
    
    const marketData = data ? prepMarketData(data["market_metrics"]) : []
    const gainers = data ? data["gainers"] : []
    const losers = data ? data["losers"] : []
    const movers = data ? data["movers"]: []
    const stocks = data ? prepStockData(data["stocks"]): []

    if (error){
        
        return <div>Error occured</div>
    }

    if (isLoading){
        return <div>Loading....</div>
    }

    return(
        <div>
            <div className="market-data">
                <MarketStatistics data={marketData}/>
            </div>
            <div className="daily-market-summary">
                <PerfomanceSummary gainers={gainers} losers={losers} movers={movers}/>
            </div>
            <div className="current-stock-data">
                <Table header={tableHeader} data={stocks} classes={classes}/>
            </div>    
        </div>
    
    
    )
}

export default Home