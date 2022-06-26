import React, { Component } from "react";
import "./Footer.css";
export default class Footer extends Component {
  render() {
    return (
      <div>
        <footer>
          <div className="row">
            <div className="col span-1-of-2">
              <ul className="footer-nav">
                <li>
                  <a href="/">
                    <b>About us</b>
                  </a>
                </li>
                <li>
                  <a href="/">
                    <b>Blog</b>
                  </a>
                </li>
                <li>
                  <a href="/">
                    <b>Press</b>
                  </a>
                </li>
                <li>
                  <a href="/">
                    <b>iOS App</b>
                  </a>
                </li>
                <li>
                  <a href="/">
                    <b>Android App</b>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="row">
            <p>
              <b>Copyright &copy; All rights reserved</b>
            </p>
            <p>
              <b>Contact Number: +91 7048328239</b>
            </p>
            <p>
              <b>Location: Mumbai,Maharashtra.</b>
            </p>
          </div>
        </footer>
      </div>
    );
  }
}
