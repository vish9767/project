import React, {useState} from 'react';
// import { Counter } from './features/counter/Counter';
import Navbar from "./HHC/Navbar";
import Footer from "./HHC/Footer";
import Header from "./HHC/Header";
import './App.css';
import { BrowserRouter, Router, Routes, Route  } from "react-router-dom";
import Viewservice from './HHC/components/HD/Viewservice';
import UserDetails from './HHC/components/UserDeatilsForm/UserDetails';
import Login from './HHC/components/Login/Login';
import Dashboard from './HHC/components/HD/Dashboard/Dashboard';
import Addservice from './HHC/components/HD/Addservice';
import Ongoingservice from './HHC/components/HD/Ongoingservice/Ongoingservice';
import Professional from './HHC/components/HD/Dashboard/Professional';
import ServiceRequest from './HHC/components/HD/Servicerequest/ServiceRequest';
import Enquiries from './HHC/components/HD/Enquiries/Enquiries';
import Schedule from './HHC/components/HD/Professional/Schedule';
import Membership from './HHC/components/HD/Membership/Membership';
import ManageProfile from './HHC/components/HR/Profile/ManageProfile';
// import ProtectedRoute from './HHC/ProtectedRoute';



function App() {
  // const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Function to handle a successful login
  // const handleLogin = () => {
  //   setIsLoggedIn(true);
  // };
  return (
    <div className="App">
      {/* <Login/> */}
      {/* <Navbar /> */}
      {/* <Header/> */}
      {/* <Footer/> */}
      {/* <BrowserRouter> */}
      {/* <Routes> */}
      {/* <Route path="/service" element={<Viewservice />}/> */}
      {/* <Route index element={<Login />} /> */}
      {/* <Route path="header" element={<Header />} /> */}
      {/* <Route path="user" element={<UserDetails />} /> */}
      {/* </Route> */}
      {/* </Routes> */}
      {/* </BrowserRouter> */}
      
      <BrowserRouter basename="/hhc">
        <div>
        {/* <Navbar /> */}
        {/* {isLoggedIn && <Navbar />} */}
          <Routes>
            {/* <Route exact path="/" element={<Login onLogin={handleLogin} />} /> */}
            <Route exact path="/" element={<Login />} />
            {/* <Route exact path="/hhc-hd-login" element={<Navbar />} /> */}
            <Route exact path="/dashboard" element={<Dashboard />} />
            <Route exact path="/addservice" element={<Addservice />} />
            <Route exact path="/viewservice" element={<Viewservice />} />
            <Route exact path="/ongoing" element={<Ongoingservice />} />
            <Route exact path="/professional" element={<Schedule />} />
            <Route exact path="/service-request" element={<ServiceRequest />} />
            <Route exact path="/enquiries" element={<Enquiries />} />
            <Route exact path="/membership" element={<Membership />} />
            <Route path="/user" element={<UserDetails />} />
            <Route path="/manage-profile" element={<ManageProfile />} />
            {/* <Route exact path="/upcoming/:user" element={<Upcoming />} /> */}
            {/* <Route path="*" element={<NotFound />} /> */}
          </Routes>
          {/* <Footer /> */}
          {/* {isLoggedIn && <Footer />} */}
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
