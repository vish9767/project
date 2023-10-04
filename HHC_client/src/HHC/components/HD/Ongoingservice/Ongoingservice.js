import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import TextField from '@mui/material/TextField';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from '@mui/material/TablePagination';
import Button from '@mui/material/Button';
import InputBase from '@mui/material/InputBase';
import CircleIcon from '@mui/icons-material/Circle';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import Modal from '@mui/material/Modal';
import { border, styled } from '@mui/system';
import CloseIcon from '@mui/icons-material/Close';
import Reschedule from './ActionComponents/Reschedule';
import Cancellation from './ActionComponents/Cancellation';
import Payment from './ActionComponents/Payment';
import useMediaQuery from '@mui/material/useMediaQuery';
import { Tooltip, IconButton } from '@mui/material';
import AppBar from '@mui/material/AppBar';
import LocalPhoneOutlinedIcon from '@mui/icons-material/LocalPhoneOutlined';
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import SearchIcon from '@mui/icons-material/Search';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import dayjs from 'dayjs';
import { DemoContainer, DemoItem } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import Professional from './ActionComponents/Professional';
import Navbar from '../../../Navbar';
import Footer from '../../../Footer';
import Header from '../../../Header';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

const customStyles = {
    "& .Mui-focused": {
        outline: 'none',
    },
};

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    pt: 2,
    px: 4,
    pb: 3,
};

