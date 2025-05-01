import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/NavBar';
import Footer from './components/Footer';
import Landing from './pages/Landing';
import Reservar from './pages/Reservar';
import Gestionar from './pages/Gestionar';

function App() {
  return (
    <div className="wrapper">
      <Router>
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/reservar" element={<Reservar />} />
            <Route path="/gestionar" element={<Gestionar />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
