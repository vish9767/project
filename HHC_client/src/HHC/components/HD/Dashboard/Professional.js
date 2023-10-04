import React, {useState, useEffect} from 'react';
import Chart from 'react-apexcharts';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from "@mui/material/Typography";

const Professional = () => {
    const port = process.env.REACT_APP_API_KEY;

    const [profCount, setProfCount] = useState([]);

    useEffect(() => {
        const getProfCount = async () => {
            // if (value) {
                try {
                    const res = await fetch(`${port}/web/jjob-type-count/`);
                    const data = await res.json();
                    console.log("Professional Count.........", data);
                    setProfCount(data);
                } catch (error) {
                    console.error("Error fetching Professional Count:", error);
                }
            // }
        };
        getProfCount();
    }, []);

    function generateSeries(profCount) {
        return [
            profCount.ONCALL,
            profCount.FULLTIME,
            profCount.FULLTIME,
        ];
    }


    const chartData = {
        // series: [44, 55, 80],
        series: generateSeries(profCount),
        options: {
            chart: {
                type: 'donut'
            },
            labels: ['On Call', 'Available', 'Tentative'],
            legend: {
                position: 'bottom',
            },
            colors: ['#E80054', '#00C5C9', '#FF8008'],
            dataLabels: {
                enabled: false, // Set this to false to remove the percentage values
            },
        }
    };
    return (
        <Box sx={{ flexGrow: 1, width: "100%", }} style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
            <Typography align="left" sx={{ fontSize: 16, fontWeight: 600, pl: "10px", pt: "8px" }} color="text.secondary" gutterBottom>PROFESSIONAL AVAILABILITY</Typography>
            <Grid item xs={12} container spacing={1}>
                <Chart
                    options={chartData.options}
                    series={chartData.series}
                    type="donut"
                    height="224"
                />
            </Grid>
        </Box>
    )
}

export default Professional
