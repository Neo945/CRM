// import libraries
import React, { Component, useEffect } from "react";
import { useParams } from "react-router-dom";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { lookup } from "../../utils";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";

// The useParams hook returns an object of key/value pairs of the dynamic 
        // params from the current URL that were matched by the <Route path> .
{/* “const [checked, setChecked] = React.useState” 
 usestate hook for checkbox check and uncheck. */}
function MarketingPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");

  //lookup sends the main data 
  useEffect(() => {
    lookup("GET", `/leads/market/job/${jobid}`, "", null).then(
      ({ data, status }) => {
        if (status === 200) {
          console.log(data);
          setData(data.data);
        }
      }
    );
  }, []);

  //table header  information
  const columns = [
    {
      Header: "ID",
      accessor: "id",
    },
    {
      Header: "Customer Name",
      accessor: "leads.customer.name",
    },
    {
      Header: "Customer ID",
      accessor: "leads.customer.id",
    },
    {
      Header: "Leads id",
      accessor: "leads.id",
    },
    {
      Header: "Email",
      accessor: "leads.customer.email",
    },
    {
      Header: "Phone",
      accessor: "leads.customer.phone",
    },
    {
      Header: "Reffered Source",
      accessor: "refered_source",
    },
    {
      Header: "Created on",
      accessor: "date_created",
    },
    {
      Header: "Created by",
      accessor: "approved_by.first_name",
    },
    {
      Header: "FeedBack",
      accessor: "cmrcss",
    },
  ];

  return (
    <div className="table">
      <CopyNav />
      {/* filtering data */}
      <ReactTable
        data={
          checked === "All"
            ? data
            : checked === "Checked"
            ? data.filter((x) => x.is_done)
            : data.filter((x) => !x.is_done)
        }
        //default fields are 10 per page.
        columns={columns}
        defaultPageSize={10}
        pageSizeOptions={[2, 4, 6]}
      />
      <br></br>
      
      <select
        style={{ display: "block" }}
        onChange={(e) => {
          console.log(e.target.value);
          setChecked(e.target.value);
        }}
      >

        <option value="All">All</option>
        <option value="Checked">Checked</option>
        <option value="Unhecked">Unhecked</option>
      </select>
      <label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Marketing ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block" ,marginLeft:"100px" }} type="submit"> Submit</button>
{/* The display property specifies if/how an element is displayed. */}
<br></br>
      <Footer></Footer>
    </div>
  );
}
export default MarketingPage;
