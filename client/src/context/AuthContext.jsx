import React, {createContext, useContext, useState} from 'react'

export const AuthContext = createContext(null)

export function useAuthContext(){
    const context = useContext(AuthContext)
    if (!context){
        throw new Error("useAuthContext must be used inside AuthContext")
    }
    
    return context;
}

export default function AuthContextProvider({children}){
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    return (
        <AuthContext.Provider value={{isAuthenticated, setIsAuthenticated}}>
            {children}
        </AuthContext.Provider>
    )
}
