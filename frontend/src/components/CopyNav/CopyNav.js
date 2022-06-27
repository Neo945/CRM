import React from "react";
import "./CopyNav.css";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <header className="header">
      <div className="mid">
        <ul className="navbar">
          <li>
            <Link to="/home">Home </Link>
          </li>

            <li>
              <Link to="/customer">Customer </Link>
            </li>


          <li>
            <Link to="/navlead">Leads</Link>
          </li>
          <li>
            <Link to="/marketingpage">Marketing</Link>
          </li>

          <li>
            <Link to="/salespage">Sales</Link>
          </li>

          <li>
            <Link to="/presales">Pre-sales</Link>
          </li>
          <li>
            <Link to="/operationpage">Operations</Link>
          </li>

          <li>
            <Link to="/accountspage">Accounts</Link>
          </li>
          <li>
              <Link to="/createjob">Customer Jobs </Link>
            </li>
          
          <li className="logo">
            <Link to="/login">LogOut</Link>
          </li>
        </ul>
      </div>
      <br></br>
      <br></br>
      <br></br>
      {/* <div className="footer">
                <p>Footer</p>
                <p>Contact: 9849329003</p>
            </div> */}
    </header>
  );
};
export default Navbar;
