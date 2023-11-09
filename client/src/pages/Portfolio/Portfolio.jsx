import React from "react";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMoneyBillAlt } from '@fortawesome/free-solid-svg-icons'
import Stats from "../../components/Portfolio/PortfolioStat/Stats";
import Table from "../../components/Table/Table";
import Button from "../../components/Button/Button";
import Loading from "../../components/Loader/Loading";
import DoughnutChart from "../../components/Chart/Doughnut/Doughnut";
import Actions from "./Action";
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch"
import './portfolio.css'


const Portfolio = () => {

    const [data, error, isLoading] = useFetch(apiService.getPortfolio)
    const marketValue = data ? data.market_valuation : 0
    const stocks = data ? data.stocks : []


    const holdingsHeader = [
        "name", "ticker", "market value", "quantity", "% weight", "price", "actions"
    ]
    const holdings = []
    let chartData = {}
    if (stocks) {
        const labels = []
        const data = []
        stocks.map(stock => {
            const stockData = []
            stockData.push(stock.name)
            stockData.push(stock.ticker)
            stockData.push((stock.price * stock.quantity).toFixed())
            stockData.push(stock.quantity)
            stockData.push((((stock.price * stock.quantity) / marketValue) * 100).toFixed())
            stockData.push(stock.price)
            stockData.push(<Actions stock={stock.ticker} />)
            holdings.push(stockData)
            labels.push(stock.ticker)
            data.push(stock.quantity)

        })
        chartData.labels = labels
        chartData.data = data
        chartData.label = "# of stocks"
    }

    const classes = [
        "d-sm-none d-md-block", "d-block", "d-sm-none d-md-none d-lg-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block"
    ]
    if (isLoading) {
        return <Loading />
    }

    if (error) {
        console.log(error)
        return <div className="no-portfolio">
            <h1>No portfolio linked to this account. <span className="create-portfolio__link">Click New portfolio to create portfolio</span>.</h1>
        </div>
    }
    return (
        <div className="">
            <div className="portfolio-actions">
                <Link to={`/portfolio/order?action=buy&stock=no-stock`}>
                    <Button primary outline >Buy</Button>
                </Link>
                <Button secondary outline>Sell All</Button>
                <Link to={`/portfolio/transactions`}>
                    <Button neutral >Transactions</Button>
                </Link>
            </div>
            <div className="container portfolio-stats">
                <div>
                    <Stats data={{ title: "Market Value", stat: marketValue, icon: <FontAwesomeIcon icon={faMoneyBillAlt} /> }} />
                </div>
                <div className="chart">
                    <DoughnutChart userData={chartData} />
                </div>
            </div>

            <div className="holdings">
                <div className="container">
                    <p>Holdings</p>
                </div>
                {stocks.length > 0 ?
                    <Table header={holdingsHeader} data={holdings} classes={classes} />
                    : <div className="stocks-info">No stocks available in this portfolio. Click the buy button to view stocks you can purchase.</div>}
            </div>
        </div>
    )
}

export default Portfolio