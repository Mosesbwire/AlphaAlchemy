
import { DateTime } from "luxon"
export function prepMarketData(data) {
    let marketData = []
    delete data.status
    Object.keys(data).forEach(key => {
        let obj = {}
        if (key === "deals") {
            obj["title"] = "Deals"
        }
        if (key === "turnover") {
            obj["title"] = "Equity Turnover"
        }
        if (key === "volume") {
            obj["title"] = "Shares Traded"
        }

        obj["stat"] = data[key]

        marketData.push(obj)
    })

    return marketData
}

export function prepStockData(data) {
    let marketData = []
    data.forEach(dt => {
        let dataPoint = []
        dataPoint.push(dt["ticker"])
        dataPoint.push(dt["prev"])
        dataPoint.push(dt["current"])
        dataPoint.push(dt["change"])
        dataPoint.push(dt["%change"])
        dataPoint.push(dt["high"])
        dataPoint.push(dt["low"])
        dataPoint.push(dt["volume"])
        dataPoint.push(dt["average"])
        marketData.push(dataPoint)
    })

    return marketData
}

export function formattedDate(datetime) {
    let date = new Date(datetime)
    const newFormat = { ...DateTime.DATETIME_SHORT_WITH_SECONDS, };
    date = DateTime.fromJSDate(date).toFormat('yyyy-MM-dd HH:MM:ss')
    return date
}