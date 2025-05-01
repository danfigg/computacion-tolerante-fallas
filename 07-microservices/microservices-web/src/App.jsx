import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/NavBar';
import Footer from './components/Footer';
import Landing from './pages/Landing';

function App() {
  return (
    <div className="wrapper">
      <Router>
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Landing />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
