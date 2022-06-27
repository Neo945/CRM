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
{
  /* “const [checked, setChecked] = React.useState” 
 usestate hook for checkbox check and uncheck. */
}

function PreSales(props) {
  let { jobid } = useParams();

  const [state, setState] = React.useState({
    id: "",
    detail_pricing: "",
    deal_details: "",
    deal_status: "",
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
      Header: "Customer ID",
      accessor: "saleslead.marketinglead.leads.customer.id",
    },
    {
      Header: "Name",
      accessor: "saleslead.marketinglead.leads.customer.name",
    },
    {
      Header: "IS Done",
      accessor: "is_done",
    },
    {
      Header: "Approved by",
      accessor: "approved_by.first_name",
    },
    {
      Header: " PreSales ID ",
      accessor: "id",
    },
    {
      Header: "Date Created",
      accessor: "date_created",
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
        name="deal_details"
        value={state.deal_details}
        onChange={(e) => setState({ ...state, deal_details: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="deal_status"
        value={state.deal_status}
        onChange={(e) => setState({ ...state, deal_status: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="detail_pricing"
        value={state.detail_pricing}
        onChange={(e) => setState({ ...state, detail_pricing: e.target.value })}
      ></input>
      <button
        style={{ display: "block", marginLeft: "100px" }}
        type="submit"
        onClick={() => {
          lookup("POST", `/leads/create/operation/${jobid}`, "", state).then(
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
      <label
        style={{
          display: "block",
          textAlign: "left",
          fontSize: "15px",
          color: "black",
          fontWeight: "bold",
        }}
      >
        Pre Sales ID
      </label>
      <input
        style={{ display: "block" }}
        type="text"
        placeholder="Enter ID"
      ></input>
      <button style={{ display: "block", marginLeft: "100px" }} type="submit">
        {" "}
        Submit
      </button>

      <br></br>
      <Footer></Footer>
    </div>
  );
}
export default PreSales;
