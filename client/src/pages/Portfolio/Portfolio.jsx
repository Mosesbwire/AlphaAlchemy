import React from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faMoneyBill1} from '@fortawesome/free-regular-svg-icons'
import {faChartLine, faMoneyBills,faMoneyBill, faMoneyBillAlt} from '@fortawesome/free-solid-svg-icons'
import Stats from "../../components/Portfolio/PortfolioStat/Stats";
import Table from "../../components/Table/Table";
import Button from "../../components/Button/Button";
import Actions from "./Action";
import './portfolio.css'



const Portfolio = ()=>{
    const portfolioData = [
        {title: "Capital Employed", stat: "13000", icon: <FontAwesomeIcon icon={faMoneyBillAlt}/>},
        {title: "Gain", stat: "25%", icon: <FontAwesomeIcon icon={faChartLine}/>},
        {title: "Market Value", stat: "17000", icon: <FontAwesomeIcon icon={faMoneyBillAlt}/>}
    ]

    const holdingsHeader = [
        "name","ticker", "capital", "value", "change", "quantity", "price", "actions"
    ]
    const holdings = [
        [
            "KCB", "KCB", "30000", "35000", "5000", "3000","30",<Actions/>
        ],
        [
            "SCOM","SCOM","10000","35000","25000", "4000","10", <Actions/>
        ],
        [
            "EQTY", "EQTY", "30000","35000","5000","3000","30", <Actions/>
        ],
        [
            "SASN", "SASN", "10000","35000","25000","3000","30", <Actions/>
        ],
    ]

    const classes = [
        "d-sm-none d-md-block","d-block", "d-sm-none d-md-none d-lg-block","d-sm-none d-md-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block"
    ]

    return(
        <div className="">
            <div className="portfolio-name container">
                <p>Name: <span className="portfolio-name_span">Growth Portfolio</span></p>
            </div>
            <div className="portfolio-actions">
                <Button primary outline >Buy</Button>
                <Button secondary outline>Sell All</Button>
                <Button neutral >Transactions</Button>
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
                <Table header={holdingsHeader} data={holdings} classes={classes}/>
            </div>
        </div>
    )
}

export default Portfolio