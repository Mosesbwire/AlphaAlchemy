import React, {useState} from "react";
import Button from "../../components/Button/Button"
import './Buy.css'

const data = [
    "ABSA", 
    "ACK","NMG", "CARB", "KCB", "WTK", "SASN", "CAGN", "EQTY", "LKL"
]

const Buy = ()=>{
    const [isOpenDropDown, setOpenDropDown] = useState(false)
    const [showInfoText, setShowInfoText] = useState(false)

    const handleClick = ()=>{
        setOpenDropDown(!isOpenDropDown)
    }

    return (
        <div className="order-action">
            <div className="d-md-none d-lg-none sm-acc-details">
                <div className=" row-flex  container">
                    <p>Account Balance</p>
                    <p>KES 50000.00</p>
                </div>
            </div>
            <div className="buy-process">
                <div className="buy-form">
                    <div className="buy-title">
                        <p>Buy</p>
                
                    </div>
                    <form action="" method="post" className="order-form container">
                        <div className="select-security form-group">
                            <label>Security Name</label>
                            <div><input type="text" name="security" id="" placeholder="Select Company" onClick={handleClick}/></div>
                            { isOpenDropDown ? <div className="drop-down-selector" onClick={handleClick}>
                                {data.map(dt => (
                                    <div>{dt}</div>
                                ))}
                            </div> : null}
                        </div>
                        <div className="security-price form-group">
                            <label htmlFor="price">Price</label>
                            <div>
                                <input type="text" name="price" id="" />
                                <p className={`info-text ${showInfoText ? 'show-info-text': 'hide-info-text'}`}>Scom current price is KES 15.25</p>
                            </div>
                        </div>
                        <div className="security-quantity form-group">
                            <label htmlFor="quantity">Quantity</label>
                            <div>
                                <input type="text" name="quantity" id="" placeholder="Should be in lots of 100 e.g 200, 300, 10000"/>
                            </div>
                        </div>
                        
                        <Button primary >Place Order</Button>
                    </form>
                </div>
            </div>
            <div className="account-details d-sm-none d-md-block d-lg-block">
                <div className="available-funds row-flex">
                    <p>Available Funds</p>
                    <p>KES 50000.00</p>
                </div>
                <div className="order-value row-flex">
                    <p>Order Value</p>
                    <p>KES 6000.00</p>
                </div>
                <div className="remaining-bal row-flex">
                    <p>Remaining Balance</p>
                    <p>KES 6000.00</p>
                </div>
            </div>
        </div>
    )
}

export default Buy