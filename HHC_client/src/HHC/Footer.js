import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import useMediaQuery from '@mui/material/useMediaQuery';
import Logo from "./assets/spero_logo_3.png";

export default function Navbar() {
  const isSmallScreen = useMediaQuery('(max-width:600px)');

  return (
    // <Box >
      <div  style={{ background: '#D8D8D8', display:"flex", marginTop:"-10px" }}>
        {/* <Toolbar variant='dense'> */}
          <img style={{ height: '30px', width: '76px',marginTop: "2px", marginLeft: "15px", color: "#ffffff" }} src={Logo} alt="Spero" />

            <Typography variant="subtitle2" component="div" align="center"
              sx={{
                flexGrow: 1,
                fontFamily: 'sans-serif',
                fontStyle: 'normal',
                color: 'black',
                textDecoration: 'none',
                marginTop: '4px'
              }}>
             Powered by Spero 2023
            </Typography>
        {/* </Toolbar> */}
      </div>
    // </Box>
  );
}