import React, { Component } from 'react'
import './Footer.css'
export default class Footer extends Component {
  render() {
    return (
      <div>
           <footer>
            <div class="row">
                <div class="col span-1-of-2">
                    <ul class="footer-nav">
                        <li><a href="#">About us</a></li>
                        <li><a >Blog</a></li>
                        <li><a >Press</a></li>
                        <li><a >iOS App</a></li>
                        <li><a >Android App</a></li>
                    </ul>
                </div>
              </div>
            <div class="row">
                <p>Copyright &copy;  All rights reserved</p>
                
            </div>
        </footer>

      </div>
    )
  }
}
