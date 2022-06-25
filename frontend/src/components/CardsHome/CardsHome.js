import React, { Component } from 'react'
import img1 from '../images/marketing.png'
import img2 from '../images/salesfunnel.png'

export default class CardsHome extends Component {
  render() {
    return (
      <div className='full'>
        <section class="about">
                <h3>About Us</h3>

              
            
            <div class="container">
                <div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
              
                        <h5>Order</h5>
                        <img src = {img1} alt = "marketing" height={250} width = {250}></img>
                        {/*  */}
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <img src = {img2} alt = "salesfunnel" height={250} width = {250}></img>
                        {/* <p>Thank you for using my words in your work. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I have never known a Jack that was in good enough shape to name bodybuilding after him. Pantone is a colour but also the singular version of pants. Are there Out-of-Stock photos? Gafuffle.</p> */}
                    </div>
                    </div>
					</div>
					<div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Order</h5>
                        <img src = {img2} alt = "salesfunnel" height={250} width = {250}></img>
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <img src = {img1} alt = "marketing" height={250} width = {250}></img>
                        
                    </div>
                    </div>
					</div>
					<div class="row">
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Order</h5>
                        <img src = {img1} alt = "marketing" height={250} width = {250}></img>
                    </div>
                    </div>
                    <div class="col s12 l4 m6">
                       <div class="card c1">
                        <h5>Deal</h5>
                        <img src = {img2} alt = "salesfunnel" height={250} width = {250}></img>
                    </div>
                    </div>
					</div>
					</div>
                

            </section>
      </div>
      
    )
  }
}
