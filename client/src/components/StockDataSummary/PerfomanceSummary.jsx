import React, { useEffect, useRef } from "react";
import StockPerfomanceSummary from "./StockPerfomanceSummary";
import { v4 as uuid } from "uuid"
import './PerfomanceSummary.css'


const PerfomanceSummary = ({ gainers, losers, movers }) => {
    const summarySections = [
        { title: "Gainers", firstHeading: "Price", secondHeading: "Change", data: gainers },
        { title: "Losers", firstHeading: "Price", secondHeading: "Change", data: losers },
        { title: "Movers", firstHeading: "Volume", secondHeading: "", data: movers }
    ]

    const targetClasses = [{ btn: "Gainers-tab", tab: "Gainers" },
    { btn: "Losers-tab", tab: "Losers" },
    { btn: "Movers-tab", tab: "Movers" }
    ]
    const activateTab = (target, className) => {
        if (target.classList.contains(className)) {
            target.classList.remove("inactive")
            target.classList.add("active")
        }
    }

    const inactivateCurrentTab = (target) => {
        if (target.classList.contains("active")) {
            target.classList.remove("active")
            target.classList.add("inactive")
        }
    }

    const tabBtns = useRef(null)
    const tabs = useRef(null)

    const handleTabClick = (e) => {

        if (tabBtns.current && tabs.current) {
            const tabChildren = Array.from(tabs.current.children)

            Array.from(tabBtns.current.children).forEach(btn => {
                if (btn.classList.contains("active-indicator")) {
                    btn.classList.remove("active-indicator")
                }
            })
            targetClasses.forEach(tc => {
                if (e.target.className === tc.btn) {
                    tabChildren.forEach(tab => {
                        inactivateCurrentTab(tab)
                        activateTab(tab, tc.tab)
                    })
                }
            })
            e.target.classList.add("active-indicator")
        }
    }

    useEffect(() => {
        const btns = document.getElementById("tabs")

        const defaultTabBtn = btns.children[0]

        defaultTabBtn.click()

    }, [])

    return (
        <div className="perfomance-summary-container container">
            <div className="tabs" id="tabs" ref={tabBtns} onClick={handleTabClick}>
                {summarySections.map(section => (
                    <div className={`${section.title}-tab`} key={uuid()}>{section.title}</div>
                ))}
            </div>
            <div className="perfomance-data" id="perfomance-data" ref={tabs}>
                {summarySections.map((section) => (
                    <div className={`section-data ${section.title} inactive`} key={uuid()}>
                        <StockPerfomanceSummary section={section} />
                    </div>
                ))}
            </div>

        </div>
    )
}

export default PerfomanceSummary