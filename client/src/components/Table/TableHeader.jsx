import React from "react";
import './Table.css'

const TableHeader = ({header, classes})=>{
    return (
        <div className="table-header">
            {header.map((text, idx) => (
                <div className={`${classes[idx]}`}>{text}</div>
            ))}
        </div>
    )
}

export default TableHeader