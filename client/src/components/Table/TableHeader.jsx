import React from "react";
import './Table.css'

const alpha = Array.from(Array(26)).map((e, i) => i + 65);
const alphabet = alpha.map((x) => String.fromCharCode(x));

const TableHeader = ({header})=>{
    return (
        <div className="table-header">
            {header.map((text, idx) => (
                <div className={`${alphabet[idx]}-header`}>{text}</div>
            ))}
        </div>
    )
}

export default TableHeader