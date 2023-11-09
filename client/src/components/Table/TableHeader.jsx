import React from "react";
import { v4 as uuid } from "uuid"
import './Table.css'

const TableHeader = ({ header, classes }) => {
    return (
        <div className="table-header">
            {header.map((text, idx) => (
                <div className={`${classes[idx]}`} key={uuid()}>{text}</div>
            ))}
        </div>
    )
}

export default TableHeader