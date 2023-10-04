import React from 'react';
import Chart from 'react-apexcharts';
import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

const Feedback = () => {
    const chartData = {
        series: [{
            data: [0, 0, 0,]
          }],

        options: {
            chart: {
                type: 'bar',
            },
            plotOptions: {
                bar: {
                   vertical: true,
                    columnWidth: '35%',
                    // distributed: true,
                }
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                show: false
            },
            colors: ['#FD7568', '#00E5D1', '#00B4D8'],
            xaxis: {
                categories: [
                    ['Good'],
                    ['Excellent'],
                    ['Average'],
                ],
                labels: {
                    style: {
                        fontSize: '12px'
                    }
                }
            },
        },
    };
    return (
            <Box sx={{ flexGrow: 1, width: "100%", }} style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
                <Typography align="left" sx={{ fontSize: 16, fontWeight: 600, pl: "10px", pt: "4px" }} color="text.secondary" gutterBottom>FEEDBACK RECEIVED</Typography>
                <div style={{ display: "flex", flexDirection: "column" }}>
                    <div>
                        <Chart
                            options={chartData.options}
                            series={chartData.series}
                            type="bar"
                            height="200"
                        />
                    </div>
                </div>
            </Box>

    )
}

export default Feedback
