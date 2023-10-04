import React from 'react';
import Chart from 'react-apexcharts';
import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

const Complaint = () => {
    const chartData = {
        series: [44, 55, 35],
        options: {
            chart: {
                type: 'pie',
            },
            labels: ['Received', 'In Action', 'Resolved'],
            legend: {
                position: 'bottom',
                // horizontalAlign: 'left',
            },
            colors: ['#7E41E2', '#B6034C', '#3EBAB2'],
            dataLabels: {
                enabled: false, // Set this to false to remove the percentage values
            },
        },
    };
    return (
        <Box sx={{ flexGrow: 1, width: "100%", }} style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
            
                <Typography align="left" sx={{ fontSize: 16, fontWeight: 600, pl: "10px", pt: "4px" }} color="text.secondary" gutterBottom>COMPLAINTS</Typography>
                <div style={{ display: "flex", flexDirection: "column" }}>
                    <div>
                        <Chart
                            options={chartData.options}
                            series={chartData.series}
                            type="pie"
                            // width="300"
                            height="220"
                        />
                    </div>
                </div>
        </Box>

    )
}

export default Complaint
