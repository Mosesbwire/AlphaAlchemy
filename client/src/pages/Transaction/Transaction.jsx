import React from "react";
import Table from "../../components/Table/Table"
import './Transaction.css'

const Transaction = ()=>{
    const header = ["date", "type", "security", "shares", "price","total cost"]
    const data =[["10/10/2023", "buy", "LKL", "1000", "12.00", "12000"],
    ["10/10/2023", "sell", "SASN", "100", "25.00", "2500.00"]
    ]
    const classes = ["d-block", "d-sm-none d-md-block", "d-sm-none d-md-block", "d-block", "d-block", "d-block"]
    return (
        <div>
            <div className="transaction-header container">
                <h2>Your Transaction Details</h2>
            </div>
            <Table header={header} classes={classes} data={data}/>
        </div>
    )
}

export default Transaction