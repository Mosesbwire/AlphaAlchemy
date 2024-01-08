import { createContext, useEffect, useState } from 'react'
import useFetch from '../hooks/useFetch'
import apiService from '../services/apiService'

export const UserContext = createContext({ name: "Admin", id: 1, balance: 0 })

export default function UserContextProvider({ children }) {
    const [data, error, isLoading] = useFetch(apiService.getLoggedInUser)
    const [user, setUser] = useState(null)
    const updateUser = async () => {
        setUser({ balance: 100, name: "admin" })
        // const resp = await apiService.getLoggedInUser()
        // if (resp.status === 200) {
        //     setUser({ ...resp.data })
        // }
        // console.log(resp.data)

        // console.log(user)
    }
    useEffect(() => {
        if (data) {
            setUser(data)
        }
    }, [data, isLoading, user])
    return (
        <UserContext.Provider value={[user, updateUser]}>
            {children}
        </UserContext.Provider>
    )
}