import { Routes, Route } from 'react-router';
import HomePage from './components/HomePage';
import ItemComponent from './components/Content/ItemComponent';
import AuthComponent from './components/Auth/AuthComponent';
import RegistrationComponent from './components/Auth/RegitrationComponent';
import UserComponent from './components/User/UserComponent';
import ForgetPassComponent from './components/Auth/ForgetPassComponent';
import ResetPassComponent from './components/Auth/ResetPassComponent';


export default function App() {
     
  return (
    <div>
        <Routes>
          <Route path='/' element={<HomePage/>}/>
          <Route path='/item/:id' element={<ItemComponent/>}/>
          <Route path='/login' element={<AuthComponent/>}/>
          <Route path='/registration' element={<RegistrationComponent/>}/>
          <Route path='/my_profile' element={<UserComponent/>}/>
          <Route path='/forget_email' element={<ForgetPassComponent/>}/>
          <Route path='/reset_password/:email' element={<ResetPassComponent/>}/>
        </Routes>
    </div>
  )
}

