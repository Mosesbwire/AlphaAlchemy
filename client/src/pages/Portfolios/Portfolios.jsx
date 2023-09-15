import React from "react";
import {Link} from 'react-router-dom'
import PortfolioSummary from "../../components/Portfolio/PortfolioSummary";
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch"
import './Portfolio.css'

const Portfolios = ()=>{
    const [data, error, isLoading] = useFetch(apiService.getPortfolios)

    if (isLoading){
        return <div>Loading..</div>
    }

    if (error){
        return <div>Error Occured</div>
    }

    console.log(data)
    return(
            <div className="portfolios-wrapper container">
                {data && data.length > 0 ? <>
                    {data.map(portfolio => (
                        <Link to={`/portfolio/${portfolio.id}`}>
                            <PortfolioSummary 
                                name={portfolio.name} 
                                marketValue={portfolio.valuation}
                                key={portfolio.id}
                            />
                        </Link>
                    ))}
                </>
                    : <div>Click Create portfolio to create a portfolio</div>   
            }
                    
            </div> 
    )
}

export default Portfolios