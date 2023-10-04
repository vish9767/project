import React, { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Typography from "@mui/material/Typography";
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import { CardContent } from '@mui/material';

const ManageProfile = () => {
  return (
    <Box>
      <Grid item xs={12} container spacing={1}>
        <Grid item lg={6} md={6} xs={12}>
          <Card
            sx={{ width: "100%", borderRadius: "10px", bgColor: "white", boxShadow: '4px 4px 10px 7px rgba(135, 135, 135, 0.05)' }}
          >
            <CardContent>
              <Typography align="left" style={{ fontSize: "16px", fontWeight: 600, }}>PROFESSIONAL DETAILS</Typography>
              <Grid container spacing={2} sx={{ marginTop: "1px" }}>
                <Grid item lg={4} sm={6} xs={12}>
                  <TextField
                    required
                    select
                    id="role"
                    label="Role"
                    placeholder="Professional/Vendor"
                    size="small"
                    fullWidth
                    sx={{
                      '& input': {
                        fontSize: '14px',
                      },
                    }}

                  />
                </Grid>
                <Grid item lg={3} sm={6} xs={12}>
                  <TextField
                    required
                    select
                    id="title"
                    label="Title"
                    placeholder="Dr/Mr/Mrs"
                    size="small"
                    fullWidth
                    sx={{
                      '& input': {
                        fontSize: '14px',
                      },
                    }}

                  />
                </Grid>

                <Grid item lg={5} md={6} xs={12}>
                  <TextField
                    required
                    id="name"
                    label="First Name"
                    // defaultValue={selectedRelation}
                    // value={selectedRelation}
                    // onChange={handleDropdownRelation}
                    size="small"
                    fullWidth
                    sx={{
                      textAlign: "left", '& input': {
                        fontSize: '14px',
                      },
                    }}
                  >
                    {/* {relation.map((option) => (
                                <MenuItem key={option.caller_rel_id} value={option.caller_rel_id}>
                                    {option.relation}
                                </MenuItem>
                            ))} */}
                  </TextField>
                </Grid>
                <Grid item lg={5} sm={6} xs={12}>
                  <TextField
                    required
                    id="name"
                    label="Last Name"
                    // defaultValue={selectedRelation}
                    // value={selectedRelation}
                    // onChange={handleDropdownRelation}
                    size="small"
                    fullWidth
                    sx={{
                      textAlign: "left", '& input': {
                        fontSize: '14px',
                      },
                    }}
                  >
                  </TextField>
                </Grid>
                <Grid item lg={3} sm={6} xs={12}>
                  <TextField
                    required
                    id="gender"
                    select
                    label="Gender"
                    // defaultValue={selectedRelation}
                    // value={selectedRelation}
                    // onChange={handleDropdownRelation}
                    size="small"
                    fullWidth
                    sx={{
                      textAlign: "left", '& input': {
                        fontSize: '14px',
                      },
                    }}
                  >
                    {/* {relation.map((option) => (
                                <MenuItem key={option.caller_rel_id} value={option.caller_rel_id}>
                                    {option.relation}
                                </MenuItem>
                            ))} */}
                  </TextField>
                </Grid>
                <Grid item lg={4} sm={6} xs={12}>
                  <TextField
                    required
                    id="dob"
                    label="DOB"
                    type="date"
                    // defaultValue={selectedRelation}
                    // value={selectedRelation}
                    // onChange={handleDropdownRelation}
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
                  >
                    {/* {relation.map((option) => (
                                <MenuItem key={option.caller_rel_id} value={option.caller_rel_id}>
                                    {option.relation}
                                </MenuItem>
                            ))} */}
                  </TextField>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>

        <Grid item lg={6} md={6} xs={12}>
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
                <Typography align="left" style={{ fontSize: "16px", fontWeight: 600 }}>EDUCATIONAL DETAILS  </Typography>
              </Grid>

              <Grid container spacing={2} sx={{ marginTop: "1px" }} >

                <Grid item lg={6} sm={6} xs={12}>
                  <TextField
                    id="outlined-patient-name"
                    label="Patient Name"
                    placeholder="First Name | Last Name *"
                    size="small"
                    fullWidth
                    sx={{
                      textAlign: "left", '& input': {
                        fontSize: '14px',
                      },
                    }}
                  />
                </Grid>

                <Grid item lg={6} sm={6} xs={12}>
                  <Grid container spacing={1}>
                    <Grid item xs={5}>
                      <TextField
                        id="name"
                        select
                        label="Gender"
                        // defaultValue={selectedGender}
                        name="name"
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left",
                          '& input': {
                            fontSize: '14px',
                          },
                        }}
                      // onChange={handleDropdownGender}
                      >
                        {/* {gender.map((option) => (
                                                <MenuItem key={option.gender_id} value={option.gender_id}>
                                                    {option.name}
                                                </MenuItem>
                                            ))} */}
                      </TextField>
                    </Grid>
                    <Grid item xs={7}>
                      <TextField
                        label="Suffered From"
                        id="outlined-size-small"
                        placeholder='Remark'
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
                    select
                    placeholder='Name'
                    size="small"
                    fullWidth
                    sx={{
                      textAlign: "left", '& input': {
                        fontSize: '14px',
                      },
                    }}
                  >
                    {/* {referHospital.map((option) => (
                                        <MenuItem key={option.hosp_id} value={option.hosp_id}>
                                            {option.hospital_name}
                                        </MenuItem>
                                    ))} */}
                  </TextField>
                </Grid>
                <Grid item lg={6} sm={6} xs={12}>
                  <Grid container spacing={1}>
                    <Grid item xs={8}>
                      <TextField
                        label="DOB"
                        id="outlined-size-small"
                        type="date"
                        defaultValue="DD/MM/YYYY"
                        size="small"
                        fullWidth
                        sx={{
                          '& input': {
                            fontSize: '14px',
                          },
                        }}
                        // onChange={handleDOB}
                        InputLabelProps={{
                          shrink: true,
                        }}
                      />
                    </Grid>
                    <Grid item xs={4}>
                      <TextField
                        label="Age"
                        id="outlined-size-small"
                        // value={age}
                        // value={changeAge}
                        // onChange={handleAgeChange}
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
                    label="Contact"
                    id="ptnNumber"
                    placeholder='+91 |'
                    // defaultValue="+91 | "
                    size="small"
                    fullWidth
                    // value={ptnNumber}
                    // onChange={handlePtnNumberChange}
                    // onInput={handlePtnInput}
                    // error={!!ptnNumberError}
                    // helperText={ptnNumberError}
                    inputProps={{
                      minLength: 10,
                      maxLength: 10, // Maximum length of the mobile number

                    }}
                    sx={{
                      '& input': {
                        fontSize: '14px', // Replace with your desired font size
                      },
                    }}
                  // InputProps={{ sx: { height: 36 } }}
                  />
                </Grid>
                <Grid item lg={6} sm={6} xs={12}>
                  <TextField
                    label="Email"
                    id="email"
                    placeholder='example@gmail.com'
                    // value={email}
                    // onChange={handleEmailChange}
                    // error={!!emailError}
                    // helperText={emailError}
                    size="small"
                    fullWidth
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
                        label="Referred Hospital"
                        id="hospital"
                        select
                        // defaultValue={selectedLocality}
                        // onChange={handleDropdownLocality}
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left", '& input': {
                            fontSize: '14px',
                          },
                        }}
                      >
                        {/* {locality.map((option) => (
                                                <MenuItem key={option.loc_id} value={option.loc_id}>
                                                    {option.location}
                                                </MenuItem>
                                            ))} */}
                      </TextField>
                    </Grid>
                    <Grid item xs={6}>
                      <TextField
                        label="Address Type"
                        id="address"
                        select
                        // defaultValue={selectedLocality}
                        // onChange={handleDropdownLocality}
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left", '& input': {
                            fontSize: '14px',
                          },
                        }}

                      >
                        {/* {locality.map((option) => (
                                                <MenuItem key={option.loc_id} value={option.loc_id}>
                                                    {option.location}
                                                </MenuItem>
                                            ))} */}
                      </TextField>
                    </Grid>
                  </Grid>
                </Grid>


                <Grid item lg={6} sm={6} xs={12}>
                  <TextField
                    label="Address"
                    id="outlined-size-small"
                    placeholder='House No,Building,Street,Area'
                    // defaultValue="Lane,Area,Street"
                    size="small"
                    fullWidth
                    sx={{
                      '& input': {
                        fontSize: '14px', // Replace with your desired font size
                      },
                    }}
                  // InputProps={{ sx: { height: 36 } }}
                  />
                </Grid>

                <Grid item lg={6} sm={6} xs={12}>
                  <Grid container spacing={1}>
                    <Grid item xs={6}>
                      <TextField
                        label="Select Zone"
                        id="location"
                        select
                        // defaultValue={selectedLocality}
                        // onChange={handleDropdownLocality}
                        // placeholder='Locality'
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left", '& input': {
                            fontSize: '14px', // Replace with your desired font size
                          },
                        }}
                      // InputProps={{ sx: { height: 36 } }}
                      >
                        {/* {locality.map((option) => (
                                                <MenuItem key={option.loc_id} value={option.loc_id}>
                                                    {option.location}
                                                </MenuItem>
                                            ))} */}
                      </TextField>
                    </Grid>

                    <Grid item xs={6}>
                      <TextField
                        label="Select City"
                        id="city"
                        select
                        // defaultValue={selectedLocality}
                        // onChange={handleDropdownLocality}
                        // placeholder='Locality'
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left", '& input': {
                            fontSize: '14px',
                          },
                        }}
                      >
                        {/* {locality.map((option) => (
                                                <MenuItem key={option.loc_id} value={option.loc_id}>
                                                    {option.location}
                                                </MenuItem>
                                            ))} */}
                      </TextField>
                    </Grid>
                  </Grid>
                </Grid>

                <Grid item lg={6} sm={6} xs={12}>
                  <Grid container spacing={1}>
                    <Grid item xs={6}>
                      <TextField
                        id="pincode"
                        label="Pincode"
                        placeholder='Pincode'
                        name="pincode"
                        size="small"
                        fullWidth
                        sx={{
                          textAlign: "left",
                          '& input': {
                            fontSize: '14px',
                          },
                        }}
                      // onChange={handleDropdownGender}
                      />

                    </Grid>
                    <Grid item xs={6}>
                      <TextField
                        label="State"
                        id="outlined-size-small"
                        select
                        placeholder='State'
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
                {/* <Grid item lg={12} sm={12} xs={12}>
                        <Button variant="contained" sx={{ m: 1, width: '30ch', backgroundColor: '#7AB8EE', borderRadius: "12px", textTransform: "capitalize", }} type="submit">Submit</Button>
                    </Grid> */}
              </Grid>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box >
  )
}

export default ManageProfile
