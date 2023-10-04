import React, { useState } from 'react';
import Box from "@mui/material/Box"
import Grid from "@mui/material/Grid"
import TextField from "@mui/material/TextField"
import Button from '@mui/material/Button';
import MenuItem from "@mui/material/MenuItem"
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';

const Payment = ({ eveID, pay, ptnData, onClose }) => {
    const port = process.env.REACT_APP_API_KEY;

    const [value, setValue] = useState('1');
    const [remark, setRemark] = useState('')
    const [paymentData, setPaymentData] = useState({ ...pay });
    const [patientData, setPatientData] = useState({ ...ptnData });
    const [amountError, setAmountError] = useState('');


    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const handleFieldChange = (field, value) => {
        setPaymentData({ ...pay, [field]: value });
        setPatientData({ ...patientData, [field]: value });
        // setPaymentData(prevPaymentData => ({
        //     ...prevPaymentData,
        //     [field]: parseFloat(value), // Parse the value to a float
        // }));
        // Calculate Pending_Amount as the difference between Total_Amount and Paid_Amount
        if (field === 'amount_paid') {
            setPaymentData(paymentData => {
                const pendingAmount = paymentData.Pending_Amount - parseFloat(value);
                const demo = paymentData.Pending_Amount
                console.log("Paid Amount.....", paymentData)
                console.log("Paid Amount.....", paymentData.amount_paid)
                console.log("Pending Amount.....", demo)

                if (parseFloat(value) > paymentData.Pending_Amount) {
                    setAmountError("Paid Amount cannot be greater than Pending Amount");

                    // return paymentData; 

                } else if (parseFloat(value) < 0) {
                    // Set an error message for negative values
                    setAmountError("Paid Amount cannot be negative");
                } 
                // else {
                //     return paymentData;
                // }

                return {
                    ...paymentData,
                    Pending_Amount: isNaN(pendingAmount) ? 0 : pendingAmount,
                };
            });
        }
    };

    async function handleCashPaymentSubmit(event) {
        event.preventDefault();
        const requestData = {
            eve_id: eveID,
            Total_cost: pay.Total_Amount,
            paid_by: ptnData.name,
            amount_paid: paymentData.amount_paid,
            amount_remaining: paymentData.Pending_Amount,
            mode: value,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/payment-detail/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                console.error(`HTTP error! Status: ${response.status}`);
                return;
            }
            const result = await response.json();
            console.log("Cash Payment data", result);
            onClose();
            window.location.reload();
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    async function handleOnlinePaymentSubmit(event) {
        event.preventDefault();
        const requestData = {
            eve_id: eveID,
            total_amount: pay.Total_Amount,
            customerName: ptnData.name,
            customeremail: ptnData.patient_email_id,
            customerPhone: patientData.phone_no,
            orderAmount: paymentData.amount_paid,
            Remaining_amount: paymentData.Pending_Amount,
            Mode: value,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/create_payment/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                console.error(`HTTP error! Status: ${response.status}`);
                return;
            }
            const result = await response.json();
            console.log("Online Payment data", result);
            onClose();
            window.location.reload();
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    return (
        <Box sx={{ marginTop: "20px" }}>
            <TabContext value={value}>
                <Box sx={{
                    typography: 'body1',
                    background: "#F2F2F2",
                    borderRadius: '10px',
                    width: "60%",
                    height: "2.8rem",
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    marginLeft: '50px',
                    // marginRight: '8px',
                }}>
                    <TabList
                        className="tab-root"
                        onChange={handleChange}
                        textColor="#51DDD4"
                        sx={{ position: 'relative', }}
                        TabIndicatorProps={{ style: { background: '#69A5EB', height: '44px', marginBottom: '2px', borderRadius: "5px" } }}
                    >
                        <Tab label={<span style={{ fontSize: '15px', textTransform: "capitalize", color: value === "1" ? '#ffffff' : 'black' }}>Online</span>} value="1" sx={{ position: 'relative', zIndex: 1, }} />
                        <Tab label={<span style={{ fontSize: '15px', textTransform: "capitalize", color: value === "2" ? '#ffffff' : 'black' }}>Cash</span>} value="2" sx={{ position: 'relative', zIndex: 1, }} />
                    </TabList>
                </Box>
                <Box sx={{ width: '100%', typography: 'body1', marginTop: '-10px' }}>
                    <TabPanel value="1">
                        <Grid container spacing={2} sx={{ marginTop: "1px" }}>

                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="total_amount"
                                    name="total_amount"
                                    label="Total Payable"
                                    size="small"
                                    // value={pay.Total_Amount}
                                    value={paymentData.Total_Amount}
                                    fullWidth
                                    // disabled
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="customerName"
                                    name="customerName"
                                    label="Customer Name"
                                    placeholder='First name | Middle name | Last name'
                                    size="small"
                                    value={ptnData.name}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="customeremail"
                                    name="customeremail"
                                    label="Customer Email"
                                    placeholder='email@gmail.com'
                                    size="small"
                                    value={ptnData.patient_email_id}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="customerPhone"
                                    name="customerPhone"
                                    label="Contact"
                                    placeholder='+91 |'
                                    size="small"
                                    value={patientData.phone_no}
                                    onChange={(e) => handleFieldChange("phone_no", e.target.value)}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="orderAmount"
                                    name="orderAmount"
                                    label="Amount Paid"
                                    size="small"
                                    type="number"
                                    // value={pay.Paid_Amount}
                                    value={paymentData.amount_paid}
                                    onChange={(e) => handleFieldChange("amount_paid", e.target.value)}
                                    fullWidth
                                    sx={{
                                        textAlign: "left", '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                    error={!!amountError}
                                    helperText={amountError}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="Remaining_amount"
                                    label="Amount Remaining"
                                    size="small"
                                    name="Remaining_amount"
                                    value={paymentData.Pending_Amount}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12}>
                                <Button variant="contained" sx={{ mt: 2, ml: 7, bgcolor: "#69A5EB", borderRadius: "10px", textTransform: "capitalize", width: "8rem" }} onClick={handleOnlinePaymentSubmit}>Send Link</Button>
                            </Grid>
                        </Grid>
                    </TabPanel>
                    <TabPanel value="2">
                        <Grid container spacing={2} sx={{ marginTop: "1px" }}>
                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="Total_Amount"
                                    label="Total Payable"
                                    name="Total_Amount"
                                    // value={pay.Total_Amount}
                                    value={paymentData.Total_Amount}
                                    size="small"
                                    fullWidth
                                    sx={{
                                        textAlign: "left", '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="name"
                                    name="name"
                                    label="Paid by"
                                    size="small"
                                    fullWidth
                                    type="text"
                                    value={ptnData.name}
                                    sx={{
                                        textAlign: "left", '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="amount_paid"
                                    name="amount_paid"
                                    label="Amount Paid"
                                    size="small"
                                    type="number"
                                    // value={pay.Paid_Amount}
                                    value={paymentData.amount_paid}
                                    onChange={(e) => handleFieldChange("amount_paid", e.target.value)}
                                    fullWidth
                                    sx={{
                                        textAlign: "left", '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                    error={!!amountError}
                                    helperText={amountError}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "10px" }}>
                                <TextField
                                    id="Pending_Amount"
                                    label="Amount Remaining"
                                    size="small"
                                    name="Pending_Amount"
                                    value={paymentData.Pending_Amount}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>
                            <Grid item lg={12} sm={12} xs={12}>
                                <Button variant="contained" sx={{ mt: 2, ml: 7, bgcolor: "#69A5EB", borderRadius: "10px", textTransform: "capitalize", width: "8rem" }} onClick={handleCashPaymentSubmit}>Done</Button>
                            </Grid>
                        </Grid>
                    </TabPanel>
                </Box>
            </TabContext>
        </Box>
    )
}

export default Payment
