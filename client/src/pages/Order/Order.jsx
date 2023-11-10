import React from "react";
import { useParams, Navigate, useLocation } from 'react-router-dom'
import Button from "../../components/Button/Button"
import Loading from "../../components/Loader/Loading"
import apiService from "../../services/apiService";
import useFetch from "../../hooks/useFetch"
import useForm from "../../hooks/useForm";
import useSubmitForm from "../../hooks/useSubmitForm";
import { toast } from "react-toastify"
import './Order.css'

const Buy = () => {
    const location = useLocation()
    const queryParams = new URLSearchParams(location.search)
    const action = queryParams.get("action")
    const stock = queryParams.get("stock")
    const orderFunction = action === "buy" ? apiService.buyStock : apiService.sellStock
    const initialValues = { price: "", quantity: "", stock_id: "" }
    const [values, handleChange, resetForm] = useForm(initialValues)
    const [data, error, isLoading] = useFetch(apiService.getStocks)

    const [onSubmit, orderData, isSubmitting, orderError] = useSubmitForm(orderFunction)
    const sortedData = data ? data.stocks : []
    const user = JSON.parse(sessionStorage.getItem("user"))

    let orderValue = 0


    orderValue = Number(values.price) * Number(values.quantity)

    if (stock !== "no-stock" && data) {
        data.stocks.forEach(dt => {
            if (dt.ticker == stock) {
                values["stock_id"] = dt.id
            }
        })
    }
    const remainingBal = action === "buy" ? 50000 - orderValue : Number(50000)

    sortedData.sort((objA, objB) => {
        if (objA.ticker < objB.ticker) return -1
        if (objA.ticker > objB.ticker) return 1
        return 0
    })
    const submitForm = async (e) => {
        e.preventDefault()
        onSubmit(values)
    }

    if (isLoading || isSubmitting) {
        return <Loading />
    }

    if (orderError) {
        toast.error(orderError.error, {
            position: toast.POSITION.TOP_CENTER,
            autoClose: false,
            theme: "light"
        })

    }

    if (orderData) {
        return <Navigate to={`/portfolio`} />
    }

    return (
        <div className="order-action">
            <div className="d-md-none d-lg-none sm-acc-details">
                <div className=" row-flex  container">
                    <p>Account Balance</p>
                    <p>KES {50000}</p>
                </div>
            </div>
            <div className="buy-process">
                <div className="buy-form">
                    <div className="buy-title">
                        <p>{action}</p>

                    </div>
                    <form action="" method="post" className="order-form container" onSubmit={submitForm}>
                        <div className="select-security form-group">
                            <label htmlFor="stock_id">Security Name</label>
                            <div>
                                <select disabled={stock !== "no-stock"} className="order-form_select" name="stock_id" value={values["stock_id"]} onChange={e => handleChange(e)}>
                                    <option value={''}>{stock === "no-stock" ? 'Select Company' : `${stock}`}</option>
                                    {sortedData.map(data => (
                                        <option value={data.id} key={data.id}>{data.ticker}</option>
                                    ))}
                                </select>
                            </div>
                        </div>
                        <div className="security-price form-group">
                            <label htmlFor="price">Price</label>
                            <div>
                                <input
                                    type="text"
                                    name="price"
                                    id=""
                                    value={values["price"]}
                                    onChange={e => handleChange(e)}
                                />

                            </div>
                        </div>
                        <div className="security-quantity form-group">
                            <label htmlFor="quantity">Quantity</label>
                            <div>
                                <input
                                    type="text"
                                    name="quantity"
                                    id=""
                                    placeholder="Should be in lots of 100 e.g 200, 300, 10000"
                                    value={values["quantity"]}
                                    onChange={e => handleChange(e)}
                                />
                            </div>
                        </div>

                        <Button primary >Place Order</Button>
                    </form>
                </div>
            </div>
            <div className="account-details d-sm-none d-md-block d-lg-block">
                <div className="available-funds row-flex">
                    <p>Available Funds</p>
                    <p>KES {50000}</p>
                </div>
                <div className="order-value row-flex">
                    <p>Order Value</p>
                    <p>KES {orderValue}</p>
                </div>
                <div className="remaining-bal row-flex">
                    <p>Remaining Balance</p>
                    <p>KES {remainingBal}</p>
                </div>
            </div>
        </div>
    )
}

export default Buy