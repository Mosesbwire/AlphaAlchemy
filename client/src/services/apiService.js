const BASE_URL = "http://localhost:5001/api/v1"

async function sendRequest(url, options){
    const response = await fetch(url, options)
    return await response.json()
}

function createRequestOptions(method, body){
    return {
        method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    }
}

async function createUser(user){
    const options = createRequestOptions('POST', user)
    return await sendRequest(`${BASE_URL}/users`, options)
}

export default  {
    createUser
}