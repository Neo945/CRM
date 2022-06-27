import React, { Component } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from '../CopyNav/CopyNav';
 import Footer from "../Footer/Footer";
class AccountsPage extends Component {

  render() {
    const data = [
      {
        Customerid:"1001",
        Marketingid:"1111",
        Name: "Ayaan",
        Email:"abc@gmail.com",
        Phone: 7419638521,
        ReferredSource: "Adv",
        Createdon:"CRM",
        Createdby:"any"
      },
   
    ];
    const columns = [
      {
        Header: "Customer id",
        accessor: "Customerid",
      },
      {
        Header: "Marketing id",
        accessor: "Marketingid",
      },
      {
        Header: "Name",
        accessor: "Name",
      },
      {
        Header: "Email",
        accessor: "Email",
      },
      {
        Header: "Phone",
        accessor: "Phone",
      },
      {
        Header: "Reffered Source",
        accessor: "ReferredSource",
      },
      {
        Header: "Created on",
        accessor: "Createdon",
      },
      {
        Header: "Created by",
        accessor: "Createdby",
      },
    ];
    
    return (
     
      <div className="table">
        <CopyNav/>
        <ReactTable
          data={data}
          columns={columns}
          defaultPageSize={10}
          pageSizeOptions={[2, 4, 6]}
      />
<br></br>

<select style={{ display: "block" }}>
          <option value="All">All</option>
          <option value="Checked">Checked</option>
          <option value="Unhecked">Unhecked</option>
        </select>


        <br></br>
<label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Accounts ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block"  }} type="submit"> Submit</button>
      
<br></br>
<Footer></Footer>
      </div>

    );
  }
}
export default AccountsPage;
