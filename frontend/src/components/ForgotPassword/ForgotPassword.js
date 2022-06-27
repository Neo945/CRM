//importing libraries

import React from "react";
import "./ForgotPassword.css";
import { Link } from "react-router-dom";

class ForgotPassword extends React.Component {
  constructor() {
    super();
    this.state = {
      fields: {},
      errors: {},
    };

    this.handleChange = this.handleChange.bind(this);
    this.submituserRegistrationForm =
      this.submituserRegistrationForm.bind(this);
  }

  handleChange(e) {
    let fields = this.state.fields;
    fields[e.target.name] = e.target.value;
    this.setState({
      fields,
    });
  }

  submituserRegistrationForm(e) {
    e.preventDefault();
    if (this.validateForm()) {
      let fields = {};
      fields["emailid"] = "";
      fields["password"] = "";
      this.setState({ fields: fields });
      alert("Form submitted");
    }
  }

  // validation Form

  validateForm() {
    let fields = this.state.fields;
    let errors = {};
    let formIsValid = true;


    if (!fields["emailid"]) {
      formIsValid = false;
      errors["emailid"] = "*Please enter your email-ID.";
    }

    if (typeof fields["emailid"] !== "undefined") {
      var pattern = new RegExp(
        /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i
      );
      if (!pattern.test(fields["emailid"])) {
        formIsValid = false;
        errors["emailid"] = "*Please enter valid email-ID.";
      }
    }

    if (!fields["password"]) {
      formIsValid = false;
      errors["password"] = "*Please enter your password.";
    }

    if (typeof fields["password"] !== "undefined") {
      if (
        !fields["password"].match(
          /^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&]).*$/
        )
      ) {
        formIsValid = false;
        errors["password"] = "*Please enter secure and strong password.";
      }
    }

    this.setState({
      errors: errors,
    });
    return formIsValid;
  }

  render() {
    

    return (
      
      <div id="main-registration-container ">
        <div id="" className="split3 left3">
          <div className="centered" />
          <h3>Forgot Password page</h3>
          <form className="fpform"
            method="post"
            name="userRegistrationForm"
            onSubmit={this.submituserRegistrationForm}
          >
            <label>Registered Email ID</label>
            <input id="fpemail"
              type="text"
              placeholder="Enter Registered Email"
              
              name="emailid"
              value={this.state.fields.emailid}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.emailid}</div>
            <label>Enter New Password</label>
            <input id="fpnewpass"
              type="password"
              placeholder="Enter New Password"
              name="password"
              value={this.state.fields.password}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.password}</div>

            <label>Re-enter New Password</label>
            <input id="fppass"
              type="password"
              placeholder="Confirm New Password"
              name="newpassword"
              value={this.state.fields.password}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.password}</div>

            <center>
              <input type="submit" className="buttonfp" value="Register" />
            </center>
{/* 
Links for navigation of login and sign up page */}
            
            <a href="/register">
              <center>No Account? Sign Up</center>
            </a>
            <Link to="/login"> Already a user? Sign-in </Link>
          </form>
        </div>

        <div className="split3 right3">
          <div className="centered">
           
          </div>
        </div>
      </div>
    );
  }
}

export default ForgotPassword;
