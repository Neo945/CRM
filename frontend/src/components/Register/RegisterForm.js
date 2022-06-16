import React from "react";
import "../style.css";
import { Link } from "react-router-dom";
import { lookup } from "../../utils";
class RegisterForm extends React.Component {
  constructor() {
    super();
    this.state = {
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
  initState() {
    let fields = {};
    fields.username = "";
    fields.email = "";
    fields.mobileno = "";
    fields.password1 = "";
    fields.password2 = "";
    this.setState({ fields: fields });
  }

  submituserRegistrationForm(e) {
    e.preventDefault();
    if (this.validateForm()) {
      // Fetch API call here using this.state.fields
      lookup("POST", "/accounts/register/", "", this.state.fields).then(
        ({ data, status }) => {
          if (status === 200) {
            console.log(data);
            // this.props.history("/");
          }
        }
      );
      this.initState();
    }
  }

  validateForm() {
    let fields = this.state.fields;
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

    this.setState({
      errors: errors,
    });
    return formIsValid;
  }

  render() {
    return (
      <div id="main-registration-container ">
        <div id="register" className="split left">
          <div className="centered" />
          <h3>Registration page</h3>
          <form
            method="post"
            name="userRegistrationForm"
            onSubmit={this.submituserRegistrationForm}
          >
            <label>Name</label>
            <input
              type="text"
              autoComplete={"username"}
              name="username"
              value={this.state.fields.username}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.username}</div>
            <label>Email ID:</label>
            <input
              type="text"
              autoComplete={"email"}
              name="email"
              value={this.state.fields.email}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.email}</div>
            <label>Mobile No:</label>
            <input
              type="text"
              name="mobileno"
              value={this.state.fields.mobileno}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.mobileno}</div>
            <label>Password</label>
            <input
              type={this.state.fields.showPassword ? "text" : "password"}
              name="password1"
              autoComplete={"new-password"}
              value={this.state.fields.password1}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.password1}</div>
            <label>Confirm Password</label>
            <input
              type={this.state.fields.showPassword ? "text" : "password"}
              name="password2"
              autoComplete={"new-password"}
              value={this.state.fields.password2}
              onChange={this.handleChange}
            />
            <div className="errorMsg">{this.state.errors.password2}</div>
            <label htmlFor="showPassword">Show Password</label>
            <input
              type={"checkbox"}
              id="showPassword"
              name="showPassword"
              onChange={(event) => {
                const fields = { ...this.state.fields };
                fields[event.target.name] = event.target.checked;
                this.setState({
                  fields,
                });
              }}
            />
            <center>
              <input type="submit" className="button" value="Register" />
            </center>

            <Link to="/login"> Already a user? Sign-in </Link>
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
}

export default RegisterForm;
