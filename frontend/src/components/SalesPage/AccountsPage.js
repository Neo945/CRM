import React, { Component, useEffect } from "react";
import { useParams } from "react-router-dom";
import ReactTable from "react-table-6";
import "react-table-6/react-table.css";
import { lookup } from "../../utils";
import CopyNav from "../CopyNav/CopyNav";
import Footer from "../Footer/Footer";
function AccountsPage(props) {
  let { jobid } = useParams();
  const [data, setData] = React.useState([]);
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
export default AccountsPage;
