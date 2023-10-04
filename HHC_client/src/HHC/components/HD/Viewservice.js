import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import TextField from '@mui/material/TextField';
import Menu from '@mui/material/Menu';
import Modal from '@mui/material/Modal';
import MenuItem from '@mui/material/MenuItem';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from '@mui/material/TablePagination';
import IconButton from '@mui/material/IconButton';
import AppBar from '@mui/material/AppBar';
// import AvailabilityProgressBar from "./Addservice/Progressbar" ;
import { styled } from '@mui/material/styles';
import MoreHorizOutlinedIcon from '@mui/icons-material/MoreHorizOutlined';
import Button from '@mui/material/Button';
import CloseIcon from '@mui/icons-material/Close';
import CallerView from './Viewservice/CallerView';
import PatientView from './Viewservice/PatientView';
import ServiceInfo from './Addservice/ServiceInfo';
import EditImage from "../../assets/editing.png";
// import Header from '../../Header';
import Footer from '../../Footer';
import Navbar from '../../Navbar';
import { useNavigate, useLocation } from 'react-router-dom';
import Payment from './Viewservice/Payment';
import HowToRegIcon from '@mui/icons-material/HowToReg';
import CircularProgress from '@mui/material/CircularProgress';
import { Autocomplete } from '@mui/material';
// import SearchIcon from '@mui/icons-material/Search';
// import InputAdornment from '@mui/material/InputAdornment';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    pt: 2,
    px: 4,
    pb: 3,
};

const ViewServiceCard = styled(Card)({
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: '10px',
    backgroundColor: '#FFFFFF',
    boxShadow: '4px 4px 10px 7px rgba(100, 135, 135, 0.05)',
    // boxShadow: '4px 4px 10px 7px rgba(10, 10, 100, 0.05)',
    height: "55px",
    borderRadius: '10px',
    transition: '2s ease-in-out',
    '&:hover': {
        backgroundColor: 'white',
        cursor: 'pointer',
    },
});

