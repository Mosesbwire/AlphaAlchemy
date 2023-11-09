import React, { createContext, useContext, useState } from 'react'
import useAuth from '../hooks/useAuth'

export const AuthContext = createContext()

export function useAuthContext() {
    const context = useContext(AuthContext)
    if (!context) {
        throw new Error("useAuthContext cannot be used outside of AuthContext.")
    }
    return context;
}

export default function AuthContextProvider({ children }) {
    const auth = useAuth()
    return (
        <AuthContext.Provider value={auth}>
            {children}
        </AuthContext.Provider>
    )
}
