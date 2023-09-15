import {useEffect, useState} from "react";

const useFetch = (callback, values=null)=>{
    const [data, setData] = useState(null)
    const [error, setError] = useState(null)
    const [isLoading, setIsLoading] = useState(false)

    useEffect(()=>{
        const fetchData = async ()=>{
            setIsLoading(true)
            try {
                const results = await callback(values)
                setData(results)
                setError(null)
            } catch (error) {
                setError(error)
            } finally {
                setIsLoading(false)
            }
        }
        fetchData()
    }, [callback, values])
    
    return [data, error, isLoading]
}

export default useFetch