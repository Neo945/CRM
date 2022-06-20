
import React from 'react';
import "./Navbar.css"
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
	<li>
      <Link to="/logout">LogOut</Link>
    </li>
		</ul>
   
  </div>
		<br></br>
		<br></br>
		<br></br>
		<section class="about">
                <h3>About Us</h3>
            
            <div class="container">
                <div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Order</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.

</p>
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.</p>
                    </div>
                    </div>
					</div>
					<div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Order</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.

</p>
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.</p>
                    </div>
                    </div>
					</div>
					<div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Order</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.

</p>
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.</p>
                    </div>
                    </div>
					</div>
					</div>
                

            </section>

    </header>
	
  );
}
export default Navbar;