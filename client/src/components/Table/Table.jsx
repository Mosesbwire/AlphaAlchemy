import React from "react";
import TableHeader from "./TableHeader";
import TableRow from "./TableRow";
import DropDown from "../DropDown/DropDown";
import './Table.css'

const tableHeader = [
    "Ticker",
    "Prev",
    "Latest",
    "Change",
    "% Change",
    "High",
    "Low",
    "Volume",
    "Average"
]

const data = [
    ["BRIT", "5.18", "5.64", "0.64", "8.88%", "5.68", "5.20", "6,000", "5.64"],
    ["TPSE", "11.55", "12.50", "0.95", "8.23%", "12.50", "12.50", "5,000", "12.50"],
    ["HFCK", "4.71", "5.00", "0.29", "6.16%", "5.10", "4.40", "107,500", "4.97"],
    ["KNRE", "1.80", "1.89", "0.09", "5.00%", "1.90", "1.82", "2,100", "1.89"],
    ["ABSA", "11.50","11.60", "0.10","0.87% ","12.00","11.60", "17,600", "11.80"],
    ["KEGN", "2.21", "2.35", "0.14", "6.33% ", "2.35", "2.30", "6,700",	"2.34"]	
]

let dropDownData = [
    "All Sectors",
    "Agricultural",
    "AutoMobiles and Accessories",
    "Banking",
    "Commercial and Services",
    "Construction and Allied",
    "Energy and Petroleum",
    "Insuarance",
    "Investment",
    "Investment Services",
    "Manufaturing and Allied",
    "Telecommunication and Technology",
    "Real Estate Investment Trust",
    "Exchange Traded Fund"
]

const Table = ()=>{
    return (
        <div className="table container">
            <div>
                <div className="stock-sector-filter">
                    <DropDown title={"Sector"} content={dropDownData}/>
                </div>
                <div className="table-header_row">
                    <TableHeader header={tableHeader}/>
                </div>
                <div className="table-row_rows">
                    {data.map((dt) => (
                        <div>
                            <TableRow data={dt}/>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Table