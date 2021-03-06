//import libraries
import React, { useState } from "react";
import "./Register.css";
import { Link, useNavigate } from "react-router-dom";
import { lookup } from "../../utils";

//use state declaration 

function RegisterForm(props) {
  const [state, setState] = useState({
    fields: {
      username: "",
      email: "",
      phone: "",
      password1: "",
      password2: "",
      type: "PSLS",
    },
    errors: {
      username: "",
      email: "",
      phone: "",
      password1: "",
      password2: "",
    },
  });
  const [list, setList] = useState([]);

  function handleChange(e) {
    console.log(e.target.value);
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
    fields.phone = "";
    fields.password1 = "";
    fields.password2 = "";
    setState({ ...state, fields: fields });
  }

  function submituserRegistrationForm(e) {
    e.preventDefault();
    if (validateForm()) {
      // Fetch API call here using state.fields
      const temp = {
        ...state.fields,
        first_name: state.fields.username.split(" ")[0],
        last_name: state.fields.username.split(" ")[1],
        username: state.fields.username.split(" ").join(""),
        company: list[0].id,
      };
      console.log(temp);
      lookup("POST", "/accounts/register/", "", temp).then(
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


  //validation form

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

    if (fields.phone.length === 0) {
      formIsValid = false;
      errors.phone = "*Please enter your mobile no.";
    }

    if (fields.phone !== 0) {
      if (!fields["phone"].match(/^[0-9]{10}$/)) {
        formIsValid = false;
        errors.phone = "*Please enter valid mobile no.";
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
  {/* Form  */}
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
            id="name1"
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
            id="email1"
          />

          <div className="errorMsg">{state.errors.email}</div>
          <label>Mobile No:</label>
          <input
            type="text"
            name="phone"
            placeholder="Enter Mobile"
            value={state.fields.phone}
            onChange={handleChange}
            id="mob1"
          />

          <div className="errorMsg">{state.errors.phone}</div>

          <label>Password</label>
          <input
            type={state.fields.showPassword ? "text" : "password"}
            name="password1"
            autoComplete={"new-password"}
            placeholder="Enter Password"
            value={state.fields.password1}
            onChange={handleChange}
            id="pass1"
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
            id="newpass1"
          />

          <div className="errorMsg">{state.errors.password2}</div>
          <input
            style={{ display: "block" }}
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
          <label htmlFor="showPassword">Show Password</label>

          <label for="type">Choose type:</label>

          <select
            name="type"
            id="type"
            style={{ display: "block" }}
            onChange={handleChange}
            value={state.fields.type}
          >
            <option value="MRK">Marketing</option>
            <option value="OPR">Operations</option>
            <option value="SLS">Sales</option>
            <option value="PSLS">Pre Sales</option>
          </select>

          <div>
            <input
              list="dropdown1"
              type="text"
              placeholder="Search.."
              name="search"
              onChange={(e) => {
                lookup(
                  "GET",
                  `/accounts/search/company?str=${e.target.value}`,
                  "",
                  null
                ).then(({ data, status }) => {
                  if (status === 200) {
                    setList(data.company);
                  }
                });
              }}
            />
            <div>
              <datalist id="dropdown1">
                {list.map((item) => (
                  <option value={item.name}>{item.id}</option>
                ))}
              </datalist>
            </div>
          </div>

          <center>
            <input
              type="submit"
              className="buttonregister"
              style={{
                textAlign: "center",
                color: "white",
                fontWeight: "normal",
              }}
              value="Register"
            />
          </center>
{/* Link  for sign in*/}
          <Link to="/login"> Already a user? Sign-in </Link>
        </form>
      </div>

      <div className="split2 right2">
        <div className="centered"></div>
      </div>
    </div>
  );
}

export default RegisterForm;
