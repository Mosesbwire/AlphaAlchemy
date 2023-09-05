import React from "react"
import './stats.css'
const Stats = ({data})=>{
    return (
        <div className="portfolio-stat-container">
            {data.icon}
            <p className="portfolio-stat-title">{data.title}</p>
            <p className="portfolio-statistic">{data.stat}</p>
        </div>
    )
}

export default Stats