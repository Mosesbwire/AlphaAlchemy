import { useState } from "react";

const useSubmitForm = (callback) => {
    const [data, setData] = useState(null)
    const [isSubmitting, setSIsSubmitting] = useState(false)
    const [error, setError] = useState(null)

    const submitData = async (formData) => {
        setSIsSubmitting(true)
        try {
            const results = await callback(formData)

            if (results.status === 200 || results.status === 201) {
                setData(results.data)
            } else {

                setError(results.error)
            }
        } catch (error) {
            setError(error)

        } finally {
            setSIsSubmitting(false)
        }
    }

    const onSubmit = async (formData) => {
        try {
            await submitData(formData)
        } catch (error) {
            setError(error)
        }
    }

    return [onSubmit, data, isSubmitting, error]
}

export default useSubmitForm