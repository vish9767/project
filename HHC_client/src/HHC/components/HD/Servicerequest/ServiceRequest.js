import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from "@mui/material/Typography";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from '@mui/material/TablePagination';
import Button from '@mui/material/Button';
import SmartphoneIcon from '@mui/icons-material/Smartphone';
import LanguageIcon from '@mui/icons-material/Language';
import CallOutlinedIcon from '@mui/icons-material/CallOutlined';
import DirectionsWalkOutlinedIcon from '@mui/icons-material/DirectionsWalkOutlined';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';
import { styled } from '@mui/system';
import useMediaQuery from '@mui/material/useMediaQuery';
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import SearchIcon from '@mui/icons-material/Search';
import { DatePicker, LocalizationProvider } from '@mui/lab';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import { useNavigate } from "react-router-dom";
import Navbar from '../../../Navbar';
import Footer from '../../../Footer';
import Header from '../../../Header';

const ServiceCard = styled(Card)({
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: '10px',
    backgroundColor: 'white',
    boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)',
    height: "55px",
    borderRadius: '10px',
    transition: '0.5s ease-in-out',
    '&:hover': {
        backgroundColor: '#F7F7F7',
        cursor: 'pointer',
    },
});

const ServiceRequest = () => {
    const navigate = useNavigate();
    const port = process.env.REACT_APP_API_KEY;

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [serviceRequest, setServiceRequest] = useState([]);
    // const [selectedCallerStatus, setSelectedCallerStatus] = useState(null);
    const [tableHeight, setTableHeight] = useState('auto');

    const [eventID, setEventID] = useState('');
    const [requestAllocation, setRequestAllocation] = useState({});

    // Usestate for Filter values in input field
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedService, setSelectedService] = useState('');
    const [selectedCallerStatus, setSelectedCallerStatus] = useState('');

    const isSmallScreen = useMediaQuery('(max-width:600px)');

    const handleDateChange = (e) => {
        setSelectedDate(e.target.value);
    };

    const handleServiceChange = (e) => {
        setSelectedService(e.target.value);
    };

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };

    useEffect(() => {
        const getServiceRequest = async () => {
            try {
                const res = await fetch(`${port}/web/service_request`);
                const data = await res.json();
                console.log("Service Request Data.........", data);
                setServiceRequest(data.event_code);
            } catch (error) {
                console.error("Error fetching Service Request Data:", error);
            }
        };
        getServiceRequest();
    }, []);

    useEffect(() => {
        const updateTableHeight = () => {
            // Calculate the available screen height and set the table height accordingly
            const screenHeight = window.innerHeight;
            setTableHeight(`${screenHeight}px`);
        };

        // Call the function initially and add a resize event listener
        updateTableHeight();
        window.addEventListener('resize', updateTableHeight);

        // Clean up the event listener on unmount
        return () => {
            window.removeEventListener('resize', updateTableHeight);
        };
    }, []);

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = date.getDate().toString().padStart(2, '0'); // Get day with leading zero
        const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Get month with leading zero
        const year = date.getFullYear();

        return `${day}/${month}/${year}`;
    };

    const getCallerStatusTooltip = (callerStatus) => {
        const icon =
            callerStatus === 1
                ? <SmartphoneIcon style={{ color: "#EB8793" }} />
                : callerStatus === 2
                    ? <LanguageIcon style={{ color: "#7AB7EE" }} />
                    : callerStatus === 3
                        ? <DirectionsWalkOutlinedIcon style={{ color: "#84CDB1" }} />
                        : callerStatus === 4
                            ? <CallOutlinedIcon style={{ color: "#8D9BED" }} />
                            : <ErrorOutlineIcon style={{ color: "#EB8793" }} />;

        return (
            <IconButton>
                {icon}
            </IconButton>
        );
    };

    // const filterByCallerStatus = () => {
    //     if (selectedCallerStatus) {
    //         return serviceRequest.filter(
    //             (row) => row.caller_status === selectedCallerStatus
    //         );
    //     }
    //     return serviceRequest;
    // };

    const filteredData = serviceRequest.filter((item) => {
        if (
            (selectedDate === '' || item.event_start_date.includes(selectedDate)) &&
            (selectedService === '' || item.service_name.toLowerCase().includes(selectedService.toLowerCase())) &&
            (selectedCallerStatus === '' || item.caller_status === selectedCallerStatus)
        ) {
            return true;
        }
        return false;
    });

    const getEventIDRequest = (eveId) => {
        const selectedRequest = serviceRequest.find(item => item.event_id === eveId);
        console.log("Selected Event:", selectedRequest);
        if (selectedRequest) {
            console.log("Selected Event ID:", selectedRequest.event_id);
            setEventID(selectedRequest.event_id);
        }
    };

    useEffect(() => {
        const getRequestAllocation = async () => {
            if (eventID) {
                try {
                    const res = await fetch(`${port}/web/agg_hhc_srv_req_prof_allocate/${eventID}`);
                    const data = await res.json();
                    console.log("Request Allocation Data.........", data);
                    setRequestAllocation(data);
                    const eventValue = data.Event_ID;
                    const patientValue = data.patient_details.agg_sp_pt_id;
                    const callerValue = data.caller_details.caller_id;
                    const eventPlanValue = data.POC[0].eve_poc_id;

                    console.log("eventID", eventValue);
                    console.log("patientID", patientValue);
                    console.log("callerID", callerValue);
                    console.log("eventPlanID", eventPlanValue);
                    navigate('/viewservice', {
                        state: {
                            patientID: patientValue,
                            callerID: callerValue,
                            eventPlanID: eventPlanValue,
                            eventID: eventValue,
                        },
                    });
                } catch (error) {
                    console.error("Error fetching Request Allocation:", error);
                }
            }
        };
        getRequestAllocation();
    }, [eventID]);

    return (
        <>
            <Navbar />
            {/* <Header/> */}
            <Box sx={{ flexGrow: 1, width: '100%', overflow: 'hidden' }}>

                <Stack direction={isSmallScreen ? 'column' : 'row'}
                    spacing={1}
                    alignItems={isSmallScreen ? 'center' : 'flex-start'}>
                    <Typography sx={{ fontSize: 16, fontWeight: 600, marginTop: "10px", marginLeft: "10px" }} color="text.secondary" gutterBottom>SERVICE REQUESTS</Typography>
                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            inputProps={{ 'aria-label': 'select date' }}
                            type="date"
                            value={selectedDate}
                            onChange={handleDateChange}
                        />
                        {/* <IconButton type="button" sx={{ p: '10px' }} aria-label="DD/MM/YYYY">
                        <CalendarTodayOutlinedIcon style={{ color: "#69A5EB" }} />
                </IconButton> */}
                    </Box>

                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1, }}
                            placeholder="Search Service |"
                            inputProps={{ 'aria-label': 'select service' }}
                            value={selectedService}
                            onChange={handleServiceChange}
                        />
                        <IconButton type="button" sx={{ p: '10px' }}>
                            <SearchIcon />
                        </IconButton>
                    </Box>

                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            placeholder="View Request by |"
                            inputProps={{ 'aria-label': 'view request by' }}
                        />
                        <IconButton type="button" sx={{ p: '6px' }} aria-label="search"
                            onClick={() => setSelectedCallerStatus(1)}
                        >

                            <SmartphoneIcon style={{ color: "#EB8793" }} />
                        </IconButton>
                        <IconButton type="button" sx={{ p: '6px' }} aria-label="search"
                            onClick={() => setSelectedCallerStatus(2)}
                        >
                            <LanguageIcon style={{ color: "#7AB7EE" }} />
                        </IconButton>
                        <IconButton type="button" sx={{ p: '6px' }} aria-label="search"
                            onClick={() => setSelectedCallerStatus(3)}
                        >
                            <DirectionsWalkOutlinedIcon style={{ color: "#84CDB1" }} />
                        </IconButton>
                        <IconButton type="button" sx={{ p: '6px' }} aria-label="search"
                            onClick={() => setSelectedCallerStatus(4)}
                        >
                            <CallOutlinedIcon style={{ color: "#8D9BED" }} />
                        </IconButton>
                    </Box>
                </Stack>

                <TableContainer
                // sx={{ height: tableHeight }}
                >
                    <Table>
                        <TableHead>
                            <TableRow >
                                <ServiceCard style={{ background: "#69A5EB", color: "#FFFFFF" }}>
                                    <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Sr. No</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Source</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Event Code</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Patient Name</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Patient Mobile</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Preferred Professional</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Service Name</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Start Date</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "8%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant="subtitle2">Zone</Typography>
                                    </CardContent>

                                    <CardContent style={{ width: "8%", }}>
                                        <Typography variant="subtitle2">Action </Typography>
                                    </CardContent>
                                </ServiceCard>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {filteredData.length === 0 ? (
                                <TableRow>
                                    <CardContent >
                                        <Typography variant="body2">
                                            No Data Available
                                        </Typography>
                                    </CardContent>
                                </TableRow>
                            ) : (
                                filteredData.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                                    .map((row, index) => (
                                        <TableRow
                                            key={row.event_id}
                                            sx={{ '&:last-child td, &:last-child th': { border: 0, } }}>
                                            <ServiceCard>
                                                <CardContent style={{ width: "5%" }}>
                                                    <Typography variant="body2">{index + 1}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "5%" }}>
                                                    <Typography variant="body2">{getCallerStatusTooltip(row.caller_status)}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "10%" }}>
                                                    <Typography variant="body2">{row.event_code}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "10%" }}>
                                                    <Typography variant="body2">{row.patient_name}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "10%" }}>
                                                    <div style={{ display: "flex", }}>
                                                        <CallOutlinedIcon sx={{ color: "#3A974C", fontSize: "18px" }} />
                                                        <Typography variant="body2">{row.patient_number}</Typography>
                                                    </div>

                                                </CardContent>
                                                <CardContent style={{ width: "15%" }}>
                                                    <Typography variant="body2">{row.professional_prefered === 1 ? "Male" : "Female"}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "15%" }}>
                                                    <Typography variant="body2">{row.service_name}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "10%" }}>
                                                    <div style={{ display: "flex", }}>
                                                        <CalendarMonthOutlinedIcon sx={{ color: "#69A5EB", fontSize: "18px" }} />
                                                        <Typography variant="body2">{formatDate(row.event_start_date)}</Typography>
                                                    </div>
                                                </CardContent>
                                                <CardContent style={{ width: "8%" }}>
                                                    <Typography variant="body2">{row.patient_zone}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "8%" }}>
                                                    <Button variant="outlined" style={{ textTransform: "capitalize", borderRadius: "8px", width: "5rem", height: "2.4rem", marginTop: "8px" }} onClick={() => getEventIDRequest(row.event_id)}>Allocate</Button>
                                                </CardContent>
                                            </ServiceCard>
                                        </TableRow>
                                    )
                                    ))}
                        </TableBody>
                    </Table>
                </TableContainer>

                <TablePagination
                    rowsPerPageOptions={[5, 10, 25, 100]}
                    component="div"
                    count={serviceRequest.length}
                    rowsPerPage={rowsPerPage}
                    page={page}
                    onPageChange={handleChangePage}
                    onRowsPerPageChange={handleChangeRowsPerPage}
                />
            </Box>
            <Footer />
        </>
    )
}

export default ServiceRequest

