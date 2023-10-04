import React, { useState, useEffect } from 'react';
import Box from "@mui/material/Box"
import Grid from "@mui/material/Grid"
import TextField from "@mui/material/TextField"
import Button from '@mui/material/Button';
import MenuItem from "@mui/material/MenuItem"
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import { useNavigate } from "react-router-dom";
import { getCurrentDateTimeString } from "../../../Utils/ValidationUtils";

const followup = [
    {
        value: '1',
        label: 'Keep in Followup',
    },
    {
        value: '2',
        label: 'Cancel',
    },
    {
        value: '3',
        label: 'Create Service',
    },
];

const cancelby = [
    {
        value: '1',
        label: 'Spero',
    },
    {
        value: '2',
        label: 'Customer',
    },
];

const Followup = ({ sendData, enqData, onClose }) => {
    const port = process.env.REACT_APP_API_KEY;

    const navigate = useNavigate();

    const [value, setValue] = useState('1');
    const [selectedOption, setSelectedOption] = useState('')
    const [selectedFollow, setSelectedFollow] = useState('')
    const [dateTime, setDateTime] = useState('')
    const [remark, setRemark] = useState('')
    const [cancelReason, setCancelReason] = useState([])
    const [selectedCancelReason, setSelectedCancelReason] = useState('');
    const [selectedReasonID, setSelectedReasonID] = useState('')
    // const [eventID, setEventID] = useState('')

    const [followDateTime, setFollowDateTime] = useState('')
    const [followRemark, setFollowRemark] = useState('')

    console.log("Previos Followup Records......", sendData)
    console.log("event id", enqData)

    useEffect(() => {
        if (sendData.length > 0) {
            const firstItem = sendData[0];
            const formattedDateTime = firstItem.follow_up_date_time || '';
            const remark = firstItem.previous_follow_up_remark || '';
            setDateTime(formattedDateTime);
            console.log(formattedDateTime);
            setRemark(remark);
            console.log(remark);
        }
    }, [sendData]);

    useEffect(() => {
        const getCancelReason = async () => {
            if (selectedReasonID) {
                console.log("Cancel BY .....", selectedReasonID)
                try {
                    const res = await fetch(`${port}/web/cancellation_reason_follow_up_list/${selectedReasonID}`);
                    const data = await res.json();
                    console.log("Cancel by with Reason.........", data);
                    setCancelReason(data);
                } catch (error) {
                    console.error("Error fetching PCancel by with Reason:", error);
                }
            }
        };
        getCancelReason();
    }, [selectedReasonID]);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    //Cancel Reason change Logic
    const handleReasonChange = (event) => {
        setSelectedReasonID(event.target.value);
    };

    //Followup change Logic
    const handleDropdownFollowupChange = (event) => {
        setSelectedFollow(event.target.value);
    };

    //TextField change Logic
    const handleDropdownChange = (event) => {
        setSelectedOption(event.target.value);
    };

    const handleCancelReasonChange = (event) => {
        setSelectedCancelReason(event.target.value);
    };

    async function handleFollowupSubmit(event) {
        event.preventDefault();
        const requestData = {
            event_id: enqData,
            follow_up: selectedOption,
            follow_up_date_time: followDateTime,
            previous_follow_up_remark: followRemark,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/Add_follow_up/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                console.error(`HTTP error! Status: ${response.status}`);
                return;
            }
            const result = await response.json();
            console.log("Keep in Follow up data", result);
            onClose();
            window.location.reload();
            // navigate('/service');
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    async function handleCancelSubmit(event) {
        event.preventDefault();
        const requestData = {
            event_id: enqData,
            follow_up: selectedOption,
            cancel_by: selectedReasonID,
            canclation_reason: selectedCancelReason,
            previous_follow_up_remark: followRemark,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/cancel_follow_up/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                console.error(`HTTP error! Status: ${response.status}`);
                return;
            }
            const result = await response.json();
            console.log("Cancel Service data", result);
            onClose();
            window.location.reload();
            // navigate('/service');
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    async function handleCreateServiceSubmit(event) {
        event.preventDefault();
        const requestData = {
            event_id: enqData,
            follow_up: selectedOption,
            previous_follow_up_remark: followRemark,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/create_service_follow_up/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),
            });
            if (!response.ok) {
                console.error(`HTTP error! Status: ${response.status}`);
                return;
            }
            const result = await response.json();
            console.log("Enquiry converted to service", result);
            navigate('/addservice');
            // onClose();
        } catch (error) {
            console.error("An error occurred:", error);
        }
    }

    return (
        <Box sx={{ marginTop: "20px" }}>
            <TabContext value={value}>
                <Box sx={{
                    typography: 'body1',
                    background: "#F2F2F2",
                    borderRadius: '10px',
                    width: "auto",
                    height: "3rem",
                    display: 'flex',
                    justifyContent: 'center',
                    marginLeft: '8px',
                    marginRight: '8px',
                }}>
                    <TabList
                        className="tab-root"
                        onChange={handleChange}
                        textColor="#51DDD4"
                        sx={{ position: 'relative' }}
                        TabIndicatorProps={{ style: { background: '#69A5EB', height: '36px', marginBottom: '6px', borderRadius: "5px" } }}
                    >
                        <Tab label={<span style={{ fontSize: '15px', textTransform: "capitalize", color: value === "1" ? '#ffffff' : 'black' }}>Previous Followup</span>} value="1" sx={{ position: 'relative', zIndex: 1, }} />
                        <Tab label={<span style={{ fontSize: '15px', textTransform: "capitalize", color: value === "2" ? '#ffffff' : 'black' }}>Add Followup</span>} value="2" sx={{ position: 'relative', zIndex: 1, }} />
                    </TabList>
                </Box>
                <Box sx={{ width: '100%', typography: 'body1', marginTop: '-10px' }}>
                    <TabPanel value="1">
                        <Grid container spacing={2} sx={{ marginTop: "1px" }}>

                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="outlined-satrt-date-time"
                                    label="Follow up Date and Time"
                                    // type="datetime-local"
                                    size="small"
                                    value={dateTime}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                // InputLabelProps={{
                                //     shrink: true,
                                // }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12} style={{ marginTop: "15px" }}>
                                <TextField
                                    id="outlined-multiline-static"
                                    label="Remark"
                                    placeholder='write remark here'
                                    size="small"
                                    value={remark}
                                    fullWidth
                                    multiline
                                    rows={2}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>
                        </Grid>
                    </TabPanel>
                    <TabPanel value="2">
                        <Grid container spacing={2} sx={{ marginTop: "1px" }}>
                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    id="outlined-select-follow-up"
                                    select
                                    label="Follow up"
                                    name="follow_up"
                                    value={selectedOption}
                                    onChange={handleDropdownChange}
                                    size="small"
                                    fullWidth
                                    sx={{
                                        textAlign: "left", '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                >
                                    {followup.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                            </Grid>

                            {selectedOption === '2' && (
                                <Grid item lg={12} sm={12} xs={12}>
                                    <TextField
                                        required
                                        id="cancel_by"
                                        name="cancel_by"
                                        select
                                        label="Cancel by"
                                        size="small"
                                        fullWidth
                                        value={selectedReasonID}
                                        onChange={handleReasonChange}
                                        sx={{
                                            textAlign: "left", '& input': {
                                                fontSize: '14px',
                                            },
                                        }}
                                    >
                                        {cancelby.map((option) => (
                                            <MenuItem key={option.value} value={option.value}>
                                                {option.label}
                                            </MenuItem>
                                        ))}
                                    </TextField>
                                </Grid>
                            )}

                            {selectedOption === '2' && (
                                <Grid item lg={12} sm={12} xs={12}>
                                    <TextField
                                        required
                                        id="canclation_reason"
                                        name="canclation_reason"
                                        select
                                        label="Cancellation Reason"
                                        size="small"
                                        value={selectedCancelReason}
                                        onChange={handleCancelReasonChange}
                                        fullWidth
                                        sx={{
                                            textAlign: "left", '& input': {
                                                fontSize: '14px',
                                            },
                                        }}
                                    >
                                        {cancelReason.map((option) => (
                                            <MenuItem key={option.cancelation_reason_id} value={option.cancelation_reason_id}>
                                                {option.cancelation_reason}
                                            </MenuItem>
                                        ))}
                                    </TextField>
                                </Grid>
                            )}

                            <Grid item lg={12} sm={12} xs={12}>
                                {selectedOption === '1' ? (
                                    <TextField
                                        required
                                        id="follow_up_date_time"
                                        label="Follow up Date and Time"
                                        type="datetime-local"
                                        name="follow_up_date_time"
                                        value={followDateTime}
                                        onChange={(e) => setFollowDateTime(e.target.value)}
                                        size="small"
                                        fullWidth
                                        sx={{
                                            '& input': {
                                                fontSize: '14px',
                                            },
                                        }}
                                        inputProps={{
                                            min: getCurrentDateTimeString(), // Set min to current date and time
                                        }}
                                        InputLabelProps={{
                                            shrink: true,
                                        }}
                                    />
                                ) : (null)}

                            </Grid>

                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    required
                                    id="previous_follow_up_remark"
                                    label="Remark"
                                    placeholder='write remark here'
                                    size="small"
                                    name="previous_follow_up_remark"
                                    value={followRemark}
                                    onChange={(e) => setFollowRemark(e.target.value)}
                                    fullWidth
                                    multiline
                                    rows={2}
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12}>
                                {selectedOption === '2' ? (
                                    <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize" }} onClick={handleCancelSubmit}>
                                        Close Enquiry
                                    </Button>
                                ) : selectedOption === '3' ? (
                                    <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize" }} onClick={handleCreateServiceSubmit}>
                                        Go to Service
                                    </Button>
                                ) : (
                                    <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize" }} onClick={handleFollowupSubmit}>
                                        Keep in Followup
                                    </Button>
                                )}
                            </Grid>
                        </Grid>
                    </TabPanel>
                </Box>
            </TabContext>
        </Box>
    )
}

export default Followup
