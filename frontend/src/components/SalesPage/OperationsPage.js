import React, { Component, useEffect } from "react";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { useParams } from "react-router-dom";
import CopyNav from '../CopyNav/CopyNav';
import { lookup } from "../../utils";
import Footer from "../Footer/Footer";
function OperationsPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
  useEffect(() => {
    lookup("GET", `/leads/operation/job/${jobid}`, "", null).then(
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
      Header: "Operation ID",
      accessor: "presaleslead.saleslead.marketinglead.leads.customer.id",
    },
    {
      Header: "Name",
      accessor: "presaleslead.saleslead.marketinglead.leads.customer.name",
    },
    {
      Header: "Presales Lead ID",
      accessor: "presaleslead.id",
    },
    
    {
      Header: "Email",
      accessor: "presaleslead.saleslead.marketinglead.leads.customer.email",
    },
    
    {
      Header: "Created on",
      accessor: "date_created",
    },
    {
      Header: "Approved By",
      accessor: "approved_by.first_name",
    },
    {
      Header: "FeedBack",
      accessor: "cmrcss",
    },
  ];
    
    return (
     
      <div>
        <CopyNav/>
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

        <select style={{ display: "block" }}
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
        <label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Operation ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block" ,marginLeft:"100px" }} type="submit"> Submit</button>
      
<br></br>
<Footer></Footer>
      </div>

    );
  }

export default OperationsPage;
