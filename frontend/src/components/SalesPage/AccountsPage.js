// import libraries as required
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
function AccountsPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);

  //lookup sends the main data 
  useEffect(() => {
    lookup("GET", `/customerget/client/job/${jobid}`, "", null).then(
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
      Header: "Client ID",
      accessor: "id",
    },
    {
      Header: "Operation ID",
      accessor: "operations.id",
    },
    {
      Header: "Name",
      accessor: "name",
    },
    {
      Header: "Email",
      accessor: "email",
    },
    {
      Header: "Phone",
      accessor: "phone",
    },
    {
      Header: "Created on",
      accessor: "date_created",
    },
    {
      Header: "Created by",
      accessor: "operations.aproved_by.first_name",
    },
  ];


     
  return (
    <div className="table">
      <CopyNav />
        {/* filtering data */}
      <ReactTable
        data={data}
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
      {/* The display property specifies if/how an element is displayed. */}
<label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Accounts ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block"  }} type="submit"> Submit</button>
      
<br></br>
      <Footer></Footer>
    </div>
  );
}
export default AccountsPage;
