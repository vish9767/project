import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Typography from "@mui/material/Typography";
import Button from '@mui/material/Button';
import { Link, useNavigate } from "react-router-dom";
import health from "../../assets/healthcare.png";
import UserNavbar from './UserNavbar';
import Footer from '../../Footer';
import { Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from '@mui/material';

const ptnStatus = [
    {
        Patient_status_at_present: 1,
        label: 'Home',
    },
    {
        Patient_status_at_present: 2,
        label: 'Hospital',
    },
];

const referby = [
    {
        refer_by: 1,
        label: 'Self',
    },
    {
        refer_by: 2,
        label: 'Hospital',
    },
    {
        refer_by: 3,
        label: 'Other',
    },
];

const UserDetails = () => {
    const navigate = useNavigate();
    const port = process.env.REACT_APP_API_KEY;

    const [ptnName, setPtnName] = useState('');
    const [ptnNo, setPtnNo] = useState('');
    const [gender, setGender] = useState([]);
    const [selectedGender, setSelectedGender] = useState('');
    const [ptnAge, setPtnAge] = useState('');
    const [famName, setFamName] = useState('');
    const [famNo, setFamNo] = useState('');
    const [service, setService] = useState([]);
    const [selectedService, setSelectedService] = useState('');
    const [startDate, setStartDate] = useState('');
    const [convertedStartDate, setConvertedStartDate] = useState('');
    const [remark, setRemark] = useState('');
    const [selectedPtnStatus, setSelectedPtnStatus] = useState('');
    const [selectedReferby, setSelectedReferby] = useState('');
    const [consultant, setConsultant] = useState([]);
    const [selectedConsultant, setSelectedConsultant] = useState('');
    const [consultantNo, setConsultantNo] = useState('');
    const [address, setAddress] = useState('');

    const [isPopupOpen, setPopupOpen] = useState(false);

    const handlePopupOpen = () => {
        setPopupOpen(true);
    };

    const handlePopupClose = () => {
        setPopupOpen(false);
        // Reset form data here
        setPtnName('');
        setPtnNo('');
        setSelectedGender('');
        setPtnAge('');
        setFamName('');
        setFamNo('');
        setSelectedService('');
        setStartDate('');
        setRemark('');
        setSelectedPtnStatus('');
        setSelectedReferby('');
        setSelectedConsultant('');
        setConsultantNo('');
        setAddress('');
    };

    useEffect(() => {
        const getGender = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_gender_api`);
                const data = await res.json();
                console.log(data);
                setGender(data);
            } catch (error) {
                console.error("Error fetching gender data:", error);
            }
        };
        getGender();
    }, []);

    useEffect(() => {
        const getService = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_services_api`);
                const data = await res.json();
                console.log("Service Data.........", data);
                setService(data);
            } catch (error) {
                console.error("Error fetching Service Data:", error);
            }
        };
        getService();
    }, []);

    useEffect(() => {
        const getConsultant = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_consultant_api`);
                const data = await res.json();
                console.log("Consultant data", data);
                setConsultant(data);
            } catch (error) {
                console.error("Error fetching Consultant data:", error);
            }
        };
        getConsultant();
    }, []);

    const handleDropdownConsultant = (event) => {
        const selectedValue = event.target.value;
        setSelectedConsultant(selectedValue);

        // Find the selected consultant's mobile number and set it as the selected contact
        const selectedConsultantData = consultant.find(consult => consult.doct_cons_id === selectedValue);
        if (selectedConsultantData) {
            setConsultantNo(selectedConsultantData.mobile_no);
        } else {
            setConsultantNo('');
        }
    };

    useEffect(() => {
        if (startDate) {
            const originalStartDate = new Date(startDate);
            const convertedStartDateTime = formatDate(originalStartDate);
            setConvertedStartDate(convertedStartDateTime);
        }
    }, [startDate]);

    function formatDate(date) {
        return `${date.getFullYear()}-${padNumber(date.getMonth() + 1)}-${padNumber(date.getDate())} ${padNumber(date.getHours())}:${padNumber(date.getMinutes())}:${padNumber(date.getSeconds())}`;
    }

    function padNumber(number) {
        return number.toString().padStart(2, '0');
    }

    async function handlePatientForm(event) {
        event.preventDefault();
        // validatePhoneNumber();
        // validateEmail();
        // validatePtnNumber()
        const requestData = {
            caller_fullname: famName,
            phone: famNo,
            name: ptnName,
            phone_no: ptnNo,
            gender_id: selectedGender,
            age: ptnAge,
            refer_by: selectedReferby,
            Patient_status_at_present: selectedPtnStatus,
            Suffered_from: remark,
            doct_cons_id: selectedConsultant,
            // doct_cons_phone: consultantNo,
            address: address,
            srv_id: selectedService,
            start_date: convertedStartDate,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/agg_hhc_add_service_form_api/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (response.ok) {
                handlePopupOpen();
            }
            else {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json();
            console.log("Patient Web Data Successfully submitted to Database.....", result);
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    return (
        <>
            < UserNavbar />
            <Grid item xs={12} container spacing={0}>
                <Grid item lg={4} sm={6} xs={12}>
                    <Box height="100%" display="flex" flexDirection="column">
                        <img src={health} alt="" style={{ width: "100%", borderRadius: "10px", }} />
                    </Box>
                </Grid>
                <Grid item lg={8} sm={6} xs={12}>
                    <Box display="flex" flexDirection="column" sx={{ backgroundColor: "#FFFFFF", boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: "10px", marginTop: "6px", marginBottom: "10px" }}>
                        <Typography variant='h6' sx={{ m: 4 }}>PATIENT DETAILS</Typography>

                        <Grid container spacing={3} sx={{ marginTop: "2px", paddingLeft: "30px", paddingRight: "30px" }}>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    label="Patient Name"
                                    id="name"
                                    name="name"
                                    placeholder="First Name | Last Name *"
                                    value={ptnName}
                                    onChange={(e) => setPtnName(e.target.value)}
                                    size="small"
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    id="phone_no"
                                    name="phone_no"
                                    label="Contact"
                                    placeholder="+91 |"
                                    size="small"
                                    fullWidth
                                    value={ptnNo}
                                    onChange={(e) => setPtnNo(e.target.value)}
                                    // onInput={handleInput}
                                    // error={!!phoneNumberError}
                                    // helperText={phoneNumberError}
                                    // inputProps={{
                                    //     minLength: 10,
                                    //     maxLength: 10, 

                                    // }}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    label="Family Member Name"
                                    id="caller_fullname"
                                    name="caller_fullname"
                                    placeholder="First Name | Last Name *"
                                    size="small"
                                    fullWidth
                                    value={famName}
                                    onChange={(e) => setFamName(e.target.value)}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    label="Family Member Contact"
                                    id="phone"
                                    name="phone"
                                    placeholder="+91 | "
                                    size="small"
                                    fullWidth
                                    value={famNo}
                                    onChange={(e) => setFamNo(e.target.value)}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} sm={12} xs={12}>
                                <Grid container spacing={1}>
                                    <Grid item xs={6} md={6} sm={6}>
                                        <TextField
                                            id="gender_id"
                                            name="gender_id"
                                            select
                                            label="Gender"
                                            size="small"
                                            fullWidth
                                            value={selectedGender}
                                            onChange={(e) => setSelectedGender(e.target.value)}
                                            sx={{
                                                textAlign: "left",
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                        >
                                            {gender.map((option) => (
                                                <MenuItem key={option.gender_id} value={option.gender_id}>
                                                    {option.name}
                                                </MenuItem>
                                            ))}
                                        </ TextField>
                                    </Grid>
                                    <Grid item xs={6} md={6} sm={6}>
                                        <TextField
                                            label="Age"
                                            id="age"
                                            name="age"
                                            size="small"
                                            fullWidth
                                            value={ptnAge}
                                            onChange={(e) => setPtnAge(e.target.value)}
                                            sx={{
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                        />
                                    </Grid>
                                </Grid>
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    id="srv_id"
                                    name="srv_id"
                                    select
                                    label="Service Required"
                                    placeholder='Select Service'
                                    size="small"
                                    fullWidth
                                    value={selectedService}
                                    onChange={(e) => setSelectedService(e.target.value)}
                                    sx={{
                                        textAlign: "left",
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                >
                                    {service.map((option) => (
                                        <MenuItem key={option.srv_id} value={option.srv_id}>
                                            {option.service_title}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    label="Start Date"
                                    id="start_date"
                                    name="start_date"
                                    type="datetime-local"
                                    size="small"
                                    fullWidth
                                    value={startDate}
                                    onChange={(e) => setStartDate(e.target.value)}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                    InputLabelProps={{
                                        shrink: true,
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    label="Diagnosis"
                                    id="Suffered_from"
                                    name="Suffered_from"
                                    placeholder='Remark'
                                    size="small"
                                    fullWidth
                                    value={remark}
                                    onChange={(e) => setRemark(e.target.value)}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    id="Patient_status_at_present"
                                    name="Patient_status_at_present"
                                    select
                                    label="Patient Status at present"
                                    size="small"
                                    fullWidth
                                    value={selectedPtnStatus}
                                    onChange={(e) => setSelectedPtnStatus(e.target.value)}
                                    sx={{
                                        textAlign: "left",
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                >
                                    {ptnStatus.map((option) => (
                                        <MenuItem key={option.Patient_status_at_present} value={option.Patient_status_at_present}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    id="refer_by"
                                    name="refer_by"
                                    select
                                    label="Refer by"
                                    size="small"
                                    fullWidth
                                    value={selectedReferby}
                                    onChange={(e) => setSelectedReferby(e.target.value)}
                                    sx={{
                                        textAlign: "left",
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                >
                                    {referby.map((option) => (
                                        <MenuItem key={option.refer_by} value={option.refer_by}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    id="doct_cons_id"
                                    name="doct_cons_id"
                                    select
                                    label="Consultant Name"
                                    size="small"
                                    fullWidth
                                    value={selectedConsultant}
                                    onChange={handleDropdownConsultant}
                                    sx={{
                                        textAlign: "left",
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                >
                                    {consultant.map((option) => (
                                        <MenuItem key={option.doct_cons_id} value={option.doct_cons_id}>
                                            {option.cons_fullname}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Grid>

                            <Grid item lg={6} md={12} sm={12} xs={12}>
                                <TextField
                                    id="doct_cons_phone"
                                    name="doct_cons_phone"
                                    label="Consultant Contact"
                                    placeholder='+91 |'
                                    size="small"
                                    fullWidth
                                    value={consultantNo}
                                    sx={{
                                        textAlign: "left",
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} md={12} sm={12} xs={12}>
                                <TextField
                                    label="Address"
                                    id="address"
                                    name="address"
                                    placeholder='Lane,Area,Street'
                                    size="small"
                                    fullWidth
                                    value={address}
                                    onChange={(e) => setAddress(e.target.value)}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} md={12} sm={12} xs={12}>
                                <Button variant="contained" sx={{ mt: 2, mb: 5, width: '30ch', backgroundColor: '#51DDD4', borderRadius: "12px", textTransform: "capitalize", }} type="submit" onClick={handlePatientForm}>Submit</Button>
                            </Grid>

                            <Dialog open={isPopupOpen} onClose={handlePopupClose}>
                                <DialogTitle>Form Submitted</DialogTitle>
                                <DialogContent>
                                    <DialogContentText>
                                        Your form has been successfully submitted!!.
                                    </DialogContentText>
                                </DialogContent>
                                <DialogActions>
                                    <Button onClick={handlePopupClose} color="primary">
                                        Close
                                    </Button>
                                </DialogActions>
                            </Dialog>
                        </Grid>

                    </Box>
                </Grid>
            </Grid>
            <Footer />
        </>
    )
}

export default UserDetails
