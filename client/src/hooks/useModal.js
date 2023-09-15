import { useState } from "react";

const useModal = ()=>{
    const [openModal, setOpenModal] = useState(false)

    
    const modalHandler = ()=>{
        setOpenModal(!openModal)
    }

    return [openModal, modalHandler]
}

export default useModal