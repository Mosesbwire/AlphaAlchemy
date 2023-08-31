import React, {useEffect, useRef} from "react";
import StockPerfomanceSummary from "./StockPerfomanceSummary";
import './PerfomanceSummary.css'


const summarySections = [
    {title: "Gainers", firstHeading: "Price", secondHeading: "Change", data: [
        {ticker: "EQTY", price: "10.80", change: "+2.50"},
        {ticker: "WTK", price: "500.00", change: "+10.00"},
        {ticker: "SASN", price: "12.50", change: "+4.40"},
        {ticker: "KCB", price: "55.03", change: "+5.25"},
        {ticker: "SCOM", price: "15.80", change: "+7.50"},
    ]},
    {title: "Losers", firstHeading: "Price", secondHeading: "Change", data: [
        {ticker: "NCBA", price: "50.05", change: "-12.50"},
        {ticker: "BAT", price: "700.00", change: "-100.00"},
        {ticker: "NBV", price: "1.00", change: "-0.50"},
        {ticker: "SBIC", price: "12.10", change: "-1.25"},
        {ticker: "CNTM", price: "27.70", change: "-7.50"},
    ]},
    {title: "Movers", firstHeading: "Volume", secondHeading: "", data: [
        {ticker: "SCOM", volume: "5,462,300"},
        {ticker: "FAHR", volume: "4,854,000"},
        {ticker: "NCBA", volume: "512,300"},
        {ticker: "KCB", volume: "490,500"},
        {ticker: "KEGN", volume: "426,200"},
    ]}
]

const PerfomanceSummary = ()=>{
    const tabRef = useRef(null)
    const tabBtnRef = useRef(null)
    let btnTabs;

    useEffect(()=>{
        btnTabs = Array.from(tabBtnRef.current.children)
        btnTabs.forEach(tab =>{
            if (tab.classList.contains("Gainers-tab")){
                tab.click()
            }
        })
    }, [])

    const inactivateCurrentTab = (tab)=>{
        if (tab.classList.contains("active")){
            tab.classList.remove("active")
            tab.classList.add("inactive")
        }
    }
    const activateTab = (tab,tabClassName) =>{
        if (tab.classList.contains(tabClassName)){
            tab.classList.remove("inactive")
            tab.classList.add("active")
        }
    }

const targetClasses = [{btn: "Gainers-tab", tab: "Gainers"}, 
                        {btn: "Losers-tab", tab: "Losers"},
                        {btn: "Movers-tab", tab: "Movers"}
                    ]
    
    const handleClick = (e)=>{
        const tabs = Array.from(tabRef.current.children)
        btnTabs.forEach(btn =>{
            if (btn.classList.contains("active-indicator")){
                btn.classList.remove("active-indicator")
            }
        })
       
        targetClasses.forEach(targetClass =>{
            if (e.target.className === targetClass.btn){
                tabs.forEach(tab => {
                    inactivateCurrentTab(tab)
                    activateTab(tab, targetClass.tab)
                })
            } 
        })
        e.target.classList.add("active-indicator")
    }

    return(
        <div className="perfomance-summary-container container">
            <div className="tabs" onClick={e => handleClick(e)} ref={tabBtnRef}>
                {summarySections.map(section => (
                    <div className={`${section.title}-tab`}>{section.title}</div>
                ))}
            </div>
            <div ref={tabRef} className="perfomance-data">
                {summarySections.map((section)=> (
                    <div className={`section-data ${section.title} inactive`}>
                        <StockPerfomanceSummary section={section}/>
                    </div>
                ))}
            </div>
            
        </div>
    )
}

export default PerfomanceSummary