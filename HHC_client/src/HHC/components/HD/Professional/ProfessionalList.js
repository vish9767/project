import React, { useState, useEffect } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from "@mui/material/Typography";
import { DemoContainer, DemoItem } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TablePagination from '@mui/material/TablePagination';
import MapOutlinedIcon from '@mui/icons-material/MapOutlined';
import CalendarTodayOutlinedIcon from '@mui/icons-material/CalendarTodayOutlined';
import FavoriteIcon from '@mui/icons-material/Favorite';
import WorkspacePremiumOutlinedIcon from '@mui/icons-material/WorkspacePremiumOutlined';
import PeopleAltOutlinedIcon from '@mui/icons-material/PeopleAltOutlined';
import LocalPhoneOutlinedIcon from '@mui/icons-material/LocalPhoneOutlined';
import { styled } from '@mui/system';
import CircularProgress from '@mui/material/CircularProgress';


const ProfessionalCard = styled(Card)({
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: '10px',
    backgroundColor: 'white',
    boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)',
    height: "55px",
    borderRadius: '10px',
    // transition: '0.5s ease-in-out',
    '&:hover': {
        cursor: 'pointer',
    },
});

const ProfessionalList = () => {
    const port = process.env.REACT_APP_API_KEY;

    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(6);
    const [tabIndex, setTabIndex] = useState(1);
    const [professionalList, setProfessionalList] = useState([]);

    const [loading, setLoading] = useState(true);

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
                const res = await fetch(`${port}/web/total_services`);
                const data = await res.json();
                console.log("Professional Listttttttt.........", data);
                setProfessionalList(data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching Professional Data:", error);
                setLoading(false);
            }
        };
        getProfessionalList();
    }, []);


    return (
        <Box sx={{ flexGrow: 1, width: "100%" }}>
            <Grid item xs={12} container spacing={0}>
                <Grid item xs={12} lg={3} sm={12} md={12}>
                    <Box sx={{ display: "flex", m: 1, height: "28rem", backgroundColor: "#ffffff", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px" }}>
                        <div>
                            {
                                tabIndex === 1 && (
                                    <>
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, marginTop: "10px" }}>CALENDER</Typography>
                                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                                            <DemoContainer components={['DateCalendar', 'DateCalendar']}>
                                                <DateCalendar calendars={1} />
                                            </DemoContainer>
                                        </LocalizationProvider>
                                    </>
                                )
                            }
                        </div>

                        <div>
                            {
                                tabIndex === 2 && (

                                    <Box>
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, marginTop: "10px", textAlign: "left", paddingLeft: "10px" }}>MAP</Typography>
                                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30275.38834977167!2d73.81502425862001!3d18.464464586918634!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2eab786f132dd%3A0x7e73bc336a4a20f3!2sDhankawadi%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1685955690124!5m2!1sen!2sin"
                                            // width="330"
                                            height="420"
                                            allowfullscreen=""
                                            loading="lazy"
                                            referrerpolicy="no-referrer-when-downgrade"
                                            className='iframe-map'
                                        >
                                        </iframe>
                                    </Box>
                                )
                            }
                        </div>
                    </Box>
                </Grid>

                <Grid item xs={12} lg={9} sm={12} md={12}>
                    <TableContainer>
                        <Table>
                            <TableHead>
                                <TableRow>
                                    <ProfessionalCard style={{ background: "#69A5EB", color: "#FFFFFF" }}>
                                        <CardContent style={{ width: "3%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Sr. No</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Professional Name</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "15%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Service Name</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "20%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Professional Contact</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "5%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Total Services</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "10%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Experience</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "8%", borderRight: "1px solid #FFFFFF" }}>
                                            <Typography variant='subtitle2'>Trustworthy</Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "3%", }}>
                                            <Typography variant='subtitle2'></Typography>
                                        </CardContent>
                                        <CardContent style={{ width: "3%", }}>
                                            <Typography variant='subtitle2'></Typography>
                                        </CardContent>
                                    </ProfessionalCard>
                                </TableRow>
                            </TableHead>
                            {loading ? (
                                // Display the loader while data is being fetched
                                <CircularProgress style={{ marginTop: "100px" }} />
                            ) : (
                                <TableBody>
                                    {professionalList.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage).map((row, index) => (
                                        <TableRow
                                            key={index}
                                            sx={{ '&:last-child td, &:last-child th': { border: 0, } }}
                                        >
                                            <ProfessionalCard>
                                                <CardContent style={{ width: "3%" }}>
                                                    <Typography variant='body2'>{index + 1}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "15%" }}>
                                                    <Typography variant='body2'>{row.prof_fullname}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "15%" }}>
                                                    <Typography variant='body2'>{row.srv_id}</Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "20%" }}>
                                                    <div style={{ display: "flex", }}>
                                                        <LocalPhoneOutlinedIcon sx={{ color: "#FD7568", fontSize: "20px" }} />
                                                        <Typography variant='body2'>+91 {row.phone_no}</Typography>
                                                    </div>
                                                </CardContent>
                                                <CardContent style={{ width: "5%" }}>
                                                    <div style={{ display: "flex" }}>
                                                        <PeopleAltOutlinedIcon sx={{ color: "#2261BE", fontSize: "20px" }} />
                                                        <Typography variant='body2'>{row.total_services}</Typography>
                                                    </div>
                                                </CardContent>
                                                <CardContent style={{ width: "10%" }}>
                                                    <div style={{ display: "flex" }}>
                                                        <WorkspacePremiumOutlinedIcon sx={{ color: "#BC80F7", fontSize: "20px" }} />
                                                        <Typography variant='body2'>{row.Experience}+ Years</Typography>
                                                    </div>
                                                </CardContent>
                                                <CardContent style={{ width: "8%" }}>
                                                    <div style={{ display: "flex" }}>
                                                        <FavoriteIcon sx={{ color: "#D62E4B", fontSize: "20px" }} />
                                                        <Typography variant='body2'>{row.Ratings}+</Typography>
                                                    </div>
                                                </CardContent>
                                                <CardContent style={{ width: "3%" }}>
                                                    <Typography variant='body2'><CalendarTodayOutlinedIcon onClick={() => setTabIndex(1)} style={{ color: tabIndex === 1 ? '#69A5EB' : 'inherit', fontSize: "22px" }} /></Typography>
                                                </CardContent>
                                                <CardContent style={{ width: "3%" }}>
                                                    <Typography variant='body2'><MapOutlinedIcon onClick={() => setTabIndex(2)} style={{ color: tabIndex === 2 ? '#69A5EB' : 'inherit', }} /></Typography>
                                                </CardContent>
                                            </ProfessionalCard>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            )}
                        </Table>
                    </TableContainer>
                    <TablePagination
                        rowsPerPageOptions={[10, 25, 100]}
                        component="div"
                        count={professionalList.length}
                        rowsPerPage={rowsPerPage}
                        page={page}
                        onPageChange={handleChangePage}
                        onRowsPerPageChange={handleChangeRowsPerPage}
                    />
                </Grid>
            </Grid>
        </Box>
    )
}

export default ProfessionalList
