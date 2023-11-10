import React from "react";
import { DateTime } from "luxon"
import Table from "../../components/Table/Table"
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch";
import { formattedDate } from "../../services/processData"
import './Transaction.css'

const Transaction = () => {

    const [transactionData, error, isLoading] = useFetch(apiService.fetchPortfolioTransactions)
    const header = ["date", "type", "security", "shares", "price", "cost"]
    let data = []
    const user = JSON.parse(sessionStorage.getItem("user"))
    let totalBuys = 0
    let totalSells = 0
    if (transactionData) {
        transactionData.forEach(transaction => {

            let tdata = [
                formattedDate(transaction.created_at),
                transaction.transaction_type,
                transaction.item,
                transaction.quantity,
                transaction.price,
                transaction.total
            ]

            if (transaction.transaction_type === "buy") {
                totalBuys += +transaction.total
            } else {
                totalSells += +transaction.total
            }

            data.push(tdata)
        })
    }

    const clickHandler = (e) => {
        console.log('clicked')
        console.log(e.target.innerText.toLowerCase())
        let dt = transactionData.filter(tr => tr.transaction_type === e.target.innerText.toLowerCase())
        console.log(dt)
    }
    const classes = ["d-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block", "d-block"]
    return (
        <div>
            <div className="container">
                <div className="transaction-header">

                </div>
                <div className="transaction-summary">
                    <div className="transaction-summary_category balance-category">
                        <div className="summary_title">
                            <p>Balance</p>
                        </div>
                        <p className="trs-summary-data">KES {"50,000"}</p>
                    </div>
                    <div className="transaction-summary_category cash-flow-category">
                        <div className="summary_title">
                            <p>Transactions</p>
                        </div>
                        <div className="trs-summary-data">
                            <small >Buy</small>
                            <p>KES {totalBuys}</p>
                        </div>
                        <div className="trs-summary-data">
                            <small>Sell</small>
                            <p>KES {totalSells}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="container">
                <div className="transaction-filters" onClick={e => clickHandler(e)}>
                    <p className="selected-filter">All Transactions</p>
                    <p>Buy</p>
                    <p>Sell</p>
                </div>
            </div>
            <div>
                <Table header={header} classes={classes} data={data} />
            </div>
        </div>
    )
}

export default Transaction