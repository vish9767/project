import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import { Button } from '@mui/material';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from '@mui/material/TablePagination';
import dayjs from 'dayjs';
import IconButton from '@mui/material/IconButton';
import ProfessionalList from './ProfessionalList';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/system';
import useMediaQuery from '@mui/material/useMediaQuery';
import CalendarComponent from './calendar/CalendarComponent';
import Navbar from '../../../Navbar';
import Footer from '../../../Footer';
import Header from '../../../Header';
import { TabContext, TabPanel } from '@mui/lab';
import CircularProgress from '@mui/material/CircularProgress';

const ScheduleCard = styled(Card)({
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: '10px',
    backgroundColor: 'white',
    boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)',
    height: "55px",
    borderRadius: '10px',
    transition: '2s ease-in-out',
    '&:hover': {
        backgroundColor: '#F7F7F7',
        cursor: 'pointer',
    },
});

const Schedule = () => {
    const port = process.env.REACT_APP_API_KEY;

    const [value, setValue] = useState(dayjs('2023-05-30'));
    const [tabIndex, setTabIndex] = useState(1);
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(6);
    const [professionalList, setProfessionalList] = useState([]);
    const [selectedProfessional, setSelectedProfessional] = useState('');
    const [isEventDetailsModalOpen, setIsEventDetailsModalOpen] = useState(false);
    const [selectedProfessionalEvents, setSelectedProfessionalEvents] = useState([]);

    const [selectedProfName, setselectedProfName] = useState('');
    const [selectedService, setSelectedService] = useState('');
    const [loading, setLoading] = useState(true);

    const isSmallScreen = useMediaQuery('(max-width:600px)');

    const handleProfChange = (e) => {
        setselectedProfName(e.target.value);
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
        const getProfessionalList = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_event_professional_api/`);
                const data = await res.json();
                console.log("Professional Data.........", data);
                setProfessionalList(data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching Profession Data:", error);
                setLoading(false);
            }
        };
        getProfessionalList();
    }, []);

    const handleEventSelect = (professionalID) => {
        if (professionalList.length > 0) {
            const selectedProfessional = professionalList.find((item) => item.srv_prof_id === professionalID);
            console.log("Professional ID......", selectedProfessional);
            setSelectedProfessional(selectedProfessional.srv_prof_id);
        } else {
            console.log("Professional list is empty.");
        }
    };

    useEffect(() => {
        const getProfessionalEvent = async () => {
            if (selectedProfessional) {
                console.log("SelectedProfessional Id........", selectedProfessional);
                try {
                    const res = await fetch(`${port}/web/agg_hhc_detailed_event_plan_of_care/?pro=${selectedProfessional}`);
                    const data = await res.json();
                    console.log("Professional Against All Events", data);
                    setSelectedProfessionalEvents(data)
                    setIsEventDetailsModalOpen(true);
                } catch (error) {
                    console.error("Error fetching Professional All Events:", error);
                }
            }
        };
        getProfessionalEvent();
    }, [selectedProfessional]);

    const filteredData = professionalList.filter((item) => {
        if (
            (selectedProfName === '' || item.prof_fullname.toLowerCase().includes(selectedProfName.toLowerCase())) &&
            (selectedService === '' || item.srv_id.toLowerCase().includes(selectedService.toLowerCase()))
        ) {
            return true;
        }
        return false;
    });

    return (
        <>
            <Navbar />
            {/* <Header /> */}
            {/* <TabContext> */}
            {/* <TabPanel> */}
            <Box sx={{ flexGrow: 1, mb: 2, width: "100%" }}>
                <Stack direction={isSmallScreen ? 'column' : 'row'}
                    spacing={1}
                    alignItems={isSmallScreen ? 'center' : 'flex-start'}>
                    {/* <div>
                    {
                        tabIndex === 1 && (
                            <div>
                                <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>PROFESSIONAL SCHEDULE</Typography>
                            </div>
                        )
                    }
                </div>
                <div>
                    {
                        tabIndex === 2 && (
                            <div>
                                <Typography sx={{ fontSize: 16, fontWeight: 600, }} color="text.secondary" gutterBottom>PROFESSIONAL LIST</Typography>
                            </div>
                        )
                    }
                </div> */}
                    <Typography sx={{ fontSize: 16, fontWeight: 600, marginTop: "10px", marginLeft: "10px" }} color="text.secondary" gutterBottom>PROFESSIONAL SCHEDULE</Typography>
                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 250, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1, }}
                            placeholder="Search Service |"
                            inputProps={{ 'aria-label': 'select service' }}
                            value={selectedService}
                            onChange={handleServiceChange}
                        />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Box>

                    <Box
                        component="form"
                        sx={{ marginLeft: '2rem', p: "2px 4px", display: 'flex', alignItems: 'center', width: 260, height: '2.5rem', backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", border: "1px solid #C9C9C9" }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            placeholder="Search Professional Name |"
                            inputProps={{ 'aria-label': 'search professional' }}
                            value={selectedProfName}
                            onChange={handleProfChange}
                        />
                        <IconButton type="button" sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Box>

                    <Button variant="contained" style={{ backgroundColor: "#69A5EB", textTransform: "capitalize", borderRadius: "8px", marginLeft: "20px", height: "2.6rem" }} onClick={() => setTabIndex(1)}>View Professional Schedule</Button>
                    <Button variant="outlined" style={{ textTransform: "capitalize", borderRadius: "8px", marginLeft: "20px", height: "2.6rem" }} onClick={() => setTabIndex(2)}>Professional List</Button>
                </Stack>

                <div>
                    {
                        tabIndex === 1 && (
                            <div>
                                <Grid item xs={12} container spacing={1}>
                                    <Grid item lg={5} md={6} xs={12}>
                                        <TableContainer  >
                                            <Table>
                                                <TableHead >
                                                    <TableRow>
                                                        <ScheduleCard style={{ background: "#69A5EB", color: "#FFFFFF" }}>
                                                            <CardContent style={{ flex: 2, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Prof. Name</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 2, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Service</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 2, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Preferred Location</Typography>
                                                            </CardContent>
                                                            <CardContent style={{ flex: 1, borderRight: "1px solid #FFFFFF" }}>
                                                                <Typography variant='subtitle2'>Type</Typography>
                                                            </CardContent>
                                                        </ScheduleCard>
                                                    </TableRow>
                                                </TableHead>
                                                {loading ? (
                                                    // Display the loader while data is being fetched
                                                    <CircularProgress style={{ marginTop: "100px" }} />
                                                ) : (
                                                    <TableBody>
                                                        {filteredData.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((row, i) => (
                                                            <TableRow
                                                                key={row.first_name}
                                                                sx={{ '&:last-child td, &:last-child th': { border: 0, } }}
                                                            >
                                                                <ScheduleCard>
                                                                    <CardContent style={{ flex: 2 }}>
                                                                        <Typography variant='body2'><button onClick={() => handleEventSelect(row.srv_prof_id)}
                                                                            style={{
                                                                                border: 'none',
                                                                                background: 'none',
                                                                                outline: 'none',
                                                                                cursor: 'pointer',
                                                                                // paddingLeft: '10px',
                                                                                borderLeft: selectedProfessional === row.srv_prof_id ? '3px solid #26C0E2' : 'none',
                                                                                height: '40px',
                                                                                display: 'flex',
                                                                                alignItems: 'center',
                                                                            }}>{row.prof_fullname}</button></Typography>
                                                                    </CardContent>
                                                                    <CardContent style={{ flex: 2 }}>
                                                                        <Typography variant='body2'>{row.srv_id}</Typography>
                                                                    </CardContent>
                                                                    <CardContent style={{ flex: 2 }}>
                                                                        <Typography variant='body2'>{row.prof_zone_id}</Typography>
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
                                                                </ScheduleCard>
                                                            </TableRow>
                                                        ))}
                                                    </TableBody>
                                                )}
                                            </Table>
                                        </TableContainer>
                                        <TablePagination
                                            rowsPerPageOptions={[5, 10, 25, 100]}
                                            component="div"
                                            count={professionalList.length}
                                            rowsPerPage={rowsPerPage}
                                            page={page}
                                            onPageChange={handleChangePage}
                                            onRowsPerPageChange={handleChangeRowsPerPage}
                                        />
                                    </Grid>

                                    <Grid item lg={7} md={6} xs={12} sx={{ marginTop: "7px" }}>
                                        <Card sx={{ backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px" }}>
                                            <div style={{ paddingTop: "20px", paddingLeft: "5px", paddingRight: "5px", paddingBottom: "5px" }}>
                                                <CalendarComponent events={selectedProfessionalEvents} />
                                                {/* <CalendarComponent /> */}
                                            </div>
                                        </Card>
                                    </Grid>
                                </Grid>
                            </div>
                        )
                    }
                </div >

                <div>
                    {
                        tabIndex === 2 && (
                            <div>
                                <ProfessionalList />
                            </div>
                        )
                    }
                </div>
            </Box >
            {/* </TabPanel> */}
            {/* </TabContext> */}
            <Footer />
        </>
    )
}

export default Schedule