const Viewservice = () => {
    const navigate = useNavigate();
    const port = process.env.REACT_APP_API_KEY;
    const location = useLocation();
    const { eventID, patientID, callerID, eventPlanID } = location.state;
    // console.log("Event id", eventID, "service ID", serviceID);

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(4);

    const [caller, setCaller] = useState('');
    // const [relation, setRelation] = useState('');
    const [patient, setPatient] = useState('');
    const [hospital, setHospital] = useState('');
    const [service, setService] = useState('');
    const [serviceID, setserviceID] = useState('');
    const [professional, setProfessional] = useState([]);
    const [profID, setProfID] = useState('');
    const [cityID, setCityID] = useState('');

    const [payment, setPayment] = useState({});

    const [openCaller, setOpenCaller] = useState(false);
    const [openPatient, setOpenPatient] = useState(false);
    const [openService, setOpenService] = useState(false);
    const [zone, setZone] = useState([]);
    const [zoneID, setZoneID] = useState("");

    const [anchorEl, setAnchorEl] = useState(null);
    const [showActions, setShowActions] = useState(true);

    const [loading, setLoading] = useState(true);

    const [value, setValue] = useState('2');

    const [isModalOpen, setIsModalOpen] = useState(false);

    const handleOpenModal = () => {
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
    };

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };

    const handleMenu = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const handleChangeAction = (event) => {
        setShowActions(event.target.checked);
    };

    //Code for Model
    const handleOpenCaller = () => setOpenCaller(true);
    const handleCloseCaller = () => setOpenCaller(false);

    const handleOpenPatient = () => setOpenPatient(true);
    const handleClosePatient = () => setOpenPatient(false);

    const handleOpenService = () => setOpenService(true);
    const handleCloseService = () => setOpenService(false);

    useEffect(() => {
        const getCallerDetails = async () => {
            if (callerID) {
                try {
                    const res = await fetch(`${port}/web/Caller_details_api/${callerID}`);
                    const data = await res.json();
                    console.log("Caller Details ID wise", data);
                    setCaller(data.caller);
                    // setRelation(data.caller.caller_rel_id);
                } catch (error) {
                    console.error("Error fetching Caller Details ID wise:", error);
                }
            }
        };
        getCallerDetails();
    }, [callerID]);

    useEffect(() => {
        const getPatientDetails = async () => {
            if (patientID) {
                console.log("Patient ID", patientID)
                try {
                    const res = await fetch(`${port}/web/patient_detail_info_api/${patientID}`);
                    const data = await res.json();
                    console.log("Patient Details ID wise", data);
                    setPatient(data.patient);
                    setHospital(data.hospital);
                    setCityID(data.patient.city_id.city_id);
                } catch (error) {
                    console.error("Error fetching Patient Details ID wise:", error);
                }
            }
        };
        getPatientDetails();
    }, [patientID]);

    useEffect(() => {
        const getServiceDetails = async () => {
            if (eventPlanID) {
                try {
                    const res = await fetch(`${port}/web/Service_requirment_api/${eventPlanID}`);
                    const data = await res.json();
                    console.log("Service Details ID wise", data);
                    setService(data.services);
                    setserviceID(data.services.srv_id.srv_id);
                    console.log("Service ID....", data.services.srv_id.srv_id)
                } catch (error) {
                    console.error("Error fetching Service Details ID wise:", error);
                }
            }
        };
        getServiceDetails();
    }, [eventPlanID]);

    useEffect(() => {
        const getPaymentDetails = async () => {
            if (eventID) {
                try {
                    const res = await fetch(`${port}/web/get_payment_details/${eventID}`);
                    const data = await res.json();
                    console.log("Payment Payment Details ID wise.....", res);
                    setPayment(data);
                } catch (error) {
                    console.error("Error fetching Payment Details ID wise:", error);
                }
            }
        };
        getPaymentDetails();
    }, [eventID]);

    useEffect(() => {
        const getZone = async () => {
            if (cityID) {
                try {
                    const res = await fetch(`${port}/web/agg_hhc_zone_api/${cityID}`);
                    const data = await res.json();
                    console.log("Zone List.........", data);
                    setZone(data);
                } catch (error) {
                    console.error("Error fetching Zone List:", error);
                }
            }
        };
        getZone();
    }, [cityID]);

    useEffect(() => {
        const getProfessional = async () => {
            try {
                let apiUrl = `${port}/web/agg_hhc_event_professional_api/`;

                if (zoneID) {
                    apiUrl = `${port}/web/agg_hhc_event_professional_api/?zone=${zoneID}`;
                }
                const res = await fetch(apiUrl);
                const data = await res.json();
                console.log("Professional List.........", data);
                setProfessional(data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching Professional List:", error);
                setLoading(false);
            }
        };
        getProfessional();
    }, [zoneID]);

    const formatDate = (dateString) => {
        const dateTime = new Date(dateString);
        const day = dateTime.getDate().toString().padStart(2, '0'); // Get day with leading zero
        const month = (dateTime.getMonth() + 1).toString().padStart(2, '0'); // Get month with leading zero
        const year = dateTime.getFullYear();
        const hours = dateTime.getHours() % 12 || 12; // Get hours in 12-hour format
        const minutes = dateTime.getMinutes().toString().padStart(2, '0'); // Get minutes with leading zero
        const ampm = dateTime.getHours() >= 12 ? 'PM' : 'AM'; // Determine AM or PM

        return `${day}/${month}/${year} ${hours}:${minutes} ${ampm}`;
    };

    const handleProfessionalSelect = (profId) => {
        const selectedProfessional = professional.find((item) => item.srv_prof_id === profId);
        if (selectedProfessional) {
            console.log("selectedProfessional....", selectedProfessional.srv_prof_id)
            setProfID(selectedProfessional.srv_prof_id);
            handleAllocation(selectedProfessional.srv_prof_id);
        }
    };

    async function handleAllocation(profID) {
        // event.preventDefault();
        const requestData = {
            eve_id: eventID,
            srv_prof_id: profID,
            srv_id: serviceID,
        };
        console.log("Professional Allocation API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/allocate_api`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json();
            console.log("Results.....", result);
            navigate('/ongoing');
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    return (
        <>
            <Navbar />
            <Box sx={{ width: '100%', typography: 'body1', mb: 2 }}>
                <Box sx={{ flexGrow: 1, width: "100%", }}>
                    <Grid container spacing={1}>
                        <Grid item xs={12} sm={6} md={6} lg={3}>

                            <Grid item xs={12}>
                                <Card style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
                                    <CardContent>
                                        <Stack direction="row" justifyContent="space-between">
                                            <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>CALLER DETAILS</Typography>
                                            <Button style={{ height: "2rem" }} onClick={handleOpenCaller}><img src={EditImage} style={{ height: "20px" }} alt="" /></Button>
                                        </Stack>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Contact Number</Typography>
                                            <Typography inline variant="body2" style={{ marginLeft: "15px" }}>{caller.phone}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Name</Typography>
                                            <Typography inline variant="body2">{caller.caller_fullname}</Typography>
                                        </Grid>

                                        {/* <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}> */}
                                            {/* <Typography inline variant="body2" color="text.secondary">Relation</Typography> */}
                                            {/* <Typography inline variant="body2">{caller.caller_rel_id.relation}</Typography> */}
                                            {/* <Typography inline variant="body2">Friend</Typography> */}
                                        {/* </Grid> */}

                                        <Modal
                                            open={openCaller}
                                            onClose={handleCloseCaller}
                                            aria-labelledby="modal-modal-title"
                                            aria-describedby="modal-modal-description"
                                        >
                                            <Box sx={{ ...style, width: 300, borderRadius: "10px" }}>

                                                <AppBar position="static" style={{
                                                    background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                    width: '22.8rem',
                                                    height: '3rem',
                                                    marginTop: '-16px',
                                                    marginLeft: "-32px",
                                                    borderRadius: "8px 10px 0 0",
                                                }}>
                                                    <div style={{ display: "flex" }}>
                                                        <Typography align="left" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "18px" }}>CALLER DETAILS</Typography>
                                                        <Button onClick={handleCloseCaller} sx={{ marginLeft: "9rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                    </div>
                                                </AppBar>
                                                <CallerView caller={caller} clrID={callerID} onClose={handleCloseCaller} />
                                            </Box>
                                        </Modal>
                                    </CardContent>
                                </Card>
                            </Grid>

                            <Grid xs={12} >
                                <Card style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px', marginTop: "10px" }}>
                                    <CardContent>
                                        <Stack direction="row" justifyContent="space-between">
                                            <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>PATIENT DETAILS</Typography>
                                            <Button style={{ height: "2rem" }} onClick={handleOpenPatient}><img src={EditImage} style={{ height: "20px" }} alt="" /></Button>
                                        </Stack>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Contact Number</Typography>
                                            <Typography inline variant="body2">{patient.phone_no}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Email</Typography>
                                            <Typography inline variant="body2">{patient.patient_email_id}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Name</Typography>
                                            <Typography inline variant="body2">{patient.name}</Typography>
                                        </Grid>

                                        {/* <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Relation</Typography>
                                            <Typography inline variant="body2">Friend</Typography>
                                        </Grid> */}

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Gender</Typography>
                                            <Typography inline variant="body2">{patient.gender_id === 1 ? 'Male' : 'Female'}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Age</Typography>
                                            <Typography inline variant="body2">{patient.Age} Years</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Remark</Typography>
                                            <Typography inline variant="body2">{patient.Suffered_from}</Typography>
                                        </Grid>

                                        {/* <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Preferred Hospital</Typography>
                                            <Typography inline variant="body2">{patient.preferred_hosp_id ? patient.preferred_hosp_id.hospital_name : "-" }</Typography>
                                        </Grid> */}

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Zone</Typography>
                                            <Typography inline variant="body2">{patient.prof_zone_id ? patient.prof_zone_id.Name : '-'}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Address</Typography>
                                            <Typography inline variant="body2">{patient.address}</Typography>
                                        </Grid>
                                        <Modal
                                            open={openPatient}
                                            onClose={handleClosePatient}
                                            aria-labelledby="modal-modal-title"
                                            aria-describedby="modal-modal-description"
                                        >
                                            <Box sx={{ ...style, width: 400, borderRadius: "10px" }}>

                                                <AppBar position="static" style={{
                                                    background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                    width: '29rem',
                                                    height: '3rem',
                                                    marginTop: '-16px',
                                                    marginLeft: "-32px",
                                                    borderRadius: "8px 10px 0 0",
                                                }}>
                                                    <div style={{ display: "flex" }}>
                                                        <Typography align="left" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "18px" }}>PATIENT DETAILS</Typography>
                                                        <Button onClick={handleClosePatient} sx={{ marginLeft: "15rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                    </div>
                                                </AppBar>
                                                <PatientView ptnID={patientID} ptnData={patient} hospData={hospital} onClose={handleClosePatient} />
                                            </Box>
                                        </Modal>
                                    </CardContent>
                                </Card>
                            </Grid>
                        </Grid>

                        <Grid item xs={12} sm={6} md={6} lg={3}>

                            <Grid item xs={12}>
                                <Card style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px', }}>
                                    <CardContent>
                                        <Stack direction="row" justifyContent="space-between">
                                            <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>SERVICE REQUIREMENTS</Typography>
                                            <Button style={{ height: "2rem" }} onClick={handleOpenService}><img src={EditImage} style={{ height: "20px" }} alt="" /></Button>
                                        </Stack>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Service</Typography>
                                            <Typography inline variant="body2">{service.srv_id ? service.srv_id.service_title : '-'}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Sub Service</Typography>
                                            <Typography inline variant="body2">{service.sub_srv_id ? service.sub_srv_id.recommomded_service : '-'}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Start Date</Typography>
                                            <Typography inline variant="body2">{formatDate(service.start_date)}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">End Date</Typography>
                                            <Typography inline variant="body2">{formatDate(service.end_date)}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Consultant Preferred</Typography>
                                            <Typography inline variant="body2">{service.prof_prefered === 1 ? 'Male' : 'Female'}</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Remark</Typography>
                                            <Typography inline variant="body2">{service.remark}</Typography>
                                        </Grid>

                                        <Modal
                                            open={openService}
                                            onClose={handleCloseService}
                                            aria-labelledby="modal-modal-title"
                                            aria-describedby="modal-modal-description"
                                        >
                                            <Box sx={{ ...style, width: 300, borderRadius: "10px" }}>
                                                <AppBar position="static" style={{
                                                    background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                    width: '22.8rem',
                                                    height: '3rem',
                                                    marginTop: '-16px',
                                                    marginLeft: "-32px",
                                                    borderRadius: "8px 10px 0 0",
                                                }}>
                                                    <div style={{ display: "flex" }}>
                                                        <Typography align="left" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "18px" }}>SERVICE DETAILS</Typography>
                                                        <Button onClick={handleCloseService} sx={{ marginLeft: "9rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                    </div>
                                                </AppBar>
                                                <ServiceInfo eveID={eventPlanID} srvData={service} />
                                            </Box>
                                        </Modal>
                                    </CardContent>
                                </Card>
                            </Grid>

                            <Grid item xs={12}>
                                <Card style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px', marginTop: "10px" }}>
                                    <CardContent>
                                        <Stack direction="row" alignItems="left">
                                            <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>PAYMENT STATUS</Typography>

                                        </Stack>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Total Amount</Typography>
                                            <Typography inline variant="body2">{payment.Total_Amount} ₹</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Paid</Typography>
                                            <Typography inline variant="body2">{payment.Paid_Amount} ₹</Typography>
                                        </Grid>

                                        <Grid container style={{ justifyContent: "space-between", marginTop: "10px" }}>
                                            <Typography inline variant="body2" color="text.secondary">Pending Amount</Typography>
                                            <Typography inline variant="body2">{payment.Pending_Amount} ₹</Typography>
                                        </Grid>
                                        <Button variant="contained" sx={{ marginTop: '22px', background: '#69A5EB', borderRadius: '10px', textTransform: "capitalize", }} onClick={handleOpenModal}>Make Payment</Button>
                                        <Modal
                                            open={isModalOpen}
                                            onClose={handleCloseModal}
                                            aria-labelledby="modal-title"
                                            aria-describedby="modal-description"
                                        >

                                            <Box sx={{ ...style, width: 300, borderRadius: "10px" }}>
                                                <AppBar position="static" style={{
                                                    background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                    width: '22.8rem',
                                                    height: '3rem',
                                                    marginTop: '-16px',
                                                    marginLeft: "-32px",
                                                    borderRadius: "8px 10px 0 0",
                                                }}>
                                                    <div style={{ display: "flex" }}>
                                                        <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "18px" }}>Billing Information</Typography>
                                                        <Button onClick={handleCloseModal} sx={{ marginLeft: "9rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                    </div>
                                                </AppBar>
                                                <Payment eveID={eventID} pay={payment} ptnData={patient} onClose={handleCloseModal} />
                                                {/* <Button onClick={handleCloseModal}>Close Modal</Button> */}
                                            </Box>
                                        </Modal>
                                    </CardContent>
                                </Card>
                            </Grid>

                        </Grid>

                        <Grid item xs={12} sm={12} md={12} lg={6}>
                            <Card style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px', }}>
                                <CardContent>
                                    <Stack direction="row" justifyContent="space-between">
                                        <Typography sx={{ fontSize: 16, fontWeight: 600 }} color="text.secondary">PROFESSIONAL AVAILABILITY</Typography>

                                        {/* <TextField
                                            id="Name"
                                            select
                                            label="select zone"
                                            size="small"
                                            sx={{ width: '24ch', textAlign: "left", }}
                                            onChange={(e) => setZoneID(e.target.value)}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '200px',
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {zone.map((option) => (
                                                <MenuItem key={option.prof_zone_id} value={option.prof_zone_id}
                                                    sx={{ fontSize: "14px" }}>
                                                    {option.Name}
                                                </MenuItem>
                                            ))}
                                        </TextField> */}

                                        <Autocomplete
                                            id="zone-select"
                                            options={zone}
                                            getOptionLabel={(option) => option.Name}
                                            sx={{ width: '24ch', textAlign: 'left', }}
                                            renderInput={(params) => <TextField {...params} label="Select Zone" size="small"
                                            />}
                                            onChange={(e, selectedOption) => {
                                                if (selectedOption) {
                                                    setZoneID(selectedOption.prof_zone_id);
                                                } else {
                                                    setZoneID("");
                                                }
                                            }}
                                            MenuProps={{
                                                PaperProps: {
                                                    style: {
                                                        maxHeight: '200px',
                                                        // overflowY: 'auto',
                                                    },
                                                },
                                            }}
                                            renderOption={(props, option) => (
                                                <MenuItem
                                                    {...props}
                                                    sx={{ fontSize: '14px' }}
                                                >
                                                    {option.Name}
                                                </MenuItem>
                                            )}
                                        />
                                    </Stack>

                                    <Box sx={{ height: "auto", marginTop: "10px" }}>
                                        <TableContainer>
                                            <Table>
                                                <TableHead >
                                                    <TableRow>
                                                        <ViewServiceCard style={{ background: "#69A5EB", color: "#FFFFFF" }}>
                                                            <CardContent style={{ flex: 3, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Professional Name</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 2, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Skill set</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 6, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Preferred Location</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 1, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Type</Typography>
                                                            </CardContent>
                                                            {/* <CardContent style={{ flex: 2, borderRight: "1px solid #FFFFFF" }}>
                                                                    <Typography variant='subtitle2'>Availability</Typography>
                                                                </CardContent> */}
                                                            <CardContent style={{ flex: 1, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Action</Typography>
                                                            </CardContent>
                                                        </ViewServiceCard>
                                                    </TableRow>
                                                </TableHead>
                                                {loading ? (
                                                    <CircularProgress style={{ marginTop: "100px" }} />
                                                ) : (
                                                    <TableBody>
                                                        {professional.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((row) => (
                                                            <TableRow
                                                                key={row.srv_prof_id}
                                                                value={row.srv_prof_id}
                                                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                                            >
                                                                <ViewServiceCard>
                                                                    <CardContent style={{ flex: 3, float: "left" }}>
                                                                        <Typography variant='body2'>{row.prof_fullname}</Typography>
                                                                    </CardContent>
                                                                    <CardContent style={{ flex: 2 }}>
                                                                        <Typography variant='body2'>{row.skill_set}</Typography>
                                                                    </CardContent>
                                                                    <CardContent style={{ flex: 6 }}>
                                                                        <Typography variant='body2'>{row.address}</Typography>
                                                                    </CardContent>
                                                                    <CardContent style={{ flex: 1 }}>
                                                                        {row.Job_type === 1 ? (
                                                                            <Typography variant='body2'>On Call</Typography>
                                                                        ) : row.Job_type === 2 ? (
                                                                            <Typography variant='body2'>Full Time</Typography>
                                                                        ) : (
                                                                            <Typography variant='body2'>Part Time</Typography>
                                                                        )}
                                                                    </CardContent>
                                                                    {/* <CardContent style={{ flex: 2 }}> */}
                                                                    {/* <Typography variant='body2'>{row.progress}</Typography> */}
                                                                    {/* <Typography variant='body2'>--</Typography> */}
                                                                    {/* </CardContent> */}
                                                                    <CardContent style={{ flex: 1 }}>
                                                                        {/* <IconButton
                                                                            size="large"
                                                                            aria-label="account of current user"
                                                                            aria-controls="menu-appbar"
                                                                            aria-haspopup="true"
                                                                            align="right"
                                                                            // onClick={handleMenu(row.srv_prof_id)}
                                                                            onClick={(event) => {
                                                                                handleProfessionalSelect(row.srv_prof_id); // Pass srv_prof_id directly here
                                                                                handleMenu(event);
                                                                              }}
                                                                            color="inherit"
                                                                        >
                                                                            <MoreHorizOutlinedIcon style={{ fontSize: "18px", cursor: "pointer" }} />
                                                                        </IconButton>
                                                                        {showActions && (
                                                                            <Menu
                                                                                id="menu-appbar"
                                                                                anchorEl={anchorEl}
                                                                                anchorOrigin={{
                                                                                    vertical: 'top',
                                                                                    horizontal: 'right',
                                                                                }}
                                                                                keepMounted
                                                                                transformOrigin={{
                                                                                    vertical: 'top',
                                                                                    horizontal: 'right',
                                                                                }}
                                                                                open={Boolean(anchorEl)}
                                                                                onClose={handleClose}
                                                                            >
                                                                                <MenuItem sx={{ color: "#2CDFAA" }}
                                                                                 onClick={(event) => {
                                                                                    event.preventDefault(); // Prevent the default navigation behavior
                                                                                    handleProfessionalSelect(row.srv_prof_id);
                                                                                  }}
                                                                                 >Allocate</MenuItem>
                                                                                <MenuItem sx={{ color: "#69A5EB" }}
                                                                               
                                                                                >Deallocate</MenuItem>
                                                                                <MenuItem sx={{ color: "#E80054" }}>Denial</MenuItem>
                                                                                <MenuItem>Calender</MenuItem>
                                                                            </Menu>
                                                                        )} */}
                                                                        <Button variant='outlined' sx={{ width: "4rem", textTransform: "capitalize", }} onClick={() => handleProfessionalSelect(row.srv_prof_id)}><HowToRegIcon /></Button>
                                                                    </CardContent>
                                                                </ViewServiceCard>
                                                            </TableRow>
                                                        ))}
                                                    </TableBody>
                                                )}
                                            </Table>
                                        </TableContainer>
                                        <TablePagination
                                            rowsPerPageOptions={[10, 25, 100]}
                                            component="div"
                                            count={professional.length}
                                            rowsPerPage={rowsPerPage}
                                            page={page}
                                            onPageChange={handleChangePage}
                                            onRowsPerPageChange={handleChangeRowsPerPage}
                                        />
                                    </Box>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                </Box>
            </Box>

            <Footer />
        </>
    )
}

export default Viewservice
