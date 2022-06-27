import React, { useState } from "react";
import "./rawdata.css";
import { lookup } from "../../utils";

function RawData(props) {
  // defining state
  // useState Hook allows us to track state in a function component. 
  const [state, setState] = useState({
    name: "",
    website: "",
    company: "",
    email: "",
    phone: "",
    linkedin_url: "",
    // street: "",
    // city: "",
    // state: "",
    // pincode: "",
    // country: "",
    address: "",
    nameError: "",
    emailError: "",
    websiteError: "",
    companyError: "",
    phoneError: "",
    linkedinError: "",
    addressError: "",
    // streetError: "",
    // cityError: "",
    // countryError: "",
    // pincodeError: "",
    // stateError: "",
    // cid: "",
    // cidError: "",
    description: "",
    descriptionError: "",
    requirement: "",
    requirementError: "",
    designation: "",
    designationError: "",
  });

  // required to change the target value
  const change = (e) => {
    props.onChange({ [e.target.name]: e.target.value });
    setState({
      ...state,
      [e.target.name]: e.target.value,
    });
  };

  // validation initiation
  const validate = () => {
    let nameError = "";
    let emailError = "";
    let websiteError = "";
    let companyError = "";
    let phoneError = "";
    let linkedinError = "";
    // let streetError = "";
    // let cityError = "";
    // let countryError = "";
    // let pincodeError = "";
    // let stateError = "";
    // let cidError = "";
    let addressError = "";
    let descriptionError = "";
    let requirementError = "";
    let designationError = "";

    // if (!state.cid) {
    //   cidError = "Customer ID cannot be blank";
    // }

//error validation  logic
    if (!state.name) {
      nameError = "Lead Owner cannot be blank";
    } else if (state.name.length > 30) {
      nameError = "Name cant be greater than 30 letters ";
    }

    if (!state.website) {
      websiteError = "Website cannot be blank";
    }

    if (!state.email.includes("@")) {
      emailError = "Invalid email";
    }

    if (!state.company) {
      companyError = "Company Name cannot be blank";
    } else if (state.company.length > 50) {
      companyError = "Company Name cant be greater than 50 letters ";
    }

    if (!state.phone) {
      phoneError = "phone Number cannot be blank";
    }

    if (!state.phone.match(/^[0-9]{10}$/)) {
      phoneError = "Please Enter Valid phone Number";
    }

    if (!state.linkedin_url) {
      linkedinError = "Linkedin ID cannot be blank";
    }

    if (!state.address) {
      addressError = "Street cannot be blank";
    } else if (state.address.length > 30) {
      addressError = "Street Name cant be greater than 30 letters ";
    }

    if (!state.address) {
      addressError = "City cannot be blank";
    } else if (state.address.length > 20) {
      addressError = "City Name cant be greater than 20 letters ";
    }

    if (!state.address) {
      addressError = "State cannot be blank";
    } else if (state.address.length > 20) {
      addressError = "State Name cant be greater than 20 letters ";
    }

    if (!state.address) {
      addressError = "Pincode cannot be blank";
    }

    if (!state.address) {
      addressError = "Country cannot be blank";
    }

    if (!state.description) {
      descriptionError = "Description cannot be blank";
    }

    if (!state.requirement) {
      requirementError = "Requiremnts cannot be blank";
    }

    if (!state.designation) {
      designationError = "Designation cannot be blank";
    }

    if (
      emailError ||
      nameError ||
      websiteError ||
      phoneError ||
      linkedinError ||
      addressError ||
      // cityError ||
      // stateError ||
      descriptionError ||
      // pincodeError ||
      // countryError ||
      requirementError ||
      designationError
    ) {
      setState({
        ...state,
        emailError,
        nameError,
        websiteError,
        companyError,
        phoneError,
        linkedinError,
        addressError,
        // cityError,
        // stateError,
        // pincodeError,
        // countryError,
        descriptionError,
        designationError,
        requirementError,
      });
      return false;
    }

    return true;
  };

  //This function will receive the form data if form validation is successful.
  const handleSubmit = (event) => {
    event.preventDefault();
    const isValid = validate();
    if (isValid) {
      console.log(state);
      // clear form
      setState(state);
      lookup("POST", "/customer/create/customer/", "", state).then(
        ({ data, status }) => {
          if (status === 200) {
            console.log(data);
            // props.history("/");
          }
        }
      );
    }
  };

  return (
    <div id="main-registration-container ">
      <div className="centered" />

      <div id="reg">
        <div className="container1">
          <h1>Customer Information</h1>
          <form onSubmit={handleSubmit} className="rawform">
            <h3>Contact Information</h3>
            <div className="wrapper">
              {/* <div className="box">
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
                <label htmlFor="name"> Customer ID </label>
              </div> */}

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Customer's Name"
                  name="name"
                  id="name"
                  value={state.name}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.nameError}
                </div>
                <label htmlFor="name"> Customer Name </label>
              </div>

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
                <label htmlFor="email"> Customer Email ID </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="number"
                  placeholder="Enter Customer phone Number"
                  name="phone"
                  id="phone"
                  value={state.phone}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.phoneError}
                </div>
                <label htmlFor="phone"> Customer phone Number </label>
              </div>

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Customer Website"
                  name="website"
                  id="website"
                  value={state.website}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.websiteError}
                </div>
                <label htmlFor="website"> Customer Website </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter LinkedIn URL"
                  name="linkedin_url"
                  id="linkedin_url"
                  value={state.linkedin_url}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.linkedinError}
                </div>
                <label htmlFor="linkedin_url"> LinkedIn ID </label>
              </div>

              <div className="box">
                <input
                  type="text"
                  placeholder="Enter LinkedIn Company Name"
                  name="company"
                  id="company"
                  value={state.company}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.companyError}
                </div>
                <label htmlFor="company"> LinkedIn Company Name </label>
              </div>
            </div>

            <div className="wrapper">
              <div className="box">
                <input
                  type="text"
                  placeholder="Enter Designation"
                  name="designation"
                  id="designation"
                  value={state.designation}
                  onChange={(e) => change(e)}
                ></input>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.designationError}
                </div>
                <label htmlFor="designation"> Designation</label>
              </div>
            </div>

            <h3> Description Information </h3>
            <div className="wrapper1">
              <div className="box">
                <textarea
                  id="description"
                  value={state.description}
                  onChange={(e) => change(e)}
                  name="description"
                ></textarea>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.descriptionError}
                </div>
                <label htmlFor="description"> Customer Description </label>
              </div>
            </div>

            <div className="wrapper1">
              <div className="box">
                <textarea
                  id="requirement"
                  value={state.requirement}
                  name="requirement"
                  onChange={(e) => change(e)}
                ></textarea>
                <div style={{ fontSize: 12, color: "red" }}>
                  {state.requirementError}
                </div>
                <label htmlFor="requirement"> Customer Requirements </label>
              </div>
            </div>

            <div className="wrapper2">
              <center>
                <input className="btnreg" type="submit" name="" value="Submit"></input>
                <input className="btnreg"type="submit" name="" value="Cancel"></input>
              </center>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default RawData;
