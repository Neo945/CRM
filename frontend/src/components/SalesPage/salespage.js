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
{/* “const [checked, setChecked] = React.useState” 
 usestate hook for checkbox check and uncheck. */}
function SalesPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
  const [checked, setChecked] = React.useState("All");
   //lookup sends the main data 
  useEffect(() => {
    lookup("GET", `/customer/get/job/${jobid}`, "", null).then(
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
      accessor: "marketinglead",
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

      


{/* The display property specifies if/how an element is displayed. */}
<label style={{ display: "block",textAlign:"left",fontSize:"15px",color:"black",fontWeight:"bold" }}>Sales ID</label>
<input style={{ display: "block" }} type="text" placeholder="Enter ID">
        </input>
<button style={{ display: "block" ,marginLeft:"100px" }} type="submit"> Submit</button>
      
<br></br>
<Footer></Footer>
      </div>

    );
  }

export default SalesPage;
