import React, { useState } from "react";
import "./Register.css";
import { Link } from "react-router-dom";
import { lookup } from "../../utils";
function RegisterForm(props) {
  const [state, setState] = useState({
    fields: {
      username: "",
      email: "",
      mobileno: "",
      password1: "",
      password2: "",
    },
    errors: {
      username: "",
      email: "",
      mobileno: "",
      password1: "",
      password2: "",
    },
  });

  function handleChange(e) {
    let fields = state.fields;
    fields[e.target.name] = e.target.value;
    setState({
      ...state,
      fields,
    });
  }
  function initState() {
    let fields = {};
    fields.username = "";
    fields.email = "";
    fields.mobileno = "";
    fields.password1 = "";
    fields.password2 = "";
    setState({ ...state, fields: fields });
  }

  function submituserRegistrationForm(e) {
    e.preventDefault();
    if (validateForm()) {
      // Fetch API call here using state.fields
      lookup("POST", "/accounts/register/", "", state.fields).then(
        ({ data, status }) => {
          if (status === 200) {
            console.log(data);
            // props.history("/");
          }
        }
      );
      initState();
    }
  }

  function validateForm() {
    let fields = state.fields;
    let errors = {};
    let formIsValid = true;

    if (fields.username.length === 0) {
      formIsValid = false;
      errors.username = "*Please enter your username.";
    }

    if (fields.username.length !== 0) {
      if (!fields.username.match(/^[a-zA-Z ]*$/)) {
        formIsValid = false;
        errors.username = "*Please enter alphabet characters only.";
      }
    }

    if (fields.email.length === 0) {
      formIsValid = false;
      errors.email = "*Please enter your email-ID.";
    }

    if (fields.email.length !== 0) {
      //regular expression for email validation
      var pattern = new RegExp(
        /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i
      );
      if (!pattern.test(fields.email)) {
        formIsValid = false;
        errors.email = "*Please enter valid email-ID.";
      }
    }

    if (fields.mobileno.length === 0) {
      formIsValid = false;
      errors.mobileno = "*Please enter your mobile no.";
    }

    if (fields.mobileno !== 0) {
      if (!fields["mobileno"].match(/^[0-9]{10}$/)) {
        formIsValid = false;
        errors.mobileno = "*Please enter valid mobile no.";
      }
    }

    if (fields.password1.length === 0) {
      formIsValid = false;
      errors.password1 = "*Please enter your password.";
    }

    if (fields.password1.length !== 0) {
      if (
        !fields["password1"].match(
          /^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&]).*$/
        )
      ) {
        formIsValid = false;
        errors.password1 = "*Please enter secure and strong password.";
      }
    }

    if (fields.password2.length === 0) {
      formIsValid = false;
      errors.password2 = "*Please enter your password.";
    }

    if (fields.password2 !== 0) {
      if (fields.password1 !== fields.password2) {
        formIsValid = false;
        errors.password2 = "*Password doesnot match.";
      }
    }

    setState({
      ...state,
      errors: errors,
    });
    return formIsValid;
  }

  return (
    <div id="main-registration-container ">
      <div id="rf" className="split2 left2">
        <h3>Registration page</h3>
        <form
          className="registerform"
          method="post"
          name="userRegistrationForm"
          onSubmit={submituserRegistrationForm}
        >
          <label>Name</label>
          <input
            type="text"
            autoComplete={"username"}
            name="username"
            placeholder="Enter Name"
            value={state.fields.username}
            onChange={handleChange}
            id = "name1"
          />
   
          <div className="errorMsg">{state.errors.username}</div>
          <label>Email ID:</label>
          <input
            type="text"
            autoComplete={"email"}
            name="email"
            placeholder="Enter Email"
            value={state.fields.email}
            onChange={handleChange}
            id = "email1"
          />
   
          <div className="errorMsg">{state.errors.email}</div>
          <label>Mobile No:</label>
          <input
            type="text"
            name="mobileno"
            placeholder="Enter Mobile"
            value={state.fields.mobileno}
            onChange={handleChange}
            id = "mob1"
          />
         
          <div className="errorMsg">{state.errors.mobileno}</div>
       
          <label>Password</label>
          <input
            type={state.fields.showPassword ? "text" : "password"}
            name="password1"
            autoComplete={"new-password"}
            placeholder="Enter Password"
            value={state.fields.password1}
            onChange={handleChange}
            id = "pass1"
          />
   

          <div className="errorMsg">{state.errors.password1}</div>
          <label>Confirm Password</label>
          <input
            type={state.fields.showPassword ? "text" : "password"}
            name="password2"
            autoComplete={"new-password"}
            placeholder="Re-enter Password"
            value={state.fields.password2}
            onChange={handleChange}
            id = "newpass1"
          />
   
          <div className="errorMsg">{state.errors.password2}</div>
          <label htmlFor="showPassword">Show Password</label>
          <input
            type={"checkbox"}
            id="showPassword"
            name="showPassword"
            onChange={(event) => {
              const fields = { ...state.fields };
              fields[event.target.name] = event.target.checked;
              setState({
                ...state,
                fields,
              });
            }}
          />
          <center>
            <input type="submit" className="buttonregister" value="Register" />
          </center>

          <Link to="/login"> Already a user? Sign-in </Link>
        </form>
      </div>

      <div className="split2 right2">
        <div className="centered">
          
        </div>
      </div>
    </div>
  );
}

export default RegisterForm;
