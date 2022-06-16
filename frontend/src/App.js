import { Link } from 'react-router-dom';

import { Route,Routes } from 'react-router-dom';
import './App.css';
import Register from './components/RegisterForm'
import Loginform from './components/loginform';
import ForgotPassword from './components/ForgotPassword';
function App() {
  return (
    <div className="App">
    
    <Routes>
    <Route
          path="/"
          element={
            
              <ol>
                <li>
                  <Link to={"/"}>Home</Link>
                </li>
                <li>
                  <Link to={"/login"}>Login</Link>
                </li>
                <li>
                  <Link to={"/register"}>Register</Link>
                  </li>
              </ol>
            
          }
        />

      <Route path='/register' element={<Register/>}/>
      <Route path='/login' element={<Loginform/>}/>
      <Route path='/forgotpassword' element={<ForgotPassword/>}/>

    </Routes>
    </div>
    
  );
}

export default App;
