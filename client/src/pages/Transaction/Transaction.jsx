import React from "react";
import {useParams} from 'react-router-dom'
import Table from "../../components/Table/Table"
import './Transaction.css'

const Transaction = ()=>{
    const  { name } = useParams()
    const header = ["date", "type", "security", "shares", "price","total cost"]
    const data =[["10/10/23", "buy", "LKL", "1000", "12.00", "12000"],
    ["10/10/23", "sell", "SASN", "100", "25.00", "2500.00"]
    ]
    const classes = ["d-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block", "d-block"]
    return (
        <div>
            <div className="container">
                <div className="transaction-header">
                    <p>{name}</p>
                </div>
                <div className="transaction-summary">
                    <div className="transaction-summary_category balance-category">
                        <div className="summary_title">
                            <p>Balance</p>
                        </div>
                        <p className="trs-summary-data">KES 90,000</p>
                    </div>
                    <div className="transaction-summary_category cash-flow-category">
                        <div className="summary_title">
                            <p>Transactions</p>
                        </div>
                        <div className="trs-summary-data">
                            <small >Buy</small>
                            <p>KES 15,000</p>
                        </div>
                        <div className="trs-summary-data">
                            <small>Sell</small>
                            <p>KES 18,000</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="container">
                <div className="transaction-filters">
                    <p className="selected-filter">All Transactions</p>
                    <p>Buy</p>
                    <p>Sell</p>
                </div>
            </div>
            <div>
                <Table header={header} classes={classes} data={data}/>
            </div>
        </div>
    )
}

export default Transaction