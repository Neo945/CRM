// import React, { Component, useEffect } from "react";
import { useParams } from "react-router-dom";
import { lookup } from "../../utils";

import React, { Component, useEffect } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";

function PreSales(props) {
  const [state, setState] = React.useState({
    id: "",
    proposal_details: "",
    proposal_date: "",
  });
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
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
      <ReactTable
        data={
          checked === "All"
            ? data
            : checked === "Checked"
            ? data.filter((x) => x.is_done)
            : data.filter((x) => !x.is_done)
        }
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

      <br></br>
      <Footer></Footer>
    </div>
  );
}
export default PreSales;
