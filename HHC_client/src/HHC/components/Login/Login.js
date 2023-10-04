import * as React from 'react';
import { useState, useEffect } from 'react';
// import axios from 'axios';
import Box from '@mui/material/Box';
import login from "../../assets/login_bg.png"
import logo from "../../assets/spero_logo_old.png";
import "./Login.css";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { useNavigate } from "react-router-dom";
import PersonOutlineOutlinedIcon from '@mui/icons-material/PersonOutlineOutlined';
import { TextField } from '@mui/material';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';

export default function Login() {
    const port = process.env.REACT_APP_API_KEY;

    const [login, setLogin] = useState({ clg_ref_id: "", password: "" })
    const [userIdError, setUserIdError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);
    const [showErrorAlert, setShowErrorAlert] = useState(false);

    const navigate = useNavigate();

    const handleChange = async (e) => {
        e.preventDefault();
        setUserIdError(login.clg_ref_id === "");
        setPasswordError(login.password === "");

        if (login.clg_ref_id === "" || login.password === "") {
            return;
        }
        const response = await fetch(`${port}/web/login/`, {
            method: "post",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ clg_ref_id: login.clg_ref_id, password: login.password })
        });

        if (response.status === 404) {
            console.log("Resource not found.");
            // alert("Invalid User ID or Password.");
            setShowErrorAlert(true);
            return;
        }
        setShowErrorAlert(false);

        const data = await response.json();
        console.log("Login Credentials.....", data);
        localStorage.setItem('token', data.token.access);
        localStorage.setItem('refresh', data.token.refresh);

        localStorage.setItem('user-image', data.token.colleague.profile_photo_path);
        localStorage.setItem('user-name', data.token.colleague.first_name);
        localStorage.setItem('user-lname', data.token.colleague.last_name);
        localStorage.setItem('user-email', data.token.colleague.email);
        localStorage.setItem('user-phone', data.token.colleague.phone_no);
        localStorage.setItem('user-loc', data.token.colleague.address);
        localStorage.setItem('user-designation', data.token.colleague.designation);
        if (data.token.user_group === "hd") {
            navigate("/dashboard");
            // onLogin();
            // window.location.reload();
        }
    }

    const onchange = (e) => {
        const { name, value } = e.target;
        setLogin((prevLogin) => ({
            ...prevLogin,
            [name]: value,
        }));
        if (name === 'clg_ref_id') {
            setUserIdError(false);
        } else if (name === 'password') {
            setPasswordError(false);

        }
        // setLogin({ ...login, [e.target.name]: e.target.value })
        // console.log(login);
    }

    return (
        <>
            <div className="container">
                <div className="input_fields">
                    <img src={logo} alt="" style={{ height: "60px" }} />
                    <Typography variant='h6' sx={{ m: 3 }}>HD LOGIN</Typography>
                    {showErrorAlert && (
                        <Alert severity="error">Invalid User ID or Password!</Alert>
                    )}
                    <TextField type="text" name="clg_ref_id" placeholder="Enter User ID"
                        id="outlined-size-small"
                        size="small"
                        fullWidth
                        sx={{marginTop:1}}
                        onChange={onchange}
                        required
                        error={userIdError}
                        helperText={userIdError && "User ID is required"}
                    />
                    <TextField type="password" name="password" placeholder="Enter Password"
                        id="outlined-size-small"
                        size="small"
                        fullWidth
                        sx={{marginTop:4}}
                        onChange={onchange}
                        required
                        error={passwordError}
                        helperText={passwordError && "Password is required"}
                    />
                   
                    <Button variant='contained' sx={{ m: 4, width: '30vh', backgroundColor: '#69A5EB', borderRadius: "10px", textTransform: "capitalize", }} onClick={handleChange}>Submit</Button>
                </div>
            </div>
        </>
    );
}

