import './App.css';
import { Routes ,Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Notfound from './components/pages/Notfound';

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="*" element={<Notfound/>}/>
      </Routes>
    </div>
  );
}

export default App;
