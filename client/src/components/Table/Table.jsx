import React from "react";
import TableHeader from "./TableHeader";
import TableRow from "./TableRow";
import './Table.css'

const Table = ({header, data, classes})=>{
    return (
        <div className="table container">
            <div>
                <div className="table-header_row">
                    <TableHeader header={header} classes={classes}/>
                </div>
                <div className="table-row_rows">
                    {data.map((dt) => (
                        <div>
                            <TableRow data={dt} classes={classes}/>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Table