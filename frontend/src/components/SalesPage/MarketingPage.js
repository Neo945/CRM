import React, { Component, useEffect } from "react";
import { useParams } from "react-router-dom";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { lookup } from "../../utils";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";
function MarketingPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
  const [state, setState] = React.useState({
    id: "",
    sales_details: "",
    sales_pricing: "",
  });
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
        value={state.sales_pricing}
        onChange={(e) => setState({ ...state, refered_source: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="requirements"
        value={state.sales_pricing}
        onChange={(e) => setState({ ...state, requirements: e.target.value })}
      ></input>
      <button
        style={{ display: "block", marginLeft: "100px" }}
        type="submit"
        onClick={() => {
          lookup("POST", `/leads/create/sales/${state.id}`, "", state).then(
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
export default MarketingPage;
