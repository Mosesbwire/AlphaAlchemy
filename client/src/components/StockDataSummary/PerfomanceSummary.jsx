import React, {useEffect, useRef} from "react";
import StockPerfomanceSummary from "./StockPerfomanceSummary";
import './PerfomanceSummary.css'




const PerfomanceSummary = ({gainers, losers, movers})=>{
    const summarySections = [
        {title: "Gainers", firstHeading: "Price", secondHeading: "Change", data: gainers},
        {title: "Losers", firstHeading: "Price", secondHeading: "Change", data: losers},
        {title: "Movers", firstHeading: "Volume", secondHeading: "", data: movers}
    ]
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