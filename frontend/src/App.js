import { Link } from "react-router-dom";
import { Route, Routes } from "react-router-dom";
import "./App.css";
import { useNavigate, Navigate } from "react-router-dom";

import {
  Navbar,
  ForgotPassword,
  Register,
  Login,
  Leads,
  RawData,
  SalesPage,
  PreSales,
  OperationsPage,
  MarketingPage,
  AccountsPage,
  CustomerData,
  CreateJob,
} from "./components";

import { useEffect, useState } from "react";
import { lookup } from "./utils";
function App() {
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("user")));
  useEffect(() => {
    if (window.location.pathname !== "/checkout")
      localStorage.removeItem("purchase");
    if (user === null) {
      lookup("GET", "/accounts/get/", "", null)
        .then(({ data, status }) => {
          if (status === 200) {
            if (data.user) {
              localStorage.setItem("user", JSON.stringify(data.user));
              setUser(data.user);
            } else {
              localStorage.setItem("user", null);
              setUser(null);
            }
          } else {
            localStorage.setItem("user", null);
            setUser(null);
          }
        })
        .catch((e) => {
          console.log(e.message);
        });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  const navigate = useNavigate();

  const [state, setState] = useState({
    fields: {},
  });

  const onChange = (updatedValue) => {
    setState({
      ...state,
      fields: {
        ...state.fields,
        ...updatedValue,
      },
    });
  };

  return (
    <div className="App">
      <Routes>
        <Route
          path="/"
          element={
            <ol>
              <li>
                <Link to={"/home"}>Home</Link>
              </li>
              <li>
                <Link to={"/login"}>Login</Link>
              </li>
              <li>
                <Link to={"/register"}>Register</Link>
              </li>
              <li>
                <Link to={"/home"}>HomeDash</Link>
              </li>
              <li>
                <Link to={"/navlead"}>Leads</Link>
              </li>

              <li>
                <Link to={"/data"}>RawData </Link>
              </li>

              <li>
                <Link to={"/salespage"}> Sales </Link>
              </li>

              <li>
                <Link to={"/createjob"}> CreateJob </Link>
              </li>
            </ol>
          }
        />

        <Route
          path="/register"
          element={
            !user ? <Register history={navigate} /> : <Navigate to={"/home"} />
          }
        />

        <Route
          path="/login"
          element={
            !user ? <Login history={navigate} /> : <Navigate to={"/home"} />
          }
        />
        <Route
          path="/forgotpassword"
          element={<ForgotPassword history={navigate} />}
        />
        <Route path="/home" element={<Navbar history={navigate} />} />
        <Route
          path="/customers/:jobid"
          element={<CustomerData history={navigate} />}
        />
        <Route path="/navlead/:jobid" element={<Leads history={navigate} />} />
        <Route
          path="/data"
          element={
            <RawData
              onChange={(fields) => onChange(fields)}
              history={navigate}
            />
          }
        />

        <Route
          path="/createjob"
          element={
            <CreateJob
              onChange={(fields) => onChange(fields)}
              history={navigate}
            />
          }
        />

        <Route
          path="/salespage/:jobid"
          element={<SalesPage history={navigate} />}
        />

        <Route path="/home" element={<Navbar history={navigate} />} />
        <Route
          path="/presales/:jobid"
          element={<PreSales history={navigate} />}
        />
        <Route
          path="/operationpage/:jobid"
          element={<OperationsPage history={navigate} />}
        />
        <Route
          path="/marketingpage/:jobid"
          element={<MarketingPage history={navigate} />}
        />
        <Route
          path="/accountspage/:jobid"
          element={<AccountsPage history={navigate} />}
        />
      </Routes>
    </div>
  );
}

export default App;
