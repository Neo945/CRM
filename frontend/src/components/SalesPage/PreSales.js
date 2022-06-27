// import libraries
// import React, { Component, useEffect } from "react";
import { useParams } from "react-router-dom";
import { lookup } from "../../utils";

import React, { Component, useEffect } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";

 // The useParams hook returns an object of key/value pairs of the dynamic 
        // params from the current URL that were matched by the <Route path> .
{/* “const [checked, setChecked] = React.useState” 
 usestate hook for checkbox check and uncheck. */}

 function PreSales(props) {
  let { jobid } = useParams();

  const [state, setState] = React.useState({
    id: "",
  });
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
   //lookup sends the main data 
  useEffect(() => {
    lookup("GET", `/leads/presales/job/${jobid}`, "", null).then(
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
      accessor: "salesleads.marketinglead.leads.customer.id",
    },
    {
      Header: "Name",
      accessor: "salesleads.marketinglead.leads.customer.name",
    },
    {
      Header: "IS Done",
      accessor: "salesleads.marketinglead.leads.customer.is_done",
    },
    {
      Header: "Approved by",
      accessor: "approved_by.first_name",
    },
    {
      Header: " Sales Leads ",
      accessor: "salesleads.marketinglead.leads.customer.saleslead",
    },
    {
      Header: "Date Created",
      accessor: "date_created",
    },
    {
      Header: "Updated date",
      accessor: "salesleads.marketinglead.leads.customer.date_updated",
    },
    {
      Header: "Proposal details",
      accessor: "salesleads.marketinglead.leads.customer.proposal_details",
    },
    {
      Header: "Proposal Dates",
      accessor: "salesleads.marketinglead.leads.customer.proposal_date",
    },

    // {
    //   Header: "FeedBack",
    //   accessor: "cmrcss",
    // },
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
        columns={columns}
        //default fields are 10 per page.
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
      <input
        style={{ display: "block" }}
        type="text"
        name="id"
        value={state.id}
        onChange={(e) => setState({ ...state, id: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="refered_source"
        value={state.proposal_details}
        onChange={(e) => setState({ ...state, refered_source: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="requirements"
        value={state.proposal_details}
        onChange={(e) => setState({ ...state, requirements: e.target.value })}
      ></input>
      <button
        style={{ display: "block", marginLeft: "100px" }}
        type="submit"
        onClick={() => {
          lookup("POST", `/leads/create/presales/${state.id}`, "", state).then(
            ({ data, status }) => {
              if (status === 200) {
                console.log(data);
              }
            }
          );
        }}
      >
        {" "}
        Submit
      </button>

        {/* The display property specifies if/how an element is displayed. */}
      <label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Pre Sales ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block" ,marginLeft:"100px" }} type="submit"> Submit</button>
      
<br></br>
      <Footer></Footer>
    </div>
  );
}
export default PreSales;
