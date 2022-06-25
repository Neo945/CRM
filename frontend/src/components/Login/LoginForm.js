import React, { useState } from "react";
 import './login.css'
import { Link } from "react-router-dom";
import { lookup } from "../../utils";

function Loginform(props) {
  const [state, setState] = useState({
    fields: {
      username: "",
      password: "",
    },
    errors: {
      username: "",
      password: "",
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
    fields.password = "";
    setState({ ...state, fields: fields });
  }

  function submituserRegistrationForm(e) {
    e.preventDefault();
    if (validateForm()) {
      // alert("Form submitted");
      console.log(state.fields);
      lookup("POST", "/accounts/login/", "", state.fields).then(
        ({ data, status }) => {
          if (status === 200) {
            console.log(data);
            initState();
            // props.history("/");
          }
        }
      );
    }
  }

  function validateForm() {
    let fields = state.fields;
    let errors = {};
    let formIsValid = true;

    if (!fields.username) {
      formIsValid = false;
      errors.username = "*Please enter your username.";
    }

   
    if (!fields.password) {
      formIsValid = false;
      errors.password = "*Please enter your password.";
    }

    if (fields.password.length !== 0) {
      if (
        !fields["password"].match(
          /^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&]).*$/
        )
      ) {
        formIsValid = false;
        errors.password = "*Please enter secure and strong password.";
      } else {
        // console.log(fields['emailid'],fields['password'])
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
      <div id="register1" className="split1 left1">
        <div className="centered" />
        <h2>Login Page</h2>
        <form className="loginform"
          method="post"
          name="userRegistrationForm"
          onSubmit={submituserRegistrationForm}
        >
          <label>Username:</label>
          <input
            type="text"
            placeholder="Enter Username"
            name="username"
            autoComplete="username"
            value={state.fields.username}
            onChange={handleChange}
            id="username"
          />
          <div className="errorMsg">{state.errors.username}</div>
          {/* <label>Email ID:</label>
            <input
              type="text"
              name="email"
              value={state.fields.email}
              onChange={handleChange}
              id="email"
            />
            <div className="errorMsg">{state.errors.email}</div> */}
          <br></br>
          <label>Password:</label>
          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            autoComplete="current-password"
            value={state.fields.password}
            onChange={handleChange}
            id="pass"
          />
          <div className="errorMsg">{state.errors.password}</div>
          <center>
            <input type="submit" className="button b1" value="Login" />
          </center>
          <Link to="/register"> Not a user? Sign-up </Link>
          <br></br>
          <br></br>
          <Link to="/forgotpassword"> Forgot Password </Link>
        </form>
      </div>

      <div className="split1 right1">
        <div className="centered">
        
        </div>
      </div>
    </div>
  );
}

export default Loginform;
