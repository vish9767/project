import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import useMediaQuery from '@mui/material/useMediaQuery';
import IconButton from '@mui/material/IconButton';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import Avatar from '@mui/material/Avatar';
import Header from './Header';
import Logo from "./assets/spero_logo.png";
import SOS from "./assets/sos.png";
// import SosIcon from '@mui/icons-material/Sos';
import { Button } from '@mui/material';
import UserDetails from './components/UserDeatilsForm/UserDetails';
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';
import PowerSettingsNewIcon from '@mui/icons-material/PowerSettingsNew';
import Footer from "./Footer"
import { useNavigate } from "react-router-dom";
import Modal from '@mui/material/Modal';
import EmailOutlinedIcon from '@mui/icons-material/EmailOutlined';
import LocalPhoneOutlinedIcon from '@mui/icons-material/LocalPhoneOutlined';
import LocationOnOutlinedIcon from '@mui/icons-material/LocationOnOutlined';
import "./Navbar.css";

export default function Navbar() {
  const port = process.env.REACT_APP_API_KEY;

  const [auth, setAuth] = React.useState(true);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [isModalOpen, setIsModalOpen] = React.useState(false);
  const isSmallScreen = useMediaQuery('(max-width:600px)');

  const navigate = useNavigate();

  const userPicture = localStorage.getItem('user-image');
  const userName = localStorage.getItem('user-name');
  const userLastName = localStorage.getItem('user-lname');
  const userDesignation = localStorage.getItem('user-designation');
  const userEmail = localStorage.getItem('user-email');
  const userPhone = localStorage.getItem('user-phone');
  const userAddress = localStorage.getItem('user-loc');


  const handleChange = (event) => {
    setAuth(event.target.checked);
  };

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleProfile = () => {
    setIsModalOpen(true);
  };


  //User Logout Api

  const handleLogout = async () => {
    const response = await fetch(`${port}/web/logout/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "refresh": localStorage.getItem('refresh') })

    });
    // alert("You have successfully logout..!")
    navigate("/");
  };

  return (
    <Box sx={{ flexGrow: 1, }}>
      <AppBar position="static" style={{
        background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
        // backgroundColor: '#F8F6F6',
        height: '3rem'
      }}>
        <Toolbar variant='dense' sx={{ display: 'flex', justifyContent: 'space-between' }}>
          {/* <img style={{ height: '36px', width: '76px', marginTop: "2px", marginLeft: "-12px", color: "#ffffff" }} src={Logo} alt="Spero" /> */}

          {!isSmallScreen && (
            // Display the Typography title for screen sizes larger than 600px
            <Typography variant="h6" component="div" align="left"
              sx={{
                flexGrow: 1,
                fontFamily: 'sans-serif',
                fontWeight: 600,
                fontStyle: 'normal',
                color: 'inherit',
                marginLeft: "12px",
                textDecoration: 'none',
              }}>
              Spero Home Healthcare Services
            </Typography>
          )}

          {/* <Toolbar sx={{ display: 'flex', justifyContent: 'flex-end' }}> */}
          {auth && (
            <div>
              Welcome, {userName} {userLastName}
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleMenu}
                color="inherit"
              >
                <Avatar alt="Shamal Bhagat" src="/static/images/avatar/2.jpg" />
              </IconButton>
              <Menu
                sx={{ mt: '45px' }}
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
                <MenuItem onClick={handleProfile} ><PersonOutlineIcon style={{ fontSize: "20px", marginRight: "10px" }} />Profile</MenuItem>
                <MenuItem onClick={handleLogout}><PowerSettingsNewIcon style={{ fontSize: "20px", marginRight: "10px" }} />Logout</MenuItem>
              </Menu>

              <Modal open={isModalOpen} onClose={() => setIsModalOpen(false)}>
                <Box sx={{
                  width: 220, height: 200, p: 2, position: 'absolute',
                  top: '32%',
                  left: '86%',
                  transform: 'translate(-50%, -50%)',
                  // bgcolor: 'background.paper',
                  bgcolor: '#F2F2F2',
                  borderRadius: '18px',
                  '@media (max-width: 600px)': {
                    left: '50%',
                  },
                }}>
                  <Typography variant="subtitle2">
                    <IconButton
                      size="large"
                      aria-label="account of current user"
                      aria-controls="menu-appbar"
                      aria-haspopup="true"
                      //onClick={handleMenu}
                      color="inherit"
                    >
                      <Avatar alt="Shamal Bhagat" src="/static/images/avatar/2.jpg" />
                    </IconButton>{userName} {userLastName}</Typography>
                    {/* <Typography variant="bdoy2">{userDesignation}</Typography> */}

                  <br />
                  <div class="contact-info"><EmailOutlinedIcon sx={{ color: "#69A5EB" }} /><Typography variant="body2">{userEmail}</Typography></div><br />
                  <div class="contact-info"><LocalPhoneOutlinedIcon sx={{ color: "#69A5EB" }} /><Typography variant="body2">{userPhone}</Typography></div><br />
                  <div class="contact-info"><LocationOnOutlinedIcon sx={{ color: "#69A5EB" }} /><Typography variant="body2">{userAddress}</Typography></div>
                </Box>
              </Modal>
            </div>
          )}
          {/* <Button align="right"><img src={SOS} alt="SOS" /></Button> */}
          {/* </Toolbar> */}
        </Toolbar>
      </AppBar>
      {/* <Toolbar sx={{ mt: 1, }}> */}
      {/* <Header /> */}
      {/* <UserDetails /> */}
      {/* </Toolbar> */}
      <div style={{ marginTop: 10, }}>
        <Header />
        {/* <Footer /> */}
      </div>

    </Box>
  );
}