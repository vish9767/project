import React, { useState, useEffect } from 'react';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import StarBorderIcon from '@mui/icons-material/StarBorder';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import Addservice from './components/HD/Addservice';
import Viewservice from './components/HD/Viewservice';
import Ongoingservice from './components/HD/Ongoingservice/Ongoingservice';
import ServiceRequest from './components/HD/Servicerequest/ServiceRequest';
import Enquiries from './components/HD/Enquiries/Enquiries';
import Schedule from './components/HD/Professional/Schedule';
import useMediaQuery from '@mui/material/useMediaQuery';
import Dashboard from './components/HD/Dashboard/Dashboard';
import Membership from './components/HD/Membership/Membership';
import { Typography } from '@mui/material';
import { Link, Routes, Route, Outlet, useLocation } from "react-router-dom";
import "./Header.css";
import Footer from "./Footer";
import Navbar from "./Navbar";

const Header = () => {
  const [anchorElUser, setAnchorElUser] = useState(null);
  const [value, setValue] = useState('1');
  const location = useLocation();
  const [showComponent, setShowComponent] = useState(false);
  const isSmallScreen = useMediaQuery('(max-width:600px)');

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  // useEffect(() => {
  //   if (location.pathname === '/dashboard') setValue('1');
  //   else if (location.pathname === '/addservice') setValue('2');
  //   else if (location.pathname === '/ongoing') setValue('3');
  //   else if (location.pathname === '/professional') setValue('4');
  //   else if (location.pathname === '/service-request') setValue('5');
  //   else if (location.pathname === '/enquiries') setValue('6');
  //   else if (location.pathname === '/membership') setValue('7');
  //   // else if (location.pathname === '/viewservice') setValue('8');
  // }, [location]);

  return (
    <>
      <Box sx={{
        typography: 'body1',
        marginTop: "10px"
      }}>
        <TabContext value={location.pathname}>
          <Box sx={{
            typography: 'body1',
            backgroundColor: '#FFFFFF',
            boxShadow: '4px 4px 10px 7px rgba(0, 0, 0, 0.05)',
            borderRadius: '10px',
            width: "auto",
            height: "3.6rem",
            display: 'flex',
            justifyContent: 'space-evenly',
            marginLeft: '8px',
            marginRight: '8px',
          }}>
            <TabList
              className="tab-root"
              onChange={handleChange}
              textColor="#51DDD4"
              TabIndicatorProps={{ style: { background: 'linear-gradient(90deg, rgba(31, 208, 196, 0.35) 0%, rgba(50, 142, 222, 0.35) 100%)', height: '40px', marginBottom: '10px', borderRadius: "5px" } }}
            
              variant="scrollable"
              scrollButtons="auto"
              aria-label="scrollable auto tabs example"
            >

              <Tab component={Link} to="/dashboard" value="/dashboard" icon={<AccessTimeIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Dashboard</span>} />
              <Tab component={Link} to="/addservice" value="/addservice" icon={<AddCircleOutlineIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Add Service</span>} />
              <Tab component={Link} to="/ongoing" value="/ongoing" icon={<PersonOutlineIcon style={{ marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Ongoing Service</span>} />
              <Tab component={Link} to="/professional" value="/professional" icon={<CalendarTodayIcon style={{ fontSize: "16px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Professional Schedule</span>} />
              <Tab component={Link} to="/service-request" value="/service-request" icon={<NotificationsNoneIcon style={{ fontSize: "20px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Service Request</span>} />
              <Tab component={Link} to="/enquiries" value="/enquiries" icon={<ChatBubbleOutlineIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Enquiries</span>} />
              <Tab component={Link} to="/membership" value="/membership" icon={<StarBorderIcon style={{ fontSize: "20px", marginBottom: "18px" }} disabled />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }} disabled >Spero Membership</span>} />
              {/* <Tab component={Link} to="/viewservice" value="8" icon={<ChatBubbleOutlineIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>View Service</span>} /> */}

              {/* <Tab icon={<AccessTimeIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Dashboard</span>} value="1" />
              <Tab icon={<AddCircleOutlineIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Add Service</span>} value="2" />
              <Tab icon={<PersonOutlineIcon style={{ marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Ongoing Service</span>} value="3" />
              <Tab icon={<CalendarTodayIcon style={{ fontSize: "16px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Professional Schedule</span>} value="4" />
              <Tab icon={<NotificationsNoneIcon style={{ fontSize: "20px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Service Request</span>} value="5" />
              <Tab icon={<ChatBubbleOutlineIcon style={{ fontSize: "18px", marginBottom: "18px" }} />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }}>Enquiries</span>} value="6" />
              <Tab icon={<StarBorderIcon style={{ fontSize: "20px", marginBottom: "18px" }} disabled />} iconPosition="start" label={<span style={{ fontSize: '1rem', textTransform: "capitalize", marginBottom: "18px" }} disabled >Spero Membership</span>} value="7" /> */}
            </TabList>
          </Box>

          <Box sx={{ width: '100%', typography: 'body1', m:1}}>
            {/* <Box sx={{ width: '100%', typography: 'body1', marginTop: '-10px' }}> */}
            {/* {value === '1' && <TabPanel value="1"><Dashboard /></TabPanel>}
          {value === '2' && <TabPanel value="2"><Addservice /></TabPanel>}
          {/* {value === '2' && <TabPanel value="2"><Viewservice /></TabPanel>} */}
            {/* {value === '3' && <TabPanel value="3"><Ongoingservice /></TabPanel>} */}
            {/* {value === '4' && <TabPanel value="4"><Schedule /></TabPanel>}
          {value === '5' && <TabPanel value="5"><ServiceRequest /></TabPanel>}
          {value === '6' && <TabPanel value="6"><Enquiries /></TabPanel>}
          {value === '7' && <TabPanel value="7">Spero Membership</TabPanel>}  */}

            <Routes>
              <Route path="/dashboard" exact element={<Dashboard />} />
              <Route path="/addservice" element={<Addservice />} />
              <Route path="/ongoing" element={<Ongoingservice />} />
              <Route path="/professional" exact element={<Schedule />} />
              <Route path="/service-request" element={<ServiceRequest />} />
              <Route path="/enquiries" element={<Enquiries />} />
              <Route path="/membership" element={<Membership />} /> 
              <Route path="/viewservice" element={<Viewservice />} />
            </Routes>

          </Box>
        </TabContext>
      </Box>
      {/* <Footer /> */}
    </>
  )
}

export default Header

