// import libraries
import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { lookup } from "../../utils";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";

// The useParams hook returns an object of key/value pairs of the dynamic
// params from the current URL that were matched by the <Route path> .
{
  /* “const [checked, setChecked] = React.useState” 
 usestate hook for checkbox check and uncheck. */
}
function SalesPage(props) {
  const [state, setState] = React.useState({
    id: "",
    proposal_date: "",
    proposal_details: "",
  });
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
  //lookup sends the main data
  useEffect(() => {
    lookup("GET", `/leads/sales/job/${jobid}`, "", null).then(
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
      Header: "Sales id",
      accessor: "id",
    },
    {
      Header: "Marketing id",
      accessor: "marketinglead.id",
    },
    {
      Header: "Name",
      accessor: "marketinglead.leads.customer.name",
    },
    {
      Header: "Email",
      accessor: "marketinglead.leads.customer.email",
    },
    {
      Header: "Phone",
      accessor: "marketinglead.leads.customer.phone",
    },
    {
      Header: "Sales Details",
      accessor: "sales_details",
    },
    {
      Header: "Sales Pricing",
      accessor: "sales_pricing",
    },
    {
      Header: "Created On",
      accessor: "date_created",
    },
    {
      Header: "Created by",
      accessor: "approved_by.first_name",
    },
    {
      Header: "Feedback",
      accessor: "cmrcss.feedback",
    },
  ];

  return (
    <div>
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

      <br></br>

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
        name="proposal_date"
        value={state.proposal_date}
        onChange={(e) => setState({ ...state, proposal_date: e.target.value })}
      ></input>
      <input
        style={{ display: "block" }}
        type="text"
        name="proposal_details"
        value={state.proposal_details}
        onChange={(e) =>
          setState({ ...state, proposal_details: e.target.value })
        }
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

export default SalesPage;
