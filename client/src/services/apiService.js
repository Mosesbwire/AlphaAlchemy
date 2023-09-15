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
            return err
        }
        if (response.status === 404 && response.statusText === "NOT FOUND") {
            const err = await response.json()
            return err
        }

        const data = await response.json()
        const token = data["token"]

        setAuthToken(token)
        return "OK"
    } catch (error) {
        return error
    }
}

async function getUsers(){
    const options = createRequestOptions('GET')
    try {
        const response = await sendRequest(`${BASE_URL}/users`, options)
        const data = await response.json()
        return data
    
    } catch (error) {
        return error
    }
}

async function getMarketMetrics(){
    const options = createRequestOptions('GET')
    
    try {
        const response = await sendRequest(`${BASE_URL}/market-data`, options)
        const data = await response.json()
        return data
    } catch(error){
        return error
    }
}

async function createPortfolio(formData){
    const options = createRequestOptions('POST', formData)
    try {
        const response = await sendRequest(`${BASE_URL}/portfolios`, options)
        
        if (response.status === "400" && response.statusText === "BAD REQUEST"){
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

export default  {
    createUser,
    getUsers,
    login, getMarketMetrics,
    createPortfolio
}