const OngoingServiceCard = styled(Card)({
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

const Ongoingservice = () => {
    const port = process.env.REACT_APP_API_KEY;

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(5);
    const [auth, setAuth] = useState(true);
    const [anchorEl, setAnchorEl] = useState(null);
    const [openReschedule, setOpenReschedule] = useState(false);
    const [openCancel, setOpenCancel] = useState(false);
    const [openPayment, setOpenPayment] = useState(false);
    const [openProfessional, setOpenProfessional] = useState(false);
    const [onServices, setOnServices] = useState([]);

     // Usestate for getting data event id wise
    const [eventID, setEventID] = useState(null);
    const [serviceID, setServiceID] = useState(null);
    const [startDateTime, setStartDateTime] = useState(null);
    const [endDateTime, setEndDateTime] = useState(null);
    const [ptnName, setPtnName] = useState(null);
    const [ptnPhn, setPtnPhn] = useState(null);

    // Usestate for Filter values in input field
    const [filteredData, setFilteredData] = useState(onServices);
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedProfessional, setSelectedProfessional] = useState('');
    const [selectedService, setSelectedService] = useState('');

    const [isOpen, setIsOpen] = useState(false);

    const [tableHeight, setTableHeight] = useState('auto');
    const isSmallScreen = useMediaQuery('(max-width:600px)');

    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        setRowsPerPage(+event.target.value);
        setPage(0);
    };

    const handleChange = (event) => {
        setAuth(event.target.checked);
    };

    const handleMenu = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    //Model open and close function
    const handleOpenReschedule = () => {
        setOpenReschedule(true);
    };
    const handleCloseReschedule = () => {
        setOpenReschedule(false);
    };
    const handleOpenCancel = () => {
        setOpenCancel(true);
    };
    const handleCloseCancel = () => {
        setOpenCancel(false);
    };
    const handleOpenPayment = () => {
        setOpenPayment(true);
    };
    const handleClosePayment = () => {
        setOpenPayment(false);
    };
    const handleOpenProfessional = () => {
        setOpenProfessional(true);
    };
    const handleCloseProfessional = () => {
        setOpenProfessional(false);
    };

    useEffect(() => {
        const updateTableHeight = () => {
            const screenHeight = window.innerHeight;
            setTableHeight(`${screenHeight}px`);
        };
        updateTableHeight();
        window.addEventListener('resize', updateTableHeight);
        return () => {
            window.removeEventListener('resize', updateTableHeight);
        };
    }, []);

    useEffect(() => {
        const getOngoingServices = async () => {
            try {
                const res = await fetch(`${port}/web/ongoing_service`);
                const data = await res.json();
                console.log("Ongoing Services Data.........", data);
                setOnServices(data);
            } catch (error) {
                console.error("Error fetching Ongoing Services Data:", error);
            }
        };
        getOngoingServices();
    }, []);

    // const filteredDataTable = onServices.filter(item => item !== null);
    // console.log("filtered Data Table...", filteredDataTable);

    const eventIDRequest = (eveId) => {
        const selectedReschedule = onServices.find(item => item.eve_id === eveId);
        console.log("Selected Service:", selectedReschedule);
        if (selectedReschedule) {
            console.log("Selected Event ID:", selectedReschedule.eve_id);
            console.log("Selected Service ID:", selectedReschedule.srv_prof_id[0].srv_id.srv_id);
            setEventID(selectedReschedule.eve_id);
            setServiceID(selectedReschedule.srv_prof_id[0].srv_id.srv_id);
            setStartDateTime(selectedReschedule.srv_prof_id[0].start_date);
            setEndDateTime(selectedReschedule.srv_prof_id[0].end_date);
            setPtnName(selectedReschedule.agg_sp_pt_id.name);
            setPtnPhn(selectedReschedule.agg_sp_pt_id.phone_no);
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const day = date.getDate().toString().padStart(2, '0'); // Get day with leading zero
        const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Get month with leading zero
        const year = date.getFullYear();

        return `${day}/${month}/${year}`;
    };

    const getServiceStatusTooltip = (serviceStatus) => {
        const title =
            serviceStatus === 1
                ? "Service about to end"
                : serviceStatus === 2
                    ? "Acknowledge pending"
                    : serviceStatus === 3
                        ? "Acknowledge by professional"
                        : serviceStatus === 4
                            ? "Closure completed"
                            : serviceStatus === 5
                                ? "Pending for closure"
                                : "";

        const iconColor =
            serviceStatus === 1
                ? "#D61616"
                : serviceStatus === 2
                    ? "#2A1D1D"
                    : serviceStatus === 3
                        ? "#3D8A00"
                        : serviceStatus === 4
                            ? "#1342BA"
                            : serviceStatus === 5
                                ? "#BA139F"
                                : "#000000";

        return (
            <Tooltip title={title} arrow>
                <IconButton>
                    <CircleIcon style={{ color: iconColor, fontSize: '20px' }} />
                </IconButton>
            </Tooltip>
        );
    };

    useEffect(() => {
        //     if (selectedDate) {
        //         const filtered = onServices.filter(item => {
        //             const itemDate = new Date(item.srv_prof_id[0].start_date); // Assuming date is a field in your data
        //             const selected = new Date(selectedDate);

        //             return itemDate.toDateString() === selected.toDateString();
        //         });
        //         console.log("Selected Data:", filtered)
        //         setFilteredData(filtered);
        //     } else {
        //         setFilteredData(onServices);
        //     }
        // }, [selectedDate, onServices]);
        const filtered = onServices.filter(item => {
            const itemDateMatches = !selectedDate || item.srv_prof_id.some(prof => {
                const itemDate = new Date(prof.start_date);
                const selected = new Date(selectedDate);
                return itemDate.toDateString() === selected.toDateString();
            });

            const profNameMatches = !selectedProfessional || item.srv_prof_id.some(prof => {
                return prof.srv_prof_id.prof_fullname.toLowerCase().includes(selectedProfessional.toLowerCase());
            });

            const serviceNameMatches = !selectedService || item.srv_prof_id.some(prof => {
                return prof.srv_id.service_title.toLowerCase().includes(selectedService.toLowerCase());
            });

            return itemDateMatches && profNameMatches && serviceNameMatches;
        });

        setFilteredData(filtered);
    }, [selectedDate, selectedProfessional, selectedService, onServices]);

    return (
        <>
            <Navbar />
            {/* <Header /> */}
            <Box sx={{ flexGrow: 1, width: '100%', overflow: 'hidden', margin: '0 auto' }} >
                <Stack direction={isSmallScreen ? 'column' : 'row'} spacing={1} alignItems={isSmallScreen ? 'center' : 'flex-start'}>
                    <Typography sx={{ fontSize: 16, fontWeight: 600, marginTop: "10px", marginLeft: "10px" }} color="text.secondary" gutterBottom>ONGOING SERVICES</Typography>
                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            type='date'
                            value={selectedDate}
                            onChange={event => setSelectedDate(event.target.value)}
                        // placeholder="Start Date | DD/MM/YYYY"
                        // inputProps={{ 'aria-label': 'select date' }}
                        />
                        {/* <IconButton type="button" sx={{ p: '10px' }} aria-label="DD/MM/YYYY">
                        <CalendarMonthOutlinedIcon style={{ color: "#69A5EB" }} />
                    </IconButton> */}

                    </Box>

                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            placeholder="Search Professional Name |"
                            inputProps={{ 'aria-label': 'search professional' }}
                            type="text"
                            value={selectedProfessional}
                            onChange={(e) => setSelectedProfessional(e.target.value)}
                        />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Box>

                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 300, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1, }}
                            placeholder="Select Service |"
                            inputProps={{ 'aria-label': 'select service' }}
                            type="text"
                            value={selectedService}
                            onChange={(e) => setSelectedService(e.target.value)}
                        />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Box>
                </Stack>

                <TableContainer
                // sx={{ height: tableHeight}}
                >
                    <Table>
                        <TableHead >
                            <TableRow >
                                <OngoingServiceCard style={{ background: "#69A5EB", color: "#FFFFFF", }}>
                                    <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Sr. No</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Event Code</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Patient Name</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Patient Mobile</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Professional Name</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "20%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Service Name</Typography>
                                    </CardContent >
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Start Date</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>End Date</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Payments</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Closure Done</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                        <Typography variant='subtitle2'>Status</Typography>
                                    </CardContent>
                                    <CardContent style={{ width: "5%" }}>
                                        <Typography variant='subtitle2'>Action</Typography>
                                    </CardContent>
                                </OngoingServiceCard>
                            </TableRow>
                        </TableHead>

                        <TableBody>
                            {filteredData.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                                .map((row, index) => (
                                    <TableRow
                                        key={index}
                                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                    >
                                        <OngoingServiceCard>
                                            <CardContent style={{ width: "5%" }}>
                                                <Typography variant="body2">
                                                    {index + 1}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "15%" }}>
                                                <Typography variant="body2">
                                                    {row.event_code}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "15%" }}>
                                                <Typography variant="body2">
                                                    {row.agg_sp_pt_id.name}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "15%" }}>
                                                <div style={{ display: "flex", }}>
                                                    <LocalPhoneOutlinedIcon sx={{ color: "#3A974C", fontSize: "18px" }} />
                                                    <Typography variant='body2'>{row.agg_sp_pt_id.phone_no}</Typography>
                                                </div>

                                            </CardContent>
                                            <CardContent style={{ width: "15%" }}>
                                                <Typography variant="body2">
                                                    {row.srv_prof_id[0].srv_prof_id.prof_fullname}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "20%" }}>
                                                <Typography variant="body2">
                                                    {row.srv_prof_id[0].srv_id.service_title}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "10%" }}>
                                                <div style={{ display: "flex" }}>
                                                    <CalendarMonthOutlinedIcon sx={{ color: "#69A5EB", fontSize: "18px" }} />
                                                    <Typography variant="body2">
                                                        {formatDate(row.srv_prof_id[0].start_date)}
                                                    </Typography>
                                                </div>
                                            </CardContent>
                                            <CardContent style={{ width: "10%" }}>
                                                <div style={{ display: "flex" }}>
                                                    <CalendarMonthOutlinedIcon sx={{ color: "#69A5EB", fontSize: "18px" }} />
                                                    <Typography variant="body2">
                                                        {formatDate(row.srv_prof_id[0].end_date)}
                                                    </Typography>
                                                </div>
                                            </CardContent>
                                            <CardContent style={{ width: "10%" }}>
                                                {row.Pending_amount === 0 ? (
                                                    <div style={{ display: "flex" }}>
                                                        <CheckCircleIcon style={{ fontSize: "16px", color: "#3D8A00" }} />
                                                        <Typography variant="body2">Completed</Typography>
                                                    </div>
                                                ) : (
                                                    <Typography variant="body2">₹ {row.Pending_amount}/{row.Total_cost}</Typography>
                                                )}
                                            </CardContent>
                                            <CardContent style={{ width: "5%" }}>
                                                <Typography variant="body2">
                                                    {row.session_status[0].session_done}/{row.session_status[0].Total_case_count}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "5%" }}>
                                                <Typography variant="body2">
                                                    {getServiceStatusTooltip(row.srv_prof_id[0].service_status)}
                                                </Typography>
                                            </CardContent>
                                            <CardContent style={{ width: "5%" }}>
                                                {auth && (
                                                    <div>
                                                        <IconButton
                                                            size="large"
                                                            aria-label="account of current user"
                                                            aria-controls="menu-appbar"
                                                            aria-haspopup="true"
                                                            align="right"
                                                            // onClick={handleMenu}
                                                            onClick={(event) => {
                                                                eventIDRequest(row.eve_id);
                                                                handleMenu(event)
                                                            }}
                                                            color="inherit"
                                                        >
                                                            <MoreHorizIcon style={{ fontSize: "18px", cursor: "pointer" }} />
                                                        </IconButton>
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
                                                            <MenuItem
                                                                onClick={() => handleOpenReschedule(() => eventIDRequest(row.eve_id))}
                                                            >Service Reschedule</MenuItem>
                                                            <MenuItem
                                                                onClick={() => handleOpenProfessional(() => eventIDRequest(row.eve_id))}
                                                            >Professional Reschedule</MenuItem>
                                                            <MenuItem
                                                                onClick={() => handleOpenCancel(() => eventIDRequest(row.eve_id))}
                                                            >Cancellation</MenuItem>
                                                            <MenuItem onClick={handleOpenPayment}>Payment Adjustments</MenuItem>
                                                            
                                                            <Modal
                                                                open={openReschedule}
                                                                onClose={handleCloseReschedule}
                                                                aria-labelledby="parent-modal-title"
                                                                aria-describedby="parent-modal-description"
                                                            >
                                                                <Box sx={{ ...style, width: 300, borderRadius: "10px", border: "none" }}>
                                                                    <AppBar position="static" style={{
                                                                        background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                                        width: '22.8rem',
                                                                        height: '3rem',
                                                                        marginTop: '-16px',
                                                                        marginLeft: "-32px",
                                                                        borderRadius: "8px 10px 0 0",
                                                                    }}>
                                                                        <div style={{ display: "flex" }}>
                                                                            <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "15px" }}>SERVICE DETAILS</Typography>
                                                                            <Button onClick={handleCloseReschedule} sx={{ marginLeft: "9rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                                        </div>
                                                                    </AppBar>
                                                                    <Reschedule eventID={eventID} eveStartDate={startDateTime} eveEndDate={endDateTime} open={openReschedule}
                                                                        onClose={handleCloseReschedule} />
                                                                </Box>
                                                            </Modal>

                                                            <Modal
                                                                open={openCancel}
                                                                onClose={handleCloseCancel}
                                                                aria-labelledby="parent-modal-title"
                                                                aria-describedby="parent-modal-description"
                                                            >
                                                                <Box sx={{ ...style, width: 300, borderRadius: "10px", border: "none" }}>
                                                                    <AppBar position="static" style={{
                                                                        background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                                        width: '22.8rem',
                                                                        height: '3rem',
                                                                        marginTop: '-16px',
                                                                        marginLeft: "-32px",
                                                                        borderRadius: "8px 10px 0 0",
                                                                    }}>
                                                                        <div style={{ display: "flex" }}>
                                                                            <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "15px" }}>SERVICE CANCELLATION</Typography>
                                                                            <Button onClick={handleCloseCancel} sx={{ marginLeft: "6rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                                        </div>
                                                                    </AppBar>
                                                                    <Cancellation eventID={eventID} onClose={handleCloseCancel} />
                                                                </Box>
                                                            </Modal>

                                                            <Modal
                                                                open={openPayment}
                                                                onClose={handleClosePayment}
                                                                aria-labelledby="parent-modal-title"
                                                                aria-describedby="parent-modal-description"
                                                            >
                                                                <Box sx={{ ...style, width: 300, borderRadius: "10px", border: "none" }}>
                                                                    <AppBar position="static" style={{
                                                                        background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                                        width: '22.8rem',
                                                                        height: '3rem',
                                                                        marginTop: '-16px',
                                                                        marginLeft: "-32px",
                                                                        borderRadius: "8px 10px 0 0",
                                                                    }}>
                                                                        <div style={{ display: "flex" }}>
                                                                            <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "15px" }}>PAYMENT ADJUSTMENT</Typography>
                                                                            <Button onClick={handleClosePayment} sx={{ marginLeft: "6rem", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                                        </div>
                                                                    </AppBar>
                                                                    <Payment />
                                                                </Box>
                                                            </Modal>

                                                            <Modal
                                                                open={openProfessional}
                                                                onClose={handleCloseProfessional}
                                                                aria-labelledby="parent-modal-title"
                                                                aria-describedby="parent-modal-description"
                                                            >
                                                                <Box sx={{ ...style, width: 300, borderRadius: "10px", border: "none" }}>
                                                                    <AppBar position="static" style={{
                                                                        background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                                                                        width: '22.8rem',
                                                                        height: '3rem',
                                                                        marginTop: '-16px',
                                                                        marginLeft: "-32px",
                                                                        borderRadius: "8px 10px 0 0",
                                                                    }}>
                                                                        <div style={{ display: "flex" }}>
                                                                            <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", marginLeft: "15px" }}>PROFESSIONAL RESCHEDULE</Typography>
                                                                            <Button onClick={handleCloseProfessional} sx={{ marginLeft: "50px", color: "#FFFFFF", marginTop: "2px", }}><CloseIcon /></Button>
                                                                        </div>
                                                                    </AppBar>
                                                                    <Professional eveID={eventID} serviceID={serviceID} ptnName={ptnName} ptnPhn={ptnPhn} onClose={handleCloseProfessional} />
                                                                </Box>
                                                            </Modal>
                                                        </Menu>
                                                    </div>
                                                )}
                                            </CardContent>
                                        </OngoingServiceCard>
                                    </TableRow>
                                ))}
                        </TableBody>
                    </Table>
                </TableContainer>

                <TablePagination
                    rowsPerPageOptions={[10, 25, 100]}
                    component="div"
                    count={onServices.length}
                    rowsPerPage={rowsPerPage}
                    page={page}
                    onPageChange={handleChangePage}
                    onRowsPerPageChange={handleChangeRowsPerPage}
                />
            </Box >
            <Footer />
        </>
    )
}

export default Ongoingservice

