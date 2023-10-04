import React, { useState, useEffect } from 'react'
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import MenuItem from '@mui/material/MenuItem';
import TextField from '@mui/material/TextField';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Typography from "@mui/material/Typography";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import InputBase from '@mui/material/InputBase';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import PersonOutlineSharpIcon from '@mui/icons-material/PersonOutlineSharp';
import FavoriteBorderOutlinedIcon from '@mui/icons-material/FavoriteBorderOutlined';
import CreditCardOutlinedIcon from '@mui/icons-material/CreditCardOutlined';
import StarOutlineOutlinedIcon from '@mui/icons-material/StarOutlineOutlined';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
// import CallerDetails from "./Addservice/CallerInfo";
// import ServiceInfo from './Addservice/ServiceInfo';
import smile from "../../assets/smile.png";
import { useNavigate } from "react-router-dom";
import Navbar from '../../Navbar';
import Footer from '../../Footer';
import ViewService from "./Viewservice";
import Header from '../../Header';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,

}));

const discount = [
    {
        discount_id: '1',
        label: '%',
    },
    {
        discount_id: '2',
        label: '₹',
    },
    // {
    //     discount_id: '3',
    //     label: 'None',
    // },
];

const Addservice = () => {
    const navigate = useNavigate();
    const port = process.env.REACT_APP_API_KEY;

    const [clrName, setClrName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [phoneNumberError, setPhoneNumberError] = useState('');
    const [call, setCall] = useState([]);
    const [selectedCall, setSelectedCall] = useState('');
    const [relation, setRelation] = useState([]);
    const [selectedRelation, setSelectedRelation] = useState('');

    const [ptnName, setPtnName] = useState('');
    const [gender, setGender] = useState([]);
    const [selectedGender, setSelectedGender] = useState('');
    const [profGender, setProfGender] = useState([]);
    const [selectedProfGender, setSelectedProfGender] = useState('');
    const [age, setAge] = useState('');
    const [referHospital, setReferHospital] = useState([]);
    const [selectedHospital, setSelectedHospital] = useState('');
    const [suffered, setSuffered] = useState('');
    const [ptnNumber, setPtnNumber] = useState('');
    const [ptnNumberError, setPtnNumberError] = useState('');
    const [email, setEmail] = useState('');
    const [emailError, setEmailError] = useState('');
    const [consultant, setConsultant] = useState([]);
    const [selectedConsultant, setSelectedConsultant] = useState('');
    const [consultantMobile, setConsultantMobile] = useState('');
    const [state, setState] = useState([]);
    const [selectedState, setSelectedState] = useState('');
    const [city, setCity] = useState([]);
    const [selectedCity, setSelectedCity] = useState('');
    const [zone, setZone] = useState([]);
    const [selectedZone, setSelectedZone] = useState('');
    const [pincode, setPincode] = useState('');
    const [pincodeError, setPincodeError] = useState('');
    const [address, setAddress] = useState('');

    const [service, setService] = useState([]);
    const [selectedService, setSelectedService] = useState('');
    const [subService, setSubService] = useState([]);
    const [selectedSubService, setSelectedSubService] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [endDateError, setEndDateError] = useState('');
    const [convertedStartDate, setConvertedStartDate] = useState('');
    const [convertedEndDate, setConvertedEndDate] = useState('');
    const [remark, setRemark] = useState('');

    // will remove these useState in future
    const [dob, setDOB] = useState('');
    const [validationMessage, setValidationMessage] = useState('');
    const [changeAge, setChangeAge] = useState('');
    const [stateName, setStateName] = useState('');


    const [calculatedAmount, setCalculatedAmount] = useState('');
    const [getCost, setGetCost] = useState('');

    const [selectedDiscountId, setSelectedDiscountId] = useState('3');
    // const [totalDiscount, setTotalDiscount] = useState(0);
    const [discountValue, setDiscountValue] = useState(0);

    const [coupon, setCoupon] = useState([]);
    const [selectedCoupon, setSelectedCoupon] = useState('');
    const [totalDiscount, setTotalDiscount] = useState('');

    const [callerDetails, setCallerDetails] = useState(null);
    const [patientDetails, setPatientDetails] = useState(null);
    const [selectedPatient, setSelectedPatient] = useState(null);
    const [selectedOption, setSelectedOption] = useState('');

    const [showAddPatient, setShowAddPatient] = useState(false);

    // Getting previous Patient details
    const [selectedPatientID, setSelectedPatientID] = useState('');
    const [prePatient, setPrePatient] = useState([]);
    const [preStartDate, setPreStartDate] = useState('');
    const [preEndDate, setPreEndDate] = useState('');

    const [openSnackbar, setOpenSnackbar] = useState(false); // State for Snackbar
    const [snackbarMessage, setSnackbarMessage] = useState(''); // State for Snackbar message

    const handleSnackbarClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOpenSnackbar(false);
    };

    // const [open, setOpen] = React.useState(false);

    // const handleClick = () => {
    //     setOpen(true);
    // };

    // const handleClose = (event, reason) => {
    //     if (reason === 'clickaway') {
    //         return;
    //     }

    //     setOpen(false);
    // };

    // Usestate for handling empty data
    const [errors, setErrors] = useState({
        clrName: '',
        phoneNumber: '',
        selectedCall: '',
        ptnName: '',
        selectedGender: '',
        age: '',
        selectedHospital: '',
        suffered: '',
        ptnNumber: '',
        email: '',
        selectedConsultant: '',
        consultantMobile: '',
        selectedState: '',
        selectedCity: '',
        selectedZone: '',
        // pincode: '',
        address: '',
        selectedService: '',
        selectedSubService: '',
        startDate: '',
        endDate: '',
    });

    // Function to handle empty fields
    const handleEmptyField = () => {
        const newErrors = {};

        if (!clrName) {
            newErrors.clrName = 'Name is required';
        }
        if (!phoneNumber) {
            newErrors.phoneNumber = 'Contact is required';
        }
        if (!selectedCall) {
            newErrors.selectedCall = 'Call Purpose is required';
        }
        if (!ptnName) {
            newErrors.name = 'Name is required';
        }
        if (!selectedGender) {
            newErrors.gender = 'Gender is required';
        }
        if (!age) {
            newErrors.age = 'Age is required';
        }
        if (!selectedHospital) {
            newErrors.hospital = 'Hospital Name is required';
        }
        if (!suffered) {
            newErrors.suffered = 'Suffered From is required';
        }
        if (!selectedConsultant) {
            newErrors.selectedConsultant = 'Consultant Name is required';
        }
        if (!consultantMobile) {
            newErrors.consultantMobile = 'Consultant No is required';
        }
        if (!selectedState) {
            newErrors.selectedState = 'State is required';
        }
        if (!selectedCity) {
            newErrors.selectedCity = 'City is required';
        }
        if (!selectedZone) {
            newErrors.selectedZone = 'Zone is required';
        }
        if (!address) {
            newErrors.address = 'Address is required';
        }
        if (!selectedService) {
            newErrors.selectedService = 'Service is required';
        }
        if (!selectedSubService) {
            newErrors.selectedSubService = 'Sub Service is required';
        }
        if (!selectedSubService) {
            newErrors.selectedSubService = 'Sub Service is required';
        }
        if (!selectedSubService) {
            newErrors.selectedSubService = 'Sub Service is required';
        }
        if (!startDate) {
            newErrors.startDate = 'Start Date is required';
        }
        if (!endDate) {
            newErrors.endDate = 'End Date is required';
        }

        // Set the new errors object
        setErrors(newErrors);

        // Return true if any field is empty
        return Object.values(newErrors).some((error) => error !== '');
    };

    useEffect(() => {
        if (startDate && endDate) {
            const originalStartDate = new Date(startDate);
            const originalEndDate = new Date(endDate);

            const convertedStartDateTime = formatDate(originalStartDate);
            const convertedEndDateTime = formatDate(originalEndDate);

            setConvertedStartDate(convertedStartDateTime);
            setConvertedEndDate(convertedEndDateTime);
        }
    }, [startDate, endDate]);

    function formatDate(date) {
        return `${date.getFullYear()}-${padNumber(date.getMonth() + 1)}-${padNumber(date.getDate())} ${padNumber(date.getHours())}:${padNumber(date.getMinutes())}:${padNumber(date.getSeconds())}`;
    }

    function padNumber(number) {
        return number.toString().padStart(2, '0');
    }

    // const handleCouponChange = (event) => {
    //     setSelectedCoupon(event.target.value);
    //   };


    const handleStartDateChange = (event) => {
        setStartDate(event.target.value);
        console.log(startDate);
        validateEndDate(event.target.value, endDate);
    };

    const handleEndDateChange = (event) => {
        setEndDate(event.target.value);
        validateEndDate(startDate, event.target.value);
    };

    const validateEndDate = (start, end) => {
        if (start && end) {
            const startDateObj = new Date(start);
            const endDateObj = new Date(end);

            if (endDateObj < startDateObj) {
                setEndDateError("End date time can't be earlier than the start date time");
            } else if (endDateObj.toISOString() === startDateObj.toISOString()) {
                setEndDateError("End date time cannot be the same as the start date time");
            } else {
                setEndDateError('');
            }
        } else {
            setEndDateError('');
        }
    };

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

    const handlePincodeChange = (e) => {
        const value = e.target.value;

        if (/^\d{0,6}$/.test(value)) {
            setPincode(value);
            setPincodeError('');
        } else {
            setPincodeError('Pincode must be a 6-digit number');
        }
    };

    const handleAddNewClick = () => {
        setShowAddPatient(true);
    };

    //Age Validation 
    const handleAgeValidation = (event) => {
        const inputAge = event.target.value;

        if (isNaN(inputAge)) {
            setValidationMessage('Age must be a number.');
        } else {
            const parsedAge = parseInt(inputAge, 10);
            if (parsedAge < 0) {
                setValidationMessage('Age cannot be negative.');
            } else if (parsedAge > 100) {
                setValidationMessage('Age cannot be greater than 100.');
            } else {
                setValidationMessage('');
            }
        }

        setAge(inputAge);
    };

    const handleAgeChange = (event) => {
        setChangeAge(event.target.value);
    };

    //Age Calculation Logic
    const calculateAge = selectedDOB => {
        const currentDate = new Date()
        const selectedDate = new Date(selectedDOB)
        const timeDiff = Math.abs(currentDate - selectedDate)

        //Calculate Age in Years
        const years = Math.floor(timeDiff / (1000 * 60 * 60 * 24 * 365))
        setAge(years)
    }

    const handleDOB = e => {
        const selectedDOB = e.target.value
        setDOB(selectedDOB)
        calculateAge(selectedDOB);
    }

    //TextField change Logic
    const handleDropdownChange = (event) => {
        setSelectedOption(event.target.value);
    };

    const handleDropdownGender = (event) => {
        const selectedGender = event.target.value;
        setSelectedGender(selectedGender);
    };

    const handleDropdownProfGender = (event) => {
        const selectedProfGender = event.target.value;
        setSelectedProfGender(selectedProfGender);
    };

    const handleDropdownConsultant = (event) => {
        const selectedValue = event.target.value;
        setSelectedConsultant(selectedValue);

        // Find the selected consultant's mobile number and set it as the selected contact
        const selectedConsultantData = consultant.find(consult => consult.doct_cons_id === selectedValue);
        if (selectedConsultantData) {
            setConsultantMobile(selectedConsultantData.mobile_no);
        } else {
            setConsultantMobile('');
        }
    };

    const handleDropdownRelation = (event) => {
        const selectedRelation = event.target.value;
        setSelectedRelation(selectedRelation);
    };

    const handleDropdownCall = (event) => {
        const selectedCall = event.target.value;
        setSelectedCall(selectedCall);
    };

    const handleDropdownService = (event) => {
        const selectedService = event.target.value;
        setSelectedService(selectedService);
    };

    const handleDropdownSubService = (event) => {
        const selectedSubService = event.target.value;
        setSelectedSubService(selectedSubService);
    };

    const handleDropdownGetCost = (event) => {
        const getCost = event.target.value;
        setGetCost(getCost);
    };

    //Caller Phone Number Validation//
    const handlePhoneNumberChange = (event) => {
        const { value } = event.target;
        setPhoneNumber(value);
    };

    const validatePhoneNumber = () => {
        const numberRegex = /^\d+$/;

        if (phoneNumber.trim() === '') {
            setPhoneNumberError('Please enter a mobile number');
        } else if (!numberRegex.test(phoneNumber)) {
            setPhoneNumberError('Mobile number should contain only numbers');
        } else {
            setPhoneNumberError('');
        }
    };

    const handleInput = (event) => {
        const { value } = event.target;
        // Remove any non-numeric characters from the input value
        const numericValue = value.replace(/[^0-9]/g, '');
        // Update the phone number state and validate it
        setPhoneNumber(numericValue);
        validatePhoneNumber();
    };

    //Patient Phone Number Validation//
    const handlePtnNumberChange = (event) => {
        const { value } = event.target;
        setPtnNumber(value);
    };

    const validatePtnNumber = () => {
        const numberRegex = /^\d+$/; // Regular expression for numbers only

        if (ptnNumber.trim() === '') {
            setPtnNumberError('Please enter a mobile number');
        } else if (!numberRegex.test(ptnNumber)) {
            setPtnNumberError('Mobile number should contain only numbers');
        } else {
            setPtnNumberError('');
        }
    };

    const handlePtnInput = (event) => {
        const { value } = event.target;
        // Remove any non-numeric characters from the input value
        const numericValue = value.replace(/[^0-9]/g, '');
        // Update the phone number state and validate it
        setPtnNumber(numericValue);
        validatePtnNumber();
    };

    //Patient Email validation//
    const handleEmailChange = (event) => {
        const { value } = event.target;
        setEmail(value);
    };

    const validateEmail = () => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regular expression for email validation

        if (email.trim() === '') {
            setEmailError('Please enter an email address');
        } else if (!emailRegex.test(email)) {
            setEmailError('Please enter a valid email address');
        } else {
            setEmailError('');
        }
    };

    useEffect(() => {
        const getGender = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_gender_api`);
                const data = await res.json();
                console.log(data);
                setGender(data);
                setProfGender(data)
            } catch (error) {
                console.error("Error fetching gender data:", error);
            }
        };
        getGender();
    }, []);

    useEffect(() => {
        const getRelation = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_caller_relation_api`);
                const data = await res.json();
                console.log("Relation...", data)
                setRelation(data);
            } catch (error) {
                console.error("Error fetching Relation data:", error);
            }
        };
        getRelation();
    }, []);

    useEffect(() => {
        const callPurpose = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_purpose_call_api`);
                const data = await res.json();
                console.log("Call Purpose", data);
                setCall(data);
            } catch (error) {
                console.error("Error fetching Call purpose data:", error);
            }
        };
        callPurpose();
    }, []);

    // state data today
    useEffect(() => {
        const getState = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_state_api`);
                const data = await res.json();
                console.log("State List....", data);
                setState(data);
            } catch (error) {
                console.error("Error fetching Zone data:", error);
            }
        };
        getState();
    }, []);

    // city data today
    useEffect(() => {
        const getCity = async () => {
            if (selectedState) {
                try {
                    const res = await fetch(`${port}/web/agg_hhc_city_api/${selectedState}`);
                    const data = await res.json();
                    console.log("City List a/c to State Data", data);
                    setCity(data);
                } catch (error) {
                    console.error("Error fetching city data:", error);
                }
            }
        };
        getCity();
    }, [selectedState]);

    // zone data today
    useEffect(() => {
        const getZone = async () => {
            if (selectedCity) {
                try {
                    const res = await fetch(`${port}/web/agg_hhc_zone_api/${selectedCity}`);
                    const data = await res.json();
                    console.log("Zone List a/c to City Data", data);
                    setZone(data);
                } catch (error) {
                    console.error("Error fetching Zone data:", error);
                }
            }
        };
        getZone();
    }, [selectedCity]);

    useEffect(() => {
        const getreferHospital = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_hospitals_api`);
                const data = await res.json();
                console.log("Refer Hospital data", data);
                setReferHospital(data);
            } catch (error) {
                console.error("Error fetching Refer Hospital data:", error);
            }
        };
        getreferHospital();
    }, []);

    useEffect(() => {
        const getConsultant = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_consultant_api`);
                const data = await res.json();
                console.log("Consultant data", data);
                setConsultant(data);
            } catch (error) {
                console.error("Error fetching Consultant data:", error);
            }
        };
        getConsultant();
    }, []);

    useEffect(() => {
        const getService = async () => {
            try {
                const res = await fetch(`${port}/web/agg_hhc_services_api`);
                const data = await res.json();
                console.log("Service Data.........", data);
                setService(data);
            } catch (error) {
                console.error("Error fetching service data:", error);
            }
        };
        getService();
    }, []);

    useEffect(() => {
        const getSubService = async () => {
            if (selectedService) {
                console.log("service Id", selectedService);
                try {
                    const res = await fetch(`${port}/web/agg_hhc_sub_services_api/${selectedService}`);
                    const data = await res.json();
                    console.log("Sub Service Data", data);
                    setSubService(data);
                    // const initialSelectedSubServices = data.map((subService) => subService.sub_srv_id);
                    // setSelectedSubService(initialSelectedSubServices);
                } catch (error) {
                    console.error("Error fetching sub service data:", error);
                }
            }
        };
        getSubService();
    }, [selectedService]);

    const handleSubServiceSelect = (event) => {
        const subServiceId = event.target.value;
        const selectedSubService = subService.find(item => item.sub_srv_id === subServiceId);
        if (selectedSubService) {
            setSelectedSubService(subServiceId);
            setGetCost(selectedSubService.cost);
        }
    };

    const subServiceData = subService[selectedService] || [];

    useEffect(() => {
        const calculateTotalAmount = async () => {
            if (getCost && startDate && endDate) {
                try {
                    const url = `${port}/web/calculate_total_amount/${getCost}/${startDate}/${endDate}/`;
                    const res = await fetch(url, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await res.json();
                    console.log("Calculated Amount.....", data.days_difference);
                    setCalculatedAmount(data.days_difference);
                } catch (error) {
                    console.error("Error fetching Calculated Amount:", error);
                }
            }
        };
        calculateTotalAmount();
    }, [getCost, startDate, endDate]);

    useEffect(() => {
        const calculateDiscount = async () => {
            if (calculatedAmount && selectedDiscountId && discountValue) {
                console.log("Discount Amount.....", calculatedAmount, selectedDiscountId, discountValue)
                try {
                    const url = `${port}/web/calculate_discount_api/${selectedDiscountId}/${discountValue}/${calculatedAmount}`;
                    const res = await fetch(url, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await res.json();
                    console.log("Calculated Amount with Discount.....", data);
                    setTotalDiscount(data.final_amount);
                } catch (error) {
                    console.error("Error fetching Calculated Amount with Discount:", error);
                }
            } else {
                setTotalDiscount(calculatedAmount);
            }
        };
        calculateDiscount();
    }, [calculatedAmount, selectedDiscountId, discountValue]);

    // useEffect(() => {
    //     const getCoupon = async () => {
    //         try {
    //             const res = await fetch(`${port}/web/coupon_code_api`);
    //             const data = await res.json();
    //             console.log("Coupon data", data);
    //             setCoupon(data);
    //         } catch (error) {
    //             console.error("Error fetching Coupon data:", error);
    //         }
    //     };
    //     getCoupon();
    // }, []);

    // Function to handle coupon selection
    const handleCouponSelect = (couponId) => {
        const selectedCoupon = coupon.find((item) => item.coupon_id === couponId.target.value);
        if (selectedCoupon) {
            setSelectedCoupon(selectedCoupon.coupon_code);
        }
    };

    useEffect(() => {
        const calculateCouponDiscount = async () => {
            if (calculatedAmount && selectedCoupon) {
                console.log("Discount with coupon Amount", calculatedAmount, selectedCoupon)
                try {
                    const url = `${port}/web/coupon_code_post_api/${selectedCoupon}/${calculatedAmount}`;
                    const res = await fetch(url, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await res.json();
                    console.log("Calculated Amount with Coupon Code.....", data);
                    setTotalDiscount(data.final_amount);
                } catch (error) {
                    console.error("Error fetching Calculated Amount with Coupon Code:", error);
                }
            }
        };
        calculateCouponDiscount();
    }, [selectedCoupon, calculatedAmount]);

    // Function to fetch caller details from API
    const fetchCallerData = () => {
        fetch(`${port}/web/agg_hhc_patient_from_callers_phone_no/${phoneNumber}`)
            .then((response) => response.json())
            .then((responseData) => {
                console.log("Caller Details Data......", responseData);
                setCallerDetails(responseData.caller);
                console.log("Patient Records......", responseData.patients);
                setPatientDetails(responseData.patients);
            })
            .catch((error) => {
                console.error('No Caller Data Found......:', error);
                setCallerDetails(null);
                setPatientDetails(null);
            });
    };

    const handleSearch = (event) => {
        if (event.key === 'Enter') {
            fetchCallerData();
        }
    };

    // useEffect to fetch Caller Details on component mount
    useEffect(() => {
        if (phoneNumber) {
            fetchCallerData(phoneNumber);
        }
    }, [phoneNumber]);

    // Function to handle patient selection from dropdown
    const handlePatientSelect = (e) => {
        const selectedPatientId = parseInt(e.target.value);
        const patient = patientDetails.find((patient) => patient.agg_sp_pt_id === selectedPatientId);
        setSelectedPatient(patient);
        setSelectedPatientID(patient.agg_sp_pt_id);
    };

    useEffect(() => {
        const getPatientPreDetails = async () => {
            if (selectedPatientID) {
                console.log("Selected Patient ID", selectedPatientID);
                try {
                    const url = `${port}/web/last_patient_service_info/${selectedPatientID}`;
                    const res = await fetch(url, {
                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await res.json();
                    console.log("Patient Previous Details.....", data);
                    setPrePatient(data);
                    setPreStartDate(data.Date.start_date)
                    setPreEndDate(data.Date.end_date)
                    console.log("Start Date:", data.Date.start_date, "End Date:", data.Date.end_date)
                } catch (error) {
                    console.error("Error fetching Patient Previous Details:", error);
                }
            }
        };
        getPatientPreDetails();
    }, [selectedPatientID]);

    const formatDateRange = (preStartDate, preEndDate) => {
        const startDate = new Date(preStartDate);
        const endDate = new Date(preEndDate);

        const startOptions = { day: "numeric", month: "short" };
        const endOptions = { day: "numeric", month: "short", year: "numeric" };

        const startFormatted = startDate.toLocaleDateString("en-US", startOptions);
        const endFormatted = endDate.toLocaleDateString("en-US", endOptions);

        return `${startFormatted} - ${endFormatted}`;
    };

    const startDateTimeString = preStartDate;
    const endDateTimeString = preEndDate;
    const formattedDateRange = formatDateRange(startDateTimeString, endDateTimeString);

    async function handleSubmit(event, actionType) {
        event.preventDefault();
        validatePhoneNumber();
        validateEmail();
        validatePtnNumber()
        handleEmptyField()
        const requestData = {
            // Caller Data //
            caller_fullname: clrName,
            caller_rel_id: selectedRelation,
            purp_call_id: selectedCall,
            phone: phoneNumber,

            // Patient Data //
            name: ptnName,
            gender_id: selectedGender,
            Age: age,
            preferred_hosp_id: selectedHospital,
            Suffered_from: suffered,
            phone_no: ptnNumber,
            patient_email_id: email,
            doct_cons_id: selectedConsultant,
            doct_cons_phone: consultantMobile,
            state_id: selectedState,
            city_id: selectedCity,
            prof_zone_id: selectedZone,
            pincode: pincode,
            address: address,

            // Service Data //
            srv_id: selectedService,
            sub_srv_id: selectedSubService,
            start_date: convertedStartDate,
            end_date: convertedEndDate,
            prof_prefered: selectedProfGender,
            remark: remark,
            Total_cost: calculatedAmount,
            discount_type: selectedDiscountId,
            discount_value: discountValue,
            final_amount: totalDiscount
            // getCost,
            // selectedDiscountId,
            // coupon,
            // selectedCoupon,
            // totalDiscount,
        };
        console.log("POST API Hitting......", requestData)
        try {
            const response = await fetch(`${port}/web/agg_hhc_add_service_details_api`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(requestData),

            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json();
            console.log("Results.....", result);
            if (actionType === "CreateService") {
                const eventValue = result["Service Created Event Code"][0]["event_id"];
                const patientValue = result["Service Created Event Code"][1]["agg_sp_pt_id"];
                const callerValue = result["Service Created Event Code"][1]["caller_id"];
                const eventPlanValue = result["Service Created Event Code"][2]["event_plan_of_care_id"][0];

                console.log("event ID", eventValue);
                console.log("patientID", patientValue);
                console.log("callerID", callerValue);
                console.log("eventPlanID", eventPlanValue);

                navigate('/viewservice', {
                    state: {
                        patientID: patientValue,
                        callerID: callerValue,
                        eventPlanID: eventPlanValue,
                        eventID: eventValue,
                    },
                });
            } else if (actionType === "Enquiry") {
                setOpenSnackbar(true);
                setSnackbarMessage('Your Enquiry has been saved successfully.');
                // Reset form fields here
                setClrName('')
                setPhoneNumber('')
                setSelectedCall('')
                setSelectedRelation('')

                setPtnName('');
                setPtnNumber('');
                setSelectedGender('');
                setAge('');
                setEmail('')
                setSelectedHospital('');
                setSuffered('');
                setSelectedState('');
                setSelectedCity('');
                setSelectedZone('')
                setSelectedConsultant('')
                setConsultantMobile('')
                setPincode('')
                setAddress('')

                setSelectedService('')
                setSelectedSubService('')
                setStartDate('')
                setEndDate('')
                setSelectedProfGender('')
                setRemark('')
                setCalculatedAmount('')
                setSelectedDiscountId('')
                setDiscountValue('')
                setTotalDiscount('')
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }

    }
    return (
        <>
            <Navbar />
            {/* <Header /> */}
            <Box sx={{ flexGrow: 1, mb: 2, typography: 'body1', width: '100%', }}>

                <Grid item xs={12} container spacing={1}>

                    {/* Previous User Details */}
                    <Grid item lg={3} md={3} xs={12}>
                        <Grid item md={6} lg={12}>
                            <Card sx={{ minWidth: 200 }} style={{ background: 'linear-gradient(90deg, #C5EEEC 20%, #D0E3F3 100%)', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
                                <CardContent>
                                    <Stack direction="row" alignItems="left" gap={10}>
                                        <PersonOutlineSharpIcon />
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, }} gutterBottom>Caller Details</Typography>
                                    </Stack>
                                    {callerDetails ? (
                                        <>
                                            <Typography sx={{ fontSize: 14 }} gutterBottom>
                                                Name: {callerDetails.caller_fullname}
                                            </Typography>
                                            <Typography sx={{ fontSize: 14 }} gutterBottom>
                                                Contact: {callerDetails.phone}
                                            </Typography>
                                        </>
                                    ) : (
                                        <>
                                            <div style={{ display: "flex", justifyContent: "center" }}>
                                                <Typography variant='subtitle2' sx={{ fontSize: 14 }} gutterBottom>
                                                    Welcome to Spero Homehealthcare
                                                    {/* 😊 */}
                                                </Typography>
                                                <img src={smile} alt="" style={{ width: "22px", height: "22px", marginLeft: "2px" }} />
                                            </div>
                                            <Typography sx={{ fontSize: 14 }} gutterBottom>
                                                Name & Contact
                                            </Typography>
                                        </>
                                    )}
                                </CardContent>
                            </Card>
                        </Grid>

                        <Grid item md={6} lg={12}>
                            <Card sx={{ minWidth: 200, mt: 1 }} style={{ background: 'linear-gradient(90deg, #C5EEEC 0%, #D0E3F3 100%)', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
                                <CardContent>
                                    <Stack direction="row" alignItems="left" gap={8}>
                                        <FavoriteBorderOutlinedIcon />
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, }} gutterBottom>Previous Services</Typography>
                                    </Stack>

                                    {prePatient && prePatient.service ? (
                                        <>
                                            <Typography sx={{ fontSize: 14 }} gutterBottom>
                                                {prePatient.service}
                                            </Typography>
                                            <Typography sx={{ fontSize: 12 }}>{formattedDateRange}</Typography>
                                        </>
                                    ) : (
                                        <Typography sx={{ fontSize: 14 }} gutterBottom>
                                            Service Name
                                        </Typography>
                                    )}

                                </CardContent>
                            </Card>
                        </Grid>

                        <Grid item md={6} lg={12}>
                            <Card sx={{ minWidth: 200, mt: 1 }} style={{ background: 'linear-gradient(90deg, #C5EEEC 0%, #D0E3F3 100%)', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px' }}>
                                <CardContent>
                                    <Stack direction="row" alignItems="left" gap={8}>
                                        <CreditCardOutlinedIcon />
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, }} gutterBottom>Payment Status</Typography>
                                    </Stack>

                                    <Typography sx={{ fontSize: 14 }} gutterBottom>
                                        Pending Amount: 00
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>

                        <Grid item md={6} lg={12}>
                            <Card sx={{ minWidth: 200, mt: 1, }} style={{ background: 'linear-gradient(90deg, #C5EEEC 0%, #D0E3F3 100%)', boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)', borderRadius: '10px', }}>
                                <CardContent
                                    sx={{
                                        height: "9.2rem",
                                        overflowY: "scroll",
                                        overflowX: "hidden",
                                        scrollbarWidth: 'thin',
                                        '&::-webkit-scrollbar': {
                                            width: '0.2em',
                                        },
                                        '&::-webkit-scrollbar-track': {
                                            background: "#DCDCDE",
                                        },
                                        '&::-webkit-scrollbar-thumb': {
                                            backgroundColor: '#7AB8EE',
                                        },
                                        '&::-webkit-scrollbar-thumb:hover': {
                                            background: '#7AB8FF'
                                        }
                                    }}>
                                    <Stack direction="row" alignItems="left" gap={10}>
                                        <StarOutlineOutlinedIcon />
                                        <Typography sx={{ fontSize: 16, fontWeight: 600, }} gutterBottom>Feedback</Typography>
                                    </Stack>

                                    <Typography sx={{ fontSize: 14, color: '#D62E4B' }} gutterBottom>
                                        <FavoriteBorderIcon /><FavoriteBorderIcon /><FavoriteBorderIcon /><FavoriteBorderIcon /><FavoriteBorderIcon />
                                    </Typography>
                                    <Typography variant="body2">
                                        <br />
                                        {'"We are waiting for your valuable feedback, stay happy and healthy :)"'}
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>

                    {/* Caller and Patient Details */}
                    <Grid item lg={6} md={6} xs={12}>
                        {/* <CallerDetails /> */}
                        <Card
                            sx={{ width: "100%", borderRadius: "10px", bgColor: "white", boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)' }}
                        >
                            <CardContent>
                                <Typography align="left" style={{ fontSize: "16px", fontWeight: 600, }}>CALLER DETAILS</Typography>
                                <Grid container spacing={2} sx={{ marginTop: "1px" }}>

                                    <Grid item lg={6} sm={6} xs={12}>
                                        <TextField
                                            required
                                            id="phone"
                                            name="phone"
                                            label="Mobile"
                                            placeholder="+91 |"
                                            size="small"
                                            fullWidth
                                            value={phoneNumber}
                                            onChange={handlePhoneNumberChange}
                                            onInput={handleInput}
                                            onKeyPress={handleSearch}
                                            error={!!phoneNumberError || !!errors.phoneNumber}
                                            helperText={phoneNumberError || errors.phoneNumber}
                                            inputProps={{
                                                minLength: 10,
                                                maxLength: 10,
                                            }}
                                            sx={{
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                        />
                                    </Grid>

                                    {callerDetails ? (
                                        <Grid item lg={6} sm={6} xs={12}>
                                            <TextField
                                                required
                                                label="Full Name"
                                                id="caller_fullname"
                                                name="caller_fullname"
                                                placeholder="First Name | Last Name *"
                                                value={callerDetails ? callerDetails.caller_fullname : ''}
                                                size="small"
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
                                    ) : (

                                        <Grid item lg={6} sm={6} xs={12}>
                                            <TextField
                                                required
                                                label="Full Name"
                                                id="caller_fullname"
                                                name="caller_fullname"
                                                value={clrName}
                                                onChange={(e) => setClrName(e.target.value)}
                                                placeholder="First Name | Last Name *"
                                                size="small"
                                                fullWidth
                                                error={!!errors.clrName}
                                                helperText={errors.clrName}
                                                sx={{
                                                    '& input': {
                                                        fontSize: '14px',
                                                    },
                                                }}
                                            />
                                        </Grid>
                                    )}

                                    <Grid item lg={6} sm={6} xs={12}>
                                        <TextField
                                            required
                                            id="purp_call_id"
                                            name="purp_call_id"
                                            select
                                            label="Select Call Type"
                                            value={selectedCall}
                                            onChange={handleDropdownCall}
                                            size="small"
                                            fullWidth
                                            error={!!errors.selectedCall}
                                            helperText={errors.selectedCall}
                                            sx={{
                                                textAlign: "left", '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '120px',
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {call.map((option) => (
                                                <MenuItem key={option.purp_call_id} value={option.purp_call_id}
                                                    sx={{ fontSize: "14px" }}>
                                                    {option.name}
                                                </MenuItem>
                                            ))}
                                        </TextField>
                                    </Grid>

                                    <Grid item lg={6} sm={6} xs={12}>
                                        <TextField
                                            required
                                            id="caller_rel_id"
                                            name="caller_rel_id"
                                            select
                                            label="Select Relation"
                                            // defaultValue={selectedRelation}
                                            value={selectedRelation}
                                            onChange={handleDropdownRelation}
                                            size="small"
                                            fullWidth
                                            sx={{
                                                textAlign: "left", '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '120px', // Adjust the height as needed
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {relation.map((option) => (
                                                <MenuItem key={option.caller_rel_id} value={option.caller_rel_id}
                                                    sx={{ fontSize: "14px" }}>
                                                    {option.relation}
                                                </MenuItem>
                                            ))}
                                        </TextField>
                                    </Grid>

                                </Grid>
                            </CardContent>
                        </Card>

                        {/* Patient Details */}
                        <Card
                            sx={{
                                width: "100%",
                                borderRadius: "10px",
                                marginTop: "8px",
                                bgColor: "white",
                                boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)',

                            }}
                        >
                            <CardContent>
                                <Grid container>
                                    <Typography align="left" style={{ fontSize: "16px", fontWeight: 600 }}>PATIENT DETAILS  </Typography>

                                </Grid>

                                <Grid container spacing={2} sx={{ marginTop: "1px" }} >
                                    {patientDetails ? (
                                        <>
                                            <Grid item lg={6} sm={6} xs={12}>
                                                <TextField
                                                    required
                                                    id="name"
                                                    name="name"
                                                    select
                                                    label="Select Patient"
                                                    size="small"
                                                    // value={ptnName}
                                                    defaultValue={selectedPatient}
                                                    onChange={handlePatientSelect}
                                                    fullWidth
                                                    sx={{
                                                        textAlign: "left", '& input': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                >
                                                    {patientDetails.map((option) => (
                                                        <MenuItem key={option.agg_sp_pt_id
                                                        } value={option.agg_sp_pt_id
                                                        }>
                                                            {option.name}
                                                        </MenuItem>
                                                    ))}
                                                </TextField>

                                            </Grid>

                                            {selectedPatient && (
                                                <>
                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <Grid container spacing={1}>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    required
                                                                    id="name"
                                                                    label="Gender"
                                                                    value={selectedPatient ? selectedPatient.gender_id : ''}
                                                                    name="name"
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        textAlign: "left",
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    required
                                                                    label="Age"
                                                                    id="outlined-size-small"
                                                                    value={selectedPatient ? selectedPatient.Age : ''}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <TextField
                                                            label="Hospital Name"
                                                            id="outlined-size-small"
                                                            placeholder='Name'
                                                            value={selectedPatient ? selectedPatient.Hospital_name : ""}
                                                            size="small"
                                                            fullWidth
                                                            sx={{
                                                                textAlign: "left", '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            InputLabelProps={{
                                                                shrink: true,
                                                            }}
                                                        />
                                                    </Grid>

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <TextField
                                                            label="Suffered From"
                                                            id="Suffered_from"
                                                            name="Suffered_from"
                                                            placeholder='Remark'
                                                            type="textarea"
                                                            value={selectedPatient ? selectedPatient.Suffered_from : ""}
                                                            size="small"
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

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <Grid container spacing={1}>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="Contact"
                                                                    id="phone_no"
                                                                    name="phone_no"
                                                                    placeholder='+91 |'
                                                                    size="small"
                                                                    fullWidth
                                                                    value={selectedPatient ? selectedPatient.phone_no : ""}
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="Email"
                                                                    id="patient_email_id"
                                                                    name="patient_email_id"
                                                                    placeholder='example@gmail.com'
                                                                    value={selectedPatient ? selectedPatient.patient_email_id : ""}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <Grid container spacing={1}>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="Consultant Name"
                                                                    id="doct_cons_id"
                                                                    name="doct_cons_id"
                                                                    placeholder='Enter Name'
                                                                    size="small"
                                                                    fullWidth
                                                                    value={selectedPatient ? selectedPatient.doct_cons_id : ""}
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>

                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="Contact"
                                                                    id="ptnNumber"
                                                                    placeholder='+91 |'
                                                                    size="small"
                                                                    fullWidth
                                                                    // value={ptnNumber}
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <Grid container spacing={1}>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="State"
                                                                    id="stateName"
                                                                    placeholder='State'
                                                                    value={selectedPatient ? selectedPatient.state_id : ""}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="City Name"
                                                                    id="cityName"
                                                                    value={selectedPatient ? selectedPatient.city_id : ''}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        textAlign: "left", '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                    <Grid item lg={6} sm={6} xs={12}>
                                                        <Grid container spacing={1}>
                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    label="Select Zone"
                                                                    id="Name"
                                                                    // value={selectedPatient ? selectedPatient.zone : ''}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        textAlign: "left", '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>

                                                            <Grid item xs={6}>
                                                                <TextField
                                                                    id="pincode"
                                                                    label="Pincode"
                                                                    placeholder='Pincode'
                                                                    name="pincode"
                                                                    value={selectedPatient ? selectedPatient.pincode : ''}
                                                                    size="small"
                                                                    fullWidth
                                                                    sx={{
                                                                        textAlign: "left",
                                                                        '& input': {
                                                                            fontSize: '14px',
                                                                        },
                                                                    }}
                                                                />
                                                            </Grid>
                                                        </Grid>
                                                    </Grid>

                                                    <Grid item lg={12} sm={12} xs={12}>
                                                        <TextField
                                                            label="Address"
                                                            id="address"
                                                            name="address"
                                                            placeholder='House No,Building,Street,Area'
                                                            size="small"
                                                            value={selectedPatient ? selectedPatient.address : ''}
                                                            fullWidth
                                                            sx={{
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />
                                                    </Grid>

                                                </>
                                            )}
                                        </>

                                    ) : (
                                        <>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <TextField
                                                    required
                                                    id="name"
                                                    name="name"
                                                    label="Patient Name"
                                                    placeholder="First Name | Last Name "
                                                    value={ptnName}
                                                    onChange={(e) => setPtnName(e.target.value)}
                                                    size="small"
                                                    fullWidth
                                                    sx={{
                                                        textAlign: "left", '& input': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                    error={!!errors.name}
                                                    helperText={errors.name}
                                                />
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <Grid container spacing={1}>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            id="gender_id"
                                                            name="gender_id"
                                                            select
                                                            label="Gender"
                                                            defaultValue={selectedGender}
                                                            size="small"
                                                            fullWidth
                                                            sx={{
                                                                textAlign: "left",
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            onChange={handleDropdownGender}
                                                            error={!!errors.gender}
                                                            helperText={errors.gender}
                                                        >
                                                            {gender.map((option) => (
                                                                <MenuItem key={option.gender_id} value={option.gender_id}
                                                                    sx={{ fontSize: "14px" }}>
                                                                    {option.name}
                                                                </MenuItem>
                                                            ))}
                                                        </TextField>
                                                    </Grid>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="Age"
                                                            id="outlined-size-small"
                                                            name="Age"
                                                            value={age}
                                                            onChange={handleAgeValidation}
                                                            size="small"
                                                            fullWidth
                                                            error={!!validationMessage || !!errors.age}
                                                            helperText={validationMessage || errors.age}
                                                            sx={{
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />

                                                    </Grid>
                                                </Grid>
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <TextField
                                                    required
                                                    label="Hospital Name"
                                                    id="preferred_hosp_id"
                                                    name="preferred_hosp_id"
                                                    select
                                                    placeholder='Hospital Name'
                                                    size="small"
                                                    fullWidth
                                                    value={selectedHospital}
                                                    onChange={(e) => setSelectedHospital(e.target.value)}
                                                    error={!!errors.hospital}
                                                    helperText={errors.hospital}
                                                    sx={{
                                                        textAlign: "left", '& input': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                    SelectProps={{
                                                        MenuProps: {
                                                            PaperProps: {
                                                                style: {
                                                                    maxHeight: '200px', // Adjust the height as needed
                                                                    maxWidth: '200px',
                                                                },
                                                            },
                                                        },
                                                    }}
                                                >
                                                    {referHospital.map((option) => (
                                                        <MenuItem key={option.hosp_id} value={option.hosp_id}
                                                            sx={{ fontSize: "14px", }}>
                                                            {option.hospital_name}
                                                        </MenuItem>
                                                    ))}
                                                </TextField>
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <TextField
                                                    required
                                                    label="Suffered From"
                                                    id="Suffered_from"
                                                    name="Suffered_from"
                                                    value={suffered}
                                                    onChange={(e) => setSuffered(e.target.value)}
                                                    placeholder='Remark'
                                                    type="textarea"
                                                    size="small"
                                                    fullWidth
                                                    error={!!errors.suffered}
                                                    helperText={errors.suffered}
                                                    sx={{
                                                        '& input': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                />
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <Grid container spacing={1}>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="Contact"
                                                            id="phone_no"
                                                            name="phone_no"
                                                            placeholder='+91 |'
                                                            size="small"
                                                            fullWidth
                                                            value={ptnNumber}
                                                            onChange={handlePtnNumberChange}
                                                            onInput={handlePtnInput}
                                                            error={!!ptnNumberError || !!errors.ptnNumber}
                                                            helperText={ptnNumberError || errors.ptnNumber}
                                                            inputProps={{
                                                                minLength: 10,
                                                                maxLength: 10,
                                                            }}
                                                            sx={{
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />
                                                    </Grid>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="Email"
                                                            id="patient_email_id"
                                                            placeholder='example@gmail.com'
                                                            name="patient_email_id"
                                                            value={email}
                                                            onChange={handleEmailChange}
                                                            error={!!emailError || errors.email}
                                                            helperText={emailError || errors.email}
                                                            size="small"
                                                            fullWidth
                                                            sx={{
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <Grid container spacing={1}>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="Consultant Name"
                                                            id="doct_cons_id"
                                                            name="doct_cons_id"
                                                            select
                                                            placeholder='Enter Name'
                                                            size="small"
                                                            defaultValue={selectedConsultant}
                                                            onChange={handleDropdownConsultant}
                                                            fullWidth
                                                            error={!!errors.selectedConsultant}
                                                            helperText={errors.selectedConsultant}
                                                            sx={{
                                                                textAlign: "left", '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            SelectProps={{
                                                                MenuProps: {
                                                                    PaperProps: {
                                                                        style: {
                                                                            maxHeight: '120px', // Adjust the height as needed
                                                                            maxWidth: '200px',
                                                                        },
                                                                    },
                                                                },
                                                            }}
                                                        >
                                                            {consultant.map((option) => (
                                                                <MenuItem key={option.doct_cons_id} value={option.doct_cons_id}
                                                                    sx={{ fontSize: "14px" }}>
                                                                    {option.cons_fullname}
                                                                </MenuItem>
                                                            ))}
                                                        </TextField>
                                                    </Grid>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            label="Contact"
                                                            id="doct_cons_phone"
                                                            name="doct_cons_phone"
                                                            placeholder='+91 |'
                                                            size="small"
                                                            fullWidth
                                                            value={consultantMobile}
                                                            error={!!errors.consultantMobile}
                                                            helperText={errors.consultantMobile}
                                                            inputProps={{
                                                                minLength: 10,
                                                                maxLength: 10,
                                                            }}
                                                            sx={{
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <Grid container spacing={1}>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="State"
                                                            id="state_id"
                                                            name="state_id"
                                                            select
                                                            placeholder='State'
                                                            defaultValue={selectedState}
                                                            onChange={(e) => setSelectedState(e.target.value)}
                                                            size="small"
                                                            fullWidth
                                                            error={!!errors.selectedState}
                                                            helperText={errors.selectedState}
                                                            sx={{
                                                                textAlign: "left", '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            SelectProps={{
                                                                MenuProps: {
                                                                    PaperProps: {
                                                                        style: {
                                                                            maxHeight: '120px', // Adjust the height as needed
                                                                            maxWidth: '200px',
                                                                        },
                                                                    },
                                                                },
                                                            }}
                                                        >
                                                            {state.map((option) => (
                                                                <MenuItem key={option.state_id} value={option.state_id}
                                                                    sx={{ fontSize: "14px" }}>
                                                                    {option.state_name}
                                                                </MenuItem>
                                                            ))}
                                                        </TextField>
                                                    </Grid>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="City Name"
                                                            id="city_id"
                                                            name="city_id"
                                                            select
                                                            value={selectedCity}
                                                            onChange={(e) => setSelectedCity(e.target.value)}
                                                            size="small"
                                                            fullWidth
                                                            error={!!errors.selectedCity}
                                                            helperText={errors.selectedCity}
                                                            sx={{
                                                                textAlign: "left", '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            SelectProps={{
                                                                MenuProps: {
                                                                    PaperProps: {
                                                                        style: {
                                                                            maxHeight: '200px', // Adjust the height as needed
                                                                            maxWidth: '200px',
                                                                        },
                                                                    },
                                                                },
                                                            }}
                                                        >
                                                            {city.map((option) => (
                                                                <MenuItem key={option.city_id} value={option.city_id}
                                                                    sx={{ fontSize: "14px" }}>
                                                                    {option.city_name}
                                                                </MenuItem>
                                                            ))}
                                                        </TextField>
                                                    </Grid>
                                                </Grid>
                                            </Grid>

                                            <Grid item lg={6} sm={6} xs={12}>
                                                <Grid container spacing={1}>
                                                    <Grid item xs={6}>
                                                        <TextField
                                                            required
                                                            label="Select Zone"
                                                            id="prof_zone_id"
                                                            name="prof_zone_id"
                                                            select
                                                            value={selectedZone}
                                                            onChange={(e) => setSelectedZone(e.target.value)}
                                                            size="small"
                                                            fullWidth
                                                            error={!!errors.selectedZone}
                                                            helperText={errors.selectedZone}
                                                            sx={{
                                                                textAlign: "left", '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            SelectProps={{
                                                                MenuProps: {
                                                                    PaperProps: {
                                                                        style: {
                                                                            maxHeight: '200px', // Adjust the height as needed
                                                                            maxWidth: '200px',
                                                                        },
                                                                    },
                                                                },
                                                            }}
                                                        >
                                                            {zone.map((option) => (
                                                                <MenuItem key={option.prof_zone_id} value={option.prof_zone_id}
                                                                    sx={{ fontSize: "14px" }}>
                                                                    {option.Name}
                                                                </MenuItem>
                                                            ))}
                                                        </TextField>
                                                    </Grid>

                                                    <Grid item xs={6}>
                                                        <TextField
                                                            id="pincode"
                                                            label="Pincode"
                                                            placeholder='Pincode'
                                                            name="pincode"
                                                            size="small"
                                                            fullWidth
                                                            value={pincode}
                                                            onChange={handlePincodeChange}
                                                            sx={{
                                                                textAlign: "left",
                                                                '& input': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                            error={Boolean(pincodeError)}
                                                            helperText={pincodeError}
                                                        />
                                                    </Grid>
                                                </Grid>
                                            </Grid>

                                            <Grid item lg={12} sm={12} xs={12}>
                                                <TextField
                                                    required
                                                    label="Address"
                                                    id="address"
                                                    name="address"
                                                    placeholder='House No,Building,Street,Area'
                                                    size="small"
                                                    fullWidth
                                                    value={address}
                                                    onChange={(e) => setAddress(e.target.value)}
                                                    error={!!errors.address}
                                                    helperText={errors.address}
                                                    sx={{
                                                        '& input': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                />
                                            </Grid>
                                        </>
                                    )}
                                </Grid>
                            </CardContent>
                        </Card>

                    </Grid>

                    {/* Service Details */}
                    <Grid item lg={3} md={3} xs={12} >
                        {/* <ServiceInfo /> */}
                        <Card sx={{ width: "100%", borderRadius: "10px", bgColor: "white", boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)' }}>
                            <CardContent>
                                <Typography align="center" style={{ fontSize: "16px", fontWeight: 600 }}>SERVICE DETAILS</Typography>
                                <Grid container spacing={2} sx={{ marginTop: "1px" }}>
                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            required
                                            id="srv_id"
                                            name="srv_id"
                                            select
                                            label="Select Service"
                                            defaultValue={selectedService}
                                            onChange={handleDropdownService}
                                            size="small"
                                            fullWidth
                                            error={!!errors.selectedService}
                                            helperText={errors.selectedService}
                                            sx={{
                                                textAlign: "left", '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '200px', // Adjust the height as needed
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {service.map((option) => (
                                                <MenuItem key={option.srv_id} value={option.srv_id}
                                                    sx={{ fontSize: "14px", }}>
                                                    {option.service_title}
                                                </MenuItem>
                                            ))}
                                        </TextField>
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            required
                                            id="sub_srv_id"
                                            name="sub_srv_id"
                                            select
                                            label="Select Sub Service"
                                            defaultValue={selectedSubService}
                                            onChange={handleSubServiceSelect}
                                            // onChange={handleDropdownSubService  }
                                            size="small"
                                            fullWidth
                                            multiple
                                            error={!!errors.selectedSubService}
                                            helperText={errors.selectedSubService}
                                            sx={{
                                                textAlign: "left", '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '200px', // Adjust the height as needed
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {subService.map((option) => (
                                                <MenuItem key={option.sub_srv_id} value={option.sub_srv_id}
                                                    sx={{ fontSize: "14px", }}>
                                                    {selectedService && (
                                                        <>
                                                            {option.recommomded_service}
                                                        </>
                                                    )}
                                                </MenuItem>
                                            ))}
                                        </TextField>
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            required
                                            id="start_date"
                                            name="start_date"
                                            label="Start Date and Time"
                                            type="datetime-local"
                                            value={startDate}
                                            onChange={handleStartDateChange}
                                            size="small"
                                            fullWidth
                                            error={!!errors.startDate}
                                            helperText={errors.startDate}
                                            sx={{
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            InputLabelProps={{
                                                shrink: true,
                                            }}
                                            inputProps={{
                                                min: getCurrentDateTimeString(), // Set min to current date and time
                                            }}
                                        />
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            required
                                            id="end_date"
                                            name="end_date"
                                            label="End Date and Time"
                                            type="datetime-local"
                                            value={endDate}
                                            onChange={handleEndDateChange}
                                            size="small"
                                            fullWidth
                                            sx={{
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            InputLabelProps={{
                                                shrink: true,
                                            }}
                                            error={endDateError !== '' || !!errors.endDate}
                                            helperText={endDateError || errors.endDate}
                                            inputProps={{
                                                min: getCurrentDateTimeString(), // Set min to current date and time
                                            }}
                                        />
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            id="prof_prefered"
                                            select
                                            name="prof_prefered"
                                            label="Preferred Professional"
                                            defaultValue={selectedProfGender}
                                            onChange={handleDropdownProfGender}
                                            size="small"
                                            fullWidth
                                            sx={{
                                                textAlign: "left", '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                            SelectProps={{
                                                MenuProps: {
                                                    PaperProps: {
                                                        style: {
                                                            maxHeight: '200px',
                                                            maxWidth: '200px',
                                                        },
                                                    },
                                                },
                                            }}
                                        >
                                            {profGender.map((option) => (
                                                <MenuItem key={option.gender_id} value={option.gender_id}
                                                    sx={{ fontSize: "14px", }}>
                                                    {option.name}
                                                </MenuItem>
                                            ))}
                                        </TextField>
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <TextField
                                            id="remark"
                                            name="remark"
                                            label="Remark"
                                            placeholder='write remark here'
                                            size="small"
                                            fullWidth
                                            value={remark}
                                            onChange={(e) => setRemark(e.target.value)}
                                            sx={{
                                                '& input': {
                                                    fontSize: '14px',
                                                },
                                            }}
                                        />
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        <Grid container spacing={1}>
                                            {/* <Grid xs={selectedDiscountId ? 6 : 12} sx={{ marginTop: 1, }}>
                                                <TextField
                                                    id="outlined-select-percentage"
                                                    name="discount_type"
                                                    select
                                                    label="Discount Type"
                                                    value={selectedDiscountId}
                                                    onChange={(e) => setSelectedDiscountId(e.target.value)}
                                                    size="small"
                                                    fullWidth
                                                    sx={{
                                                        textAlign: "left",
                                                        '& input': {
                                                            fontSize: '12px',
                                                        },
                                                    }}
                                                >
                                                    {discount.map((option) => (
                                                        <MenuItem key={option.discount_id} value={option.discount_id}>
                                                            {option.label}
                                                        </MenuItem>
                                                    ))}
                                                </TextField>
                                            </Grid> */}

                                            <Grid xs={selectedDiscountId === '3' ? 12 : 6} sx={{ marginTop: 1 }}>
                                                <TextField
                                                    id="outlined-select-percentage"
                                                    name="discount_type"
                                                    select
                                                    label="Discount Type"
                                                    value={selectedDiscountId}
                                                    onChange={(e) => setSelectedDiscountId(e.target.value)}
                                                    size="small"
                                                    fullWidth
                                                    sx={{
                                                        textAlign: "left",
                                                        '& input': {
                                                            fontSize: '12px',
                                                        },
                                                    }}
                                                >
                                                    {discount.map((option) => (
                                                        <MenuItem key={option.discount_id} value={option.discount_id}>
                                                            {option.label}
                                                        </MenuItem>
                                                    ))}
                                                </TextField>
                                            </Grid>

                                            <Grid item xs={6}>
                                                {selectedDiscountId === '1' && (
                                                    <TextField
                                                        id="discount-percentage"
                                                        name="discount_value"
                                                        label="%"
                                                        type="number"
                                                        size="small"
                                                        fullWidth
                                                        value={discountValue}
                                                        onChange={(e) => setDiscountValue(e.target.value)}
                                                        sx={{
                                                            textAlign: "left",
                                                            '& input': {
                                                                fontSize: '16px',
                                                            },
                                                        }}
                                                    />
                                                )}

                                                {selectedDiscountId === '2' && (
                                                    <TextField
                                                        id="discount-currency"
                                                        name="discount_value"
                                                        label="₹"
                                                        size="small"
                                                        type="number"
                                                        fullWidth
                                                        value={discountValue}
                                                        onChange={(e) => setDiscountValue(e.target.value)}
                                                        sx={{
                                                            textAlign: "left",
                                                            '& input': {
                                                                fontSize: '16px',
                                                            },
                                                        }}
                                                    />
                                                )}
                                            </Grid>
                                        </Grid>
                                        {/* <TextField
                                            id="outlined-select-coupon"
                                            select
                                            label="Select Coupon"
                                            value={selectedCoupon}
                                            onChange={handleCouponSelect}
                                            size="small"
                                            fullWidth
                                            sx={{
                                                textAlign: "left",
                                                '& input': {
                                                    fontSize: '12px',
                                                },
                                            }}
                                        >
                                            {coupon.map((option) => (
                                                <MenuItem key={option.coupon_id} value={option.coupon_id}>
                                                    {option.coupon_code}
                                                </MenuItem>
                                            ))}
                                        </TextField> */}
                                    </Grid>

                                    <Grid item lg={12} sm={12} xs={12}>
                                        {/* <TextField
                                        id="outlined-select-amount"
                                        placeholder='Amount'
                                        // value={calculatedAmount}
                                        // value={selectedDiscountId ? totalDiscount : calculatedAmount}
                                        value={totalDiscount ? totalDiscount : calculatedAmount}
                                        size="small"
                                        fullWidth
                                        disabled
                                        sx={{
                                            '& input': {
                                                // fontSize: '12px', 
                                                bgcolor: "#CBE3FF",
                                                color: "black"

                                            },
                                        }}
                                    /> */}
                                        <Box
                                            component="form"
                                            sx={{ p: "2px 4px", display: 'flex', alignItems: 'center', height: '2.5rem', backgroundColor: "#CBE3FF", boxShadow: "4px 4px 10px 7px rgba(135, 135, 135, 0.05)", borderRadius: "10px", }}
                                        >
                                            <Typography sx={{ pl: 2 }}>
                                                Amount:
                                            </Typography>
                                            <InputBase
                                                sx={{ ml: 10, flex: 1, }}
                                                placeholder=""
                                                inputProps={{ 'aria-label': 'Amount' }}
                                                // name="final_amount"
                                                name={totalDiscount ? "final_amount" : "Total_cost"}
                                                value={totalDiscount ? `₹${totalDiscount}` : `₹${calculatedAmount}`}
                                            // value={selectedCoupon ? totalDiscount : calculatedAmount}
                                            />
                                        </Box>
                                    </Grid>

                                </Grid>

                                {/* </Grid> */}
                                {/* </Grid> */}
                            </CardContent>
                        </Card>

                    </Grid>

                </Grid>
                <Grid>
                    {selectedCall !== 2 && (
                        <Button variant="contained" sx={{ marginTop: "6px", width: '30ch', backgroundColor: '#69A5EB', borderRadius: "12px", textTransform: "capitalize", }} type="submit" onClick={(event) => handleSubmit(event, "CreateService")}>Create Service</Button>
                    )}
                    {selectedCall === 2 && (
                        <Button variant="contained" sx={{ marginTop: "6px", width: '30ch', backgroundColor: '#69A5EB', borderRadius: "12px", textTransform: "capitalize", }} type="submit" onClick={(event) => handleSubmit(event, "Enquiry")}>Save Enquiry</Button>
                    )}
                    <Snackbar
                        open={openSnackbar}
                        autoHideDuration={6000}
                        onClose={handleSnackbarClose}
                    >
                        <Alert
                            onClose={handleSnackbarClose}
                            severity="success"
                            sx={{ width: '100%', }}
                        >
                            {snackbarMessage}
                        </Alert>
                    </Snackbar>
                </Grid>
            </Box>
            <Footer />
        </>
    )
}
export default Addservice

