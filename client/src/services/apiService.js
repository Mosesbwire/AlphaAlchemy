import setAuthToken from "./setAuthToken"
const BASE_URL = "http://localhost:5001/api/v1"

async function sendRequest(url, options){
    
    const response = await fetch(url, options)
    return response
}

function createRequestOptions(method, body=null){
    
    let options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'x-auth-token': sessionStorage.getItem("token"),
        },
    }

    if (body) {
        options["body"] = JSON.stringify(body)
    }

    return options
}

async function createUser(user){
    const options = createRequestOptions('POST', user)
    try {
        
        const response = await sendRequest(`${BASE_URL}/users`, options)
        
        if (response.status === 400 && response.statusText === "BAD REQUEST" ){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }
        const data = await response.json()
        const token = data["token"]
        setAuthToken(token)
        return {
            status: 200,
            data: "OK",
            error: null
        }
    } catch (error) {
        return {
            status: 500,
            data: null,
            error: error
        }
    }   
}

async function login(formData){
    const options = createRequestOptions('POST', formData)
    try {
        const response = await sendRequest(`${BASE_URL}/auth/login`, options)
        
        if (response.status === 400 && response.statusText === "BAD REQUEST"){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }
        if (response.status === 404 && response.statusText === "NOT FOUND") {
            const err = await response.json()
            return {
                status: 404,
                data: null,
                error: err
            }
        }

        const data = await response.json()
        const token = data["token"]

        setAuthToken(token)
        return {
            status: 200,
            data: "OK",
            error: null
        }
    } catch (error) {
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}



async function getLoggedInUser(){
    const options = createRequestOptions('GET')
    try {
        const response = await sendRequest(`${BASE_URL}/auth`, options)
        if (response.status === 404){
            const err = await response.json()
            return {
                status: 404,
                data: null,
                error: err
            }
        }

        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }

    
        const data = await response.json()
        const user = data.user
        sessionStorage.setItem('user',JSON.stringify(user))
        return {
            status: 200,
            data: user,
            error: null
        }
    
    } catch (error) {
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function getMarketMetrics(){
    const options = createRequestOptions('GET')
    
    try {
        const response = await sendRequest(`${BASE_URL}/market-data`, options)
        if (response.status === 404){
            const err = await response.json()
            return {
                status: 404,
                data: null,
                error: err
            }
        }

        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }

        return {
            status: 200,
            data: await response.json(),
            error: null
        }
    } catch(error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function createPortfolio(formData){
    const options = createRequestOptions('POST', formData)
    try {
        const response = await sendRequest(`${BASE_URL}/portfolios`, options)
        
        if (response.status === 400 && response.statusText === "BAD REQUEST"){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }

        return {
            status: 200,
            data: await response.json(),
            error: null
        }
    } catch (error) {
        
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function getPortfolioById(portfolioId){
    const options = createRequestOptions('GET')
    
    try {
        
        const response = await sendRequest(`${BASE_URL}/portfolios/${portfolioId}`, options)
        
        if (response.status === 404){
            const err = await response.json()
            return {
                status:404,
                data: null,
                error: err
            }
        }
        
        return {
            status: 200,
            data: await response.json(),
            error: null
        }
        
    } catch (error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function getPortfolios(){
    const options = createRequestOptions('GET')
    
    try {
        const response = await sendRequest(`${BASE_URL}/portfolios`, options)
        if (response.status === 404){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }

        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }
        
        return {
            status: 200,
            data: await response.json(),
            error: null
        }
    } catch (error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function getStocks(){
    const options = createRequestOptions("GET")

    try {
        const response = await sendRequest(`${BASE_URL}/stocks`, options)

        if (response.status === 404){
            const err = await response.json()
            return {
                status: 404,
                data: null,
                error: err
            }
        }

        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }

        return {
            status: 200,
            data: await response.json(),
            error: null
        }
    } catch(error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

async function buyStock(data){
    const options = createRequestOptions("POST", data)

    const portfolioId = data["id"]
    try {
        const response = await sendRequest(`${BASE_URL}/portfolios/${portfolioId}/buy`, options)
        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }

        if (response.status === 400){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }

        return {
            status: 200,
            data: await response.json(),
            error: null
        }

    } catch (error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}
async function sellStock(data){
    const options = createRequestOptions("POST", data)

    const portfolioId = data["id"]
    try {
        const response = await sendRequest(`${BASE_URL}/portfolios/${portfolioId}/sell`, options)

        if (response.status === 401){
            const err = await response.json()
            return {
                status: 401,
                data: null,
                error: err
            }
        }

        if (response.status === 400){
            const err = await response.json()
            return {
                status: 400,
                data: null,
                error: err
            }
        }

        return {
            status: 200,
            data: await response.json(),
            error: null
        }

    } catch (error){
        return {
            status: 500,
            data: null,
            error: error
        }
    }
}

export default  {
    createUser,
    getLoggedInUser,
    login, getMarketMetrics,
    createPortfolio,
    getPortfolioById,
    getPortfolios,
    getStocks,
    buyStock,
    sellStock
}