import React, { useState } from "react";
import "./rawdata.css";

function RawData(props) {
  const [state, setState] = useState({
    cname: "",
    website: "",
    company: "",
    email: "",
    mobile: "",
    lid: "",
    street: "",
    city: "",
    state: "",
    pincode: "",
    country: "",
    nameError: "",
    emailError: "",
    websiteError: "",
    companyError: "",
    mobileError: "",
    linkedinError: "",
    streetError: "",
    cityError: "",
    countryError: "",
    pincodeError: "",
    stateError: "",
    // lcpnError:'',
    // lcdError:'',
    // lcpn:'',
    // lcd:'',
    // lmn:'',
    // lemail:'',
    // lmobileError:'',
    // lemailError:'',
    // lcw:'',
    // lwebsiteError:'',
    // logid:'',
    // logidError:'',
    cid: "",
    cidError: "",
  });

  const change = (e) => {
    props.onChange({ [e.target.name]: e.target.value });
    setState({
      ...state,
      [e.target.name]: e.target.value,
    });
  };

  const validate = () => {
    let nameError = "";
    let emailError = "";
    let websiteError = "";
    let companyError = "";
    let mobileError = "";
    let linkedinError = "";
    let streetError = "";
    let cityError = "";
    let countryError = "";
    let pincodeError = "";
    let stateError = "";
    // let lcpnError = "";
    // let lcdError = "";
    // let lemailError = "";
    // let lmobileError = "";
    // let lwebsiteError = "";
    // let logidError = "";
    let cidError = "";

    if (!state.cid) {
      cidError = "Customer ID cannot be blank";
    }

    if (!state.cname) {
      nameError = "Lead Owner cannot be blank";
    } else if (state.cname.length > 30) {
      nameError = "Name cant be greater than 30 letters ";
    }

    if (!state.website) {
      websiteError = "Website cannot be blank";
    }

    // if (!state.lcw) {
    //   lwebsiteError = "LinkedIN Contact Website cannot be blank";
    // }

    if (!state.email.includes("@")) {
      emailError = "Invalid email";
    }

    // if (!state.lemail.includes("@")) {
    //   lemailError = "Invalid LinkedIn Contact email";
    // }

    if (!state.company) {
      companyError = "Company Name cannot be blank";
    } else if (state.company.length > 50) {
      companyError = "Company Name cant be greater than 50 letters ";
    }

    if (!state.mobile) {
      mobileError = "Mobile Number cannot be blank";
    }

    if (!state.mobile.match(/^[0-9]{10}$/)) {
      mobileError = "Please Enter Valid Mobile Number";
    }

    // if (!state.lmn) {
    //   lmobileError = "LinkedIn Contact Mobile Number cannot be blank";
    // }

    if (!state.lid) {
      linkedinError = "Linkedin ID cannot be blank";
    }

    // if (!state.logid) {
    //   logidError = "Log ID cannot be blank";
    // }

    // if (!state.lcpn) {
    //   lcpnError = "LinkedIn Contact Person Name cannot be blank";
    // }

    // else if ((state.lcpn).length > 30) {
    //   lcpnError = "LinkedIn Contact Person Name cant be greater than 30 letters "
    // }

    // if (!state.lcpn) {
    //   lcdError = "LinkedIn Contact Designation cannot be blank";
    // }

    // else if ((state.lcpn).length > 30) {
    //   lcdError = "LinkedIn Contact Designation cant be greater than 30 letters "
    // }

    if (!state.street) {
      streetError = "Street cannot be blank";
    } else if (state.street.length > 30) {
      streetError = "Street Name cant be greater than 30 letters ";
    }

    if (!state.city) {
      cityError = "City cannot be blank";
    } else if (state.city.length > 20) {
      cityError = "City Name cant be greater than 20 letters ";
    }

    if (!state.state) {
      stateError = "State cannot be blank";
    } else if (state.state.length > 20) {
      stateError = "State Name cant be greater than 20 letters ";
    }

    if (!state.pincode) {
      pincodeError = "Pincode cannot be blank";
    }

    if (!state.country) {
      countryError = "Country cannot be blank";
    }

    if (
      emailError ||
      nameError ||
      websiteError ||
      companyError ||
      mobileError ||
      linkedinError ||
      streetError ||
      cityError ||
      stateError ||
      pincodeError ||
      countryError ||
      cidError
    ) {
      // lcpnError || lcdError || lemailError || lmobileError ||
      // lwebsiteError || logidError
      setState({
        ...state,
        emailError,
        nameError,
        websiteError,
        companyError,
        mobileError,
        linkedinError,
        streetError,
        cityError,
        stateError,
        cidError,
        pincodeError,
        countryError,
        // lcpnError, lcdError, lemailError,
        // lmobileError, lwebsiteError, logidError
      });
      return false;
    }

    return true;
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const isValid = validate();
    if (isValid) {
      console.log(state);
      // clear form
      setState(state);
    }
  };

  return (
    <div id="main-registration-container ">
      <div className="centered" />

      <div id="reg">
        <div className="container1">
          <h1>Raw Data</h1>
          <form onSubmit={handleSubmit} className="rawform">
            <h3>Contact Information</h3>
            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Customer ID"
                  name="cid"
                  id="cid"
                  value={state.cid}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.cidError}
                </div>
                <label for="cname"> Customer ID </label>
              </div>

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Customer's Name"
                  name="cname"
                  id="cname"
                  value={state.cname}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.nameError}
                </div>
                <label for="cname"> Customer Name </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="email"
                  placeholder="Enter Customer Email ID"
                  name="email"
                  id="email"
                  value={state.email}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.emailError}
                </div>
                <label for="email"> Customer Email ID </label>
              </div>

              <div className="box">
                <input
                  type="number"
                  placeholder="Enter Customer Mobile Number"
                  name="mobile"
                  id="mobile"
                  value={state.mobile}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.mobileError}
                </div>
                <label for="mobile"> Customer Mobile Number </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Customer Website URL"
                  name="website"
                  id="website"
                  value={state.website}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.websiteError}
                </div>
                <label for="website"> Customer Website </label>
              </div>

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter LinkedIn ID"
                  name="lid"
                  id="lid"
                  value={state.lid}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.linkedinError}
                </div>
                <label for="lid"> LinkedIn ID </label>
              </div>
            </div>

            {/* <div className='wrapper'>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Company Name" name="company" id="company"
                    value={state.company}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.companyError}
                  </div>
                  <label for="company"> LinkedIn Company Name </label>
                </div>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Contact Person Name" name="lcpn" id="lcpn"
                    value={state.lcpn}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.lcpnError}
                  </div>
                  <label for="lid"> LinkedIn Contact Person Name </label>
                </div>

              </div>

              <div className='wrapper'>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Contact Designation" name="lcd" id="lcd"
                    value={state.lcd}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.lcdError}
                  </div>
                  <label for="company"> LinkedIn Contact Designation </label>
                </div>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Contact Email ID" name="lemail" id="lemail"
                    value={state.lemail}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.lemailError}
                  </div>
                  <label for="lid"> LinkedIn Contact Email ID </label>
                </div>

              </div>


              <div className='wrapper'>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Contact Mobile Number" name="lmn" id="lmn"
                    value={state.lmn}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.lmobileError}
                  </div>
                  <label for="company"> LinkedIn Contact Mobile Number </label>
                </div>

                <div className='box'>
                  <input type="text" placeholder="Enter LinkedIn Contact Website" name="lcw" id="lcw"
                    value={state.lcw}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.lwebsiteError}
                  </div>
                  <label for="lid"> LinkedIn Contact Website </label>
                </div>

              </div>

              <div className='wrapper'>

                <div className='box'>
                  <input type="text" placeholder="Enter Log ID" name="logid" id="logid"
                    value={state.logid}
                    onChange={e => change(e)}
                  ></input>
                  <div style={{ fontSize: 12, color: "red" }}>
                    {state.logidError}
                  </div>
                  <label for="company"> Log ID  </label>
                </div>


                <div className='box'>
                  <input type="date" id="dateupdate" name="dateupdate" required></input>
                  <label> Log Date Update </label>
                </div>
              </div>


              <div className='wrapper'>

                <div className='box'>
                  <input type="date" id="dateupdate" name="dateupdate" required></input>
                  <label> Log Updated By </label>
                </div>

              </div> */}

            <h3> Customer's Address Information </h3>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Street Name"
                  name="street"
                  id="street"
                  value={state.street}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.streetError}
                </div>
                <label for="street"> Street </label>
              </div>

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter City Name"
                  name="city"
                  id="city"
                  value={state.city}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.cityError}
                </div>
                <label for="city"> City </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter State Name"
                  name="state"
                  id="state"
                  value={state.state}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.stateError}
                </div>
                <label for="state"> State </label>
              </div>

              <div className="box">
                <input
                  type="number"
                  placeholder="Enter Pincode"
                  name="pincode"
                  id="pincode"
                  value={state.pincode}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.pincodeError}
                </div>
                <label for="pincode"> Pincode </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Country's Name"
                  name="country"
                  id="country"
                  value={state.country}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.countryError}
                </div>
                <label for="country"> Country </label>
              </div>
            </div>

            <h3> Description Information </h3>
            <div className="wrapper1">
              <div className="box">
                <textarea id="mes"></textarea>
                <label for="mes"> Customer Description </label>
              </div>
            </div>

            <div className="wrapper1">
              <div className="box">
                <textarea id="mes"></textarea>
                <label for="mes"> Customer Requirements </label>
              </div>
            </div>

            {/* <div className='wrapper1'>

                <div className='box'>
                  <textarea id="mes" ></textarea>
                  <label for="mes"> LinkedIn Company Description</label>
                </div>
              </div>

              <div className='wrapper1'>

                <div className='box'>
                  <textarea id="mes" ></textarea>
                  <label for="mes"> LinkedIn Requirements </label>
                </div>
              </div> */}

            <div className="wrapper2">
              <center>
                <input type="submit" name="" value="Submit"></input>
                <input type="submit" name="" value="Cancel"></input>
              </center>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default RawData;
