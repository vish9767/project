import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from "@mui/material/Typography";
import Modal from '@mui/material/Modal';

const Service = ({ value }) => {
    const port = process.env.REACT_APP_API_KEY;

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedSliceData, setSelectedSliceData] = useState({ label: '', value: 0 });
    const [service, setService] = useState([]);

    useEffect(() => {
        const getService = async () => {
            if (value) {
                try {
                    const res = await fetch(`${port}/web/srv_dtl_dash/${value}`);
                    const data = await res.json();
                    console.log("Service Count.........", data);
                    setService(data);
                } catch (error) {
                    console.error("Error fetching Service Count:", error);
                }
            }
        };
        getService();
    }, [value]);

    function generateSeries(service) {
        return [
            service.Completed_services?.percent_srv || 0,
            service.Pending_services?.percent_pen_srv || 0,
            service.ongoing_services?.percent_on_srv || 0,
            service.schedule_services || 0
        ];
    }

    const chartData = {
        series: generateSeries(service),
        // series: [],
        options: {
            chart: {
                type: 'pie',
                events: {
                    click: (event, chartContext, config) => {
                        if (!config || config.dataPointIndex === undefined || config.seriesIndex === undefined) {
                            return;
                        }
                        const { dataPointIndex } = config;
                        const { labels, series } = chartContext.w.config;

                        const selectedLabel = labels[dataPointIndex];
                        const selectedValue = series[dataPointIndex];

                        setSelectedSliceData({ label: selectedLabel, value: selectedValue });
                        setIsModalOpen(true);
                    }
                }
            },
            // responsive: true,
            labels: ['Completed Services', 'Pending', 'Ongoing', 'Schedule Services'],
            legend: {
                show: true,
                position: 'bottom',
                horizontalAlign: 'left',
            },
            colors: ['#D2709D', '#FECA57', '#3A0CA3', '#00C5C9'],
            dataLabels: {
                enabled: false, // Enable data labels
            textAnchor: 'start', // Start the label text from the slice
            formatter: function (val, opts) {
                // Display each label on a separate line
                return opts.w.globals.labels[opts.seriesIndex];
            },
            style: {
                fontSize: '12px',
            },
            },
        },
    };

    return (
        <Box sx={{ flexGrow: 1, width: "100%", }} style={{ background: '#ffffff', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
            <Typography align="left" sx={{ fontSize: 16, fontWeight: 600, pl: "10px", pt: "8px" }} color="text.secondary" gutterBottom>SERVICE DETAILS</Typography>
            <Grid item xs={12} container spacing={1}>
                <Grid item lg={12} md={12} xs={12}>
                    <Typography variant='h5' sx={{ fontWeight: "600" }}>{service.Total_services}</Typography>
                    <Typography variant='subtitle2'>TOTAL SERVICES</Typography>
                    <Chart
                        options={chartData.options}
                        series={chartData.series}
                        type="pie"
                        height="400"
                        // width="400"
                    />
                    <Modal open={isModalOpen} onClose={() => setIsModalOpen(false)}>
                        <Box sx={{
                            width: 300, height: 300, p: 2, position: 'absolute',
                            top: '50%',
                            left: '50%',
                            transform: 'translate(-50%, -50%)',
                            bgcolor: 'background.paper',
                        }}>
                            <Typography variant="body1">Service: {selectedSliceData.value}</Typography>
                            <Chart
                                options={chartData.options}
                                series={chartData.series}
                                type="pie"
                                height="300"
                            />
                        </Box>
                    </Modal>
                </Grid>
            </Grid>

        </Box>

    )
}

export default Service
