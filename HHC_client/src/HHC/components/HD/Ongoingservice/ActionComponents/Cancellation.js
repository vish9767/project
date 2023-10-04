import React, { useState, useEffect } from 'react';
import Box from "@mui/material/Box"
import Typography from "@mui/material/Typography"
import Grid from "@mui/material/Grid"
import TextField from "@mui/material/TextField"
import MenuItem from '@mui/material/MenuItem';
import Button from '@mui/material/Button';
import CardContent from '@mui/material/CardContent';

const cancelby = [
    {
        value: 1,
        label: 'Spero',
    },
    {
        value: 2,
        label: 'Customer',
    },
];

const Cancellation = ({ eventID, onClose }) => {
    const port = process.env.REACT_APP_API_KEY;
    const [cancelReason, setCancelReason] = useState([])
    const [selectedCancelReason, setSelectedCancelReason] = useState('');
    const [selectedReasonID, setSelectedReasonID] = useState('')

    const [remark, setRemark] = useState('')

    const [serviceCancel, setServiceCancel] = useState([])
    const [eventCancel, setEventCancel] = useState([])
    console.log("Cancel Service Data", eventID);

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
                    console.error("Error fetching Cancel by with Reason:", error);
                }
            }
        };
        getCancelReason();
    }, [selectedReasonID]);

    useEffect(() => {
        const getServiceCancel = async () => {
            if (eventID) {
                console.log("Event ID .....", eventID)
                try {
                    const res = await fetch(`${port}/web/service_cancellation/${eventID}`);
                    const data = await res.json();
                    console.log("Service Cancel.........", data);
                    setServiceCancel(data.Service_date);
                    setEventCancel(data.event_data);
                } catch (error) {
                    console.error("Error fetching Service Cancel:", error);
                }
            }
        };
        getServiceCancel();
    }, [eventID]);

    //Cancel Reason change Logic
    const handleReasonChange = (event) => {
        setSelectedReasonID(event.target.value);
    };

    const handleCancelReasonChange = (event) => {
        setSelectedCancelReason(event.target.value);
    };

    const formatDate = (dateString) => {
        const dateTime = new Date(dateString);
        const day = dateTime.getDate().toString().padStart(2, '0'); // Get day with leading zero
        const month = (dateTime.getMonth() + 1).toString().padStart(2, '0'); // Get month with leading zero
        const year = dateTime.getFullYear();
        const hours = dateTime.getHours() % 12 || 12; // Get hours in 12-hour format
        const minutes = dateTime.getMinutes().toString().padStart(2, '0'); // Get minutes with leading zero
        const ampm = dateTime.getHours() >= 12 ? 'PM' : 'AM'; // Determine AM or PM

        return `${day}/${month}/${year} ${hours}:${minutes} ${ampm}`;
    };

    async function handleCancelService(event) {
        event.preventDefault();
        const requestData = {
            event_id: eventID,
            cancellation_by: selectedReasonID,
            reason: selectedCancelReason,
            remark: remark,
        };
        console.log("POST API Hitting......", requestData)
        if (eventID) {
            try {
                const response = await fetch(`${port}/web/service_cancellation/${eventID}`, {
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
                console.log("Successfully submitted Service Cancellation data", result);
                onClose();
                window.location.reload();
            } catch (error) {
                console.error("Error fetching Service Cancellation:", error);
            }
        }
    }

    return (
        <Box>
            <CardContent>
                <Grid container spacing={2} sx={{ marginTop: "1px" }}>

                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="cancellation_by"
                            name="cancellation_by"
                            select
                            label="Cancellation by"
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
                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="reason"
                            name="reason"
                            select
                            label="Cancellation Reason"
                            size="small"
                            fullWidth
                            value={selectedCancelReason}
                            onChange={handleCancelReasonChange}
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
                    <Grid item lg={12} sm={12} xs={12}>
                        <Typography variant="body2">Service Allocation Date & Time: {formatDate(serviceCancel.start_date)}</Typography>
                        <Typography variant="body2">Amount Deducted: {eventCancel.refund_amt}</Typography>
                    </Grid>
                    <Typography variant='body2' color="primary" sx={{ marginTop: "10px", marginLeft: "16px", cursor: "pointer" }}>Cancellation Policy</Typography>
                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="outlined-multiline-static"
                            label="Remark"
                            name="remark"
                            placeholder='write remark here'
                            size="small"
                            fullWidth
                            value={remark}
                            onChange={(e) => setRemark(e.target.value)}
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
                        <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize", }}
                            onClick={handleCancelService}>
                            Cancel Service
                        </Button>
                    </Grid>
                </Grid>
            </CardContent>
        </Box>
    )
}

export default Cancellation
