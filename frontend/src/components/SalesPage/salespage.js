import React, { Component } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from '../CopyNav/CopyNav';
 import Footer from "../Footer/Footer";
class SalesPage extends Component {

  render() {
    const data = [
      {
        Salesid:"1001",
        Marketingid:"1111",
        Name: "Ayaan",
        Email:"abc@gmail.com",
        Phone: 7419638521,
        SalesDetails: "xyz",
        SalesPricing: "xyz",
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
        Header: "Sales Details",
        accessor: "SalesDetails",
      },
      {
         Header: "Sales Pricing",
        accessor: "SalesPricing",
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
<Footer></Footer>
      </div>

    );
  }
}
export default SalesPage;