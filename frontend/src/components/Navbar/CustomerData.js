import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { lookup } from "../../utils";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";
import "./Leads.css";
function CustomerData(props) {
  let { jobid } = useParams();
  const [checked, setChecked] = React.useState(true);
  const [data, setData] = React.useState([]);
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

  const columns = [
    {
      Header: "Lead ID",
      accessor: "id",
    },
    {
      Header: "Name",
      accessor: "name",
    },
    {
      Header: "Mobile",
      accessor: "phone",
    },
    {
      Header: "Linkedin ID",
      accessor: "linkedin.linkedin_url",
    },
    {
      Header: "Email",
      accessor: "email",
    },
    {
      Header: "requirement",
      accessor: "linkedin.requirement",
    },
    {
      Header: "Created on",
      accessor: "date_created",
    },
    {
      id: "checkbox",
      accessor: "",
      Cell: ({ original }) => {
        return (
          <input
            style={{ opacity: "1" }}
            type="checkbox"
            className="checkbox"
            checked={checked}
            onChange={(e) => setChecked(e.target.checked)}
          />
        );
      },
    },
  ];

  return (
    <div>
      <CopyNav />
      <button className="rawbutton">
        {" "}
        <a href="/data">Create Leads</a>
      </button>
      <br></br>
      <br></br>
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
export default CustomerData;
