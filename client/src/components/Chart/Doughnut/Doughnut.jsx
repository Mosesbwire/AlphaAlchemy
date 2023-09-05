import React from "react";
import { Chart as Chartjs, ArcElement, Tooltip, Legend} from 'chart.js'
import {Doughnut} from 'react-chartjs-2'

const opt = [ArcElement,Tooltip,Legend]

Chartjs.register(...opt)

const data = {
    labels : ['SCOM', 'KCB', 'SASN', 'SBIC', 'WTK', 'TPSE', 'KNRE', 'KEGN'],
    datasets : [{
        label: "# of shares",
        data: [1000, 2000, 4000, 500, 600, 10000, 20000, 5000],
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(0, 159, 64, 0.2)',
            'rgba(200, 159, 64, 0.2)',
            'rgba(255, 100, 64, 0.2)',
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(0, 159, 64, 1)',
            'rgba(200, 159, 64, 1)',
            'rgba(255, 100, 64, 1)',
        ],
        borderWidth: 1
    }]
}

const options = {
    plugins: {
      legend: {
        labels: {
          position: 'right'
        }
      }
    }
  };

const DoughnutChart = ()=>{
    return (
        <Doughnut data={data} options={options}/>
    )
}

export default DoughnutChart