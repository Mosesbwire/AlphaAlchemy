import React from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faCaretUp, faCaretDown} from '@fortawesome/free-solid-svg-icons'
import './StockPerfomanceSummary.css'


const StockPerfomanceSummary = ({section})=>{
    const classes = {Gainers:"gainers", Losers: "losers", Movers: "movers"}
    const carets = {Gainers: faCaretUp, Losers:faCaretDown, Movers: ""}
    return(
        <div className="stock-perfomance-summary">
            <div className={`title ${classes[section.title]}`}>
                <p>{section.title}</p>
            </div>
            <div className={`heading`}>
                <div className="heading-wrapper row">
                    <p>{section.firstHeading}</p>
                    <p>{section.secondHeading}</p>
                </div>
            </div>
            <div className="data-section">
                {section.data.map(data => (
                    <div className="data-row row">
                        {section.title !== "Movers" ? 
                        <>
                            <p>{data.ticker}</p>
                            <p>{data.price}</p>
                            <p className={`${classes[section.title]}-change`}>{data.change}<span><FontAwesomeIcon icon={carets[section.title]}/></span></p>

                        </> : 
                        <>
                            <p>{data.ticker}</p>
                            <p>{data.volume}</p>
                        </>}
                    </div>
                ))}

            </div>
        </div>
    )
}

export default StockPerfomanceSummary