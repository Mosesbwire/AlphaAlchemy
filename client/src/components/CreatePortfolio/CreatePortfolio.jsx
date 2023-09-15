
import useForm from "../../hooks/useForm"
import Button from "../Button/Button"
import './CreatePortfolio.css'
const CreatePortfolio = ({onSubmit})=>{
    const initialValues = {name: ""}
    const [values, handleChange, resetForm] = useForm(initialValues)

    const submitForm = async (e)=>{
        e.preventDefault()
        await onSubmit(values)
        resetForm()
    }

    return (
        <div className="create-portfolio">
            <div className="create-portfolio-form">
                <div>
                    <h1>Create Portfolio</h1>
                    <p className="tag-line">Virtual Investing, Real Learning</p>
                </div>
                <div>
                    <form onSubmit={submitForm}>
                        <div className="cp-form-group">
                            <label htmlFor="name">Name</label>
                            <input 
                                type="text" 
                                name="name" 
                                placeholder="Give your portfolio a unique name e.g Growth Portfolio, Defensive Porfolio"
                                value={values["name"]}
                                onChange={e => handleChange(e)}
                            />
                        </div>
                        <Button secondary>Create</Button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default CreatePortfolio