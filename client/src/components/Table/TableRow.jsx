import React from "react";
import './Table.css'

const TableRow = ({data, classes}) =>{
    return (
        <div className="table-row">
            {data.map((dt, idx) => (
                <div className={`${classes[idx]}`}>{dt}</div>
            ))}
        </div>
    )
}

export default TableRow