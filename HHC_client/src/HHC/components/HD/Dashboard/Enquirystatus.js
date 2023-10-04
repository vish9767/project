import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Typography from "@mui/material/Typography";

const Enquirystatus = ({ value }) => {
    const port = process.env.REACT_APP_API_KEY;

    const [enqStatus, setEnqStatus] = useState([]);

    useEffect(() => {
        const getEnqStatus = async () => {
            if (value) {
                try {
                    const res = await fetch(`${port}/web/Dashboard_enquiry_status_count_api/${value}`);
                    const data = await res.json();
                    console.log("Enquiries Status Count.........", data);
                    setEnqStatus(data);
                } catch (error) {
                    console.error("Error fetching Enquiries Status Count:", error);
                }
            }
        };
        getEnqStatus();
    }, [value]);

    const chartData = {
        // series: [44, 55],
        series: [],
        options: {
            chart: {
                type: 'donut'
            },

            labels: ['Converted', 'In Follow up'],
            legend: {
                position: 'top',
                // horizontalAlign: 'left',
            },
            colors: ['#2EAED6', '#FF8008'],
            dataLabels: {
                enabled: false,
            },
        }
    };

    const seriesData = [
        enqStatus["converted_to_service_percentage"],
        enqStatus["in_follow_up_percentage"],
    ];

    // Update the series property in your chartData object
    chartData.series = seriesData;
    return (
        <Box sx={{ flexGrow: 1, width: "100%", }} style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
            <Typography align="left" sx={{ fontSize: 16, fontWeight: 600, pl: "10px", pt: "8px" }} color="text.secondary" gutterBottom>ENQUIRY STATUS</Typography>
            <Grid item xs={12} container spacing={1}>
                <Chart
                    options={chartData.options}
                    series={chartData.series}
                    type="donut"
                    height="216"
                />
            </Grid>
        </Box>
    )
}

export default Enquirystatus
