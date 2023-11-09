
import { Navigate } from "react-router-dom"


function RequireAuth({ children }) {
    const token = sessionStorage.getItem("token")


    if (!token) {
        return <Navigate to={"/login"} />
    }
    return children
}

export default RequireAuth