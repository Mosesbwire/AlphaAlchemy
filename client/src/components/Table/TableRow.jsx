import React from "react";
import './Table.css'

const alpha = Array.from(Array(26)).map((e, i) => i + 65);
const alphabet = alpha.map((x) => String.fromCharCode(x));

const TableRow = ({data}) =>{
    return (
        <div className="table-row">
            {data.map((dt, idx) => (
                <div className={`${alphabet[idx]}-row`}>{dt}</div>
            ))}
        </div>
    )
}

export default TableRow