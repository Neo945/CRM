import React from 'react';
import "./CopyNav.css"
import {  Link } from "react-router-dom";
const Navbar= () =>{
  return (
		<header class="header">
	  <div class="mid">
		<ul class="navbar">
			 <li>
      <Link to="/navlead">Leads</Link>
    </li>
    <li>
      <Link to="/cats">Contact</Link>
    </li>
    <li>
      <Link to="/sheeps">Order</Link>
    </li>
    <li>
      <Link to="/goats">Deal</Link>
    </li>
	<li className='logo'>
      <Link to="/logout">LogOut</Link>
    </li>
		</ul>
   
  </div>
		<br></br>
		<br></br>
		<br></br>
            {/* <div class="footer">
                <p>Footer</p>
                <p>Contact: 9849329003</p>
            </div> */}

    </header>
    
	
  );
}
export default Navbar;