import { Link } from "react-router-dom";
import { Route, Routes } from "react-router-dom";
import "./App.css";
import { useNavigate, Navigate } from "react-router-dom";

import { Navbar,ForgotPassword,Register, Login,Leads, RawData} from "./components";

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
                <Link to={"/navbar"}>HomeDash</Link>
              </li>
              <li>
                <Link to={"/navlead"}>Leads</Link>
              </li>
              <li>
                <Link to={"/RawData"}>RawData</Link>
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
        <Route
          path="/navbar"
          element={<Navbar history={navigate} />}
        />
        <Route
          path="/navlead"
          element={<Leads history={navigate} />}
        />

        <Route
          path="/RawData"
          element={<RawData history={navigate} />}
        />

        <Route path="/home" element={<h1>Home</h1>} />
        
  
      </Routes>
    </div>
  );
}

export default App;
