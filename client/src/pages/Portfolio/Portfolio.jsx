import React from "react";
import { useParams, Link } from "react-router-dom";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faChartLine, faMoneyBillAlt} from '@fortawesome/free-solid-svg-icons'
import Stats from "../../components/Portfolio/PortfolioStat/Stats";
import Table from "../../components/Table/Table";
import Button from "../../components/Button/Button";
import Actions from "./Action";
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch"
import './portfolio.css'



const Portfolio = ()=>{
    const { id } = useParams()
    const [data, error, isLoading] = useFetch(apiService.getPortfolioById, id)
    const capital = data ? data.capital : 0
    const marketValue = data ? data.valuation : 0
    const change = data ? (data.roi * 100).toFixed(2) : 0
    const name = data ? data.name : 'Portfolio'
    const stocks = data ? data.stocks: []
    
    const portfolioData = [
        {title: "Capital Employed", stat: capital, icon: <FontAwesomeIcon icon={faMoneyBillAlt}/>},
        {title: "Return On Investment", stat: !change ? 0: change, icon: <FontAwesomeIcon icon={faChartLine}/>},
        {title: "Market Value", stat: marketValue, icon: <FontAwesomeIcon icon={faMoneyBillAlt}/>}
    ]

    const holdingsHeader = [
        "name","ticker", "market value", "quantity", "% weight", "price", "actions"
    ]
    const holdings = []
    if (stocks){
        stocks.map(stock =>{
            const stockData = []
            stockData.push(stock.name)
            stockData.push(stock.ticker)
            stockData.push(stock.current_value)
            stockData.push(stock.quantity)
            stockData.push(`${stock.weight * 100}%`)
            stockData.push(stock.current_unit_price)
            stockData.push(<Actions id={id} stock={stock.ticker}/>)
            holdings.push(stockData)

        })
    }
    
    const classes = [
        "d-sm-none d-md-block","d-block", "d-sm-none d-md-none d-lg-block","d-sm-none d-md-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block"
    ]
    if (isLoading){
        return <div>Loading...</div>
    }

    if (error){
        console.log(error)
        return <div>Error Occured. 404</div>
    }
    const selectedStock ="SCOM"
    return(
        <div className="">
            <div className="portfolio-name container">
                <p>Name: <span className="portfolio-name_span">{name}</span></p>
            </div>
            <div className="portfolio-actions">
                <Link to={`/portfolio/${id}/order?action=buy&stock=no-stock`}>
                    <Button primary outline >Buy</Button>
                </Link>
                <Button secondary outline>Sell All</Button>
                <Link to={`/portfolio/${name}/${id}/transactions`}>
                    <Button neutral >Transactions</Button>
                </Link>
            </div>
            <div className="container portfolio-stats">
                {portfolioData.map(data => (
                    <Stats data={data}/>
                ))}
            </div>
            <div className="holdings">
                <div className="container">
                    <p>Holdings</p>
                </div>
                {stocks.length > 0 ?
                    <Table header={holdingsHeader} data={holdings} classes={classes}/>
                : <div>Click here to buy stocks for your portfolio</div>}
            </div>
        </div>
    )
}

export default Portfolio