import React, { Component } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from '../CopyNav/CopyNav';
 import Footer from "../Footer/Footer";
class PreSales extends Component {

  render() {
    const data = [
        {
            Salesid:"1001",
            PreSalesid:"1111",
            Name: "Ayaan",
            Email:"abc@gmail.com",
            Phone: 7419638521,
            ProposalDetails: "xyz",
            ProposalDates: "xyz",
            Create:"CRM",
            Createdby:"any"
          },
    ];
    const columns = [
        {
            Header: "Sales id",
            accessor: "Salesid",
          },
          {
            Header: "PreSales id",
            accessor: "PreSalesid",
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
            Header: "ProposalDetails",
            accessor: "ProposalDetails",
          },
          {
             Header: "Proposal Dates",
            accessor: "ProposalDates",
          },
          {
            Header: "Created On",
            accessor: "Create",
          },
          {
            Header: "Created by",
            accessor: "Createdby",
          },
    ];
    
    return (
     
      <div>
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

<Footer></Footer>
      </div>

    );
  }
}
export default PreSales;
