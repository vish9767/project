import React, { useState, useEffect } from 'react';
import Typography from "@mui/material/Typography"
import Grid from "@mui/material/Grid"
import TextField from "@mui/material/TextField"
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import { CardContent } from '@mui/material';
import { Box, Stack } from '@mui/system';
import { isDateDisabled } from "../../../Utils/ValidationUtils";

const Professional = ({ eveID, serviceID, ptnName, ptnPhn, onClose }) => {
    const port = process.env.REACT_APP_API_KEY;
    const [prof, setProf] = useState([]);
    const [selectedProf, setSelectedProf] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [remark, setRemark] = useState('');

    useEffect(() => {
        const getProfessional = async () => {
            if (serviceID) {
                console.log("Service ID .....", serviceID)
                try {
                    const res = await fetch(`${port}/web/professional_availability_api/${serviceID}/`);
                    const data = await res.json();
                    console.log("Professional against service id.........", data);
                    setProf(data);
                } catch (error) {
                    console.error("Error fetching Professional:", error);
                }
            }
        };
        getProfessional();
    }, [serviceID]);

    async function handleProfessional(event) {
        event.preventDefault();
        const requestData = {
            eve_id: eveID,
            start_date: startDate,
            end_date: endDate,
            srv_prof_id: selectedProf,
            remark: remark,
        };
        console.log("POST API Hitting......", requestData)
        if (eveID) {
            try {
                const response = await fetch(`${port}/web/prof_reschedule/${eveID}/`, {
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
                console.log("Successfully submitted Professional Reschedule data", result);
                onClose();
                window.location.reload();
            } catch (error) {
                console.error("Error fetching Professional Reschedule:", error);
            }
        }
    }

    return (
        <Box>
            <CardContent>
                <Grid container spacing={2} sx={{ marginTop: "1px" }}>
                    <Grid item lg={12} sm={12} xs={12}>
                        <div style={{ display: "flex" }}>
                            <Typography variant='body2' sx={{ width: "44%" }} color="text.secondary">Patient Name:</Typography>
                            <Typography variant='subtitle2'>{ptnName}</Typography>
                        </div>
                        <div style={{ display: "flex" }}>
                            <Typography variant='body2' sx={{ width: "44%" }} color="text.secondary">Contact Number:</Typography>
                            <Typography variant='subtitle2'>+91 {ptnPhn}</Typography>
                        </div>
                    </Grid>

                    <Grid item lg={12} sm={12} xs={12} sx={{ marginTop: "2px" }}>
                        <TextField
                            required
                            id="start_date"
                            name="start_date"
                            label="Start Date and Time"
                            // type="datetime-local"
                            type="date"
                            size="small"
                            fullWidth
                            value={startDate}
                            onChange={(e) => setStartDate(e.target.value)}
                            sx={{
                                '& input': {
                                    fontSize: '14px',
                                },
                            }}
                            inputProps={{
                                min: new Date().toISOString().split('T')[0], // Set min to today's date
                                disabledDates: { // Custom attribute to disable dates
                                    isDisabled: isDateDisabled,
                                },
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
                            name="end_date"
                            label="End Date and Time"
                            // type="datetime-local"
                            type="date"
                            size="small"
                            fullWidth
                            value={endDate}
                            onChange={(e) => setEndDate(e.target.value)}
                            sx={{
                                '& input': {
                                    fontSize: '14px',
                                },
                            }}
                            inputProps={{
                                min: startDate, // Set min to the selected Start Date
                                disabledDates: {
                                    isDisabled: isDateDisabled, // Use the same function for date validation
                                },
                            }}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>

                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="srv_prof_id"
                            name="srv_prof_id"
                            select
                            label="Professional Available"
                            size="small"
                            fullWidth
                            value={selectedProf}
                            onChange={(e) => setSelectedProf(e.target.value)}
                            sx={{
                                textAlign: "left", '& input': {
                                    fontSize: '14px',
                                },
                            }}
                        >
                            {prof.map((option) => (
                                <MenuItem key={option.srv_prof_id.srv_prof_id} value={option.srv_prof_id.srv_prof_id}>
                                    {option.srv_prof_id.prof_fullname}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid item lg={12} sm={12} xs={12}>
                        <TextField
                            required
                            id="remark"
                            name="remark"
                            label="Remark"
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
                        <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize", }} onClick={handleProfessional}>
                            Professional Reschedule
                        </Button>
                    </Grid>
                </Grid>
            </CardContent>
        </Box>
    )
}

export default Professional
