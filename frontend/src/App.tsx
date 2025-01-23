import { Routes, Route } from 'react-router';
import HomePage from './components/HomePage';
import ItemComponent from './components/ItemComponent';


export default function App() {
     
  return (
    <div>
        <Routes>
          <Route path='/' element={<HomePage/>}/>
          <Route path='/item/:id' element={<ItemComponent/>}/>
        </Routes>
    </div>
  )
}

