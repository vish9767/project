import React, { useState } from "react";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import CheckIcon from '@mui/icons-material/Check';
import CloseIcon from '@mui/icons-material/Close';

const EventModal = ({ isOpen, onClose, isEditingEvent, profEvent, selectedEvent,  }) => {
    const port = process.env.REACT_APP_API_KEY;

    const [startDateTime, setStartDateTime] = useState("");
    const [endDateTime, setEndDateTime] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newEvent = {
            actual_StartDate_Time: startDateTime,
            actual_EndDate_Time: endDateTime,
        };
        try {
            const response = await fetch(`${port}/web/agg_hhc_detailed_event_plan_of_care_per_day/?pro=${profEvent}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(newEvent),
            });
            if (!response.ok) {
                throw new Error("Failed to create event");
            }
            // fetchEvents();
            // onClose();
        } catch (error) {
            console.error("Error creating event:", error);
        }
    };

    const handleSave = () => {
        if (isEditingEvent) {
            onClose();
        }
    };

    return (
        <Modal open={isOpen} onClose={onClose}>
            <Box style={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                width: 400,
                background: 'white',
                borderRadius: '10px',
                pt: 2,
                px: 4,
                pb: 3,
            }}>
                <AppBar position="static" style={{
                    background: 'linear-gradient(45deg, #1FD0C4 38.02%, #0E8FE4 100%)',
                    width: '25rem',
                    height: '3rem',
                    marginTop: '-16px',
                    borderRadius: "8px 10px 0 0",
                }}>
                    <Typography align="center" style={{ fontSize: "16px", fontWeight: 600, color: "#FFFFFF", marginTop: "10px", }}>PROFESSIONAL SCHEDULE</Typography>
                </AppBar>
    
                    <CardContent>
                        <Grid container spacing={3} sx={{ marginTop: "1px" }}>

                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="outlined-name"
                                    label="Professional Name"
                                    size="small"
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px', // Replace with your desired font size
                                        },
                                    }}
                                />
                            </Grid>
                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="actual_StartDate_Time"
                                    label="Start Date and Time"
                                    type="datetime-local"
                                    name="actual_StartDate_Time"
                                    size="small"
                                    value={isEditingEvent ? 'Edit Event' : startDateTime}
                                    onChange={(e) => setStartDateTime(e.target.value)}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px', // Replace with your desired font size
                                        },
                                    }}
                                    InputLabelProps={{
                                        shrink: true,
                                    }}
                                />
                            </Grid>
                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="actual_EndDate_Time"
                                    label="End Date and Time"
                                    name="actual_EndDate_Time"
                                    type="datetime-local"
                                    size="small"
                                    value={isEditingEvent ? 'Edit Event' : endDateTime}
                                    onChange={(e) => setEndDateTime(e.target.value)}
                                    fullWidth
                                    sx={{
                                        '& input': {
                                            fontSize: '14px',
                                        },
                                    }}
                                    InputLabelProps={{
                                        shrink: true,
                                    }}
                                />
                            </Grid>

                            <Grid item lg={12} sm={12} xs={12}>
                                <TextField
                                    id="outlined-multiline-static"
                                    label="Remark"
                                    placeholder='write remark here'
                                    size="small"
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

                            <Grid item lg={12} sm={12} xs={12} sx={{ marginLeft: "50px" }}>
                                {isEditingEvent && (
                                    <Button variant="contained" onClick={handleSave}>Save</Button>
                                )}
                                <Button variant="contained" sx={{ m: 1, backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize", }} startIcon={<CheckIcon />} onClick={handleSubmit}>
                                    Schedule
                                </Button>
                                <Button variant="contained" sx={{ m: 1, backgroundColor: '#E5492F', borderRadius: "12px", textTransform: "capitalize", }} startIcon={<CloseIcon />} onClick={onClose}>
                                    Cancel
                                </Button>
                            </Grid>
                        </Grid>
                    </CardContent>
            </Box>
        </Modal>
    );
};

export default EventModal;
