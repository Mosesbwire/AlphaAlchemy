import React from "react";
import { v4 as uuid } from "uuid"
import './Table.css'

const TableRow = ({ data, classes }) => {
    return (
        <div className="table-row">
            {data.map((dt, idx) => (
                <div className={`${classes[idx]}`} key={uuid()}>{dt}</div>
            ))}
        </div>
    )
}

export default TableRow