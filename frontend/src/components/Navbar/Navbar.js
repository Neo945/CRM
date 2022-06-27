//import libraries

import CardsHome from "../CardsHome/CardsHome";
import React from "react";
import "./Navbar.css";
import { Link } from "react-router-dom";
import Footer from "../Footer/Footer";
import img from "../images/logo.jpg";

const Navbar = () => {
  return (
    <header class="header">
      <div class="mid">
 
        {/* Navbar links for routing or navigation from one page to another */}
        <div></div>
        <ul
          class="navbar"
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            width: "100%",
          }}
        >
          <div className="navlist">
            <li>
              <Link to="/home">Home </Link>
            </li>
            <li>
              <Link to="/navlead">Leads</Link>
            </li>
            <li>
              <Link to="/customer/1">Customer </Link>
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
              <Link to="/createjob">Create Jobs </Link>
            </li>
            
          </div>
          <div className="navlogout">
            <li className="logo">
              <Link to="/login">LogOut</Link>
            </li>
          </div>
        </ul>
      </div>
      <br></br>
      <br></br>
      <br></br>
      <CardsHome></CardsHome>

      <Footer />
    </header>
  );
};
export default Navbar;
