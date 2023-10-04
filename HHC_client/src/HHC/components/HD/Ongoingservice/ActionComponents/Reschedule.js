import React, { useState, useEffect } from 'react';
import Box from "@mui/material/Box"
import Grid from "@mui/material/Grid"
import TextField from "@mui/material/TextField"
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import { CardContent } from '@mui/material';

const genders = [
    {
        value: '1',
        label: 'Male',
    },
    {
        value: '2',
        label: 'Female',
    },
];

const Reschedule = ({ eventID, eveStartDate, eveEndDate, onClose }) => {
    const port = process.env.REACT_APP_API_KEY;

    const [startDate, setStartDate] = useState(eveStartDate);
    const [endDate, setEndDate] = useState(eveEndDate);
    const [remark, setRemark] = useState('');

    // console.log("Service Reschedule Event ID", eveStartDate);

    // Function to format the current date and time as a string
    const getCurrentDateTimeString = () => {
        const currentDate = new Date();
        const year = currentDate.getFullYear();
        const month = String(currentDate.getMonth() + 1).padStart(2, '0');
        const day = String(currentDate.getDate()).padStart(2, '0');
        const hours = String(currentDate.getHours()).padStart(2, '0');
        const minutes = String(currentDate.getMinutes()).padStart(2, '0');
        return `${year}-${month}-${day}T${hours}:${minutes}`;
    };

    useEffect(() => {
        // Update the startDate and endDate states when props change
        setStartDate(eveStartDate);
        setEndDate(eveEndDate);
      }, [eveStartDate, eveEndDate]);

    async function handleRescheduleSubmit(event) {
        event.preventDefault();
        const requestData = {
            event_id: eventID,
            start_date: startDate,
            end_date: endDate,
            remark: remark,
        };
        console.log("POST API Hitting......", requestData)
        if (eventID) {
            try {
                const response = await fetch(`${port}/web/service_reschedule/${eventID}/`, {
                    method: "PATCH",
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
                console.log("Successfully submitted Service Reschedule data", result);
                onClose();
                window.location.reload();
            } catch (error) {
                console.error("Error fetching Service Reschedule:", error);
            }
        }
    }

    return (
        <Box>
            <CardContent>
                <Grid container spacing={3} sx={{ marginTop: "1px" }}>

                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="start_date"
                            label="Start Date and Time"
                            // type="datetime-local"
                            type="text"
                            name="start_date"
                            value={startDate}
                            onChange={(e) => setStartDate(e.target.value)}
                            size="small"
                            fullWidth
                            sx={{
                                '& input': {
                                    fontSize: '16px',
                                },
                            }}
                            inputProps={{
                                min: getCurrentDateTimeString(), // Set min to current date and time
                            }}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>
                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="end_date"
                            label="End Date and Time"
                            type="datetime-local"
                            // type="date"
                            name="end_date"
                            value={endDate}
                            onChange={(e) => setEndDate(e.target.value)}
                            size="small"
                            fullWidth
                            sx={{
                                '& input': {
                                    fontSize: '16px',
                                },
                            }}
                            inputProps={{
                                min: getCurrentDateTimeString(), // Set min to current date and time
                            }}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>

                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            id="outlined-select-consultant"
                            select
                            label="Consultant Preferred"
                            size="small"
                            fullWidth
                            sx={{
                                textAlign: "left", '& input': {
                                    fontSize: '16px',
                                },
                            }}
                        >
                            {genders.map((option) => (
                                <MenuItem key={option.value} value={option.value}>
                                    {option.label}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>
                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="remark"
                            label="Remark"
                            placeholder='write remark here'
                            size="small"
                            name="remark"
                            value={remark}
                            onChange={(e) => setRemark(e.target.value)}
                            fullWidth
                            multiline
                            rows={2}
                            sx={{
                                '& input': {
                                    fontSize: '16px',
                                },
                            }}
                        />
                    </Grid>
                    <Grid item lg={12} sm={12} xs={12}>
                        <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize", }} onClick={handleRescheduleSubmit}>
                            {/* <Link
                to="/service"
              >
                service
              </Link> */}
                            Create Service
                        </Button>
                    </Grid>
                </Grid>
            </CardContent>
        </Box>
    )
}

export default Reschedule
