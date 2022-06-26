import React, { Component } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from '../CopyNav/CopyNav';
import Footer from "../Footer/Footer";
import "./Leads.css"
class Leads extends Component {

  render() {
    const data = [
      {
        name: "Ayaan",
        age: 26,
        code: 10,
        phonenumber: 7419638521,
        city: "Sydney",
        Country: "Australia",
        Feedback:'Nice',
        
      },
      {
        name: "Ahana",
        age: 22,

        code: 11,
        phonenumber: 9637411021,
        city: "Nashik",
        Country: "India",
        Feedback:'Nice',
      },
      {
        name: "Peter",
        age: 40,

        code: 12,
        phonenumber: 7418529630,
        city: "Kolkata",
        Country: "India",
        Feedback:'Nice',
      },
      {
        name: "Virat",
        age: 30,

        code: 13,
        phonenumber: 4749651741,
        city: "NJ",
        Country: "USA",
        Feedback:'Nice',
      },
      {
        name: "Rohit",
        age: 32,
        code: 13,
        phonenumber: 7417418963,
        city: "Mumbai",
        Country: "Inida",
        Feedback:'Nice',
      },
      {
        name: "Dhoni",
        age: 37,
        code: 14,
        phonenumber: 8779143651,
        city: "Pune",
        Country: "India",
        Feedback:'Nice',
      },
    ];
    const columns = [
      {
        Header: "Name",
        accessor: "name",
      },
      {
        Header: "Mobile",
        accessor: "age",
      },
      {
        Header: "Linkedin ID",
        accessor: "code",
      },
      {
        Header: "Email",
        accessor: "phonenumber",
      },
      {
        Header: "city",
        accessor: "city",
      },
      {
        Header: "country",
        accessor: "Country",
      },
      {
        Header: "Feedback",
        accessor: "Feedback",
      },
    ];
    
    return (
     
      <div>
        <CopyNav/>
        <button className="rawbutton"> <a href="/data">Create Leads</a></button>
        <br></br>
        <br></br>
        <ReactTable
          data={data}
          columns={columns}
          defaultPageSize={10}
          pageSizeOptions={[2, 4, 6]}
      />
<br></br> 
<Footer></Footer>
      </div>

    );
  }
}
export default Leads;
