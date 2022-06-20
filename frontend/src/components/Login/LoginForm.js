import React, { useState } from "react";
import "./login.css";
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

    // if (fields.username.length !== 0) {
    //   if (!fields.username.match(/^[a-zA-Z ]*$/)) {
    //     formIsValid = false;
    //     errors.username = "*Please enter alphabet characters only.";
    //   }
    // }

    // if (!fields["emailid"]) {
    //   formIsValid = false;
    //   errors["emailid"] = "*Please enter your email-ID.";
    // }

    // if (typeof fields["emailid"] !== "undefined") {
    //   //regular expression for email validation
    //   var pattern = new RegExp(
    //     /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i
    //   );
    //   if (!pattern.test(fields["emailid"])) {
    //     formIsValid = false;
    //     errors["emailid"] = "*Please enter valid email-ID.";
    //   }
    // }

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
      <div id="register" className="split left">
        <div className="centered" />
        <h3>Login Page</h3>
        <form
          method="post"
          name="userRegistrationForm"
          onSubmit={submituserRegistrationForm}
        >
          <label>Username:</label>
          <input
            type="text"
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
          <label>Password</label>
          <input
            type="password"
            name="password"
            autoComplete="current-password"
            value={state.fields.password}
            onChange={handleChange}
            id="pass"
          />
          <div className="errorMsg">{state.errors.password}</div>
          <center>
            <input type="submit" className="button" value="Login" />
          </center>
          <Link to="/register"> Not a user? Sign-up </Link>
          <br></br>
          <br></br>
          <Link to="/forgotpassword"> Forgot Password </Link>
        </form>
      </div>

      <div className="split right">
        <div className="centered">
          <h2>John Doe</h2>
          <p>Some text here too.</p>
        </div>
      </div>
    </div>
  );
}

export default Loginform;
